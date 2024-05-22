from django.shortcuts import render, redirect
from django.contrib import messages
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.conf import settings

User = settings.AUTH_USER_MODEL

#signup
def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            username = form.cleaned_data.get ("username")
            messages.success(request, f'Your {username }account has been created successfully! You can now log in.')
            new_user =authenticate(username=form.cleaned_data['email'],password=form.cleaned_data['password1'])
            login(request,new_user)
            return redirect("core:index")
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, "userauths/sign-in.html", context)

#login
def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request,f"already logged in")
        return redirect("core:index") 
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get (email=email)
        except:
            messages.warning(request,f"Does not exist")

        user = authenticate (request, email=email , password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"logged in")
            return redirect("core:index")
        else:
            messages.warning(request,"user Does Not exist")
    context={}

    return render(request,"userauths/sign-up.html")
