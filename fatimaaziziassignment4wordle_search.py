# Function to load Wordle answers and game days into a dictionary
def load_wordle_data(filename):
    """Reads the Wordle file and stores data in a dictionary."""
    wordle_dict = {}
    try:
        # Open the file and read each line
        with open(filename, "r") as file:
            for line in file:
                day, word = line.strip().split(",")  # Split day and word
                wordle_dict[word] = int(day)  # Store in dictionary
    except FileNotFoundError:
        print("Error: File not found.")
    return wordle_dict

# Function to search for a word and return its game day
def search_word(wordle_dict, word):
    """Searches for a word and returns its game day if found."""
    word = word.lower()  # Convert word to lowercase to handle case insensitivity
    if word in wordle_dict:
        return f"'{word}' appeared on day {wordle_dict[word]}."
    else:
        return f"'{word}' was not found in the database."

# Main program
def main():
    # Define the filename with the Wordle answers
    filename = "wordle_answers.txt"
    
    # Load the Wordle data from the file
    wordle_data = load_wordle_data(filename)

    if wordle_data:
        # Ask the user to input a word
        user_word = input("Enter a Wordle word to search: ").strip().lower()
        # Output the result of the search
        print(search_word(wordle_data, user_word))

# Run the program
if __name__ == "__main__":
    main()
