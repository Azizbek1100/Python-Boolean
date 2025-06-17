def is_session_inactive(logged_in, session_time):
    return not logged_in or session_time == 0


print(is_session_inactive(False, 30))  # True (Foydalanuvchi login qilmagan)
print(is_session_inactive(True, 0))    # True (Sessiya vaqti 0)
print(is_session_inactive(False, 0))   # True (Login qilmagan va sessiya vaqti 0)
print(is_session_inactive(True, 15))   # False (Sessiya aktiv)