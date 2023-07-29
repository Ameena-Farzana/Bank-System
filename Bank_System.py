from getpass import getpass

class User_Data:

    def __init__(self,):
        self.users_account = {}

    def create_account(self, name, age):
        self.name = name
        self.age = age
        account_number = 100 + age
        pin = age + 3443

        if account_number in self.users_account:
            print("Account already exists")
        else:
            print("""\tCONGRATULATIONS!!!!
            Your account created successfully""")

        self.users_account[account_number] = {'name': name, 'age': age, 'pin': pin}
        self.users_account.update(self.users_account)
        print(self.users_account)
        return self.users_account

    def close_account(self):
        account_number = int(input("Enter the Account number ::  "))
        # pin = int(input("Enter the pin"))
        pin = int(getpass(prompt="Enter the pin : "))
        if account_number in self.users_account and self.users_account[account_number]['pin'] == pin:
            del self.users_account[account_number]
            print("Your account closed Successfully")
        else:
            print("Invalid account number or pin")

    def exit_account(self):
        print("""\t\tThank You for using banking system
                HAVE A GREATE DAY""")


class Bank_Data(User_Data):
    def __init__(self):
        super().__init__()
        self.balance = 0


    def deposit(self):
        account_number = int(input("Enter the account number ::  "))
        pin = pwinput(prompt= "Enter the pin ::  ", mask= "*")
        if account_number in self.users_account and self.users_account[account_number]['pin'] == pin:
            deposit_amount = int(input("Enter the amount to deposit"))
            self.balance = self.balance + deposit_amount
            print("Hi {}, \nThe amount of {} credited Successfully. Your current account balance is {}"
                  .format(self.name, deposit_amount, self.balance))
        else:
            print("Invalid Account number or Pin")


    def withdraw(self):
        withdraw_amount = int(input("Enter the amount to withdraw ::  "))
        if self.balance > withdraw_amount:
            self.balance = self.balance - withdraw_amount
            print("Hi {}, The amount of {} debited Successfully. Your current balance is {}"
                  .format(self.name, withdraw_amount, self.balance))
        else:
            print("Withdrawal Failed  ::: Insufficient Balance")


    def balance_check(self):
        print("Hi {}, Your current account Balance is :: {}".format(self.name, self.balance))



b = Bank_Data()

account = {}

print("\t\tWELCOME TO BANKING SYSTEM\n")

while True:
    opt = int(input("""Select an option  ::  
        1. Create an account
        2. Close an account
        3. Deposit into an account
        4. Withdraw from account
        5. Check account Balance
        6. Exit\n"""))

    if opt == 1:
        name = input("Enter the Name ::  ")
        age = int(input("Enter the Age ::  "))
        account = b.create_account(name, age)
        print()
        print(account, "\n")

    if opt == 2:
        b.close_account()
    if opt == 3:
        b.deposit()
    if opt == 4:
        b.withdraw()
    if opt == 5:
        b.balance_check()
    if opt == 6:
        b.exit_account()

