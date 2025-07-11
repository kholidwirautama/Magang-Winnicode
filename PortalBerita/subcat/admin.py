from django.contrib import admin
from .models import SubCat

# Custom admin untuk SubCat
class SubCatAdmin(admin.ModelAdmin):
    list_display = ('catid', 'catname', 'name')  # Kolom yang akan ditampilkan di admin

admin.site.register(SubCat, SubCatAdmin)