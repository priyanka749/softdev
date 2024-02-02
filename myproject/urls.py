import statistics
from django.conf import Settings, settings
from django.contrib import admin
from django.urls import include, path

from django.urls import path
from django.views import View
from django.conf.urls.static import static

from myapp import views
from django.urls import include

urlpatterns = [
    path('myproject-admin/', admin.site.urls),
    path('',include('myapp.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)