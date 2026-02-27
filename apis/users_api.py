from apis.base_api import BaseAPI

class UsersApi(BaseAPI):
    def __init__(self, base_url: str, session):
        super().__init__(base_url, session)
        
    def create_user(self, data):
        return self.post("/createAccount", data=data)

    def login_user(self, data):
        return self.post("/verifyLogin", data=data)