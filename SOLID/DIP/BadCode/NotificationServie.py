from EmailService import EmailService
from SMSService import SMSService

class NotificationService:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SMSService()
    # this is a bad code because the NotificationService class is tightly coupled with the EmailService 
    # and SMSService classes. If we want to add a new notification type, we will have to modify the 
    # NotificationService class, which violates the Open/Closed Principle,Dependency Inversion Principle 
    #   and Single Responsibility Principle.
    # here high level module (NotificationService) directly  depends on low level modules (EmailService and SMSService) 
    # which is not good design.
    def send_notificationViaEmail(self, message):
       
            self.email_service.send_email(message)
    def send_notificationViaSms(self,message):
            self.sms_service.send_sms(message)