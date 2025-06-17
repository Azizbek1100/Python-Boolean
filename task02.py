def is_valid_phone(phone):
    return len(phone) == 9

print(is_valid_phone("123456789"))  # True
print(is_valid_phone("12345"))      # False
print(is_valid_phone("987654321"))  # True
