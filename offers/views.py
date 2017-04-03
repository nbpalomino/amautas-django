from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Job
from .forms import OfferForm
# Create your views here.

# URL: ofertas/
def index(request):
    jobs = Job.objects.all()
    context = {'title':'Amautas', 'jobs':jobs}
    return render(request, 'offers/index.html', context)

# URL: ofertas/:job_id
def show(request, job_id):
    job = Job.objects.get(pk=job_id)
    context = {'job':job}
    return render(request, 'offers/show.html', context)

# URL: ofertas/create
def create(request):
    form = OfferForm()
    context = {
            'title':'Amautas',
            'form':form
        }

    return render(request, 'offers/create.html', context)

# URL: ofertas/store (method=POST)
def store(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            context = {
                    'title':'Amautas',
                    'form':form
                }
            return render(request, 'offers/create.html', context)
    return HttpResponseRedirect('/ofertas/create')

# URL: ofertas/:job_id/edit
def edit(request):
    context = {'title':'Amautas'}
    return render(request, 'offers/edit.html', context)

# URL: ofertas/:job_id/update (method=POST)
def update(request):
    context = {'title':'Amautas'}
    return render(request, 'offers/update.html', context)

# URL: ofertas/:job_id/delete (method=POST)
def delete(request):
    context = {'title':'Amautas'}
    return render(request, 'offers/delete.html', context)
