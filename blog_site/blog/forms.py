from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    # title = forms.CharField(
    #     max_length=100,
    #     required=True,
    #     widget = forms.widgets.TextInput(
    #         attrs ={
    #             'placeholder':'Blog Title..',
    #             'class':'custom-input'
    #         }
    #     )
    # )
    # blog_body = forms.CharField(
    #     required=True,
    #     widget= forms.widgets.Textarea(
    #         attrs={
    #             'placeholder':'Bolg Body..',
    #             'class':'custom-textarea'
    #         }
    #     )
    # )
    # blog_image = forms.FileField(required=False)

    class Meta:
        model= Blog
        fields =['title','blog_body','blog_image']
        exclude = ['user','likes','comments']
