def read_land_info(filename):
    """
    This is a function that reads land information from a text file specified by the `filename` parameter
    and returns this information as a list.
    """
    land_info = []  # Initialize an empty list to store land information
    
    try:
        with open(filename, 'r') as file:  # Open the file in read mode
            for line_number, line in enumerate(file, start=1):  # Iterate over each line in the file
                data = line.strip().split(',')  # Split the line into individual data fields
                if len(data) == 7:  # Check if all fields are present
                    try:
                        # Extract data and convert to appropriate types, then append to land_info list
                        kitta_number, location, direction, area, price, status, total_months_rented = [item.strip() for item in data]
                        land_info.append({
                            'kitta_number': int(kitta_number),
                            'location': location,
                            'direction': direction,
                            'area': int(area),
                            'price': int(price),
                            'status': status,
                            'total_months_rented': int(total_months_rented)
                        })
                    except ValueError:
                        # Handle error if conversion to int fails
                        print(f"Invalid data format in line {line_number}: {line}")
                else:
                    # Handle error if number of fields is not as expected
                    print(f"Invalid data format in line {line_number}: {line}")
    except FileNotFoundError:
        # Handle error if the file is not found
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")
    
    return land_info  # Return the list of land information