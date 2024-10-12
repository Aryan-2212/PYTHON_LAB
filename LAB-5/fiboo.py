def fibonacci(n):
    sequence=[0,1]
    for i in range(2,n):
        sequence.append(sequence[i-1] + sequence[i-2])
        return sequence[:n]
    
def sq_fibonacci(n):
    fib_numbers=fibonacci(n)
    squared=list(map(lambda x: x**2, fib_numbers))
    return squared

n= int(input("Enter the number of fibonacci numbers: "))

result=sq_fibonacci(n)
print("Square of first", n, "Fibonacci numbers are:", result)
def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

def square(x):
    return x * x

def square_fibonacci(n):
    fib_numbers = fibonacci(n)
    return list(map(square, fib_numbers))

N = 10
result = square_fibonacci(N)
print(result)