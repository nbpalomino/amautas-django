from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
# Create your views here.
def index(request):
    jobs = Job.objects.all()
    context = {'title':'Amautas', 'jobs':jobs}
    return render(request, 'base.html', context)

def login(request):
    context = {'title':'Amautas'}
    return render(request, 'offers/index.html', context)

def show(req, job_id):
    job = Job.objects.get(pk=job_id)
    context = {'job':job}
    return render(req, 'offers/show.html', context)
