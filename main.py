from staff import Staff
from admin import Admin
from customers import Customer

def main_menu():
    while True:
        print("============== MAIN MENU ==============")
        print("1.Create Customer account")
        print("2.Login as Staff")
        print("3.Login as Admin")
        print("4.Exit")

        choice = int(input("Enter your choice: "))

        print("\n")

        if choice == 1:
            customer = Customer()
            customer.create_account()
            print("\n")
        elif choice == 2:
            user_name = input("Enter your Staff username:")
            staff_passwd = input("Enter your password:")
            print("\n")
            staff = Staff(user_name,staff_passwd)
            staff_menu(staff)
            print("\n")
        elif choice == 3:
            user_name = input("Enter your admin username: ")
            admin_passwd = input("Enter your password: ")
            print("\n")
            admin = Admin(user_name,admin_passwd)
            admin_menu(admin)
            print("\n")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid option please!")


def staff_menu(staff):
    while True:
        print("---------STAFF PANEL-----------")
        print("1.Deposit")
        print("2.Withdarw")
        print("3.Transfer")
        print("4.Troubleshoot Account")
        print("5.View all accounts")
        print("6.Exit")

        choice = int(input("Enter choice: "))
        print("\n")

        if choice == 1:
            account = input("Enter Account number: ")
            print("\n")
            amount = float(input("Enter amount: "))


            staff.deposit(account,amount)
            print("\n")
        elif choice == 2:
            account = input("Enter Account number: ")
            amount = float(input("Enter amount: "))
            print("\n")
            staff.withdraw(account,amount)
            print("\n")
        elif choice == 3:
            sender = input("Enter Receiver account number: ")
            receiver = input("Enter Sender account number: ")
            amount = float(input("Enter amount: "))
            print("\n")
            staff.transfer(sender,receiver,amount)
            print("\n")
        elif choice == 4:
            account = input("Enter Account number: ")
            print("\n")
            staff.troubleshoot(account)
            print("\n")
        elif choice == 5:
            staff.view_all_accounts()
            print("\n")
        elif choice == 6:
            break
        else:
            print("Invalid option!")


def admin_menu(admin):
    while True:
        print("---------------ADMIN MENU----------------")
        print("1.Block Account")
        print("2.Unblock Account")
        print("3.View all Accounts")
        print("4.Exit")

        choice = int(input("Enter your choice: "))
        print("\n")

        if choice == 1:
            account = input("Enter account number: ")
            admin.block_account(account)
            print("\n")
        elif choice == 2:
            account = input("Enter account number: ")
            admin.unblock_account(account)
            print("\n")
        elif choice == 3:
            admin.view_all_accounts()
            print("\n")
        elif choice == 4:
            break
        else:
            print("Invalid option")



main_menu()
