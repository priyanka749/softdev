from django.contrib import admin
from django.urls import include, path

from django.urls import path
from django.views import View

from myapp import views

urlpatterns = [

    path('', views.signup,name='signup'),
     path('signup/', views.signup, name='signup'),
    path('login/',views.login,name='login'),
    path('contact/', views.contact, name='contact'),
     path('dash/', views.dash,name='dash'),
     path('faq/',views.faq,name='faq'),
     path('aboutus/',views.aboutus,name='aboutus'),
    path('admin/', admin.site.urls),
    path('',include('myapp.urls'))
]