from django.contrib import admin

from .models import user,type,clean,mycart,orders

# Register your models here.
admin.site.register(user)
admin.site.register(type)
admin.site.register(clean)
admin.site.register(mycart)
admin.site.register(orders)
