def is_long_password(password):
    return len(password) >= 8

print(is_long_password("qwerty12"))  # True
print(is_long_password("12345"))     # False
print(is_long_password("password"))  # True
