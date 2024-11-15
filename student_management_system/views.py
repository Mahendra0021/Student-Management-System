from django.shortcuts import render, redirect, HttpResponse
from APP.EmailBackend import EmailBackend
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from APP.models import CustomUser
from APP.models import Profile

def BASE(request):
    return render(request, 'base.html')

def Login(request):
    return render(request, 'login.html')

def doLogin(request):
    if request.method == "POST":
        # Authenticate user via email and password
        user = EmailBackend.authenticate(
            request,
            username=request.POST.get('email'),
            password=request.POST.get('password'),
        )
        
        if user is not None:
            login(request, user)
            user_type = user.user_type
            print(f"User type: {user_type}")  # Debug to check user_type


            # Check user type and respond accordingly
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return redirect('staff_home')
            elif user_type == '3':
                return redirect('student_home')
            else:
                messages.error(request, "Email and Password Are Invalid !..")
                return redirect('login')
        else:
            messages.error(request, "Email and Password Are Invalid !..")
            return redirect('login')
    
    # For GET requests, redirect to the login page
    # return redirect('login')



def doLogout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/')
def Profile(request):
    user = CustomUser.objects.get(id = request.user.id)
   
    print(user)
    context = { "user":user}
    return render (request, 'profiles.html',context)

@login_required(login_url='/')
def Profile_update(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name 
            # customuser.profile_pic = profile_pic 

            if password:
                customuser.set_password(password)
            if profile_pic:
                customuser.profile_pic = profile_pic
               
            customuser.save()
            messages.success(request, "Your Profile Updated Successfully!")
            return redirect('profile')

        except CustomUser.DoesNotExist:
            messages.error(request, "User does not exist.")
            return redirect('login')  # Redirect to login or any other page
        except Exception as e:
            messages.error(request, f"Failed to Update Your Profile! Error: {e}")
      
    return render(request, 'profiles.html')
