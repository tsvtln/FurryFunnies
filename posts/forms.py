from django import forms
from .models import Posts


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            'title',
            'image_url',
            'content',
        ]


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'image_url', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Put an attractive and unique title...'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Provide URL to Image...'}),
            'content': forms.Textarea(attrs={'placeholder': 'Share some interesting facts about your adorable pets...'})
        }
        labels = {
            'title': 'Title: ',
            'image_url': 'Post Image URL: ',
            'content': 'Content: ',
        }
        help_texts = {
            'image_url': 'Share your funniest furry photo URL!',
        }
        error_messages = {
            'title': {
                'unique': "Oops! That title is already taken. How about something fresh and fun?"
            }
        }
