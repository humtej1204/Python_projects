from infrastructure.configuration.database import database

class Base(database.Model):
    __abstract__ = True
    db = database

    id = database.Column(db.Integer, primary_key=True)
    
    def serialize(self):
        return serialize_model(self)
    
def serialize_model(model):
    return {column.name: getattr(model, column.name) for column in model.__table__.columns}
