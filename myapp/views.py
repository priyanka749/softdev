from imaplib import _Authenticator
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_list_or_404
from django.contrib import messages

from .models import ContactMessage

def login(request):
    return render(request,'login.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = _Authenticator(request, email=email, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page or perform actions after successful login
            return redirect('dash.html') # Replace 'success_page' with your URL name
        
        else:
            messages.error(request, 'Incorrect email or password. Please try again.')

    return render(request, 'login.html')  # Render the login page

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

# def profile(request, pet_id):
    
#     pet = get_object_or_404(Animal_dog, pet_id=pet_id)

#     # Prepare data to be passed to the template
#     data = {
#         'pet': pet,
#     }

#     # Render the profile template with the pet details
#     print(data)
#     return render(request, 'profile.html', data)

from django.shortcuts import render, get_object_or_404
from .models import Animal_dog, Cats

def profile(request, pet_id, animal_type):
    # Use a generic model name parameter to handle both dogs and cats
    model_class = Animal_dog if animal_type == 'dog' else Cats

    # Choose the appropriate identifier field based on the animal_type
    identifier_field = 'cat_id' if animal_type == 'cats' else 'pet_id'

    # Retrieve the specific pet object based on the identifier field and pet_id
    pet = get_object_or_404(model_class, **{identifier_field: pet_id})

    # Prepare data to be passed to the template
    data = {
        'pet': pet,
        'animal_type': animal_type,  # Pass the animal type to the template
    }

    # Render the profile template with the pet details
    print(data)
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
# ONLY FOR CATS
def showbirds(request):
    BirdsData=Birds.objects.all() 
    data={
        'BirdsData':BirdsData
    }
    return render(request, 'showbirds.html',data)  # Assuming your form is in showpets.html


