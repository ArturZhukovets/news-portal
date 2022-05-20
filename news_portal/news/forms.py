from .models import NewsArticles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class NewArticlesForm(ModelForm):

    class Meta:
        """add placeholder, and class with styles"""
        model = NewsArticles
        fields = '__all__'                  # all fields will be displayed

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article title'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article preview'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Article text'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': "Date of publication"
            }),
        }
