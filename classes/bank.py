class Bank:
    bank_name='Equity'
    def __init__(self,account_name,account_number,Amount):
        self.account_name=account_name
        self.account_number=account_number
        self.amount=Amount
    def bank_details(self):

        return f'{self.bank_name} your account name is{self.account_name}, account number is{self.account_number},and your balance is{self.amount}'
    def account_balance_after_deposit(self,deposit):
        balance=self.amount+deposit
        return f'your account balance is {balance}'
    def account_balance_after_withdrawal(self,withdral):
        new_balance=self.amount-withdral
        return f'dear {self.account_name} your balance is {new_balance}'
