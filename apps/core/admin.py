from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *

admin.site.unregister(User)

class UserAdminWithEmail(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2')
            },
        ),
    )

admin.site.register(User, UserAdminWithEmail)
admin.site.register(Action)
admin.site.register(UserProfile)
admin.site.register(Notification)
admin.site.register(Comment)
admin.site.register(Activity)
admin.site.register(ActionRefLink)
admin.site.register(ActionPicture)
admin.site.register(Invitation)
