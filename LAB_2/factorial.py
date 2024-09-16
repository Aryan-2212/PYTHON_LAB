x=int(input("enter a number"))
factorial=1
if(x==0):
    print("factorial is : ", factorial)
else:   
   for i in range(1,x+1):
        factorial*=i
print("Factorial is : ",factorial)    