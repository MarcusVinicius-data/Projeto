class Connection:
    def __init__(self, host='loclhost') -> None:
        self.host = host
        self.user = None
        self.password = None
        
    def set_user(self, user):
        self.user = user
    
    def set_password(self, password):
        set.password = password
        
            
    @classmethod    
    def create_whit_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password =  password
        return connection
    
c1 = Connection.create_whit_auth('Marcus', '1234')
#c1.set_user("Marcus")
#c1.set_password('123')
print(c1.user)
print(c1.password)


