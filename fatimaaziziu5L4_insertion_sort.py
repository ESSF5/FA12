# Swap function to exchange two elements in a list
def swap(B, p, q):
    temp = B[p]
    B[p] = B[q]
    B[q] = temp

# Insertion sort function to sort a list alphabetically
def iSort(A):
    for i in range(1, len(A)):  # Start from the second element
        for j in range(i, 0, -1):  # Compare backwards
            if A[j] < A[j - 1]:  # If current element is smaller, swap
                swap(A, j, j - 1)
            else:
                break

# Function to trim the newline character from strings
def trim(word):
    return word.strip()

# Function to print words in rows of 10
def printIt(A):
    for i in range(0, len(A), 10):  # Step by 10 to create rows
        print(" ".join(A[i:i + 10]))

# Main program
filename = "words40.dat"

try:
    # Open the file and read words
    with open(filename, "r") as file:
        words = [trim(word) for word in file.readlines()]

    # Sort the words alphabetically
    iSort(words)

    # Print the sorted words
    printIt(words)
    print(f"\n{len(words)} words.")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
