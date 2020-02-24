from django import forms
from .models import List, Comment

class MajorNew(forms.ModelForm):
    class Meta:
        model = List
        fields = ['title','score','body']

class LiberalNew(forms.ModelForm):
    class Meta:
        model = List
        fields = ['title','score','body']

class ElectiveNew(forms.ModelForm):
    class Meta:
        model = List
        fields = ['title','score','body']                
        
class New(forms.ModelForm):
    class Meta:
        model = List
        fields = ['title','field','score','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']