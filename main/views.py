from django.shortcuts import render
from .forms import CustomForms
# Create your views here.
def index(request):
    form = CustomForms(request.POST or None, request.FILES or None)

    context = {
        'form': form
    }
    return render(request, 'index.html', context)