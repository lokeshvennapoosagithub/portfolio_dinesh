from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
      context = {
            'navbar': 'home'
      }
      return render(request, 'home.html', context)

def education(request):
      context = {
            'navbar': 'education'
      }
      return render(request, 'education.html', context)

def work_experience(request):
      context = {
            'navbar': 'experience'
      }
      return render(request, 'workexperience.html', context)

def achievements(request):
      context = {
            'navbar': 'achievements'
      }
      return render(request, 'achievements.html', context)

def contact(request):
      context = {
            'navbar': 'home'
      }
      return render(request, 'contact.html', context)