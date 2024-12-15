import sys
import os

# Add the project directory to the Python path
project_home = '/home/andylie/mysite'
sys.path.insert(0, project_home)

# Import the Flask app
from app import app as application

# Ensure the database directory exists
os.makedirs(os.path.join(project_home, 'instance'), exist_ok=True)

# Update database path for PythonAnywhere
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(project_home, 'instance', 'lorawan_eval.db')
