from django.shortcuts import render
from . models import Marchandise
from . models import product_details
from . models import Email
from . forms import ContactModelForm

from django.template.loader import get_template





# Create your views here.

def index(request):	
	return render(request, 'index.html')

def shop(request):
	march = Marchandise.objects.all()
	context = {
	'march':march,
	}
	return render(request, 'shop.html',context)


def Product_details(request):	
	march = Marchandise.objects.all()
	context = {
	'march':march

	}

	return render(request, 'product-details.html',context)


def order(request):
	form = ContactModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ContactModelForm()

	context = {
	"form":form,
	}
	return render(request, 'order.html',context)


