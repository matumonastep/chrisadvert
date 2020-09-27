from django.shortcuts import render,redirect
from django.contrib import messages
from . forms import UserRegisterForm
# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		form.save()
		if form.is_valid():
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your Account Has been created {username}!')
			return redirect('login')

	else:
		form = UserRegisterForm()

	return render(request, 'user/register.html', {'form':form})
