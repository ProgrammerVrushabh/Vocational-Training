import random

s1 = ""      # lowercase
s2 = ""      # uppercase
for i in range(256):
    if 97 <= i <= 122:
        s1 += chr(i)
    elif 65 <= i <= 90:
        s2 += chr(i)
message = input("Enter a message: ")
shift = 3
encrypted = ""

for ch in message:
    if ch in s1:
        pos = s1.index(ch)
        encrypted += s1[(pos + shift) % 26]
    elif ch in s2:
        pos = s2.index(ch)
        encrypted += s2[(pos + shift) % 26]
    else:
        encrypted += ch

print("Encrypted message:", encrypted)