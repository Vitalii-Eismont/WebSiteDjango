from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesFrom(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Назва новини'
            }),
            "anons": TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Анонс новини'
            }),
            "date": DateTimeInput(attrs={
                'class': "form-control",
                'placeholder': 'Дата публікації'
            }),
            "text": Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Текст новини'
            })
        }