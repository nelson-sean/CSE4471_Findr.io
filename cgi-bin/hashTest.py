import bcrypt

password = b"Hello World!"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

if bcrypt.checkpw(password, hashed):
    print("It Matches!")
    print(str(hashed))
else:
    print("AWW")
