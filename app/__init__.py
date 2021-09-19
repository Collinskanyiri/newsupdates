from app.config import DevConfig
from flask import Flask
from flask_bootstrap import Bootstrap
from flask import app
from app import app
#init app
app = Flask(__name__)

#setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#initialzing Flask Extention
bootstrap = Bootstrap(app)

