from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.forms import ModelForm, CharField, PasswordInput
from django.forms import CharField, TextInput
# from django.core.exceptions import ValidationError
from shop.models import User


class ShopUserCreationForm(UserCreationForm):
    # phone_no = CharField(
    #     widget=TextInput(attrs={'type': 'number'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'name', 'phone_no', 'address',)

# class ShopUserCreationForm(ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""
#     password1 = CharField(label='Password', widget=PasswordInput)
#     password2 = CharField(
#         label='Password confirmation', widget=PasswordInput)

#     class Meta:
#         model = User
#         fields = ('name', 'email', 'phone_no', 'address',)

#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Passwords don't match")
#         return password2

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


class ShopUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    class Meta:
        model = User
        fields = ('email', 'name',  'phone_no', 'address', )
