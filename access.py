#accessing and modifying data in python
#use of protected attributes = single underscore - can be accessed outside the class but should not be modified directly
# use of private attributes = double underscore - cant be acessed outside the class
from datetime import datetime
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
    

    def get_email(self):
        print(f'Email accessed at {datetime.now()}')
        return self._email.strip().lower()
    
    def set_email(self, new_email):
        if '@gmail.com' not in new_email:
            raise ValueError("Email must be a Gmail address")
        self._email = new_email.strip().lower()
    
    

user_1 = User('Alice', 'Damam@gmail.com     ', 'password123')

print(user_1.get_email()) # Accessing the email using the getter method

user_1.set_email('musa@gmail.com')
print(user_1.get_email())  # Accessing the updated email using the getter method