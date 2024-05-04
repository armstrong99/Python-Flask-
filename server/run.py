from app import app, db
from app.models import Drone, Task, Image

# Initialize database
with app.app_context():
    # db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000, debug=True)
