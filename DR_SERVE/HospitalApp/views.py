from django.shortcuts import render
from django.http import HttpResponse
# from .models import Service
# from .models import Hospital


# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate
# from django.contrib import messages
# from django.urls import reverse
# from django.views.decorators.csrf import csrf_protect
# Create your views here.
def Home(request):
    # return HttpResponse("hello hospital home")
    return render(request,'HospitalApp/Home.html')
def Management(request):
    return render(request,'HospitalApp/Management.html')

def About(request):
    return render(request,'HospitalApp/About.html')
# @csrf_protect
def Make_Payment(request):

    return render(request, 'HospitalApp/make-payment.html')

   
        
    



# Assuming you have a Service model to store service details


def Register(request):
   return render(request,'HospitalApp/Register.html')
 
    
   



def Signin(request):
    return render(request,'HospitalApp/Signin.html')

def Forgot_Password(request):
    return render(request,'HospitalApp/Forgot_Password.html')
def Whats_new(request):
    return render(request,"HospitalApp/What's_new.html")
def Contactus(request):
    return render(request,'HospitalApp/Contactus.html')
































#     if request.method == 'POST':
#         # Get form data
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('cpassword')
#         selected_services = request.POST.getlist('services')  # Get list of selected services
        
#         # Form validation
#         if password != confirm_password:
#             messages.error(request, "Passwords do not match!")
#             return redirect('HospitalApp:Register')  # Redirect back to register page
        
#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email is already in use!")
#             return redirect('HospitalApp:Register')
        
#         # Create a new user
#         user = User.objects.create_user(username=email, email=email, password=password)
        
#         # Add the selected services (assume Service is a model for services)
#         for service_id in selected_services:
#             service = Service.objects.get(id=service_id)
#             user.Hospital.Service.add(service)  # Assuming user has a related profile to store services
        
#         # Authenticate and log the user in
#         user = authenticate(request, username=email, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Registration successful!")
#             return redirect(reverse('HospitalApp:Make_Payment'))  # Redirect to payment page
#         else:
#             messages.error(request, "Registration failed. Please try again.")
#             return redirect('RHospitalApp:Register')
#      # GET request, render the register template
#     services = Service.objects.all()  # Fetch available services for checkboxes
    # return render(request, 'HospitalApp/make-payment.html', {'services': services})