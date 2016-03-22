from django.contrib import admin
from pantry.models import Address, Pantry


class PantryAdmin(admin.ModelAdmin):
    readonly_fields=('coordinates', 'raw_coordinate_data')


admin.site.register(Address, PantryAdmin)
admin.site.register(Pantry)

