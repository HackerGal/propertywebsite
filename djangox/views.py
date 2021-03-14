from django.shortcuts import render, redirect
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login

# add login function to the login page
def register(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      login(request, user)
      return redirect("Property Website/mainpage .html")

    else:
        for msg in form.error_messages:
          print(form.error_messages[msg])

        return render(request = request,
                      template_name = "Property Website/register.html",
                      context={"form":form})

  form = UserCreationForm
  return render(request = request,
                template_name = "Property Website/register.html",
                context={"form":form})

def login_request(request):
  form = AuthenticationForm(request=request, data=request.POST)
  if form.is_valid(): 
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')
    user = authenticate(username=username, password=password)
  return render(request = request,
                template_name = "Property Website/loginpage.html",
                context = {"form":form})