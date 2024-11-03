from django import forms
from .models import ContactUs, Subscribe


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({
            'type': 'text',
            'placeholder': 'Your Name',
        })
        self.fields['mail'].widget.attrs.update({
            'type': 'email',
            'placeholder': 'Email Address',
        })
        self.fields['phone'].widget.attrs.update({
            'type': 'tel',
            'placeholder': 'Phone Number (optional)',
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Message',
        })


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mail'].widget.attrs.update({
            'type': 'email',
            'placeholder': 'Get updates',
        })

