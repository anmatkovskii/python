from django.contrib import admin
from main_backend.models import User, Task


admin.site.register(User),
admin.site.register(Task)
