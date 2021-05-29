from django.apps import AppConfig
from testapp.models import Resume

class ResumeAdmin(admin.ModelAdmin):
    list_display=['name']



admin.site.register(Resume,ResumeAdmin)