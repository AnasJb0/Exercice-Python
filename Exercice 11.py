a = float(input("Enter the first number:"))
while a==0 :
    a = float(input("Re-enter the number:"))
b = float(input("Enter the second number:"))
while b==0 :
    b = float(input("Re-enter the second number:"))
r = a*b
if r>0 :
    print("Both numbers have the same sign")
else :
    print("The two numbers do not have the same sign")
print("The result is:",r)