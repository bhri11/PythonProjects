import bcrypt

password = b"thisismypassword" # b used for make string byte

hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

# entered_password = input("Enter password to login: ")
# entered_password = bytes(entered_password, encoding="utf-8")
#
# if bcrypt.checkpw(entered_password,hashed):
#     print("Login successful")
# else:
#     print("Invalid password")