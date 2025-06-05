import random
import operations

def generate_account_number(max_attempts=100):
    attempts = 0
    while attempts < max_attempts:
        account_number = '234' + ''.join([str(random.randint(0, 9)) for _ in range(7)])
        # Ensure uniqueness
        if not operations.find_customer(account_number):
            return account_number
        attempts += 1
    raise Exception("Failed to generate a unique account number after maximum attempts.")

class Customer:
    def __init__(self):
        self.account_number = None
        self.name = ""
        self.email = ""
        self.phone = ""
        self.balance = 0.0  # Initialize to 0.0

    def create_account(self):
        self.name = input("Enter your name: ")
        self.email = input("Enter your email: ")
        self.phone = input("Enter your phone number: ")
        
        while True:
            try:
                self.balance = float(input("Enter initial deposit: "))
                break  # Exit the loop if conversion is successful
            except ValueError:
                print("Invalid input. Please enter a numeric value for the deposit.")
        
        self.account_number = generate_account_number()
        customer_data = {
            "account_number": self.account_number,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "balance": self.balance,
            "is_blocked": False
        }
        
        db = operations.load_database()
        db['customers'].append(customer_data)
        operations.save_database(db)
        print(f"Account created successfully! Your account number is {self.account_number}")
