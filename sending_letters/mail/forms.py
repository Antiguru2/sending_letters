from django.forms import ModelForm
from .models import Mail_sending


class MailForm(ModelForm):
    class Meta:
        model = Mail_sending
        fields = (
            'Mail',             
        )