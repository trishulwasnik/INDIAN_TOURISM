from django.contrib import admin
from kerelaapp.models import KERELA_MODEL

# Register your models here.
class KERELA_ADMIN(admin.ModelAdmin):
    Applicant_form=['DURATION','HOTELS','BUDGET','CITIES']
admin.site.register(KERELA_MODEL,KERELA_ADMIN)

