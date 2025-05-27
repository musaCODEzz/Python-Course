
# setter and getter propperties in python
from datetime import datetime
class User:
    def __init__(self, username, email, password):
        self.userername = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print(f'Email accessed at {datetime.now()}')
        return self._email.strip().lower()
    
    @email.setter
    def email(self, new_email):
        if '@gmail.com' not in new_email:
            raise ValueError("Email must be a Gmail address")
        self._email = new_email.strip().lower()

user_1 = User('musa', 'musa@gmail.x', 'hjhkjj')
print(user_1.email)

user_1.email = 'jhjhkj@gmail.com'
print(user_1.email)