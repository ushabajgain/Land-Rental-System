# Importing necessary functions from operations, read, and write modules
from Operation import display_lands, rent_land, return_land  # Ensure operations.py is in the same directory as Main.py
from Read import read_land_info
from Write import write_land_data

# Main function to control the flow of the land management system
def main():
    filename = "land_data.txt"
    
    # Attempt to read land data from the file
    try:
        land_data = read_land_info(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")  # Handling file not found error
        return
    
    # Main loop for user interaction
    while True:
        print("============================================================================")
        print("                         Techno Property Nepal                              ")
        print("============================================================================")
        print("           Premium rental lands by Techno Property Nepal,                   ")
        print("             Nepal's top private real estate company.                       ")
        print()
        print("Select operation:")
        print()
        print("1. Show available and unavailable lands")
        print("2. Rent land")
        print("3. Return land")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        try:
            if choice == "1":  # Display all available lands
                display_lands(land_data, status="Available")
            elif choice == "2":  # Rent a land
                display_lands(land_data, status="Available")
                name = input("Enter customer name: ")
                kitta_number = int(input("Enter Kitta number of the land to rent: "))
                # Validate kitta number
                if kitta_number < 0:
                    raise ValueError("Kitta number cannot be negative.")
                # Check if the provided kitta number exists
                if not any(land['kitta_number'] == kitta_number for land in land_data):
                    raise ValueError("Invalid kitta number.")
                phone_number = input("Enter customer phone number: ")
                if len(phone_number) != 10:
                    raise ValueError("\n###############################################################################"
                        "\nPhone number must be 10 characters long and must start with '97' or '98'"
                        "\n###############################################################################\n"
                        "\n-------------------------------------------------------------------------------\n")
                # Validate phone number format
                if not phone_number.startswith(('97', '98')):
                    raise ValueError("\n###############################################################################"
                        "\nPhone number must be 10 characters long and must start with '97' or '98'"
                        "###############################################################################\n"
                        "\n-------------------------------------------------------------------------------\n")
                duration = int(input("Enter duration of rent (in months): "))
                rent_land(land_data, name, kitta_number, phone_number, duration)
                write_land_data(filename, land_data)  # Write updated data to file
            elif choice == "3":  # Return a rented land
                print("Currently rented lands:")
                display_lands(land_data, status="Not Available")
                name = input("Enter customer name: ")
                phone_number = input("Enter customer phone number: ")
                if len(phone_number) < 9:
                    raise ValueError("Phone number must start with '97' or '98' and be 10 characters long.")
                kitta_number = int(input("Enter Kitta number of the land to return: "))
                if kitta_number < 0:
                    raise ValueError("Kitta number cannot be negative.")
                rented_months = int(input("Enter the number of months the land was rented: "))
                return_months = int(input("Enter the number of months the land was returned after renting: "))
                return_land(land_data, name, kitta_number, phone_number, rented_months, return_months)
                write_land_data(filename, land_data)  # Write updated data to file
            elif choice == "4":  # Exit the program
                print("\n")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("       Thank You for using our application.")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                print("\n")
                break
            else:  # Handle invalid choices
                print("Invalid choice. Please enter a valid option.")
        except ValueError as ve:  # Handle value error exceptions
            print(f"Error: {ve}")
        except Exception as e:  # Handle any other exceptions
            print(f"An error occurred: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()