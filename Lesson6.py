class Client:
    def __init__(self,name,balance,creditbalance,passport):
        self._name = name
        self._balansOwnFunds = balance
        self._balansCreditFunds = creditbalance
        self._passport = passport
    def addOwnFunds(self,money):
        self.balansOwnFunds =+ money
    def addCreditFuns(self,money):
        self.balanceCreditFunds =+ money
    #def printProtectedData(self):
        #print(self._name,self._balansOwnFunds,self._balansCreditFunds, self._passport)
    def printProtectedData(self):
        print(self._name,self._balansOwnFunds,self._balansCreditFunds, self._passport)

account1 = Client("Bob",1000,300,567890)

account1.addOwnFunds(1000)
account1._Client__printPrivateData()
#account1.printProtectedData()
#print(account1._name)
#print(account1._balansCreditFunds)
#print(account1._passport)
