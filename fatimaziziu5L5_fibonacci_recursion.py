Python Code File: u5L5_fibonacci_recursion.py
# Function to get a valid whole number from the user
def getNum(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num > 0:
                return num
            else:
                print("Please enter a positive whole number.")
        except ValueError:
            print("That's not a valid number. Try again.")

# Recursive function to find the nth Fibonacci number
def fib(n):
    if n == 1 or n == 2:  # Base cases: first two terms are 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)  # Recursive formula

# Main program
print("Program for printing the Fibonacci sequence!")
num_terms = getNum("Please input a whole number: ")

# Generate and print the Fibonacci sequence
for i in range(1, num_terms + 1):
    print(fib(i), end=" ")

print()
