'''Name -> Sushain Sanan 
SID -> 21107065
Branch -> Mechanical'''
#Question 1
print("QUESTION 1")
V = int(input("Enter the First Number:"))
U = int(input("Enter the Second Number:"))
S = int(input("Enter the Third Number:"))
Average = (V + U + S)/3 
print("The Average of these three numbers is :",Average)

#Question 2
print("QUESTION 2")
GI = int(input("Enter the Gross Income :"))
Dep = int(input("Enter the Number of Dependents :"))
taxable_income= ( (GI - 10000) - Dep*3000 )
Tax= taxable_income*(0.2)
print(f"Your Tax is : {Tax}")

#Question 3
print("QUESTION 3")
N = int(input("Enter seconds: "))

Mins = N // 60
Secs = N % 60

print(Mins, "Minutes and", Secs, "Seconds")

#Question 4
print("QUESTION 4")
M = 25 
num = '25'
N = int(num) 
new = 25.0 
O = int(new)
D=M+N+O 
D=str(D)
print(D)
print(type(D))

#Question 5
print("QUESTION 5")
from math import pi,sin,cos
deg=0
y=0
z=0
for deg in range(0,346,15):
    rad=deg*(pi/180)
    y=round(sin(rad),4)
    z=round(cos(rad),4)
    
    print(deg,"---",y,z)
    
     

