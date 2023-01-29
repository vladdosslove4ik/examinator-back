from django.contrib import admin
from .models import Moderator, User, BusinessUser

# Register your models here.
admin.site.register(Moderator)
admin.site.register(User)
admin.site.register(BusinessUser)
