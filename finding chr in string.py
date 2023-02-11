s1=input("enter ")
s2=input("enter ")
s=s1.lower()
res=None
for i in range (0,len(s)):
    if s[i]==s2:
        res=True
        print(s[i],"index",s.index (s[i]))
if res==None:
    print("not ture")
