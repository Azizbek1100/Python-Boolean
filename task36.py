def is_auto_update_allowed(auto_update, mode):
    return auto_update and mode.lower() == "light"

print(is_auto_update_allowed(True, "light"))   # True (Avtomatik yangilanish yoqilgan va light modeda)
print(is_auto_update_allowed(True, "dark"))    # False (Avtomatik yangilanish yoqilgan, lekin dark modeda)
print(is_auto_update_allowed(False, "light"))  # False (Avtomatik yangilanish o‘chiq)
print(is_auto_update_allowed(False, "dark"))   # False (Avtomatik yangilanish o‘chiq)