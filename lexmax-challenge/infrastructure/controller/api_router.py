from infrastructure.controller.user.user_api_controller import UserApiController
from flask import Blueprint

class ApiRouter():
    def __init__(self, app_context):
        self.app = Blueprint('api_router', __name__)
        self.user_controller = UserApiController(app_context).app
        
        self.router()
        
    def router(self):
        self.app.register_blueprint(self.user_controller, url_prefix='/users')
