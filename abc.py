def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Input number
num = 5

# Calculate factorial
result = factorial(num)

# Display the result
print(f"The factorial of {num} is {result}")
