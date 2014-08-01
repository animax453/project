from django.contrib import admin
from scratchApp.models import User,Player
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    exclude=["posted"]
    
class PlayerAdmin(admin.ModelAdmin):
    exclude=["posted"]
    
admin.site.register(User,UserAdmin)
admin.site.register(Player,PlayerAdmin)
