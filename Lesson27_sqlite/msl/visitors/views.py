from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Visitor
from django.views.generic import ListView, TemplateView, DetailView

class VisitorListView(ListView):
    model = Visitor
    template_name = 'visitors/visitors.html'


class AboutTemlateView(TemplateView):
    template_name = 'visitors/about.html'


class VisitorDetailView(DetailView):
    model = Visitor
    template_name = 'visitors/visitors_full.html'


def index(request):
    visitors = Visitor.objects.all()
    #visitors = Visitor.objects.select_related('first_name', 'ticket__name_visitors')
    context = {
        'visitors': visitors,
        'org_name': 'Детский центр "Тропикано"'
    }
    return render(request, 'visitors/index.html', context=context)