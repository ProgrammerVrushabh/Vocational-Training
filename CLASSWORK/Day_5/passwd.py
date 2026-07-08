import random

s1 = ""      # lowercase
s2 = ""      # uppercase
s3 = ""      # special
s4 = ""      # digits

for i in range(256):
    if 97 <= i <= 122:
        s1 += chr(i)
    elif 65 <= i <= 90:
        s2 += chr(i)
    elif 33 <= i <= 47:
        s3 += chr(i)
    elif 48 <= i <= 57:
        s4 += chr(i)

R = random.randrange(4, 6)      # gives 4 or 5

def password():
    passwd = ""

    for i in range(R):
        passwd += random.choice(s1)
        passwd += random.choice(s2)
        passwd += random.choice(s3)
        passwd += random.choice(s4)

    if (16 <= len(passwd) <= 24 and
        any(c.islower() for c in passwd) and
        any(c.isupper() for c in passwd) and
        any(c.isdigit() for c in passwd) and
        any(c in s3 for c in passwd)):
        return passwd
    else:
        return "Password generation failed."

print(password())