from src.server import create_app
from src.infrastructure.configuration.database import database

app = create_app()
with app.app_context():
    database.create_all()

if __name__ == "__main__":
    app.run(debug=True)