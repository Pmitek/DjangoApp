from django import forms
from .models import Post, Images


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_name','description')

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image') 
    widget=forms.ClearableFileInput(attrs={"multiple": True}),   
    class Meta:
        model = Images
        fields = ('images', )