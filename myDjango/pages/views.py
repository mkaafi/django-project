from django.shortcuts import render

def home(request):
	return render(request, "home.html", {})

def about(request):
	from pages.main import namer
	return render(request, "about.html", {"my_name": namer})

def contact(request):
	return render(request, "contact.html", {})
