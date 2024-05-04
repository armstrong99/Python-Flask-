import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Flask configuration
SECRET_KEY = '3737739903-sjsjs-s-3us'  # Set a secret key for session management

# SQLite database configuration
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://userTest:password2024@localhost/main_uav_database'
SQLALCHEMY_TRACK_MODIFICATIONS = False