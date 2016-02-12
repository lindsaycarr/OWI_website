
from flask import Flask

app = Flask(__name__.split()[0], instance_relative_config=True)

# Loads configuration information from config.py and instance/config.py
app.config.from_object('config')  # load configuration before passing the app object to other things
app.config.from_pyfile('config.py')


import views

# Now we can access the configuration variables via app.config["VAR_NAME"].