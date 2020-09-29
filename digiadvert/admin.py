from django.contrib import admin
from django.contrib.auth.models import Group
from . models import Client
from . models import Magasinier
from . models import Fournisseur
from . models import Email

from . models import Order
from . models import Marchandise

# Register your models here.

admin.site.site_header = "Chris Admin Dashboard"

admin.site.register(Client)
admin.site.register(Magasinier)
admin.site.register(Fournisseur)
admin.site.register(Email)
admin.site.register(Order)
admin.site.register(Marchandise)



