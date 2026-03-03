from PaymentMethod import PaymentMethod

class PaymentService:
    # used for storing and making the payment using different payment method
    # In-memory Data Structure
    # PaymentMethods={}
    def __init__(self):
        self.PaymentMethods={}
    def addPaymentMethod(self,name,pm:PaymentMethod):
        self.PaymentMethods[name]=pm
    def makePayment(self,name):
        if name in self.PaymentMethods:
            # run time polymorphism
            # depending upon what type of object is extracted from teh dictionary
            # the pay method will be called
            self.PaymentMethods[name].pay()
        else:
            print("Payment method not found")