from django.shortcuts import render, redirect
from .models import Owner
from .forms import FeedbackForm


def homepage(request):
    owner = Owner.objects.all()
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    data = {
        'owner': owner,
        'form': form,
    }

    return render(request, "index.html", data)
