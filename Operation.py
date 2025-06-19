# Function to display land information
def display_lands(land_info, status=None):
    # Printing header for land information table
    print("+----------+--------------+-------------+-------+-------------+")
    print("| Land No. | Location     | Direction   | Area  | Price       |")
    print("+----------+--------------+-------------+-------+-------------+")
    
    # Iterating over each land in the land info
    for land in land_info:
        # Checking if status is specified or land matches the status
        if status is None or land['status'] == status:
            # Printing land details in a formatted table
            print(f"| {land['kitta_number']:<9}| {land['location']:<13}| {land['direction']:<12}| {land['area']:<6}| {land['price']:<12}|")
    
    # Printing footer for land information table
    print("+----------+--------------+-------------+-------+-------------+")

# Function to rent a land
def rent_land(land_data, name, kitta_number, phone_number, duration):
    try:
        total_amount = None
        for land in land_data:
            if land['kitta_number'] == kitta_number and land['status'] == "Available":
                land['status'] = "Not Available"
                land['total_months_rented'] += duration
                # Validate phone number
                if len(phone_number) != 10 or (not phone_number.startswith(('97', '98'))):
                    raise ValueError("Invalid phone number. Phone number must be 10 characters long and start with '97' or '98'.")
                total_amount = duration * land['price']
                break
        if total_amount is not None:
            print(f"Land rented successfully. Total amount: {total_amount} NPR")
            invoice_filename = input("Enter filename for the rent invoice (without extension): ")
            invoice_filename += "_rent.txt"  # Add the '_rent.txt' extension
            generate_invoice(kitta_number, name, phone_number, duration, total_amount, 0, invoice_filename)
        else:
            print("Invalid kitta number or land not available for rent.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Function to return a rented land
def return_land(land_data, name, kitta_number, phone_number, rented_months, return_months):
    try:
        # Check if the provided kitta number exists in land data
        if not any(land['kitta_number'] == kitta_number for land in land_data):
            raise ValueError("Invalid kitta number.")

        # Validate phone number format
        if len(phone_number) != 10 or not phone_number.startswith(('97', '98')):
            raise ValueError("Invalid phone number. Phone number must start with '97' or '98' and be 10 characters long.")

        fine_per_month = 20000  # Assuming fine per month is 20000 NPR

        for land in land_data:
            # Checking if the land matches the kitta number and is rented
            if land['kitta_number'] == kitta_number and land['status'] == "Not Available":
                # Updating land status
                land['status'] = "Available"
                # Calculating total amount including any fines
                total_amount = rented_months * land['price']
                fine_months = max(0, return_months - rented_months)
                fine_amount = fine_months * fine_per_month
                total_amount += fine_amount
                print(f"Land returned successfully. Total amount: {total_amount} NPR")
                # Generating return invoice
                invoice_filename = input("Enter filename for the return invoice (without extension): ")
                invoice_filename += "_return.txt"  # Adding extension
                generate_invoice(kitta_number, name, phone_number, rented_months, total_amount, fine_amount, invoice_filename)
                # Updating total_months_rented when returning land
                land['total_months_rented'] -= rented_months
                return
        print("Invalid kitta number or land not rented.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Function to generate invoice
def generate_invoice(kitta_number, customer_name, phone_number, duration, total_amount, fine_amount, filename):
    try:
        # Encoding filename to bytes using UTF-8 encoding
        filename_bytes = filename.encode('utf-8')
        
        # Writing invoice details to file
        with open(filename_bytes, 'a', encoding='utf-8') as invoice_file:
            invoice_file.write("────────────────────── INVOICE ────────────────────\n")
            invoice_file.write(f" Kitta Number: {kitta_number:<39}\n")
            invoice_file.write(f" Customer Name: {customer_name:<37}\n")
            invoice_file.write(f" Phone Number: {phone_number:<38}\n")
            invoice_file.write(f" Duration (months): {duration:<34}\n")
            if fine_amount > 0:
                invoice_file.write(f" Fine Amount: {fine_amount} NPR{' ':<25}\n")
            invoice_file.write(f" Total Amount: {total_amount} NPR{' ':<22}\n")
            invoice_file.write("───────────────────────────────────────────────────\n")
        print(f"Invoice generated successfully. Path: {filename}")
    except IOError as e:
        print(f"Error writing invoice: {e}")