def login():
    users = {
        "user1": {"username": "user1", "password": "password1"},
        "user2": {"username": "user2", "password": "password2"},
    }

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username]["password"] == password:
        print(f"Welcome, {username}!")
    else:
        print("Invalid credentials")

if __name__ == '__main__':
    login()


