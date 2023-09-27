from django.contrib import admin
from crudapp2.models import Library   #### import library class in models file
class LibraryAdmin(admin.ModelAdmin):
    list_display=['member_id','member_name','book_price','member_city'] ### these are fields in database or models

admin.site.register(Library,LibraryAdmin) #### register in admin site
