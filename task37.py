def is_language_invalid(language):
    return language.lower() not in ["uz", "en"]

print(is_language_invalid("uz"))   # False (To‘g‘ri til)
print(is_language_invalid("en"))   # False (To‘g‘ri til)
print(is_language_invalid("ru"))   # True (Xato til)
print(is_language_invalid("fr"))   # True (Xato til)