from django.contrib import admin
from accounts.models import contact, ProjectInput, InterviewInput

# Register your models here.
admin.site.register(contact)
admin.site.register(ProjectInput)
admin.site.register(InterviewInput)