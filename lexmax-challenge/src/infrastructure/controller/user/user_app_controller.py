from flask import Blueprint, render_template, request
from src.application.user.user_service import UserApplicationService

class UserAppController:
    def __init__(self, app_context):
        self.app = Blueprint('user_app', __name__)
        self.user_service = UserApplicationService(app_context)
        
        self.router()

    def router(self):
        @self.app.route('/', methods=['GET'])
        def get_all():
            user = self.user_service.get_all()
            
            print(f'data: {str(user)}')
            return render_template("index.html")
