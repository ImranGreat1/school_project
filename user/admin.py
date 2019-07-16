from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'membership', 'department', 'level')
    list_editable = ('membership',)


admin.site.register(Profile, ProfileAdmin)
