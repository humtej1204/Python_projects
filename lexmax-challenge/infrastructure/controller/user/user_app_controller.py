from flask import Blueprint, render_template, request
from application.user.user_service import UserApplicationService
import json
from domain.user.user_model import User

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
        
        # @self.app.route('/by-id', methods=['GET'])
        # def get_by_id():
        #     user = User.query.find()
            
        #     print(f'{str(user)}')
        #     return render_template("index.html")
        
        # @self.app.route('/', methods=['POST'])
        # def create():
        #     name_request = request.form['name']
        #     lastname_request = request.form['lastname']
        #     email_request = request.form['email']
        #     new_user = User(
        #         name=name_request,
        #         lastname=lastname_request,
        #         email=email_request
        #     )
            
        #     self.db.session.add(new_user)
        #     self.db.session.commit()
            
        #     print(f'{str(user)}')
        #     return json.dumps(user)
        
        # @self.app.route('/', methods=['PUT'])
        # def update():
        #     user = User.query.all()
            
        #     print(f'{str(user)}')
        #     return render_template("index.html")
        
        # @self.app.route('/', methods=['DELETE'])
        # def delete():
        #     user = User.query.all()
            
        #     print(f'{str(user)}')
        #     return render_template("index.html")
