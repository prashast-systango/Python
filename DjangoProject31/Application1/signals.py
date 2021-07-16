from django.dispatch import Signal, receiver
#Creating Custom Signal
notification = Signal(providing_args = ["request", "user"])

# Reciever function
@receiver(notification)
def show_notification(sender, **kwargs):
    print(f'Sender : {sender}')
    print(f'Kwargs : {kwargs}')
    print('Notification')