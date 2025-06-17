def is_user_logged_in_only(logged_in, is_admin):
    return logged_in and not is_admin

print(is_user_logged_in_only(True, False))  # True (Foydalanuvchi login qilgan, lekin admin emas)
print(is_user_logged_in_only(True, True))   # False (Foydalanuvchi admin)
print(is_user_logged_in_only(False, False)) # False (Foydalanuvchi login qilmagan)
print(is_user_logged_in_only(False, True))  # False (Foydalanuvchi login qilmagan, lekin admin)