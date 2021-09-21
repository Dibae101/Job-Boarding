from django.contrib import admin
from .models import DesignerRegister, ProjectDescriptionModel, ProjectTagsModel, DesignerExperience, DesignerEducation


# Register your models here.

admin.site.register(DesignerRegister)
admin.site.register(ProjectDescriptionModel)
admin.site.register(ProjectTagsModel)

admin.site.register(DesignerExperience)
admin.site.register(DesignerEducation)