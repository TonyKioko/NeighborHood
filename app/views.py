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

    nhoods = Neighborhood.objects.all()
    context ={"nhoods":nhoods,"message":message}

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


# @login_required
def join_hood(request,id):
    hood = get_object_or_404(Neighborhood, pk=id)
    request.user.profile.neighborhood = hood
    request.user.profile.save()
    return redirect(index)
@login_required
def exit_hood(request,id):
    hood = get_object_or_404(Neighborhood, pk=id)
    if request.user.profile.neighborhood == hood:
        request.user.profile.neighborhood=None
        request.user.profile.save()
    return redirect('index')
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

def new_alert(request):
	current_user = request.user
	if request.method == 'POST':
		form = AlertForm(request.POST,request.FILES)
		if form.is_valid():
			new_business = form.save(commit=False)
			new_business.user = current_user
			new_business.save()
            # messages.success(request, "Image uploaded!")
			return redirect('index')
	else:
			form = AlertForm()
            # context= {"form":form}
	return render(request, 'new_alert.html',{"form":form})

def search_business(request):
    # profile = Profile.get_profile()

    # if 'caption' in request.GET and request.GET["caption"]:
    if 'name' in request.GET and request.GET["name"]:

        search_term = request.GET.get("name")
        found_businesses = Business.search_by_name(search_term)
        message = f"{search_term}"
        print(search_term)

        context = {"found_businesses":found_businesses,"message":message}

        return render(request, 'search.html',context)

    else:
        message = "You haven't searched for any term"
        # context={"message":message}
        return render(request, 'search.html',{"message":message})
