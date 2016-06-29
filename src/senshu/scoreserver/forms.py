from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class UserUpdateForm(forms.ModelForm):
    """
    Userの更新(profile.html)
    """
    class Meta:
        model = User
        fields = ("username", "password", )