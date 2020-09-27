from django.contrib import admin
from django.contrib.auth.models import Group
from . models import *
# Register your models here.

admin.site.site_header = "Chris Admin Dashboard"

admin.site.register(Client)
admin.site.register(Magasinier)
admin.site.register(Fournisseur)
admin.site.register(Email)
admin.site.register(Order)