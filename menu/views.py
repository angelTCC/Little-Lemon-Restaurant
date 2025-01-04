from django.shortcuts import render
from .models import MenuItem

# Create your views here.
def menu(request):
    menu_data = MenuItem.objects.all()
    #menu_data = {"menu":menu_data}
    return render(request, 'menu.html', {"menu":menu_data})