from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.

# def wedding(request):
#     wedding = Wedding.objects.first()
#     return render(request, 'wedding_details.html', {'wedding': wedding})


def rsvp(request):
    if request.method == 'POST':
        form = RSVPForm(request.POST)
        if form.is_valid():
            attending = form.cleaned_data.get('attending')
            if attending:
                form.save()
                return redirect('thank_you')
            else:
                return render(request, 'rsvp/not_attending.html')
    else:
        form = RSVPForm()
    return render(request, 'rsvp/rsvp_form.html', {'form': form})

def thank_you(request):
    return render(request, 'rsvp/thank_you.html')
