from NotificationChannel import NotificationChannel
class SmsService(NotificationChannel):
    def send(self,message):
        # Code to send SMS
        print(f"Sending SMS to reciver")