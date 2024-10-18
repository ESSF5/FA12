def find_pythagorean_triples(n):
    triples = []  # To store the triples
    
    for num in range(3, n+1):
        if num % 2 != 0:  # If num is odd
            a = num**2
            b = (num // 2) * (num + 1)
            c = b + 1
        else:  # If num is even
            a = num
            m = (num**2) // 4
            b = m - 1
            c = m + 1
        
        triples.append([a, b, c])  # Append the triple to the list
    
    return triples

# Example usage
upper_limit = int(input("Please enter an upper limit: "))
triples = find_pythagorean_triples(upper_limit)

for triple in triples:
    a, b, c = triple
    print(f"[{a}, {b}, {c}] => {a} + {b**2} = {c**2}")
