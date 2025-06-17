def is_password_incorrect(password):
    return password != "secret123"

print(is_password_incorrect("mypassword"))  # True
print(is_password_incorrect("secret123"))   # False
print(is_password_incorrect("SECRET123"))   # True
