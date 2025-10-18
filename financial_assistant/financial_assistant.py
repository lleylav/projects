import datetime

from fmclasses import Transaction, FinanceManager
    


def main():
    while True:
        try:
            balance = int(input("Enter your balance: "))
            if balance<0:
                print("Negative balance entered")
                continue
            break
        except ValueError:
            print("Enter numbers only")

    fm = FinanceManager(balance)

    while True:
        print(f"""\n=== Personal Finance Manager ===

1. Add Income
2. Add Expense
3. View All Transactions
4. View Balance
5. Delete a Transaction
6. Export Report
7. Exit""")
        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Enter only numbers (1-8)")


        if option == 1:
            while True:
                try:
                    amount = int(input("Enter amount: "))
                    if amount<0:
                        print("Enter 0 or positive numbers")
                        continue
                    break
                except ValueError:
                    print("Enter numbers only")          
            source = input("Enter source (Salary, Allowance, Freelance): ")
            date = input("Enter date YYYY-MM-DD or press enter for today: ")
            if date=="":
                date = datetime.date.today()
                print(f"Added income: ${amount} from {source} on {date}.")
                t = Transaction("Income", amount, source, date)
                
                fm.add_transaction(t)  
                fm.add_income(amount)
                fm.dump_file()
                
            else:
                print(f"Added income: ${amount} from {source} on {date}.")
                t = Transaction("Income", amount, source, date)
                
                fm.add_transaction(t)
                fm.add_income(amount)
                fm.dump_file()
                

        
        elif option == 2:
            while True:
                try:
                    amount = int(input("Enter amount: "))
                    if amount<0:
                        print("Enter 0 or positive numbers")
                        continue
                    elif amount>fm.balance:
                        print("You can't spend more than you have")
                        continue
                    break
                except ValueError:
                    print("Enter numbers only")  

            source = input("Enter category (Food, Entertainment, Transport): ")
            date = input("Enter date YYYY-MM-DD or press enter for today: ")
            if date=="":
                date = datetime.date.today()
                print(f"Added expense: ${amount} on {source} on {date}.")
                t = Transaction("Expense", amount, source, date)
                
                fm.add_transaction(t)
                fm.add_expense(amount)
                fm.dump_file()

            else:
                print(f"Added expense: ${amount} on {source} on {date}.")
                t = Transaction("Expense", amount, source, date)
                
                fm.add_transaction(t)
                fm.add_expense(amount)
                fm.dump_file()
            

        elif option == 3:
            fm.load_file()

        elif option == 4:
            fm.view_balance()

        elif option == 5:
            fm.load_file()
            while True:
                try:
                    index = int(input("Enter index of transaction you want to delete: "))
                    fm.delete_transaction(index)
                    break
                except ValueError:
                    print("Enter numbers only")

        elif option == 6:
            fm.export_report()

        elif option == 7:
            break

        else:
            print("Enter only numbers in range 1-8")


if __name__ == "__main__":
    main() 