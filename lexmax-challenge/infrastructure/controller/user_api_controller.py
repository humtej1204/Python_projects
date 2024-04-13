from flask import Blueprint, request, jsonify

from application.user.user_service import UserApplicationService

class UserApiController:
    def __init__(self, app_context):
        self.app = Blueprint('user_api', __name__)
        self.user_service = UserApplicationService(app_context)
        
        self.router()
        
    def router(self):
        @self.app.route('/', methods=['GET'])
        def get_all():
            users = self.user_service.get_all()
            
            return jsonify(users)
        
        @self.app.route('/by_id/<id>', methods=['GET'])
        def get_by_id(id):
            user = self.user_service.get_by_id(id)
            
            return jsonify(user)
        
        @self.app.route('/', methods=['POST'])
        def create():
            user = self.user_service.create(request.json)
            
            return user
        
        @self.app.route('/<id>', methods=['PATCH'])
        def update(id):
            user = self.user_service.update(id, request.json)
            
            return jsonify(user)
        
        @self.app.route('/<id>', methods=['DELETE'])
        def delete(id):
            user = self.user_service.delete(id)
            
            return jsonify(user)