import math

def find_best_dimensions(N):
    # This function finds the best dimensions (x, y) that minimize the perimeter for N photos
    min_perimeter = float('inf')
    best_x, best_y = 0, 0

    # Search for factors up to the square root of N
    for x in range(1, math.isqrt(N) + 1):
        if N % x == 0:  # x is a factor
            y = N // x  # Find the corresponding y
            perimeter = 2 * (x + y)
            if perimeter < min_perimeter:
                min_perimeter = perimeter
                best_x, best_y = x, y
    
    return best_x, best_y, min_perimeter

def school_yearbook_program():
    print("Welcome to the school yearbook program!")
    
    while True:
        user_input = input("Please input your number of photographs (or type 'done' to finish): ")
        
        if user_input.lower() == "done":
            print("Goodbye!")
            break
        
        if user_input.isdigit():
            num_photos = int(user_input)
            
            if num_photos < 1:
                print(f"{num_photos} is not a valid number of photos. Please enter a positive number.")
            else:
                # Find the best dimensions and the minimum perimeter
                x, y, min_perimeter = find_best_dimensions(num_photos)
                print(f"Minimum perimeter is {min_perimeter} with dimensions {x} x {y}.")
        else:
            print("Invalid input. Please enter a positive number or 'done' to exit.")

# Run the program
school_yearbook_program()
