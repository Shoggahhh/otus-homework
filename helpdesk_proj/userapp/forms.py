from django.contrib.auth.forms import UserCreationForm
from userapp.models import MyUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = 'username', 'email', 'password1', 'password2'

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
