def write_land_data(filename, land_data):
    try:
        with open(filename, 'w') as file:  # Open the file in 'w' mode to overwrite existing data
            for land in land_data:  # Iterate over each land in the land_data list
                # Write land information to the file in a comma-separated format
                file.write(f"{land['kitta_number']}, {land['location']}, {land['direction']}, {land['area']}, {land['price']}, {land['status']}, {land['total_months_rented']}\n")
    except IOError as e:
        # Handle IOError exception
        print(f"Error writing to file: {e}")
    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")