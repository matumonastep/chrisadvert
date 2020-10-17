from django.db import models
from twilio.rest import Client

# Create your models here.

class Address(models.Model):
	STATUS = (

		('client','Client'),
		('fournisseur','Fournisseur')
		)

	email = models.CharField(max_length = 200)
	TelPhone = models.CharField(max_length = 200)
	category = models.CharField(max_length=200, null=True, choices = STATUS )

	def __str__(self):
		return self.email

class Client_T(models.Model):
	NomClient = models.CharField(max_length = 250)
	PostNomCli = models.CharField(max_length = 250)
	PreNomCli = models.CharField(max_length = 250)
	address = models.ForeignKey(Address, null = True, on_delete = models.SET_NULL)

	def __str__(self):
		return self.NomClient
		
class Fournisseur(models.Model):
	CodeFourni = models.CharField(max_length = 250)
	NomFourni  = models.CharField(max_length = 250)
	PostNomFourni  = models.CharField(max_length = 250)
	PreNomFourni = models.CharField(max_length = 250)
	address = models.ForeignKey(Address, null = True, on_delete = models.SET_NULL)

	def __str__(self):
		return self.NomFourni

class Contact(models.Model):
	TelPhone = models.PositiveIntegerField()

	def __str__(self):
		return str(self.TelPhone)


	def save(self, *args, **kwargs):

		if self.TelPhone > 1:
			account_sid = 'AC11b29ee73b0bc8a6b4d2b8e5159f4180'
			auth_token = 'b6dc9c8fed141e8a11ae62baa1a6ba7b'
			client = Client(account_sid, auth_token)

			message = client.messages.create(
			                              body='Bienvenue cher client, vous recevrez un message SMS à chaque fois que le nouveau produit est sorti merci!',
			                              from_='+12319946563',
			                              to='+256705340567'
			                          )

			print(message.sid)
		return super().save(*args, **kwargs)












class Magasinier(models.Model):
	CodeMag = models.CharField(max_length = 250)
	NomMag  = models.CharField(max_length = 250)
	NumTelMaga = models.CharField(max_length = 250)

	def __str__(self):
		return self.NomMag


class Marchandise(models.Model):

	CATEGORY = (
		('women','Women'),
		('men','Men'),
		('kid','Kid'),

		)
	imageMarch = models.FileField(upload_to = 'marchandise')
	CodeMarch = models.CharField(max_length = 250)
	NomMarch =models.CharField(max_length = 250)
	Designation = models.TextField()
	Quantity = models.CharField(max_length = 250)
	PrixUnitaire = models.CharField(max_length = 250)
	fournisseur = models.ForeignKey(Fournisseur, null = True, on_delete = models.SET_NULL)
	Magasinier = models.ForeignKey(Magasinier, null = True, on_delete = models.SET_NULL)

	def __str__(self):
		return self.NomMarch


class product_details(models.Model):
	marchimg = models.ForeignKey(Marchandise, on_delete=models.CASCADE)







class Email(models.Model):
	Addmail = models.EmailField()
	Client = models.CharField(max_length = 250)
	sujet = models.CharField(max_length = 250)
	description = models.TextField()

	def __str__(self):
		return self.Client



class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	client = models.ForeignKey(Client_T, null = True, on_delete = models.SET_NULL)
	marchandise = models.ForeignKey(Marchandise, null = True, on_delete = models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)


	def __str__(self):
		return self.marchandise.NomMarch











