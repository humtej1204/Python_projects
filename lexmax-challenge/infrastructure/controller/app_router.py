from infrastructure.controller.user.user_app_controller import UserAppController
from flask import Blueprint

class AppRouter():
    def __init__(self, app_context):
        self.app = Blueprint('app_router', __name__)
        self.user_controller = UserAppController(app_context).app
        
        self.router()
        
    def router(self):
        self.app.register_blueprint(self.user_controller, url_prefix='/users')
