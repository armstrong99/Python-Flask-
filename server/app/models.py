from app import db

# Association Table for Many-to-Many Relationship

task_drone_association = db.Table(
    'task_drone_association',
    db.Column('task_id', db.Integer, db.ForeignKey('task.id')),
    db.Column('drone_id', db.Integer, db.ForeignKey('drone.id'))
)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(256))
    is_executed = db.Column(db.Boolean, default=False) 
    drones = db.relationship('Drone', secondary=task_drone_association, backref=db.backref('tasks', lazy='dynamic'))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'drones': [drone.serialize() for drone in self.drones],
            'is_executed': self.is_executed,
        }

class Drone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }



class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    image_url = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f'<Image {self.id}>'

    def serialize(self):
        return {
            'id': self.id,
            'task_id': self.task_id,
            'image_url': self.image_url
        }
