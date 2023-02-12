import itertools
digit=int(input("enter the number of digits:"))
num=input("enter the number:")

while True:
    x=True
    if (len(num)!=digit):
        x=False
        print("invalid input, OUT of LIMIT!")
    elif digit==2:
        if num[0]==num[1]:
            print("invalid input, unique permutation")
            x=False
    elif digit==3:
        if num[0]==num[1]==num[2]:
            print("invalid input, unique permutation")
            x=False
    break
if x==True:
    nums=list(num)
    permutations=list(itertools.permutations(nums))
    p=([''.join(permutation)for permutation in permutations])
    p.remove(num)
    print(p)
