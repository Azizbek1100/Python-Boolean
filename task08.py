def is_login_successful(input_username, expected_username):
    return input_username == expected_username

print(is_login_successful("user123", "user123"))  # True
print(is_login_successful("admin", "user123"))   # False
print(is_login_successful("USER123", "user123"))  # False
