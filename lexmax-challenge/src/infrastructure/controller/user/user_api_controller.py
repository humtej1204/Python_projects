from flask import Blueprint, request
from src.utils.app_response import ApiResponse

from src.application.user.user_service import UserApplicationService

class UserApiController:
    def __init__(self, app_context):
        self.app = Blueprint('user_api', __name__)
        self.user_service = UserApplicationService(app_context)
        
        self.router()
        
    def router(self):
        @self.app.route('/', methods=['GET'])
        def get_all():
            users = self.user_service.get_all()
            
            return ApiResponse().success(users)
        
        @self.app.route('/by_id/<id>', methods=['GET'])
        def get_by_id(id):
            user = self.user_service.get_by_id(id)
            
            return ApiResponse().success(user)
        
        @self.app.route('/', methods=['POST'])
        def create():
            user = self.user_service.create(request.json)
            
            return ApiResponse().success(user, 201)
        
        @self.app.route('/<id>', methods=['PATCH'])
        def update(id):
            user = self.user_service.update(id, request.json)
            
            return ApiResponse().success(user)
        
        @self.app.route('/<id>', methods=['DELETE'])
        def delete(id):
            user = self.user_service.delete(id)
            
            return ApiResponse().success(user, 200)