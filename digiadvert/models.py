from django.db import models

# Create your models here.

class Client(models.Model):
	NomClient = models.CharField(max_length = 250)
	PostNomCli = models.CharField(max_length = 250)
	PreNomCli = models.CharField(max_length = 250)
	AddressCli = models.CharField(max_length = 250)
	NumTelCli = models.CharField(max_length = 250)
	mailCli = models.CharField(max_length = 250)

	def __str__(self):
		return self.NomClient


class Marchandise(models.Model):

	CATEGORY = (
		('women','Women'),
		('men','Men'),
		('kid','Kid'),

		)
	CodeMarch = models.CharField(max_length = 250)
	NomMarch =models.CharField(max_length = 250)
	Designation = models.TextField()
	Quantity = models.CharField(max_length = 250)
	PrixUnitaire = models.CharField(max_length = 250)

class Magasinier(models.Model):
	CodeMag = models.CharField(max_length = 250)
	NomMag  = models.CharField(max_length = 250)
	NumTelMaga = models.CharField(max_length = 250)

	def __str__(self):
		return self.NomMag

class Fournisseur(models.Model):

	CodeFourni = models.CharField(max_length = 250)
	NomFourni  = models.CharField(max_length = 250)
	PostNomFourni  = models.CharField(max_length = 250)
	PreNomFourni = models.CharField(max_length = 250)
	AddressFourni = models.CharField(max_length = 250)
	NumTelFourni = models.CharField(max_length = 250)
	mailFourni = models.CharField(max_length = 250)

	def __str__(self):
		return self.NomFourni

class Email(models.Model):
	client = models.ForeignKey(Client, null = True, on_delete = models.SET_NULL)
	sujet = models.CharField(max_length = 250)
	description = models.TextField()

	def __str__(self):
		return self.client.NomClient



class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	client = models.ForeignKey(Client, null = True, on_delete = models.SET_NULL)
	marchandise = models.ForeignKey(Marchandise, null = True, on_delete = models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)


	def __str__(self):
		return self.marchandise.NomMarch

