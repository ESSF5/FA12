# Function to convert expiry date to sortable integer (YYYYMM)
def convert_date(month, year):
    return year * 100 + month  # Example: (1, 2025) → 202501

# Try reading the file
try:
    with open("data.dat", "r") as file:
        file_data = file.readlines()  # Read all lines from the file
except FileNotFoundError:
    print("Error: The file 'data.dat' was not found.")
    exit()  # Exit the program

# List to store extracted customer data
expired_customers = []

# Process file data
for line in file_data:
    data = line.strip().split(",")  # Split line by comma

    # Skip malformed lines
    if len(data) != 6:
        continue  

    # Extract customer details
    first_name = data[0]
    last_name = data[1]
    cc_type = data[2]
    cc_number = data[3]
    exp_month = int(data[4])  # Convert to integer
    exp_year = int(data[5])   # Convert to integer

    # Convert expiry date to YYYYMM format
    expiry_date = convert_date(exp_month, exp_year)

    # Only process expired or soon-to-expire cards (January 2025 or earlier)
    if expiry_date <= 202501:
        expired_customers.append((expiry_date, first_name, last_name, cc_type, cc_number))


# Sort by expiry date (earliest first)
expired_customers.sort(key=lambda x: x[0])
# Write results to output file
with open("expired_cards_report.txt", "w") as output:
    for expiry_date, first_name, last_name, cc_type, cc_number in expired_customers:
        # Determine card status
        status = "EXPIRED" if expiry_date < 202501 else "RENEW IMMEDIATELY"
        
        # Convert expiry_date back to YYYY-MM format
        expiry_year = expiry_date // 100
        expiry_month = expiry_date % 100
        
        # Write formatted data
        output.write(f"{first_name} {last_name} ({cc_type}) - Card: #{cc_number} | Expiry: {expiry_year}-{expiry_month:02} | Status: {status}\n")

print("Report successfully generated: 'expired_cards_report.txt'")




Barbara Hadley (Visa) - Card: #4532415491630710 | Expiry: 2022-05 | Status: EXPIRED
Benjamin Miller (MasterCard) - Card: #5299136428589478 | Expiry: 2025-01 | Status: RENEW IMMEDIATELY

# Final Project: Credit Card Report
# ICS3U - Fatima

# Function to convert expiry date to sortable integer (YYYYMM)
def convert_date(month, year):
    return year * 100 + month  # Example: (1, 2025) → 202501

# Try reading the file
try:
    with open("data.dat", "r") as file:
        file_data = file.readlines()  # Read all lines from the file
except FileNotFoundError:
    print("Error: The file 'data.dat' was not found.")
    exit()  # Exit the program

# List to store extracted customer data
expired_customers = []

# Process file data
for line in file_data:
    data = line.strip().split(",")  # Split line by comma

    # Skip malformed lines
    if len(data) != 6:
        continue  

    # Extract customer details
    first_name = data[0]
    last_name = data[1]
    cc_type = data[2]
    cc_number = data[3]
    exp_month = int(data[4])  # Convert to integer
    exp_year = int(data[5])   # Convert to integer

    # Convert expiry date to YYYYMM format
    expiry_date = convert_date(exp_month, exp_year)

    # Only process expired or soon-to-expire cards (January 2025 or earlier)
    if expiry_date <= 202501:
        expired_customers.append((expiry_date, first_name, last_name, cc_type, cc_number))

# Sort by expiry date (earliest first)
expired_customers.sort(key=lambda x: x[0])

# Write results to output file
with open("expired_cards_report.txt", "w") as output:
    for expiry_date, first_name, last_name, cc_type, cc_number in expired_customers:
        # Determine card status
        status = "EXPIRED" if expiry_date < 202501 else "RENEW IMMEDIATELY"
        
        # Convert expiry_date back to YYYY-MM format
        expiry_year = expiry_date // 100
        expiry_month = expiry_date % 100
        
        # Write formatted data
        output.write(f"{first_name} {last_name} ({cc_type}) - Card: #{cc_number} | Expiry: {expiry_year}-{expiry_month:02} | Status: {status}\n")

print("Report successfully generated: 'expired_cards_report.txt'")
