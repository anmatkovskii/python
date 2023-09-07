from django.contrib import admin
from first_bot.models import Product, User, Orders
from import_export import resources
from import_export.admin import ImportExportModelAdmin


admin.site.register(Product)
admin.site.register(Orders)


class UserResource(resources.ModelResource):
   class Meta:
      model = User
class UserAdmin(ImportExportModelAdmin):
   resource_class = UserResource
admin.site.register(User, UserAdmin)