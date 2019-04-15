from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.db import models
from .models import Human
from .forms import HumanForm
# Create your views here.

class List(TemplateView):

    def get(self, request):
        humans = Human.objects.all()
        sort_humans_birth = Human.objects.all().order_by('-birth')
        sort_humans_salary = Human.objects.all().order_by('salary')
        return render(request,'content.html',context={'humans':humans,
                                                      'sort_humans_birth': sort_humans_birth,
                                                      'sort_humans_salary' : sort_humans_salary})
    def post(self, request):
        query = request.POST['company']
        humans = Human.objects.filter(company=query)
        return render(request,'search.html', context = {'humans':humans})


