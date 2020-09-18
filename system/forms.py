from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#this is for ordercreation or submission(placing order)
class Orderform(ModelForm):
    class Meta:
        model= Order
        fields = '__all__'


#for register form and login form
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class Customerform(ModelForm):
    class Meta:
        model=customer
        fields='__all__'
        exclude=['user']
