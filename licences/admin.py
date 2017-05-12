from django.contrib import admin
from licences.models import *

# Register your models here.
admin.site.register(LicenceType)
admin.site.register(States)
admin.site.register(LicenceDuration)
admin.site.register(LicenceSesion)
admin.site.register(ValidFor)
