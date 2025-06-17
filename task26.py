def is_valid_mode(mode):
    return mode.lower() in ["light", "dark"]

print(is_valid_mode("light"))  # True
print(is_valid_mode("dark"))   # True
print(is_valid_mode("blue"))   # False
