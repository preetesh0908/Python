class discover:
    def __init__(self, card_number, name, expiration_date, SecurityCode, purAPR, withdAPR, balance,  date_issued, payments_due, last_payment):
        self.__card_number = card_number
        self._name = name
        self.__expiration_date = expiration_date
        self.__SecurityCode = SecurityCode
        self.__purAPR = purAPR
        self.__withdAPR = withdAPR
        self.__balance = balance
        self.__date_issued = date_issued 
        self.__payments_due = payments_due 
        self.__last_payment = last_payment
    
    def setcard(self):
            return self.card_number
    def setname (self):
            return self.__name
    def setdate (self):
            return self.__expiration_date
    def setcode (self):
            return self.__SecurityCode
    def getbalance (self):
            return self.__balance
    def getdate (self):
            return self.__date_issued
    def getpayment (self):
            return self.__payments_due

    def minimalPayment (self):
        if self.getbalance()<= 500:
            self.__payments= self.getbalance() * 0.02
            return self.__payments
        else:
            self.__payments = self.getbalance() * 0.05
            return self.__payments
    def addCharge (self,amount):
        if amount > self.__balance:
            return "Declined"

    def makePayment (self,month,date,price ):
        if self.__payments_due[month] == date:
            self.__payments = self.__balance - price 
        else:
            return "Transaction declined"
        
        

        
        
        
month = {1:31, 2:27,3:31,4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31,11:30, 12:31}        
discovercard = discover(8008, "Snoop Dogg", "04/2021", "11",.03, 0.7,550, "05/2016",month,"09/23")     






 
        

        
        
        
