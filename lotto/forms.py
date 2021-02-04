from django import forms
from .models import GuessNumbers

# ModelForm안에 Meta라는 자식객체를 오버라이드해서 사용
class PostForm(forms.ModelForm):
    class Meta:
        model = GuessNumbers
        fields = ('name','text')
