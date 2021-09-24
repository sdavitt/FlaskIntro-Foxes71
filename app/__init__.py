# import necessary modules/files/classes/packages we need for this file to work
from flask import Flask
from config import Config

# defining our app as an instance of the Flask object
app = Flask(__name__)

# configure that app using our Config class
app.config.from_object(Config)


# tell our app where it can find its routing information (from the routes file)
# note that this import specifically (and later a models import) must come after app is defined
from . import routes