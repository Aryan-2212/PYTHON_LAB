x=int(input("enter a number"))
temp=x
ar=0 
while(x>0):
    ld=x%10
    ar+=ld**3
    x=x//10
if(ar==temp):
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")        