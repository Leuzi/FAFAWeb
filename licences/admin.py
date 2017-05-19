from django.contrib import admin
from licences.models import *

# Register your models here.
admin.site.register(LicenceType)
admin.site.register(Licence)
admin.site.register(LicenceState)
admin.site.register(LicenceDuration)
admin.site.register(ValidFor)
