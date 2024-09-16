x=int(input("enter a number"))
sumOfFactors=0
for i in range (1,(x),1):
    if(x%i==0):
        sumOfFactors+=i
if(sumOfFactors==x):
    print("Perfect Number")
else:    
    print("Not a perfect Number")