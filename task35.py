def is_user_typing_anonymously(is_typing, username):
    return is_typing and username == ""


print(is_user_typing_anonymously(True, ""))     # True (Noaniq foydalanuvchi yozmoqda)
print(is_user_typing_anonymously(True, "Ali"))  # False (Foydalanuvchi yozmoqda, lekin aniq)
print(is_user_typing_anonymously(False, ""))    # False (Foydalanuvchi yozmayapti)
print(is_user_typing_anonymously(False, "Ali")) # False (Foydalanuvchi yozmayapti)