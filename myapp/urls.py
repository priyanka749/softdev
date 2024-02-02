
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from django.urls import path
from django.views import View
from .views import profile
from myapp import views
from . import views
from .views import *

urlpatterns =[
    path('', views.dash,name='dash'),
    path('signup/', views.signup, name='signup'),
    path('save', views.save, name='save'),
    path('login_view/',views.login_view,name='login_view'),
    # path('contact/', views.contact, name='contact'),
    path('dash/', views.dash, name='dash'),
    
    path('faq/',views.faq,name='faq'),
    path('aboutus/',views.aboutus,name='aboutus'),
    
    path('showpets/', views.showpets, name='showpets'),

    path('showpets/<str:animal_type>/<int:pet_id>/', views.profile, name='profile'),

    path('contact_view/', views.contact_view, name='contact_view'),
    path('showcats/',views.showcats, name='showcats'),
    path('showbirds/',views.showbirds, name='showbirds'),

    path('show_more/',views.SearchView, name='show_more'),

    path('donation_form/',views.save_donateInfo, name='save_donateInfo'),
    path('adoption_form', views.adoption_form, name='adoption_form'),
    path('tryadopt', views.TryAdopt, name='tryadopt'),
  
    path('logout_view/', logout_view, name='logout_view'), 
    path('api/verify_payment',verify_payment,name='verify_payment'),
    path('verify_payment/', verify_payment, name='verify_payment'), 
     path('add_to_favorites/<int:animal_id>/', add_to_favorites, name='add_to_favorites'),
    
    path('question/',views.question,name='question'),
]

# Serving media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)