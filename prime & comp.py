n=[1,2,3,4,5,6]
prime=[]
composite=[]
for num in n:
    if(num==2):
        prime.append(num)
    else:
        for i in range (2,num):
            if(n%i==0):
                composite.append(num)
                break
            else:
                prime.append(num)
                break
print("prime=",prime.len(prime))
print("composite=",composite.len(composite))

