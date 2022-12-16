from django.contrib import admin
from mysite.models import Socity_Members,Notice,Visitors,Events,Watchman,Complaint


# Register your models here.
admin.site.register(Socity_Members)
admin.site.register(Notice)
admin.site.register(Visitors)
admin.site.register(Events)
admin.site.register(Watchman)
admin.site.register(Complaint)

# @admin.register(Socity_Members)
# class UserAdmin(admin.ModelAdmin):
    # list_display=['product_name','product_price','product_info','Product_image']