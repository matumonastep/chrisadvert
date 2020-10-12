from django.shortcuts import render
from django.http import HttpResponse
from . models import Marchandise
from . models import product_details
from . models import Email
from . forms import ContactModelForm
from chrisadvert.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, EmailMessage
from django.core.files.storage import FileSystemStorage
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

def contact(request):
	return render(request, 'contact.html')


def SendPlainEmail(request):
	pass

	

def send_mail_plain_with_stored_file(request):
	pass

def send_mail_plain_with_file(request):
    message = request.POST.get('message', '')
    subject = request.POST.get('subject', '')
    mail_id = request.POST.get('email', '')
    mail_id2 = request.POST.get('from_mail', '')

    email = EmailMessage(subject,message,EMAIL_HOST_USER,[mail_id2],[mail_id])
    email.content_subtype = 'html'

    file = request.FILES['file']
    email.attach(file.name, file.read(), file.content_type)

    email.send()
    return HttpResponse("Your Mail have been Sent")

