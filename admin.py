import operations

class Admin:
    def __init__(self, username, admin_id):
        self.username = username
        self.admin_id = admin_id

    def block_account(self,account_number):
        customer = operations.find_customer(account_number)

        if customer:
            customer['is_blocked'] = True
            operations.update_customer(account_number,customer)
            print(f"Account {account_number} Blocked!")
        else:
            print("Account not found!")
    

    def unblock_account(self,account_number):
        customer = operations.find_customer(account_number)

        if customer:
            customer['is_blocked'] = False
            operations.update_customer(account_number,customer)
            print(f"Account {account_number} Unblocked!")
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
