from django.shortcuts import render
from app.forms import *

# Create your views here.

def hey_name(request):
    form = HeyName(request.GET)
    if form.is_valid():
        name = form.cleaned_data['name']
        answer = f'Hey, {name}'
        return render(request, "heyname.html", {"form": form, "name":  name})
    return render(request, "heyname.html", {"form": form})


def age_in(request):
  form = AgeForm(request.GET)
  if form.is_valid():
    end = form.cleaned_data["end"]
    birthyear = form.cleaned_data["birthyear"]
    age = end - birthyear
    print(age)
    return render(request, "age-in.html", {"form": form, "age": age})
  
  return render(request, "age-in.html", {"form": form})


def order(request):
  form = OrderForm(request.GET)
  if form.is_valid():
    burgers = form.cleaned_data["burgers"]
    fries = form.cleaned_data["fries"]
    drinks = form.cleaned_data["drinks"]
    total = (burgers * 4.50) + (fries * 1.50) + (drinks * 1.00)
    final = f'Your Total is ${total:.2f}!'
    return render(request, "order.html", {"form": form, "total" : final})
  return render(request, "order.html", {"form": form})
