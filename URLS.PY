
from django.contrib import admin
from django.urls import path
from crudapp2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('check/',views.get_view),
    path('add/',views.create_view),
    path('delete/<id>',views.delete_view),     #### it will get the fields id (arguments),see index.html file
    path('update/<id>',views.update_view),
]
