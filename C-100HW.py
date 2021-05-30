class ATM():
    def __init__(self, cardNo, pin, name, amount, cashWith, cashDep):
        self.cardNo = cardNo
        self.pin = pin
        self.name = name
        self.amount = amount
        self.cashWith = cashWith
        self.cashDep = cashDep

        def CashWithDrawl(self):
            print(self.amount - self.cashWith)
        
        def BalanceEnquiry(self):
            print(self.amount)

        def CashDeposit(self):
            print(self.amount + self.cashDep)

myATM = ATM(12345,111,"Chakri", 6000, 200, 500)

myATM.CashWithDrawl()
myATM.BalanceEnquiry()
myATM.CashDeposit()