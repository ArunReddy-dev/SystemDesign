from NotificationChannel import NotificationChannel 
class EmailService(NotificationChannel):
    def send_email(self,message):
        # Code to send email
        print(f"Sending email to reciver")  