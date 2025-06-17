def are_months_equal(month1, month2):
    return month1.lower() == month2.lower()

print(are_months_equal("Yanvar", "yanvar"))  # True
print(are_months_equal("Fevral", "Mart"))   # False
print(are_months_equal("APRIL", "april"))   # True
