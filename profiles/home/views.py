from django.http.response import Http404
from django.shortcuts import redirect, render, HttpResponse
from django.http import FileResponse
from .forms import RegisterForm, ProfileCreationForm
from .constants import IMAGE_PATH
from .utils import file_handler
from .models import Profile
import os



# Create your views here.
def index(request):
	return redirect('home')

def home(request):
	user = request.user
	profile = None
	if user.is_authenticated:
		profile = Profile.objects.filter(author_email=user.email).first()
	context = {
		'profile': profile
	}
	return render(request, 'home/home.html', context=context)

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = RegisterForm()
	
	context = {
		'form': form
	}
	return render(request, 'home/register.html', context=context)


def create_profile(request):
	user = request.user
	if request.method == 'POST':
		form = ProfileCreationForm(request.POST)
		if form.is_valid():
			file = request.FILES['input-b1']
			file_name = file_handler(file, static_dir='images/')
			new_profile = Profile.objects.create(name=form.cleaned_data['name'], author_email=user.email, image_token=file_name)
			return redirect('home')
	else:
		form = ProfileCreationForm()
	
	profile = Profile.objects.filter(author_email=user.email).first()
	context = {
		'form': form,
		'profile': profile
	}
	return render(request, 'home/create-profile.html', context=context)

def image_token(request, token):
	path = os.path.join(IMAGE_PATH, f'{token}')
	if os.path.exists(path):
		image = open(path, 'rb')
		return FileResponse(image)
	return HttpResponse('image doesnt exist')

def delete_profile(request):
	user = request.user
	profile = Profile.objects.filter(author_email=user.email).first()
	if profile is not None:
		profile.delete()
	return redirect('home')
