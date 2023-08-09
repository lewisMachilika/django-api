from django.contrib import admin
from .models import CustomUser

admin.site.site_header = "Client Dashboard"
admin.site.site_title = "Food Delivery"
admin.site.index_title = "Welcome Foot Delivery Portal"

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'email','phone','user_type')


