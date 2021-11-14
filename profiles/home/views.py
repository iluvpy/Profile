from django.http.response import Http404
from django.shortcuts import redirect, render, HttpResponse
from django.http import FileResponse
from .forms import RegisterForm
from .constants import IMAGE_PATH
import os



# Create your views here.
def index(request):
	return redirect('home')

def home(request):

	context = {
		'user': request.user
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

def image_token(request, token):
	path = os.path.join(IMAGE_PATH, f'{token}')
	if os.path.exists(path):
		image = open(path, 'rb')
		return FileResponse(image)
	return HttpResponse('image doesnt exist')