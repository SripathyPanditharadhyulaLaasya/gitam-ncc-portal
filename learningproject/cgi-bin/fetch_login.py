#!/usr/bin/env python

import cgi
import cgitb

cgitb.enable()

print("Content-type: text/html\n")

form = cgi.FieldStorage()

if "username" in form and "password" in form:
    username = form["username"].value
    password = form["password"].value

    # Dummy user data for demonstration purposes
    users = {
        "Student": {"username": "Student", "password": "password1"},
        "Faculty": {"username": "Faculty", "password": "password2"},
    }

    if username in users and users[username]["password"] == password:
        print(f"Welcome, {username}!")
    else:
        print("Invalid credentials")
else:
    print("Please provide both username and password.")
