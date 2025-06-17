def is_online_not_typing(online, is_typing):
    return online and not is_typing

print(is_online_not_typing(True, False))  # True (Foydalanuvchi online, lekin yozmayapti)
print(is_online_not_typing(True, True))   # False (Foydalanuvchi online va yozayapti)