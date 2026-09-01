from notificationchannel import NotificationChannel

class EMail(NotificationChannel):

    def send_notification(self, message: str) -> None:
        print(f"Sending email notification: {message}")

