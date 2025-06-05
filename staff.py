import operations
from datetime import datetime



now = datetime.now()

formated_date_time = now.strftime("%d/%m/%y/ %H:%M:%S")
class Staff:
    def __init__(self, username, staff_id):
        self.username = username
        self.staff_id = staff_id

    

    def deposit(self, account_number, amount):
        customer = operations.find_customer(account_number)

        if customer and not customer['is_blocked']:
            customer['balance'] +=amount
            operations.update_customer(account_number,customer)
            print(f"Deposited {amount} to {account_number}")
            print(formated_date_time)
        else:
            print(f"Account not found or blocked!")
            print(formated_date_time)
    
    def withdraw(self, account_number, amount):
        customer = operations.find_customer(account_number)

        if customer and not customer['is_blocked']:
            customer['balance']-=amount
            operations.update_customer(account_number,customer)
            print(f"Withdrew {amount} from {account_number}")
            print(formated_date_time)
        else:
            print(f"Account not found or blocked")
            print(formated_date_time)

    def transfer(self,sender_account_number, receiver_account_number, amount):
        sender = operations.find_customer(sender_account_number)
        receiver = operations.find_customer(receiver_account_number)

        if sender and receiver:
            if not sender['is_blocked'] and not receiver['is_blocked'] and sender['balance'] >= amount:
                receiver['balance']-=amount
                operations.update_customer(receiver_account_number,receiver)
                sender['balance']+=amount
                operations.update_customer(sender_account_number,sender)
                print(f"{amount} transferred from {sender_account_number} to {receiver_account_number}")
                print(formated_date_time)
            elif sender['is_blocked']:
                print(f"Sender {sender_account_number} blocked")
            elif receiver['is_blocked']:
                print(f"Receiver {receiver_account_number} is blocked")
            elif sender['balance'] <= amount:
                print("Insuficient funds")
        elif not sender:
            print(f"Sender account not found")
        elif not receiver:
            print(f"Receiver not found")

    

    def troubleshoot(self, account_number):
        db = operations.load_database()
        customers = db.get('customers', [])
    
        customer = next((cust for cust in customers if cust['account_number'] == account_number), None)

        if customer:
            readable_status = "Blocked" if customer.get('is_blocked', False) else "Active"
            print(f"{'Account':<15} {'Name':<20} {'Balance':<20} {'Status':<10}")
            print("-" * 70)
            print(f"{account_number:<15} {customer['name']:<20} {customer['balance']:<20} {readable_status:<10}")
        else:
            print("Account not found")

    def view_all_accounts(self):
        db = operations.load_database()
        customers = db.get('customers',[])

        if not customers:
            print("Account not found!")
            return
        else:
            print(f"{'Account':<15} {'Name':<20} {'Balance':<20} {'Status':<10}")
            print("-"*70)

            for customer in customers:
                readable_status = "Blocked" if customer['is_blocked'] else "Active"
                print(f"{customer['account_number']:<15} {customer['name']:<20} {customer['balance']:<20} {readable_status:<10}")




