# here in the config file we're going to define some variables/a class that help configure our application

# imports - getting some additional functionality through python modules
import os

# setting the base directory of the entire project - so that our computer knows where to find files within the project
# telling flask the location of the 'foxes71-flask' folder
basedir = os.path.abspath(os.path.dirname(__name__))

# setting what are known as the configuration variables for our flask app
class Config:
    """
        Set config variables for our flask app
        Use environmental variables where necessary to keep things hidden
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')