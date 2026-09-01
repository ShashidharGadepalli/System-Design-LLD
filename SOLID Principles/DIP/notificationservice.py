from notificationchannel import NotificationChannel

class NotificationService:

    def __init__(self, channel: NotificationChannel) -> None:
        self.channel = channel

    def notify(self, message: str) -> None:
        self.channel.send_notification(message)