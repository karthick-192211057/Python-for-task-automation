grade=input("Enter the grade of the Employee:")
s=int(input("Enter Employee's salary:"))
if (s>=0):
    if (grade=='A' or grade=='a'):
        bonus=s*(0.05)
        if (s<10000):
            bonus+=s*(0.02)
    elif (grade=='B' or grade=='b'):
        bonus=s*(0.1)
        if (s<10000):
            bonus+=s*(0.2);
    else:
        print("\nEnter a valid Grade (A or B)!!")
    else:
        print("Enter Valid Salary Amount")
	
print("Enter Valid Salary Amount")
print("Bonus = ",bonus)
print("sal = ",s+bonus)
	
	
