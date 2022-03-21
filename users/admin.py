from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser
from users.forms import CustomUserCreationForm, CustomUserChnageForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # add_form = CustomUserCreationForm
    # form = CustomUserChnageForm

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'username',
                    'gender',
                    'groups',
                )
            }
        )
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'gender',
                )
            }
        )
    )