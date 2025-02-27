import random
import string

password = ""
loop = 25

while loop > 0:
    password = password + random.choice(string.ascii_letters)
    loop = loop - 1

print(password)