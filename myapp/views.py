from imaplib import _Authenticator
from multiprocessing import AuthenticationError
from typing import Any
from django.contrib.auth import authenticate, login
# from myapp.models import User
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
from .models import DogAdoption 
from django.db.models import Q
from django.contrib.auth import logout
from django.contrib.auth.models import User
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

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Log in the user
            login(request, user)
            # Redirect to a success page. You can replace 'home' with your desired URL.
            return redirect('dash')
        else:
            # Return an invalid login message or perform other actions
            return render(request, 'login.html', {'error_message': 'Invalid login credentials'})

    return render(request, 'login.html')



from django.shortcuts import render, redirect
from django.contrib import messages

def signup(request):
      
    return render(request, 'signup.html')  # Render the signup page

def save(request):
    if request.method == 'POST':
        name = request.POST.get('name_input')
        email = request.POST.get('email_input')
        password = request.POST.get('password_input')
        confirm_password = request.POST.get('con_password_input')

        # Create a new user using the create_user method
        new_user = User.objects.create_user(username=email, email=email, password=password)
        new_user.first_name = name  # Set the first name (assuming 'name' is the first name field)

        # Save the user instance
        new_user.save()

        # Your remaining code...
        return redirect('login_view')

    return render(request, 'signup.html')


def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name_input']
        email = request.POST['email_input']
        telephone = request.POST['telephone_input']
        subject = request.POST['subject_input']
        message=request.POST['message_input']
        print(name,email,telephone,subject,message)
       
        c = ContactMessage.objects.create(
            name=name,
            email=email,
            telephone=telephone,
            subject=subject,
            message=message
        )
    
        c.save()
        
    return render(request, 'contact_view.html')

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
       
        c = ContactMessage.objects.create(
            name=name,
            email=email,
            telephone=telephone,
            subject=subject,
            message=message
        )
 
        c.save()
        
    return render(request, 'contact_view.html')
   


from django.shortcuts import render
from .models import Animal_dog  # Import your Animal model
from django.http import HttpResponse

def showpets(request):
    animalData = Animal_dog.objects.all()
    if request.method == 'POST':
        print(request.POST)
        petname = request.POST.get('petName')
        breed = request.POST.get('breedInput')
        color = request.POST.get('colourInput')
        behavior = request.POST.get('behavioursInput')
        age = request.POST.get('ageInput')
        weight = request.POST.get('sizeInput')
        dog_Description=request.POST.get('dog_Description')
        

        # Filter the queryset based on form data
        animalData = Animal_dog.objects.filter(
            Q(name__icontains=petname),
            Q(breed=breed) if breed else Q(),
            Q(color=color) if color else Q(),
            Q(behavior=behavior) if behavior else Q(),
            Q(age=age) if age else Q(),
            Q(weight=weight) if weight else Q(),
        )
        print("Search vayepaxi ko records: ")
        print(animalData)

    else:
        # If the form is not submitted, show all records
        animalData = Animal_dog.objects.all()

    data = {'animalData': animalData}
    return render(request, 'showpets.html', data)

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
    catData = Cats.objects.all()

    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        color = request.POST.get('colour')
        age = request.POST.get('age')
        weight = request.POST.get('weight')
        Friendliness = request.POST.get('Friendliness')

        # Filter the queryset based on form datas
        catData = Cats.objects.filter(
            Q(name=name) if name else Q(),
            Q(color=color) if color else Q(),
            Q(age=age) if age else Q(),
            Q(weight=weight) if weight else Q(),
            Q(friendliness=Friendliness) if Friendliness else Q(),
        )
        print("Search results: ")
        print(catData)

    else:
        # If the form is not submitted, show all cat records
        catData = Cats.objects.all()

    data = {'catData': catData}
    return render(request, 'showcats.html', data)


from .models import Birds 
# ONLY FOR brids
def showbirds(request):
    birdData = Birds.objects.all()

    if request.method == 'POST':
        petname = request.POST.get('petName')
        species = request.POST.get('breedInput')
        color = request.POST.get('colourInput')
        age = request.POST.get('ageInput')

        # Filter the queryset based on form data
        birdData = Birds.objects.filter(
            Q(name__icontains=petname),
            Q(species=species) if species else Q(),
            Q(color=color) if color else Q(),
            Q(age=age) if age else Q(),
        )

    data = {'birdData': birdData}
    return render(request, 'showbirds.html', data)

def donation_form(request):
    
    return render(request, 'donation_form.html') 
   

def save_donateInfo(request):

    if request.method=="POST":
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        ph_number=request.POST.get('ph_number')
        amount=request.POST.get('amount')
        message=request.POST.get('message')
        

        record=Donation_data(full_name=full_name,email=email,phone_number=ph_number,message=message,amount=amount)
        record.save()
    return render(request, 'donation_form.html') 

def adoption_form(request):
    if request.method == 'POST':
        # Retrieve form data directly from request.POST
        name = request.POST.get('name_input')
        email = request.POST.get('email_input')
        phone = request.POST.get('telephone_input')
        country = request.POST.get('country')
        zip_code = request.POST.get('zipCode')
        city = request.POST.get('city')
        petname = request.POST.get('petname_input')
        petgender = request.POST.get('petgender')
        dogBreed = request.POST.get('dogBreed')
        experience = request.POST.get('Experience')
        reason_for_adoption = request.POST.get('Reason')

        # Create and save the DogAdoption model instance
        adoption_instance = DogAdoption.objects.create(
            name=name,
            email=email,
            telephone=phone,
            country=country,
            zip_code=zip_code,
            city=city,
            petname=petname,
            petgender=petgender,
            dogBreed=dogBreed,
            experience=experience,
            reason_for_adoption=reason_for_adoption,
        )
        return redirect("dash")  # Redirect to a success URL after successful form submission
    return render(request, 'adoption_form.html')

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

from django.contrib.auth.decorators import login_required
@login_required(login_url='/login_view')  # Replace 'login' with the actual URL name or path of your login view
def TryAdopt(request):
    # Your view logic for the 'tryadopt' page goes here
    return render(request, 'adoption_form.html')

@login_required(login_url='/login_view')
def logout_view(request):
    logout(request)
    return redirect('login_view')  # Redirect to your desired page after logout
