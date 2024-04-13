from flask_swagger_ui import get_swaggerui_blueprint

def swagger_config(app):
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger/swagger.json'

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Lexmax User API"
        },
    )

    app.register_blueprint(swaggerui_blueprint)