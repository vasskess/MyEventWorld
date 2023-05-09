from django.forms import ModelForm

from MyEventWorld.common_stuff.models import *
from MyEventWorld.core.mixins.form_fields_mixin import DisabledFieldsMixin


class BaseInterestForm(ModelForm):
    class Meta:
        model = Interest
        exclude = ("interest_creator",)


class CreateInterestForm(BaseInterestForm):
    pass


class EditInterestForm(BaseInterestForm):
    pass


class DeleteInterestForm(DisabledFieldsMixin, BaseInterestForm):
    pass


class BaseMessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["topic", "message_text"]


class CreateMessageForm(BaseMessageForm):
    pass


class DeleteMessageForm(DisabledFieldsMixin, BaseMessageForm):
    pass
