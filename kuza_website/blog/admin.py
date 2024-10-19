# admin.py
from django.contrib import admin
from .models import Post
from ckeditor.widgets import CKEditorWidget
from django import forms

# Create a custom form for the Post model admin
class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'  # Include all fields

# Create a custom admin class to use the form
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

# Register the Post model with the custom admin class
admin.site.register(Post, PostAdmin)