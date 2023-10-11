a = int(input("type the age of the inhabitants:"))
while a<=0 :
    a =int(input("Re-enter the age:"))
s = input("type the sex of the inhabitants:")
while s!="man" and s!="woman"  :
    s =input("Re- enter the sex:")
if a==20 and s=="man" :
    print("He must pay tax")
elif (a>=18 and a<=35) and s=="woman" :
    print("She must pay tax")
else :
    print("You don't have to pay tax")
