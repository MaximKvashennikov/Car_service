from django.shortcuts import render, redirect
from .models import Owner, Feedback
from .forms import FeedbackForm


def homepage(request):
    owner = Owner.objects.all()
    form = FeedbackForm()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            delete_old_feedback()
            form.save()
            return redirect('/')

    data = {
        'owner': owner,
        'form': form,
    }

    return render(request, "index.html", data)


def delete_old_feedback():
    """The function keeps the last 100 reviews and deletes the old ones."""
    if Feedback.objects.count() > 99:
        max_date = Feedback.objects.order_by('-date_create')[98]
        Feedback.objects.filter(date_create__lt=max_date.date_create).delete()
