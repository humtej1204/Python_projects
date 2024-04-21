from src.domain.user.user_model import User

class UserRepository():
    def __init__(self, db):
        self.db = db
        
    def get_all(self):
        users = self.db.session.execute(
            self.db.select(User)
        ).scalars()
        return users
    
    def get_by_id(self, id):
        user = self.db.session.execute(
            self.db.select(User)
            .filter_by(id=id)
        ).scalar_one()
        return user
    
    def create(self, data):
        new_user = User(
            name=data['name'],
            lastname=data['lastname'],
            email=data['email'],
            address=data.get('address'),
            reference_address=data.get('reference_address'),
            phone_number=data.get('phone_number')
        )
        
        self.db.session.add(new_user)
        self.db.session.commit()
        
        return new_user
    
    def update(self, id, data):
        user = self.get_by_id(id)
        
        user.name = data['name']
        user.lastname = data['lastname']
        user.email = data['email']
        user.address = data.get('address', user.address)
        user.reference_address = data.get('reference_address', user.reference_address)
        user.phone_number = data.get('phone_number', user.phone_number)
    
        self.db.session.commit()
        
        return user
    
    def delete(self, id):
        user = self.get_by_id(id)
        
        self.db.session.delete(user)
        self.db.session.commit()
        
        return id
