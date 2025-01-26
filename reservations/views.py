from django.shortcuts import render
from .forms import ReservationsForm

# Create your views here.
def reservations(request):
    form = ReservationsForm()
    if request.method == "POST":
        form = ReservationsForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, 'reservations.html', context)