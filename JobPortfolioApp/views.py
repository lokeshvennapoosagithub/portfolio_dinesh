from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
      return render(request, 'home.html')

def education(request):
      return render(request, 'education.html')

def work_experience(request):
      return render(request, 'workexperience.html')

def achievements(request):
      return render(request, 'achievements.html')

def contact(request):
      return render(request, 'contact.html')