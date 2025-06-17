def is_discount_applicable(price):
    return price > 500000

print(is_discount_applicable(600000))  # True
print(is_discount_applicable(500000))  # False
print(is_discount_applicable(450000))  # False
