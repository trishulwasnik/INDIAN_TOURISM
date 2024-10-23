from django.contrib import admin
from andamanapp.models import ANDAMAN_MODEL


# Register your models here.
class ANDAMAN_ADMIN(admin.ModelAdmin):
    Applicant_form=['DURATION','HOTELS','BUDGET','CITIES']
admin.site.register(ANDAMAN_MODEL,ANDAMAN_ADMIN)