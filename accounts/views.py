from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully. Please log in.")
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "accounts/registration.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("resource-page")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            messages.success(request, "You are successfully logged in.")

            next_url = request.GET.get("next")
            if next_url:
                return redirect(next_url)

            return redirect("resource-page")

        messages.error(request, "Username or password is invalid.")
    else:
        form = AuthenticationForm()

    return render(request, "registration/login.html", {"form": form})


@login_required
def logout_view(request):
    if request.method == "POST":
        auth_logout(request)
        messages.info(request, "You are successfully logged out.")
        return redirect("login")

    return render(request, "registration/logout.html")
    
