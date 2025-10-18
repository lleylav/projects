
import json

file_path = "transactions.json"

class Transaction:
    def __init__(self, type, amount, source, date):
        self.type = type
        self.amount = amount
        self.source = source
        self.date = date

class FinanceManager():
    def __init__(self, balance):
        self.transactions = []
        self.balance = balance
        self.income = 0
        self.expense = 0
        
    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def dump_file(self):
        t_dict_list = []

        for transaction in self.transactions:
            t_dict_list.append({
                "type": transaction.type,
                "amount": transaction.amount,
                "source/category": transaction.source,
                "date": str(transaction.date)
            })
        with open(file_path, "w") as file:
            json.dump(t_dict_list, file, indent=4)


    def load_file(self):
        self.transactions = []
        try:
            with open(file_path, "r") as file:
                transactions = json.load(file)

            print("#".ljust(4), "Type".ljust(10), "Amount".ljust(10), "Source/Category".ljust(20), "Date".ljust(12))
            print("-" * 60)

            for i, t in enumerate(transactions, 1):
                print(str(i).ljust(4), t["type"].ljust(10), str(t["amount"]).ljust(10),
                    t["source/category"].ljust(20), t["date"].ljust(12))
                self.transactions.append(Transaction(
                    t["type"], t["amount"], t["source/category"], t["date"]
                ))
        except FileNotFoundError:
            print("No transaction file found.")
                

    def add_income(self, amnt):
        self.balance += amnt
        self.income += amnt

    def add_expense(self, amnt):
        self.balance -= amnt
        self.expense += amnt

    def view_balance(self):
        print(self.balance)

    def export_report(self):
        print()
        print("=== Total monthly report ===")
        print(f"Spent in total: ${self.expense}")
        print(f"Earned in total: ${self.income}")
        if self.income>self.expense:
            print(f"\nProfit: ${self.income-self.expense}")
        elif self.expense>self.income:
            print(f"\nLoss: ${self.expense-self.income}")
        else:
            print("\nNo loss no profit")
        print("============================")


    def delete_transaction(self, index):
        while True:
            if 0 <= index < len(self.transactions)+1:
                removed = self.transactions.pop(index-1)
                self.dump_file()  
                print(f"Deleted transaction: {removed.type} ${removed.amount}")
                break
            else:
                print("Invalid transaction number.")