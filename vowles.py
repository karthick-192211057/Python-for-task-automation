#2 vowels
n=input("enter a strng: ")
vow=0
cons=0
s=0
vowels=[]
consonants=[]
for i in range(len(n)):
    if n[i]=="a"or n[i]=="A"or n[i]=="e"or  n[i]=="E"or n[i]=="i"or n[i]=="I"or n[i]=="o"or n[i]=="O" or n[i]=="u"or n[i]=="U":
        vow= vow+1
        vowels.append(n[i])
    elif (n[i].isspace()):
        s=s+1
    else:
        cons=cons+1
        consonants.append(n[i])
print("vowels = ",vowels,vow)
print("consonants = ",consonants,cons)
