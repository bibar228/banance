from django.contrib import admin

from vision.models import Orders


# Register your models here.
class OrdersAdmin(admin.ModelAdmin):
    list_display = ["name_cript", "side", "id"]

admin.site.register(Orders, OrdersAdmin)