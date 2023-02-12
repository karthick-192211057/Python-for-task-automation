n = int(input("Enter the number of rows:"))  
for i in range(n):    
   print(' '*(n-i), end='')   
   print(' '.join(map(str, str(11**i))))

sum=0
row=int(input("Enter the row number: "))
sum = sum + (1 << row)
print(sum)
sum=0
for row in range(n):
   sum = sum + (1 << row)
print(sum)
