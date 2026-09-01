from notificationchannel import NotificationChannel

class SMS(NotificationChannel):

    def send_notification(self, message: str) -> None:
        print(f"Sending SMS notification: {message}")