from flask import Flask
from infrastructure.configuration.app_context import AppContext
from infrastructure.configuration.database import database
from infrastructure.configuration.environments import env
from infrastructure.configuration.swagger import swagger_config

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = env['database']['url']
    app_context = AppContext(database)
    
    swagger_config(app)
    
    from infrastructure.routes import user_routes
    user_routes(app, app_context)
    
    database.init_app(app)
    
    return app
