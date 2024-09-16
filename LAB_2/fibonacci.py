x=int(input("enter the number of terms of the series\n"))
firstTerm,secTerm=0,1
count=0
if x==1:
    print(firstTerm)
else:
    print("Fibonacci Series is: \n")
    while count<x:  
      print(firstTerm)
      nthTerm=firstTerm+secTerm
      firstTerm=secTerm
      secTerm=nthTerm
      count+=1  