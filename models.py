from django.db import models
class Library(models.Model):
    member_id=models.IntegerField()
    member_name=models.CharField(max_length=100)
    book_price=models.IntegerField(default=0)
    member_city=models.CharField(max_length=100,default='salem')          ##### create models file this will create single database table in db (object relational mapping ) django uses this 
                                                                          ##### then in cmd python manage.py makemigrations (for particular app name if it has more than one app)
                                                                          ##### then in cmd python manage.py migrate ----then table will made in db ,fields as column
