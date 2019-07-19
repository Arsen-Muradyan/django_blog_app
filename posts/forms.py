from django import forms
from .models import Post
class RawPostForm(forms.Form):
  title = forms.CharField(max_length=100, widget=forms.TextInput(
     attrs ={
    'class': 'form-control'
  } 
  ))
  body = forms.CharField(widget=forms.Textarea(
   attrs ={
    'class': 'form-control'
  } 
  ))
class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = [
      'title',
      'body'
    ]
  def __init__(self, *args, **kwargs):
    super(PostForm, self).__init__(*args, **kwargs)
    self.fields['title'].widget = forms.TextInput(
      attrs={
        'class': 'form-control'
      }
    )
    self.fields['body'].widget = forms.Textarea(
      attrs={
        'class': 'form-control'
      }
    )