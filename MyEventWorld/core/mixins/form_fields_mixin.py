from django import forms


class DisabledFieldsMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__hide_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __hide_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()
            field.required = False
