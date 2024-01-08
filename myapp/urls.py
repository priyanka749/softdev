
from django.conf.urls.static import static
from django.conf import settings
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

    path('showpets/<str:animal_type>/<int:pet_id>/', views.profile, name='profile'),

    # path('product/',view.product_detail_showpets,name='profile'),

    # path ('profile/',views.profile, name='profile'),
    path('contact/', views.contact_view, name='contact'),
    path('showcats/',views.showcats, name='showcats'),
    path('showbirds/',views.showbirds, name='showbirds')
    
]



# Serving media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)