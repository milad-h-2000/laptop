from django.shortcuts import render, get_object_or_404
from .models import Computer

def home(request):
    return render(request, 'computer\\home.html')


def computers(request):
    computers = Computer.objects.all()
    my_dict = {'computers': computers}
    return render(request, 'computer\\computers.html', my_dict)


def computer_details(request, computer_id):
    computer = get_object_or_404(Computer, pk=computer_id)
    return render(request, 'computer\\computer_details.html', {"computer": computer})