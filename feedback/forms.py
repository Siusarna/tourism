from django import forms
from .models import Contact

#Форма обратной связи
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
