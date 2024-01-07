from django.contrib import admin
from django.urls import include, path

from .urls import path
# from views import View,save

from myapp import views

urlpatterns = [

    path('', views.dash,name='dash'),
     path('signup/', views.signup, name='signup'),
     path('save', views.save, name='save'),
    path('login/',views.login_view,name='login'),
    path('contact_view/', views.contact_view, name='contact_view'),
    #  path('dash/', views.dash,name='dash'),
     path('faq/',views.faq,name='faq'),
     path('aboutus/',views.aboutus,name='aboutus'),
      path('adoption_form', views.adoption_form, name='adoption_form'),
    # path('admin/', admin.site.urls),
    
]