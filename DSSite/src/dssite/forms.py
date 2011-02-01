from dssite.models import LaunchReminder
from django.forms.models import ModelForm

class LaunchReminderForm(ModelForm):
    class Meta:
        model = LaunchReminder
