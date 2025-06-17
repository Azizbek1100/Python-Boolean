def is_temperature_safe(temperature):
    return temperature < 37.5 or temperature > 42

print(is_temperature_safe(36.5))  # True (Harorat xavfli emas)
print(is_temperature_safe(40.0))  # False (Harorat xavfli)
print(is_temperature_safe(43.0))  # True (Harorat xavfli emas)
print(is_temperature_safe(37.5))  # False (Harorat xavfli)