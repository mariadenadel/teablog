from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'preview', 'full_text', 'created_at',]


        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва статті'
            }),
            'preview': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статті'
            }),
            'full_text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стаття'
            }),
            'created_at': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публікації'
            })
        }