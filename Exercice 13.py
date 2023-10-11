n = int(input("type the number of photocopies:"))
while n<=0 :
    n = int(input("Re-enter the number of photocopies:"))
if n<=10 :
    f = n*0.30
elif n>10 and n<=30 :
    f = 10*0.30+(n-10)*0.25
else :
    f = 10*0.30+20*0.25+(n-30)*0.2
print("the invoice is:",f)

    
