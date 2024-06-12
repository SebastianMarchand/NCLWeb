import sys
import os

# Add project directory to sys.path
project_home = u'/home/your_username/public_html/your_project_directory'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set environment variables
os.environ['FLASK_APP'] = 'run.py'

# Activate your virtual environment
activate_this = os.path.join(project_home, 'venv/bin/activate_this.py')
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Import your application
from deploy.wsgi import app as application
