def triangle(ch, num):
    if num == 1:  # Base case: smallest row
        print(ch)  # Print the smallest row
        return
    else:  # Recursive step
        print(ch * num)  # Print the current row first
        triangle(ch, num - 1)  # Call the function with num - 1

# Example usage:
ch = "#"
n = 8
triangle(ch, n)
