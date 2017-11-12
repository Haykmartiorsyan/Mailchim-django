from django import forms
from django.conf import settings
from mailsnake import MailSnake
from mailsnake.exceptions import *

key = MailSnake(settings.MAILCHIMP_API_KEY)
list_sub = settings.MAILCHIMP_SUBSCRIBE_LIST_ID


class SubscribeForm(forms.Form):
    list_id = list_sub
    email = forms.EmailField(label='E-mail')
    name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    def save(self):
        try:
            key.ping()
        except MailSnakeException:
            return False
        except ListAlreadySubscribedException:
            return False
        except:
            return False
        else:
            return key.listSubscribe(
                id=self.list_id,
                email_address=self.cleaned_data['email'],
                name=self.cleaned_data['name'],
                merge_vars={'FNAME': self.cleaned_data['name'],
                            'LNAME': self.cleaned_data['last_name']
                            },
                double_optin=False, send_welcome=True
            )
