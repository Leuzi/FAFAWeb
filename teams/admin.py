from django.contrib import admin
from teams.models import *

# Register your models here.
admin.site.register(Team)
admin.site.register(Stadium)
admin.site.register(Uniform)
admin.site.register(Logo)
admin.site.register(StadiumSeason)
admin.site.register(UniformSeason)
admin.site.register(LogoSeason)
