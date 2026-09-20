class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.__balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print("Deposit successful.")
        else:
            print("Amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance = self.__balance - amount
            print("Withdrawal successful.")

    def get_balance(self):
        return self.__balance

    def display_info(self):
        print("\n--- Account Information ---")
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.__balance)


def find_account(accounts, account_number):
    for account in accounts:
        if account.account_number == account_number:
            return account
    return None


def get_account(accounts):
    if len(accounts) == 0:
        print("No accounts yet. Please create an account first.")
        return None
    try:
        number = int(input("Enter account number: "))
    except ValueError:
        print("Invalid account number.")
        return None
    account = find_account(accounts, number)
    if account is None:
        print("Account not found.")
    return account


def get_amount():
    try:
        return float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return 0


def create_account(accounts):
    name = input("Enter account holder name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return
    try:
        balance = float(input("Enter opening balance: "))
    except ValueError:
        print("Invalid amount. Account not created.")
        return
    if balance < 0:
        print("Opening balance cannot be negative.")
        return

    account_number = 1001 + len(accounts)
    account = BankAccount(name, account_number, balance)
    accounts.append(account)
    print("Account created successfully!")
    print("Your account number is:", account_number)


def main():
    accounts = []
    while True:
        print("\n===== Bank Account System =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Account Information")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            account = get_account(accounts)
            if account is not None:
                account.deposit(get_amount())
        elif choice == "3":
            account = get_account(accounts)
            if account is not None:
                account.withdraw(get_amount())
        elif choice == "4":
            account = get_account(accounts)
            if account is not None:
                print("Current balance:", account.get_balance())
        elif choice == "5":
            account = get_account(accounts)
            if account is not None:
                account.display_info()
        elif choice == "6":
            print("Thank you for using the Bank Account System. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()

   