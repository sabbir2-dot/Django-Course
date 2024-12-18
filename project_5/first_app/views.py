from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, './first_app/home.html')

def about(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, './first_app/about.html', {'name' : name, 'email' : email, 'select': select})
    else:
        return render(request, './first_app/about.html')

def submit_form(request):
    # if request.method == 'POST':
    #     name = request.POST.get('username')
    #     email = request.POST.get('email')
    #     return render(request, './first_app/form.html', {'name' : name, 'email' : email})
    # else:
        return render(request, './first_app/form.html')

def DjangoForm(request):
    if request.method == 'POST':
        form = forms.contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #      for chunk in file.chunks():
            #           destination.write(chunk)
            print(form.cleaned_data)
    else:
         form = forms.contactForm()
    return render(request, './first_app/django_form.html', {'form' : form})


def StudentForm(request):
     if request.method == 'POST':
          form = forms.StudentData(request.POST)
          if form.is_valid():
               print(form.cleaned_data)
     else:
        form = forms.StudentData()
     return render(request, './first_app/django_form.html', {'form' : form})

              
def PasswordValidation(request):
     if request.method == 'POST':
          form = forms.PasswordValidationProject(request.POST)
          if form.is_valid():
               print(form.cleaned_data)
     else:
          form = forms.PasswordValidationProject()
     return render(request, './first_app/django_form.html', {'form' : form})