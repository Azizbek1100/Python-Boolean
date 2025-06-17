def is_pin_invalid(pin, correct_pin):
    return pin != correct_pin or len(pin) != 4


print(is_pin_invalid("1234", "5678"))  # True (PIN noto‘g‘ri)
print(is_pin_invalid("5678", "5678"))  # False (PIN to‘g‘ri)
print(is_pin_invalid("123", "1234"))   # True (PIN 4 xonali emas)
print(is_pin_invalid("99999", "9999")) # True (PIN 4 xonali emas)