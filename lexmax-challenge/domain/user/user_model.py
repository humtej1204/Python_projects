from domain.common.base_model import Base

class User(Base):
    __tablename__ = 'user'
    db = Base.db
    
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    address = db.Column(db.Text)
    reference_address = db.Column(db.Text)
    phone_number = db.Column(db.String(20))
    
    def __repr__(self):
        return f'Task: {self.id}'
