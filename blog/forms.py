# forms.py
from django import forms
from .models import Artwork

class ArtworkUploadForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['image']

from .models import Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']