from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Relation, Profile


class ProfilleInline(admin.StackedInline):
    model = Profile
    can_delete = False


class ExtendUserAdmin(UserAdmin):
    inlines = (ProfilleInline,)



admin.site.unregister(User)
admin.site.register(User, ExtendUserAdmin)

admin.site.register(Relation)