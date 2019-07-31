from django.forms import ModelForm
from django.forms.widgets import  Textarea
from .models import Post

class NewPostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['text', ]
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 20})
        }
