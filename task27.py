def is_product_available(in_stock, on_delivery):
    return in_stock or on_delivery

print(is_product_available(True, False))  # True
print(is_product_available(False, True))  # True
print(is_product_available(False, False)) # False
