def is_male_or_senior(gender, age):
    return gender.lower() == "male" or age > 60

print(is_male_or_senior("male", 45))  # True (Erkak)
print(is_male_or_senior("female", 65)) # True (Yoshi katta)
print(is_male_or_senior("male", 70))   # True (Erkak va yoshi katta)
print(is_male_or_senior("female", 50)) # False (Ayol va yoshi 60 dan kichik)