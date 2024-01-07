from django.contrib import admin

from .models import ContactMessage, DogAdoption
from .models import User_profile
admin.site.register(ContactMessage)
admin.site.register(User_profile)
admin.site.register(DogAdoption)
# Register your models here.
