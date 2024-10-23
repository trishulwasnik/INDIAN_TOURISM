from django.contrib import admin
from darjelingapp.models import DARJELING_MODEL

# Register your models here.
class DARJELING_ADMIN(admin.ModelAdmin):
    Applicant_form=['DURATION','HOTELS','BUDGET','CITIES']
admin.site.register(DARJELING_MODEL,DARJELING_ADMIN)
