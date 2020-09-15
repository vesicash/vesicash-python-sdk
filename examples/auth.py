from vesicashapi.auth import Auth
"""
Login example
"""

login = Auth.login(
    username="precious@vesicash.com",
    password="test"
)

print(login)

"""
Sign up example
"""

signup = Auth.signup(
    email_address="precious@vesicash.com",
    password="test"
)

print(signup)