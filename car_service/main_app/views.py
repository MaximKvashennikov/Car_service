from django.shortcuts import render
from .models import Owner


def homepage(request):
    owner = Owner.objects.all()
    return render(request, "index.html", {'owner': owner})
