class User:
    def __init__(self, username, email, password):
        if not username or not email or not password:
            raise ValueError("Username, Email, and Password must be provided")
        self.username = username
        self.email = email
        self.password = password
       
    
    def say_hi_to_user(self, user):
        print(
              f"Sending a message to {user.username}: Hi {user.username}, welcome to our platform!, it is {self.username} "
              )

#First user input
username = input("Enter first user's username: ").strip().title()
email = input("Enter first user's email: ").strip()
password = input("Enter first user's password: ").strip()
user_1 = User(username, email, password)

# Second user input
username = input("Enter second user's username: ").strip().title()
email = input("Enter second user's email: ").strip()
password = input("Enter second user's password: ").strip()
user_2 = User(username, email, password)

# User1 says hi to User2
user_1.say_hi_to_user(user_2)
# Optionally, User2 can say hi to User1
user_2.say_hi_to_user(user_1)