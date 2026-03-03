from PaymentMethod import PaymentMethod

class Card(PaymentMethod):
    _cardno=None
    _username=None
    
    def __init__(self, cardno, name):
        self._cardno = cardno
        self._username = name
        
    def getCardNo(self):
        return self.__cardno__
    
    def getName(self):
        return self.__name__
    
   