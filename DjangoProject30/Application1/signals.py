from typing import Sequence
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_delete, pre_save, post_delete, post_init, post_save
from django.core.signals import request_started, request_finished, got_request_exception


# will be called when user logged in successfully
@receiver(user_logged_in, sender= User)
def login_success(sender, request, user, **kwargs):
    print("------------------------")
    print("Logged in signal....")
    print("Sender :", sender)
    print("Request :", request)
    print("User :", user)
    print("Password :", user.password)
    print(f'Kwargs :{kwargs}')
# user_logged_in.connect(login_success, sender= User)


# will be called when user logged out
@receiver(user_logged_out, sender= User)
def logout_success(sender, request, user, **kwargs):
    print("------------------------")
    print("Log out signal....")
    print("Sender :", sender)
    print("Request :", request)
    print("User :", user)
    print(f'Kwargs :{kwargs}')
# user_logged_in.connect(logout_success, sender= User)


# will be called when user log in failed(wrong credentials)
@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print("------------------------")
    print("Login failed signal....")
    print("Sender :", sender)
    print("Request :", request)
    print("Credentials :", credentials)
    print(f'Kwargs :{kwargs}')
# user_login_failed.connect(login_failed)


# will be called before new user added or old user record updated 
@receiver(pre_save, sender= User)
def save_at_beginning(sender, instance, **kwargs):
    print("------------------------")
    print("Pre save signal....")
    print("Sender :", sender)
    print("Instance :", instance)
    print(f'Kwargs :{kwargs}')
# pre_save.connect(save_at_beginning, sender= User)



# will be called when new user added or old user record updated 
@receiver(post_save, sender= User)
def save_at_ending(sender, instance, created, **kwargs):
    print("------------------------")
    # called when new user created
    if created:
        print("Post save signal....")
        print("New Record created")
        print("Sender :", sender)
        print("Instance :", instance)
        print("Created :", created)
        print(f'Kwargs :{kwargs}')
    # called when old user record updated
    else:
        print("Post save signal....")
        print("Record Updated")
        print("Sender :", sender)
        print("Instance :", instance)
        print("Created :", created)
        print(f'Kwargs :{kwargs}')
# post_save.connect(save_at_ending, sender= User)


# will be called when user record is being deleted
@receiver(pre_delete, sender= User)
def at_beginning_delete(sender, instance, **kwargs):
    print("------------------------")
    print("Pre delete signal....")
    print("At beginning delete")
    print("Sender :", sender)
    print("Instance :", instance)
    print(f'Kwargs :{kwargs}')
# pre_delete.connect(at_beginning_delete, sender= User)



# will be called when user record is deleted
@receiver(post_delete, sender= User)
def at_ending_delete(sender, instance, **kwargs):
    print("------------------------")
    print("Post delete signal....")
    print("At ending delete")
    print("Sender :", sender)
    print("Instance :", instance)
    print(f'Kwargs :{kwargs}')
# post_delete.connect(at_ending_delete, sender= User)


@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print('----------------------------')
    print('At beginning request......')
    print(f'Sender :{sender}')
    print(f'Environ :{environ}')
    print(f'Kwargs :{kwargs}')
# request_started.connect(at_beginning_request)


@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print('----------------------------')
    print('At beginning request......')
    print(f'Sender :{sender}')
    print(f'Kwargs :{kwargs}')
# request_finished.connect(at_ending_request)


@receiver(got_request_exception)
def at_request_exception(sender, environ, **kwargs):
    print('----------------------------')
    print('At request exception......')
    print(f'Sender :{sender}')
    print(f'Environ :{environ}')
    print(f'Kwargs :{kwargs}')
# got_request_exception.connect(at_request_exception)