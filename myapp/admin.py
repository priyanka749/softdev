from django.contrib import admin
from .models import Animal_dog
from .models import ContactMessage
from .models import Cats
admin.site.register(ContactMessage)
# Register your models here.

admin.site.register(Animal_dog)
admin.site.register(Cats)
