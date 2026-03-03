from CreditCard import CreditCard
from DebitCard import DebitCard
from wallet import wallet
from Upi import Upi
from PaymentMethod import PaymentMethod
from PaymentService import PaymentService


class Client:
    if __name__=="__main__":
        ps=PaymentService()
        # we can use any payment method to make payment
        # we can add any payment method to the payment service  
        ps.addPaymentMethod("ArunCreditCard",CreditCard("1234-5678-9012-3456","Arun"))
        ps.addPaymentMethod("ArunDebitCard",DebitCard("1234-5678-9012-3456","Arun"))
        ps.addPaymentMethod("ArunUpi",Upi("arun@upi"))
        ps.addPaymentMethod("ArunWallet",wallet("arun_wallet_id"))
        
        ps.makePayment("ArunCreditCard")
        ps.makePayment("ArunDebitCard")
        ps.makePayment("ArunUpi")
        ps.makePayment("ArunWallet")
        