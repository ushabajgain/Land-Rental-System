# Land Rental Management System

A command-line application for managing land rentals, written in Python.  
This system allows users to view available lands, rent a land, return a rented land, and generate invoices for transactions.  
It demonstrates file handling, input validation, and basic data management.

---

## Features

- **Display All Lands**: View a list of all available lands with location, direction, area, price, and status.
- **Rent Land**: Rent a land by providing customer details, rental duration, and generate a rent invoice.
- **Return Land**: Return rented land, calculate late fines, and generate a return invoice.
- **Data Persistence**: Data stored and updated in `land_data.txt`.
- **Input Validation**: Validates phone numbers (must start with `97` or `98` and be 10 digits).

---

## File Structure

| File           | Description                                  |
|----------------|----------------------------------------------|
| `main.py`      | Main entry point and user interface loop     |
| `operations.py`| Core functions for renting and returning     |
| `read.py`      | Reads land data from file                    |
| `write.py`     | Writes updated land data to file             |
| `land_data.txt`| Stores land info in CSV format               |

---

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ushabajgain/Land-Rental-System.git
   cd Land-Rental-System
   ```

2. **Run the Application**:
   ```bash
   python main.py
   ```

---

## 📄 Data Format - `land_data.txt`

```plaintext
101, Katmandu, North, 4, 50000, Available, 0
102, Pokhara, East, 5, 60000, Available, 0
```

**Format**:  
`kitta_number, location, direction, area, price, status, total_months_rented`

---

## Usage

- **Option 1 - Display All Lands**
- **Option 2 - Rent Land**  
  Enter name, kitta number, phone number, duration (months).  
  Invoice saved as `<filename>_rent.txt`.

- **Option 3 - Return Land**  
  Enter name, phone number, kitta number.  
  Return invoice saved as `<filename>_return.txt`.

- **Option 4 - Exit Application**

---

## Example Invoice

```plaintext
────────────────────── INVOICE ────────────────────
 Kitta Number: 101
 Customer Name: John Doe
 Phone Number: 9800000000
 Duration (months): 3
 Total Amount: 150000 NPR
───────────────────────────────────────────────────
```

---

## Requirements

- Python 3.x

---

## Notes

- Ensure `land_data.txt` is in the same folder as the `.py` files.
- Invoices are saved in the same directory as the program.

---

## 🪪 License

This project is for educational purposes only.
