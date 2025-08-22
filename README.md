# Banking System

## Objective

This Python project implements a console-based banking system that allows the creation and management of customer accounts. It supports deposits, withdrawals, transfers, and viewing balances. The system is structured for different user roles: customer, staff, and admin.

### Skills Learned

* Implementing account management systems.
* Handling file-based data storage (`JSON`) for persistent data.
* Creating role-based access control in CLI applications.
* Error handling and input validation.
* Python programming with modular code design.

### Tools Used

* Python 3.x
* JSON for data storage
* Command-line interface (CLI)

## File Structure

```
Banking-System/
│
├─ main.py                 # Main entry point of the application
├─ database.json           # Stores all account data persistently
├─ customer.py             # Customer-related functions and menu
├─ staff.py                # Staff-related functions and menu
├─ admin.py                # Admin-related functions and menu
├─ utils.py                # Utility functions used across modules
├─ README.md               # Project documentation
└─ requirements.txt        # Python dependencies (if any)
```

## Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/LeviRichard/Banking-System.git
   cd Banking-System
   ```

2. **Run the application:**

   ```bash
   python main.py
   ```

3. **Navigate the CLI menus:**

   * Customers can create accounts and view balances.
   * Staff can deposit and withdraw money from customer accounts.
   * Admin can view all accounts and delete accounts.

4. **Account Management:**

   * Creating an account involves providing user details.
   * Deposits, withdrawals, and transfers are secured and logged in `database.json`.
   * Admin functions allow oversight and management of all accounts.

*Ref 1: Customer account creation screen*

*Ref 2: Staff deposit/withdrawal interface*

*Ref 3: Admin view of all accounts*

