from django.contrib import admin
from second_app.models import Product, Match
from import_export import resources
from import_export.admin import ImportExportModelAdmin


admin.site.register(Product),
class MatchResource(resources.ModelResource):
   class Meta:
      model = Match
class MatchAdmin(ImportExportModelAdmin):
   resource_class = MatchResource
admin.site.register(Match, MatchAdmin)
# Register your models here.
