from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from shop.models import User
from shop.forms import ShopUserCreationForm, ShopUserChangeForm


class ShopUserAdmin(BaseUserAdmin):
    add_form = ShopUserCreationForm
    form = ShopUserChangeForm

    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'phone_no', 'password')}),
        (('Personal info'), {'fields': ('name', 'address')}),
        (('Permissions'), {
         'fields': ('is_active', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', )}),
    )
    add_filedsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'phone_no', 'address', 'password', 'password2')}
         ),
    )

    search_fields = ('name', 'email', )
    ordering = ('email', )

    filter_horizontal = ()


# Register your models here.
admin.site.register(User, ShopUserAdmin)
# admin.site.register(User)
admin.site.unregister(Group)
