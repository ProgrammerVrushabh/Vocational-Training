import random
flag = True
count1=0
print("User 1")
while ( flag):
    a=int(input("Enter number :"))
    b= random.randint(1,6)
    print("system generated: ",b)
    count1+=1
    if a==b:
        print("\n score matched: score= ", count1)
        flag= False
        break
    print("\n not matched, try again")

print("\n User 2")
print()
flag = True
count2=0
while ( flag):
    a=int(input("Enter number :"))
    b= random.randint(1,6)
    print("system generated: ",b)
    count2+=1
    if a==b:
        print("\n score matched: score= ", count2)
        flag= False
        break
    print("\n not matched, try again ")
if count1<count2:
    print(" User 1 guessed earlier than User 2\n . User 1 wins")
elif count1== count2:
    print("User 1 and  User 2 guessed in  same time. \n Draw")
else:
    print("User 2 wins")