from django import forms

class EmailForm(forms.Form):
    email_text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Type your email here',  # Set the placeholder here
                'rows': 5,  # Adjust the height of the textarea
                'cols': 50,  # Adjust the width of the textarea
                'class': 'form-control'  # Add Bootstrap class for styling
            }
        ),
        max_length=10000,  # Set max length to match your requirement
    )
