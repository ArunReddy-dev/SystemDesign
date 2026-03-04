from EmailService import EmailNotification

# here we implemented the DIP by creating a NotificationService class that depends on an abstraction (NotificationChannel) rather than a concrete implementation (EmailNotification). 
# This allows us to easily switch to a different notification channel (e.g., SMS, PushNotification) without modifying the NotificationService class, thus adhering to the Dependency Inversion Principle.
# in DIP, high-level modules should not depend on low-level modules. Both should depend on abstractions. 
# In this example, the NotificationService is the high-level module that depends on the abstraction of a notification channel,
# rather than directly depending on a specific implementation like EmailNotification.
class NotificationService:
    
    def __init__(self,NotificationChannel):
        self.NotificationChannel = NotificationChannel()
    def send_notification(self, message):
        self.NotificationChannel.send(message)

if __name__ == "__main__":
    notification_service = NotificationService(EmailNotification)
    notification_service.send_notification("Hello, this is a notification!")
    
       