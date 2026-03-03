from PaymentMethod import PaymentMethod

class Upi(PaymentMethod):
    __upi_id=None
    def __init__(self,upi_id):
        self.__upi_id=upi_id
    def pay(self):  
        print("Payment done using upi")