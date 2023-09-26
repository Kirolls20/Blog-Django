from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from blog.models import User
class BlogForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        required=True,
        widget = forms.widgets.TextInput(
            attrs ={
                'placeholder':'Blog Title..',
                'class':'input-field'
            }
        )
    )
    blog_body = forms.CharField(
        required=True,
        widget= forms.widgets.Textarea(
            attrs={
                'placeholder':'Bolg Body..',
                'class':'custom-textarea'
            }
        )
    )
    blog_image = forms.FileField(required=False)

    class Meta:
        model= Blog
        # fields =['title','blog_body','blog_image']
        exclude = ['user','likes','comments']


class createNewAccountForm(UserCreationForm):
    first_name = forms.CharField( 
        required=True,
        max_length=120,
        widget= forms.widgets.TextInput(
                attrs={
                        'class':'input-field',
                        'placeholder': 'First Name'
                        
                        }
                    ) ,
        label= ''
                                
            )
    last_name=forms.CharField( 
        required=True,
        max_length=120,
        widget= forms.widgets.TextInput(
                attrs={
                        'class':'input-field',
                        'placeholder': 'Last Name'
                        }
                    ) ,
        label= ''
                                
            )
    email = forms.EmailField(
        required=True,
        widget= forms.TextInput(
            attrs={
               'class':'input-field', 
               'placeholder':'Email Address'
            }
        
            ),
        label=''
        
    )
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'input-field'
        self.fields['username'].help_text = ''
        self.fields['username'].widget.attrs['placeholder'] ='Username'
        self.fields['username'].label = ''
        self.fields['password1'].widget.attrs['class'] = 'input-field'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].widget.attrs['class'] = 'input-field'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''

    