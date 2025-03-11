from user import User

print(User.create("gael", "gael@gmail.com", "Gael@123"))
print(User.create("gael", "gael@gmail.com", "@123"))
print(User.create("gael", "gael@gmail.com", "G@123"))
print(User.create("gael", "gael@gmail.com", "Gael@"))
print(User.create("gael", "gael@gmail.com", ""))
print(User.create("gael", "gael@gmail.com", "gael"))
print(User.create("", "gael@gmail.com", "Gael@123"))
print(User.create("                    ", "gaelgmail.com", "ael@123"))