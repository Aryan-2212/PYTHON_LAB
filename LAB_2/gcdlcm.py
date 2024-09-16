n1 = int(input("Enter a number"))
n2 = int(input("Enter a number"))
a = n1
b = n2
while b!=0:
    temp = b
    b = a%b
    a = temp

gcd = a
lcm = int((n1*n2)/gcd)

print("\nLCM (" + str(n1) + ", " + str(n2) + ") = ", lcm)
print("GCD (" + str(n1) + ", " + str(n2) + ") = ", gcd)