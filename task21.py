def is_uzbek_language(language):
    return language.lower() == "uz"

print(is_uzbek_language("uz"))    # True
print(is_uzbek_language("en"))    # False