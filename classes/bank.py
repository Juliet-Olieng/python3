class Bank:
    bank_name = 'Equity'

    def __init__(self, account_name, account_number, Amount):
        self.account_name = account_name
        self.account_number = account_number
        self.amount = Amount
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0

    def check_balance(self):
        return self.amount

    def deposit(self, amount, narration):
        self.amount += amount
        self.deposits.append({
            "amount": amount,
            "narration": "deposit"
        })

    def withdrawal(self, amount, narration):
        if self.amount < amount:
            raise ValueError("Insufficient balance")
        self.amount -= amount
        self.withdrawals.append({
            "amount": amount,
            "narration": narration
        })

    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(f"{transaction['narration']} - {transaction['amount']}")

    def borrow_loan(self, amount):
        if self.loan_balance > 0:
            raise ValueError("Account has outstanding loan")
        if amount < 100:
            raise ValueError("Loan amount must be more than 100")
        if len(self.deposits) < 10:
            raise ValueError("Customer must make at least 10 deposits")
        if amount > self.total_deposits / 3:
            raise ValueError("Amount requested is more than 1/3 of total deposits")
        self.loan_balance += amount
        return amount

    def total_deposits(self):
        return sum([deposit['amount'] for deposit in self.deposits])

    def repay_loan(self, amount):
        if amount > self.loan_balance:
            raise ValueError("Amount to repay is more than outstanding loan")
        self.loan_balance -= amount
        self.amount += amount
        return amount

    def transfer(self, amount, other_account):
        if amount > self.amount:
            raise ValueError("Insufficient balance")
        self.amount -= amount
        other_account.amount += amount
        return amount

        
    




