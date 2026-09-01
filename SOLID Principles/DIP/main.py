from notificationchannel import NotificationChannel
from notificationservice import NotificationService
from email import EMail
from message import SMS

sms_channel = SMS()
email_channel = EMail()
ns = NotificationService(sms_channel)
ns.notify("Hello, this is a test notification.")

email_ns = NotificationService(email_channel)
email_ns.notify("Hello, this is a test notification.")