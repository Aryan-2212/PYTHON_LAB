per=int(input("Enter the percentage"))
if per>=90:
    grade='A'
elif per>=80:
    grade='B'
elif per>=70:
    grade='C'
elif per>=60:
    grade='D'
elif per>=50:
    grade='E'
else:
    grade='F'   

print(grade)       