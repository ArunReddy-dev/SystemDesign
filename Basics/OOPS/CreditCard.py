from Card import Card

class CreditCard(Card):
    def __init__(self, cardno, name):
        super().__init__(cardno, name)
    def pay(self):
        print(f"{self._username} ({self._cardno}): Payment done using credit card")
        
    