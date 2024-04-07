from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileEditForm(UserChangeForm):
    password = None
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        # Agregar clases CSS para mejorar la apariencia
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super(ProfileEditForm, self).save(commit=False)
        # Actualizar el avatar del usuario si se proporciona una imagen
        image = self.cleaned_data.get('image', None)
        if image:
            try:
                avatar = user.avatar
                avatar.image = image
            except Avatar.DoesNotExist:
                avatar = Avatar(user=user, image=image)
            avatar.save()
        
        # Guardar los cambios en el usuario
        if commit:
            user.save()
        return user

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = fields = ['first_name', 'last_name', 'username', 'email']
        exclude = ['password']