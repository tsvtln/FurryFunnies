from django import forms

from authors.models import Author


class AuthorsBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'first_name',
            'last_name',
            'passcode',
            'pets_number',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'passcode': forms.PasswordInput(attrs={'placeholder': 'Enter 6 digits...'}),
            'pets_number': forms.NumberInput(attrs={'placeholder': 'Enter the number of your pets...'}),
        }
        labels = {
            'first_name': 'First Name: ',
            'last_name': 'Last Name: ',
            'passcode': 'Passcode: ',
            'pets_number': 'Pets Number: ',
        }
        help_texts = {
            'passcode': 'Your passcode must be a combination of 6 digits',
        }


class AuthorCreateForm(AuthorsBaseForm):
    pass
