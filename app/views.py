from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from app.models import *
from app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
# @login_required(login_url='/accounts/login/')
def index(request):

    message = "Hello World"


    context ={"message":message}

    return render(request,'index.html',context)
# @login_required(login_url='/accounts/login')
def new_nhood(request):
	current_user = request.user
	if request.method == 'POST':
		form = NeighborhoodForm(request.POST,request.FILES)
		if form.is_valid():
			new_nhood = form.save(commit=False)
			new_nhood.user = current_user
			new_nhood.save()
            # messages.success(request, "Image uploaded!")
			return redirect('index')
	else:
			form = NeighborhoodForm()
            # context= {"form":form}
	return render(request, 'new_nhood.html',{"form":form})

def new_business(request):
	current_user = request.user
	if request.method == 'POST':
		form = BusinessForm(request.POST,request.FILES)
		if form.is_valid():
			new_business = form.save(commit=False)
			new_business.user = current_user
			new_business.save()
            # messages.success(request, "Image uploaded!")
			return redirect('index')
	else:
			form = BusinessForm()
            # context= {"form":form}
	return render(request, 'new_business.html',{"form":form})
