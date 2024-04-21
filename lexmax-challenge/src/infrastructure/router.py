from src.infrastructure.controller.api_router import ApiRouter
from src.infrastructure.controller.app_router import AppRouter


def router(app, app_context):
    api_router = ApiRouter(app_context).app
    app_router = AppRouter(app_context).app
    
    app.register_blueprint(api_router, url_prefix='/api')
    app.register_blueprint(app_router, url_prefix='/app')
