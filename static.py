# static attributes in python
from datetime import datetime
class User:
    user_count = 0

    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
        User.user_count += 1

    @property
    def email(self):
        print(f'Email accessed at {datetime.now()}')
        return self._email.strip().lower()
    
    @email.setter
    def email(self, new_email):
        if '@gmail.com' not in new_email:
            raise ValueError("Email must be a Gmail address")
        self._email = new_email.strip().lower()

user_1 = User('Alice', 'alise@gmail.com', 'password123')
user_2 = User('Bob', 'bob@gmail.com', 'password456')

print(f'Total users created: {User.user_count}')  # Accessing the static attribute
print (f'No of :{user_2.user_count}')
print(user_1.email)  # Accessing the email property
print(user_2.email)  # Accessing the email property

user_1.email = 'mum@gmail.com'
print(user_1.email)  # Accessing the updated email property
print(f'Total users created: {User.user_count}')  # Accessing the static attribute again