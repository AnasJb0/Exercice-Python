a = float(input("Type the first number:"))
while a==0 :
    a = float(input("Re-enter the number:"))
b = float(input("Type the second number:"))
while b==0 :
    b = float(input("Re-enter the number:"))
r =a*b
if r>0 :
    c=a
    a=b
    b=c
    print("the first number is:",a)
    print("the second number is:",b)
else :
    print("The sum is:",a+b)
    print("the product is:",a*b)

    
