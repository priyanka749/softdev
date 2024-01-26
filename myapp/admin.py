from django.contrib import admin
from .models import Animal_dog
from .models import ContactMessage
from .models import Cats
from .models import Birds

from .models import other_animals
from .models import Donation_data
from .models import DogAdoption
admin.site.register(ContactMessage)
# Register your models here.

admin.site.register(Animal_dog)
admin.site.register(Cats)
admin.site.register(Birds)
admin.site.register(Donation_data)
admin.site.register(other_animals)

admin.site.register(DogAdoption)