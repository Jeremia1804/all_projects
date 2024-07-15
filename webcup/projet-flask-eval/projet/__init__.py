from flask import Flask

app = Flask("projet",static_folder='static')

from projet.models import *
from projet.config import *
from projet.configdatabase import *
from projet.controllers import *
# from projet.controllers.home import MoiController, ToiController

# app.add_url_rule('/salut','test_salut',MoiController.salut, methods=['GET'])
# app.add_url_rule('/quoi','test_quoi',ToiController.salut, methods=['GET'])
# app.add_url_rule('/court','test_court',ToiController.court, methods=['GET'])
