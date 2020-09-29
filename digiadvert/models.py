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

	client = models.ForeignKey(Client, null = True, on_delete = models.SET_NULL)
	marchandise = models.ForeignKey(Marchandise, null = True, on_delete = models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)


	def __str__(self):
		return self.marchandise.NomMarch

