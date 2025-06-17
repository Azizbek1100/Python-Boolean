def is_password_invalid(password):
    return password not in ["", "secret"]

print(is_password_invalid(""))        # False (Bo‘sh parol)
print(is_password_invalid("secret"))  # False (Tog‘ri parol)
print(is_password_invalid("mypassword"))  # True (Xato parol)
print(is_password_invalid("SECRET"))  # True (Xato parol)