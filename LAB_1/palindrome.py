x=int(input("enter a number "))
temp=x
rev=0
while(x>0):
    ld=x%10
    rev=rev*10+ld
    x=x//10
if(temp==rev):
    print("Palindrome Number")
else:        
    print("Not a Palindrom Number")