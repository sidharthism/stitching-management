from django.contrib.auth.forms import UserCreationForm
from shop.models import User


class ShopUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('name', 'email', 'phone_no', 'address',)
