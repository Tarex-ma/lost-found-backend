from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import User
from core.models import LostItem
from core.models import FoundItem
from core.models import ClaimRequest
from core.models import Comment
from core.models import Notification


admin.site.register(User, UserAdmin)
admin.site.register(LostItem)
admin.site.register(FoundItem)
admin.site.register(ClaimRequest)
admin.site.register(Comment)
admin.site.register(Notification)