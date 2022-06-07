from bankAccount import BankAccount

class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = [BankAccount(int_rate=0.2, balance=0)]

    def make_deposit(self, amount, account_num):	
        if account_num < len(self.account):
            self.account[account_num].balance += amount	
        elif account_num == len(self.account):
            self.account += [BankAccount(int_rate=0.02, balance=0)]
            self.account[account_num].balance += amount
        else:
            print("wrong account number")
        return self
    	
        
        
       
   
    def make_withdrawal(self, amount, account_num):
        if account_num < len(self.account):
            self.account[account_num].balance -= amount
        else:
            print("wrong account number")
        return self


    def display_user_balance(self, account_num):
        print(f"User: {self.name}, Account Number:{account_num},")
        return self

    def transfer_money(self, account_num, other_user, user_account_num, amount):
        if account_num < len(self.account) and user_account_num < len(other_user.account):
            other_user.account[user_account_num].balance += amount
            self.account[account_num].balance -= amount
        else:
            print("wrong account number")
        return self

mohammed=User("Mohammed","mohammed@gmail.com")
asma= User("Asma", "Asma@gmail.com")
lateen= User("lateen","lateem@gmail.com")

asma.make_deposit(100,1)
asma.make_deposit(1000,1)
asma.make_deposit(3000,2)
asma.make_withdrawal(900,1)
asma.display_user_balance(1)

mohammed.make_deposit(2000,2)
mohammed.make_deposit(2500,1)
mohammed.make_withdrawal(600,0)
mohammed.make_withdrawal(150,1)
mohammed.display_user_balance(2)

lateen.make_deposit(5000,1)
lateen.make_withdrawal(200,2)
lateen.make_withdrawal(300,1)
lateen.make_withdrawal(1000,1)
lateen.display_user_balance(1)

asma.transfer_money(0,lateen,1,3000)
lateen.display_user_balance(1)
asma.display_user_balance(1)

