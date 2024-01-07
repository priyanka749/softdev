from django.contrib import admin
from django.urls import include, path

from django.urls import path
from django.views import View
from .views import profile
from myapp import views

urlpatterns =[
    path('', views.signup,name='dash'),
    path('signup/', views.signup, name='signup'),
    path('login/',views.login,name='login'),
    path('contact/', views.contact, name='contact'),
    path('dash/', views.dash, name='dash'),
    path('faq/',views.faq,name='faq'),
    path('aboutus/',views.aboutus,name='aboutus'),
    
    path('showpets/', views.showpets, name='showpets'),

    path('showpets/<int:pet_id>/', views.profile, name='profile'),
    # path('product/',view.product_detail_showpets,name='profile'),

    # path ('profile/',views.profile, name='profile'),
    path('contact/', views.contact_view, name='contact'),
    path('showcats/',views.showcats, name='showcats')

]