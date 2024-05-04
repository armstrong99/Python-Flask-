from flask import jsonify, request
from app import app, db
from app.models import Drone, Task, Image
from app.util import generate_noisy_images

@app.route('/api/drones', methods=['POST'])
def create_drone():
    data = request.get_json()
    name = data.get('name')

    new_drone = Drone(name=name)
    db.session.add(new_drone)
    db.session.commit()
    return jsonify({'message': 'Drone created successfully', "droneId": new_drone.id})
@app.route('/api/drones', methods=['GET'])
def get_drones():
    drones = Drone.query.all()
    drones_serialized = [drone.serialize() for drone in drones]
    return jsonify(drones_serialized)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    drone_ids = data.get('drone_ids', [])

    if not all([name, description, drone_ids]):
        return jsonify({'error': 'Name, description, and at least one drone ID are required'}), 400

    drones = Drone.query.filter(Drone.id.in_(drone_ids)).all()
    if len(drones) != len(drone_ids):
        return jsonify({'error': 'One or more drone IDs are invalid'}), 400

    task = Task(name=name, description=description)
    task.drones.extend(drones)
    db.session.add(task)
    db.session.commit()

    return jsonify({'message': 'Task created successfully', "taskId": task.id}), 201
   

@app.route('/api/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    return jsonify(task.serialize()), 200

@app.route('/api/tasks/<int:id>/execute', methods=['POST'])
def execute_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    # Generate random noisy images (5 images in this case)
    image_paths = generate_noisy_images(5)

    # Update the task execution status and link images to the task
    task.is_executed = True
    for img_path in image_paths:
        image = Image(task_id=id, image_url=img_path)
        db.session.add(image)

    db.session.commit()

    return jsonify({'message': 'Task executed successfully'}), 200

@app.route('/api/tasks/<int:id>/images', methods=['GET'])
def get_task_images(id):
    task_images = Image.query.filter_by(task_id=id).all()
    return jsonify([image.serialize() for image in task_images])
