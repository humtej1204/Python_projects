from flask import Flask
from flask_cors import CORS
from src.infrastructure.configuration.app_context import AppContext
from src.infrastructure.configuration.database import database
from src.infrastructure.configuration.environments import env
from src.infrastructure.configuration.swagger import swagger_config

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = env['database']['url']
    app_context = AppContext(database)
    
    swagger_config(app)
    
    from src.infrastructure.router import router
    router(app, app_context)
    
    database.init_app(app)
    
    CORS(app, resources={
        r"/api/*": {
            "origins": [
                "http://localhost:*",
                "http://127.0.0.1:*",
            ]
        }
    })
    
    return app
