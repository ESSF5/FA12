def swap(B, p, q):
    # Swap elements at index p and q in the array B
    temp = B[p]
    B[p] = B[q]
    B[q] = temp

def sort(C):  # Exchange Sort
    for i in range(len(C) - 1):  # Loop through each element except the last
        for j in range(i + 1, len(C)):  # Compare with subsequent elements
            if C[i] > C[j]:  # Swap if out of order
                swap(C, i, j)

# Test the code
A = [4, -1, 7, 3, 9, 0, 11, 2, 14]
sort(A)
print(A)
