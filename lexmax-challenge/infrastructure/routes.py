from infrastructure.controller.user_api_controller import UserApiController
from infrastructure.controller.user_app_controller import UserAppController

def user_routes(app, app_context):
    user_api_routes = UserApiController(app_context).app
    user_app_routes = UserAppController(app_context).app
    
    app.register_blueprint(user_api_routes, url_prefix='/api')
    app.register_blueprint(user_app_routes, url_prefix='/app')
