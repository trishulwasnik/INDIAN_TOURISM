from django.contrib import admin
from manaliapp.models import MANALI_MODEL

# Register your models here.
class MANALI_ADMIN(admin.ModelAdmin):
    Applicant_form=['DURATION','HOTELS','BUDGET','CITIES']
admin.site.register(MANALI_MODEL,MANALI_ADMIN)
