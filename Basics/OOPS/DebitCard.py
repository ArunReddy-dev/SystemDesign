from Card import Card

class DebitCard(Card):
    def __init__(self,cardno,name):
        super().__init__(cardno,name)
    def pay(self):
        print(f"{self._username} Payment done using debit card")
    