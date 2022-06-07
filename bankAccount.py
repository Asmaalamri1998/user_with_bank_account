class BankAccount:		
    def __init__(self, int_rate, balance):
        self.int_rate = float(int_rate)
        self.balance = balance
        self.account_balance = 0

    def make_deposite(self,amount):
        self.account_balance+=amount
        return self
   
    def make_withdrawal(self, amount):
        if self.balance> amount:
         self.account_balance-=amount
        
        else:
            print("your balance does not allow you to perform this operation")
        return self



    def display_account_info(self):

       print(f" the account balance is {self.balance}")
       return self

    def yeild_interest(self):
        if self.int_rate>0:
         self.balance=(self.balance*self.int_rate)
        return self
	

first_account= BankAccount(0.4,20000)
second_accoount= BankAccount(0.3,3000)

first_account.make_deposite(500).make_deposite(1000).make_deposite(90).make_withdrawal(900) .yeild_interest().display_account_info()
second_accoount.make_deposite(2000).make_deposite(100).make_withdrawal(100).make_withdrawal(900).make_withdrawal(800).make_withdrawal(500).yeild_interest().display_account_info()
