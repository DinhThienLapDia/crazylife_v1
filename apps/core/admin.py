from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *
from django import forms

admin.site.unregister(User)

def verified(modeladmin, request, queryset):
        queryset.update(isverified=True)
verified.short_description = "Verified all selected"
def unverified(modeladmin, request, queryset):
        queryset.update(isverified=False)
unverified.short_description = "unerified all selected"
#class LocationImages(admin.TabularInline):
 #   model = Action
 #   extra = 0
 #
 #   def formfield_for_dbfield(self, db_field, **kwargs):
 #       if db_field.name == 'firstPicture':
 #           request = kwargs.pop("request", None)
 #           kwargs['widget'] = AdminImageWidget
 #           return db_field.formfield(**kwargs)
 #       return super(LocationImages, self).formfield_for_dbfield(db_field, **kwargs)

class TitleAdminForm(forms.ModelForm):
    class Meta:
        widgets = { 'title': forms.TextInput(attrs={'size': 80})}

class UserAdminWithEmail(admin.ModelAdmin):
    model = Action
    list_display = ('title','createDate', 'modified','author','isverified')
    #list_filter =('isverified')
    fields = ('title','showimage','firstPicture','content','startDate', 'endDate')
    readonly_fields = ['showimage']
    search_fields = ['title','author__username','isverified']
    actions = [verified, unverified]
    form = TitleAdminForm
   # inlines = [LocationImages]
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
#    def verified(self, request, queryset):
#        queryset.update(isverified=True)
#    verified.short_description = "Verified all selected"
    #def get_queryset(self, request):
     #   qs = super(UserAdminWithEmail, self).get_queryset(request)
      #  if request.user.is_superuser:
       #     return qs
       # return qs.filter(author=request.user)
class UserAdminForUser(UserAdmin):
    model = User
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2')
            },
        ),
    )



admin.site.register(User, UserAdminForUser)
admin.site.register(Action, UserAdminWithEmail)
#admin.site.register(UserProfile)
#admin.site.register(Notification)
#admin.site.register(Comment)
#admin.site.register(Activity)
admin.site.register(ActionRefLink)
admin.site.register(ActionPicture)
#admin.site.register(Invitation)
