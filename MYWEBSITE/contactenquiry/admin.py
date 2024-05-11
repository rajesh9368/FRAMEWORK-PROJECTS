from django.contrib import admin
from contactenquiry.models import contactEnquiry
# Register your models here.
class CN(admin.ModelAdmin):
  list_display = ('name','email','phone','website','message')
admin.site.register(contactEnquiry,CN)
# Register your models here.
