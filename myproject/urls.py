
import statistics
from django.conf import Settings, settings
from django.contrib import admin
from django.urls import include, path

from django.urls import path
from django.views import View

from myapp import views

urlpatterns = [
     path('myproject-admin/', admin.site.urls),
 path('login/',views.login,name='login'),
     path('signup/', views.signup, name='signup'),
      path('contact/', views.contact, name='contact'),
     path('dash/', views.dash,name='dash'),
     path('faq/',views.faq,name='faq'),
     path('aboutus/',views.aboutus,name='aboutus'),
     path('',views.dash,name='dash'),

]
