from django.http import HttpResponse
from django.shortcuts import render
from .models import place, plac


# Create your views here.
def bikedemo(request):
    obj=place.objects.all()
    obj1=plac.objects.all()
    return render(request, 'index.html', {'result':obj,'results':obj1})

