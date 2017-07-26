import bcrypt

password = "Hello World!"

hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

print(hashed.decode())

if bcrypt.checkpw(password.encode(), hashed):
    print("It Matches!")
    print(str(hashed))
else:
    print("AWW")
