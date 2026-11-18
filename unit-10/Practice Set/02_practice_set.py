class Account():
    def __init__(self,account_no,Bal):
        self.account=account_no
        self.Bal=Bal
    def debit (self,debit):
        self.debit=debit
        self.Bal-=self.debit
        print(f"Your debited acc is  Rs {self.debit}")
        print(f"Your avalaible bals is Rs {self.avl_bal()}")

    def credit (self,credit):
        self.credit=credit
        self.Bal+=self.credit
        print(f"Your credited acc is  Rs {self.credit}")
        print(f"Your avalaible bals is Rs {self.avl_bal()}")
    def avl_bal(self):
        return self.Bal

acc1=Account(int(input("Enter you Acc no ")),float(input("Enter your balance")))
print(acc1.Bal,acc1.account)
acc1.debit(float(input("Enter your Debited amount")))
acc1.credit(40000)    



        