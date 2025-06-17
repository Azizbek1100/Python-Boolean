from getpass import getpass

password = getpass("password: ")
confirm = getpass("confirm password: ")

result = pasword == confirm
print(result)