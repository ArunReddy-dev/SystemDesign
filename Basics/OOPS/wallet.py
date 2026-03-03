from PaymentMethod import PaymentMethod
class wallet(PaymentMethod):
    def __init__(self,wallet_id):
        self.wallet_id=wallet_id
    def pay(self):
        print("Payment done using wallet")
    