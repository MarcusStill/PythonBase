from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Visitor

def index(request):
    visitors = Visitor.objects.all()
    context = {
        'visitors': visitors,
        'org_name': 'Детский центр "Тропикано"'
    }
    return render(request, 'visitors/index.html', context=context)
    #return HttpResponse("Test recording. Visitors index.")