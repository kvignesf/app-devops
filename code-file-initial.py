# Simple program to print the first 5 Fibonacci numbers

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Print first 5 Fibonacci numbers
fibonacci(5)
