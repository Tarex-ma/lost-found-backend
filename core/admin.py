from django.contrib import admin
from .models import LostItem, FoundItem, ClaimRequest, Comment
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )

admin.site.register(User, CustomUserAdmin)

class LostItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'location', 'status', 'created_at')
    list_filter = ('status', 'category')
    search_fields = ('title', 'description', 'location')
class FoundItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'location', 'status', 'created_at')
    list_filter = ('status', 'category')
    search_fields = ('title', 'description', 'location')
class ClaimRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'lost_item', 'found_item', 'status', 'created_at')
    list_filter = ('status',)
    
admin.site.register(LostItem, LostItemAdmin)
admin.site.register(FoundItem, FoundItemAdmin)
admin.site.register(ClaimRequest, ClaimRequestAdmin)
admin.site.register(Comment)