from projet.db import db
from projet import app
from flask_migrate import Migrate

postgresql = {'host': 'localhost',
         'user': 'postgres',
         'passwd': 'postgres',
         'db': 'eval'}

postgresqlConfig = "postgresql+psycopg2://{}:{}@{}/{}".format(postgresql['user'], postgresql['passwd'], postgresql['host'], postgresql['db'])

app.config['SQLALCHEMY_DATABASE_URI'] = postgresqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app,db)

db.init_app(app)


def create_tables():
    db.create_all()

with app.app_context():
    app.before_request_funcs = [(None, create_tables())]
    pass
    
