from django import forms

from app.models import User


class DateInput(forms.DateInput):
    input_type = 'date'
    widgets = {
        'date_of_birth': forms.DateInput(format='%d.%m.%Y', attrs={'class': 'datepicker'}),
    }


class UserForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DateInput, label="Date of birth")

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'date_of_birth', 'role', 'email', 'street', 'street_number',
                  'phone_number', 'post_number', 'city', 'country')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
