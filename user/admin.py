from django.contrib import admin
from .models import (CustomUser , CustomUserRole, 
                     CustomUserPermission,CustomUserModule)

admin.site.register(CustomUser)
admin.site.register(CustomUserRole)
admin.site.register(CustomUserPermission)
admin.site.register(CustomUserModule)

