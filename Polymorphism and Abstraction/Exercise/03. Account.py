class Account:

    def __init__(self, owner, amount = 0):
        self.owner = owner
        self.amount = amount
        self._transactions  = []

    def handle_transaction(self, transaction_amount):
         
        if self.balance + transaction_amount < 0:
             raise ValueError("sorry cannot go in debt!")
                              
        self._transactions.append(transaction_amount)
        return f"New balance: {self.balance}"



    def add_transaction(self, amount):

        if type(amount) != int:
            raise ValueError("please use int for amount")
        

        if self.balance + amount < 0:
            raise ValueError("sorry cannot go in debt!")
        

        self._transactions.append(amount)
        return f"New balance: {self.balance}"
                             
    @property
    def balance(self):
        return self.amount + sum(self._transactions)
    

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"


    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"


    def __len__(self):
        return len(self._transactions)
    

    def __getitem__(self, index: int):
        return self._transactions[index]

## by amount

    def __gt__(self, other):
        return self.balance > other.balance


    def __lt__(self, other):
        return self.balance < other.balance
    
    def __ge__(self, other):
        return self.balance >= other.balance
    
    def __le__(self, other):
        return self.balance <= other.balance
    

    def __eq__(self, other):
        return self.balance == other.balance
    
    def __ne__(self, other):
        return self.balance != other.balance

    def __reversed__(self):
        return reversed(self._transactions)

    def __add__(self, other):
        new_owner = f"{self.owner}&{other.owner}"
        new_balance = self.amount + other.amount

        new_account = Account(new_owner, new_balance)
        new_account._transactions = self._transactions + other._transactions

        return new_account
