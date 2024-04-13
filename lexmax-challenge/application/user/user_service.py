class UserApplicationService:
    def __init__(self, app_context):
        self.user_repo = app_context.user_repository
        
    def get_all(self):
        users = self.user_repo.get_all()
        
        return [user.serialize() for user in users]
        
    def get_by_id(self, id):
        user = self.user_repo.get_by_id(id)
        
        return user.serialize()
    
    def create(self, data):
        new_user = self.user_repo.create(data)
        
        return new_user.serialize()
    
    def update(self, id, data):
        user = self.user_repo.update(id, data)
        
        return user.serialize()
    
    def delete(self, id):
        self.user_repo.delete(id)
        
        return id