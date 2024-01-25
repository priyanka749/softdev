import decimal
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator # for Class Based Views
from django.views import View
import requests
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm


from imaplib import _Authenticator
from typing import Any
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_list_or_404
from django.contrib import messages
from .models import Donation_data
from .models import ContactMessage
from django.views.generic import ListView
import json
from .models import other_animals


from django.shortcuts import render
from .models import other_animals

def SearchView(request):
    template_name = 'show_more.html'
    context_object_name = 'posts'

    queryset = other_animals.objects.all()
    query = request.GET.get('q')

    if query:
        queryset = queryset.filter(animal__icontains=query).order_by('animal')

    context = {
        context_object_name: queryset,
    }

    return render(request, 'show_more.html', context)

def show_more(request):
    queryset = other_animals.objects.all()
    context_object_name = 'more_animalInfo'

    context = {
        context_object_name: queryset,
    }

    return render(request, 'show_more.html', context)



def login(request):
    return render(request,'login.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match. Please try again.')
            return redirect('signup')  # Redirect to the signup page with error message

        if User.objects.filter(email=email).exists():
            messages.error(request, 'The email is already taken. Please use a different email.')
            return redirect('signup')  # Redirect to the signup page with error message

        # Create a new user
        user = User.objects.create_user(email=email, password=password)
        user.is_active = False  # Account needs to be activated via email confirmation
        user.save()

        messages.success(request, 'Your account has been created. Please check your email for confirmation.')

        # Redirect to a success page or login page
        return redirect('login')  # Replace 'login' with your login URL name

    return render(request, 'signup.html')  # Render the signup page
def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Basic validation, you can add more complex validation as per your needs
        if not (full_name and email and message):
            messages.error(request, 'Please fill in all fields.')
        else:
            # Example sending an email (requires email backend setup in settings.py)
            email(
                subject='Contact Form Submission',
                message=f'Name: {full_name}\nEmail: {email}\nMessage: {message}',
                from_email=email,
                recipient_list=['your@example.com'],  # Replace with your email
                fail_silently=False,  # Set it to True for production
            )
            messages.success(request, 'Your message has been sent. We will get back to you soon!')

    return render(request, 'contact.html')

def dash(request):
    
    return render(request, 'dash.html', {'login':login ,signup:signup}) 
   

def faq(request):
        
        # Your view logic for handling FAQ requests
        return render(request,'faq.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name_input']
        email = request.POST['email_input']
        telephone = request.POST['telephone_input']
        subject = request.POST['subject_input']
        message=request.POST['message_input']
        print(name,email,telephone,subject,message)
       
        
        form = ContactMessage(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')  # Redirect to a success page after form submission
    else:
        form = ContactMessage()
    
    return render(request, 'contact_form.html', {'form': form})



from django.shortcuts import render
from .models import Animal_dog  # Import your Animal model
from django.http import HttpResponse

def showpets(request):

    animalData=Animal_dog.objects.all()


    data={
        'animalData':animalData
    }

    return render(request, 'showpets.html',data)  # Assuming your form is in showpets.html



from django.shortcuts import get_object_or_404
from .models import Animal_dog  # Import your Animal model or replace this with your actual Animal model import


from django.shortcuts import render, get_object_or_404
from .models import Animal_dog, Cats, other_animals, Birds

def profile(request, pet_id, animal_type):
    # Use if-else to determine the appropriate model class and identifier field
    if animal_type == 'dog':
        model_class = Animal_dog
        identifier_field = 'pet_id'
    elif animal_type == 'cat':
        model_class = Cats
        identifier_field = 'cat_id'
    elif animal_type == 'other_animal':
        model_class = other_animals
        identifier_field = 'animal_id'
    elif animal_type == 'bird':
        model_class = Birds
        identifier_field = 'bird_id'
    # else:
    #     raise Http404("Invalid animal type")

    # Retrieve the specific pet object based on the identifier field and pet_id
    pet = get_object_or_404(model_class, **{identifier_field: pet_id})

    # Prepare data to be passed to the template
    data = {
        'pet': pet,
        'animal_type': animal_type,
    }

    return render(request, 'profile.html', data)



from .models import Cats 
# ONLY FOR CATS
def showcats(request):

    catData=Cats.objects.all()
    

    data={
        'catData':catData
    }

    return render(request, 'showcats.html',data)  # Assuming your form is in showpets.html

from .models import Birds 
# ONLY FOR brids
def showbirds(request):
    BirdsData=Birds.objects.all() 
    data={
        'BirdsData':BirdsData
    }
    return render(request, 'showbirds.html',data)  



def donation_form(request):
    
    return render(request, 'donation_form.html') 
   

def save_donateInfo(request):

    if request.method=="POST":
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        ph_number=request.POST.get('ph_number')
        amount=request.POST.get('amount')
        message=request.POST.get('message')
        image=request.POST.get('image')
        

        record=Donation_data(full_name=full_name,email=email,phone_number=ph_number,message=message,amount=amount,image=image)
        record.save()
    return render(request, 'donation_form.html') 


import requests
import json 

from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def verify_payment(request):
   data = request.POST
   product_id = data['product_identity']
   token = data['token']
   amount = data['amount']

   url = "https://khalti.com/api/v2/payment/verify/"
   payload = {
   "token": token,
   "amount": amount
   }
   headers = {
   "Authorization": "test_secret_key_509ae363986140abbe09ce09cafaa1fb"
   }
   

   response = requests.post(url, payload, headers = headers)
   
   response_data = json.loads(response.text)
   status_code = str(response.status_code)

   if status_code == '400':
      response = JsonResponse({'status':'false','message':response_data['detail']}, status=500)
      return response

   import pprint 
   pp = pprint.PrettyPrinter(indent=4)
   pp.pprint(response_data)
   
   return JsonResponse(f"Payment Done !! With IDX. {response_data['user']['idx']}",safe=False)

def Feedback(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        feedback=request.POST["feedback"]
        obj=FeedBack(name=name,email=email,feedback=feedback)
        obj.save()
        print(f"the name is{name}, email:{email}")
    return render(request,'feedback.html')


# views.py
from django.shortcuts import render, redirect
from .models import Donation

def donation(request):
    if request.method == 'POST' and request.FILES:
        image = request.FILES['image']
        donation = Donation.objects.create(image=image)
        # Add any additional logic or processing for the uploaded image here
        return redirect('donation_success')  # Redirect to a success page
    return render(request, 'donation.html')
