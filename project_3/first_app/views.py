from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    d = {'author' : 'Rahim', 'age' : 9, 'lst' : ["Amin","Anna","Abir"], 'courses': [
        {
            'id' : 1,
            'name' : 'Python'
        },
        {
            'id' : 2,
            'name' : 'C'
        },
        {
            'id' : 3,
            'name' : 'CSharp'
        }
    ], 'birthday': datetime.datetime.now()}
    return render(request, "first_app/home.html", context=d)