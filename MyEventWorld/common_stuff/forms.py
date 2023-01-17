from django.forms import ModelForm

from MyEventWorld.common_stuff.models import *


class BaseInterestForm(ModelForm):
    class Meta:
        model = Interest
        exclude = ("interest_creator",)


class CreateInterestForm(BaseInterestForm):
    pass


class EditInterestForm(BaseInterestForm):
    pass


class DeleteInterestForm(BaseInterestForm):
    pass


class BaseMessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["topic", "message_text"]


class CreateMessageForm(BaseMessageForm):
    pass


class DeleteMessageForm(BaseMessageForm):
    pass
