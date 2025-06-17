def is_name_capitalized(name):
    return name and name[0].isupper()

print(is_name_capitalized("Ali"))    # True (Ism bosh harfi katta)
print(is_name_capitalized("ali"))    # False (Ism bosh harfi kichik)
print(is_name_capitalized("John"))   # True (Ism bosh harfi katta)
print(is_name_capitalized(""))       # False (Ism berilmagan)