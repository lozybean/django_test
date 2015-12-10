from django.shortcuts import render

from .models import Person

# Create your views here.

def home(request):
    print list(request.META.iterkeys())
    vars = {
        'user': request.user,
        'address': request.get_host(),
        'peoples': list(Person.objects.all()),
    }
    return render(request, 'home.html', vars)
