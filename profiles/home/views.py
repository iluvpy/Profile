from django.shortcuts import redirect, render
from .forms import RegisterForm

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