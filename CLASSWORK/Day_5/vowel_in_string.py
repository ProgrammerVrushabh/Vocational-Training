"""s1=input("enter a string: ")
count=0
for i in range(len(s1)):
    if s1[i] in 'aeiouAEIOU':
        count+=1
print("number of vowels in the string is:", count)"""


#repeated method


'''s2=input("enter a string: ")
count=0
for i in range(len(s2)):
    if s2[i]=='a' or s2[i]=='e' or s2[i]=='i' or s2[i]=='o' or s2[i]=='u' or s2[i]=='A' or s2[i]=='E' or s2[i]=='I' or s2[i]=='O' or s2[i]=='U':
        count+=1
        
print("number of vowels in the string is:", count)'''

#indivisual count of vowels
'''s3=input("enter a string: ")
ac,ec,ic,oc,uc=0,0,0,0,0
for i in s3:
    if i=='a' or i=='A':
        ac+=1
    elif i=='e' or i=='E':
        ec+=1
    elif i=='i' or i=='I':
        ic+=1
    elif i=='o' or i=='O':
        oc+=1
    elif i=='u' or i=='U':
        uc+=1
print("individual counts of vowels are:")
print("a=",ac)
print("e=",ec)
print("i=",ic)
print("o=",oc)
print("u=",uc)
print("total number of vowels in the string is:",ac+ec+ic+oc+uc)'''

#List method
'''

s4=input("enter a string: ")
print("number of vowels in the string is:",len([i for i in s4 if i in 'aeiouAEIOU']))'''

#replace function
'''s5=input("enter a string: ")
s6=s5.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','').replace('A','').replace('E','').replace('I','').replace('O','').replace('U','')
print("number of vowels in the string is:",len(s5)-len(s6))'''
