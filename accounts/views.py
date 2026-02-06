from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login,logout, authenticate 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

# register view
def register(request):
    if request.method=='POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
        form.save()
        form = UserCreationForm()
        messages.success(request, "User is successfully created.")
        return redirect('login') 
       
    else:
       form = UserCreationForm()
    return render(request, 'accounts/registration.html',{'form':form})


# login view
def login(request):
    if request.method=='POST':
       form = AuthenticationForm(request,data=request.POST)

       username = form.cleaned_data.get('username')
       password = form.cleaned_data.get('password')

       user=authenticate(username=username, password=password)

       if user is not None:
        login(request, user)
        messages.success(request,"You are successfully logged in.")
        return redirect('home')
       else:
          messages.error(request,"Username or password is invalid.")
    else:
       form = AuthenticationForm()     


    return render(request, 'registration/login.html',{'form':form})


# # login view
# def loginView(request):

#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username=username, password=password)

#         if user is not None:
#             login(request, user)
#             messages.info(request,"You are successfully logged in.")
#             return redirect('home')
#         else:
#             messages.error(request,"Invalid username or password")
#             return redirect('login')
      
   
#     return render(request, 'accounts/login.html', {})

@login_required
def logoutView(request):
    
   if request.method == "POST":
      logout(request)
      messages.info(request,"You are successfully logged out!")
      return redirect('login')
       
    
    
   return render(request, "registration/logout.html", {}) 