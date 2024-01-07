from imaplib import _Authenticator
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages

from .models import ContactMessage, User_profile
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user with both email and password
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Check if the authenticated user's name matches the provided name (optional)
            if user.first_name == name:
                login(request, user)
                # Redirect to a success page or perform actions after successful login
                return redirect('dash')  # Replace 'dash' with your URL name
            else:
                messages.error(request, 'Name does not match the provided email/password.')
        else:
            messages.error(request, 'Incorrect email or password. Please try again.')
    
    return render(request,'login.html')

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def signup(request):
    

        # Redirect to a success page or login page
    # Replace 'login' with your login URL name
      
    return render(request, 'signup.html')  # Render the signup page

def save(request):
    if request.method == 'POST':
        print("helo")
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password')
        print(name)
        # if password != confirm_password:
        #     messages.error(request, 'Passwords do not match. Please try again.')
        #     return redirect('signup')  # Redirect to the signup page with error message

        # if User.objects.filter(email=email).exists():
        #     messages.error(request, 'The email is already taken. Please use a different email.')
        #     return redirect('signup')  # Redirect to the signup page with error message

        # Create a new user with name, email, and password
        new_user = User_profile.create(name=name, email=email, password=password)
        # new_user.name = name  # Set the user's first name
        # user.is_active = False  # Account needs to be activated via email confirmation
        new_user.save()

        # messages.success(request, 'Your account has been created. Please check your email for confirmation.')
        return redirect('login')  # Replace 'login' with your login URL name
      
    return render(request, 'signup.html')  # Render the signup page





# def contact(request):
#     if request.method == 'POST':
#         full_name = request.POST.get('full_name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')

#         # Basic validation, you can add more complex validation as per your needs
#         if not (full_name and email and message):
#             messages.error(request, 'Please fill in all fields.')
#         else:
#             # Example sending an email (requires email backend setup in settings.py)
#             email(
#                 subject='Contact Form Submission',
#                 message=f'Name: {full_name}\nEmail: {email}\nMessage: {message}',
#                 from_email=email,
#                 recipient_list=['your@example.com'],  # Replace with your email
#                 fail_silently=False,  # Set it to True for production
#             )
#             messages.success(request, 'Your message has been sent. We will get back to you soon!')

#     return render(request, 'contact.html')



def dash(request):
    
    return render(request, 'dash.html', {'login':login ,signup:signup}) 
   
def faq(request):
        
        # Your view logic for handling FAQ requests
        return render(request,'faq.html')



def aboutus(request):
    return render(request,'aboutus.html')
# views.py

# from django.shortcuts import render
# from django.http import HttpResponse
from .models import DogAdoption  # Import your DogAdoption model
 # Import your DogAdoptionForm if you have a custom form
from django.shortcuts import render
# from .forms import DogAdoptionForm  # Import your DogAdoptionForm from forms.py
from .models import DogAdoption  # Import your DogAdoption model if available
from django.shortcuts import render, redirect
from .models import DogAdoption  # Import your DogAdoption model


from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import DogAdoption

def adoption_form(request):
    if request.method == 'POST':
        # Retrieve data from POST request
        name = request.POST.get('name', 'hari')
        email = request.POST.get('email', '')
        telephone = request.POST.get('telephone', '9852182125')
        country = request.POST.get('country', '')
        zip_code = request.POST.get('zip_code', '')
        city = request.POST.get('city', '')
        petname = request.POST.get('petname', '')
        petgender = request.POST.get('petgender', '')
        dog_breed = request.POST.get('dogBreed', '')
        experience = request.POST.get('experience', '')
        reason_for_adoption = request.POST.get('reason_for_adoption', '')

        # Create DogAdoption instance and save
        dog_adoption = DogAdoption(
            name=name,
            email=email,
            telephone=telephone,
            country=country,
            zip_code=zip_code,
            city=city,
            petname=petname,
            petgender=petgender,
            dogBreed=dog_breed,
            experience=experience,
            reason_for_adoption=reason_for_adoption
        )
        dog_adoption.save()

        # Redirect to a success page or render a success message
        return render(request, 'success.html')  # Assuming success.html exists
    else:
        # Render the form on GET request
        return render(request, 'dog_adoption.html')


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
        # c.name=name
        # c.email=email
        # c.telephone=telephone
        # c.subject=subject
        # c.message=message
        c.save()
        
    return render(request, 'contact_view.html')
        # form = ContactMessage(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return HttpResponseRedirect('/success/')  # Redirect to a success page after form submission
    # else:
    #     form = ContactMessage()
    

    
    
    # return render(request, 'contact_form.html', {'form': form})