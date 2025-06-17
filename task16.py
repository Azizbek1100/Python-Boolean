def is_fully_logged_in(login, password):
    return bool(login) and bool(password)

print(is_fully_logged_in("user123", "mypassword"))  # True
print(is_fully_logged_in("", "mypassword"))        # False
print(is_fully_logged_in("user123", ""))           # False
