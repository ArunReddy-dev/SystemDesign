from abc import ABC,abstractmethod

class PaymentMethod(ABC):
     @abstractmethod
     def pay(self):
        # we dont know which method or way we will be using for payment
        # so we make it abstract method and we will implement it in child class
        # there might be multiple payment method like card, upi, net banking etc
        pass