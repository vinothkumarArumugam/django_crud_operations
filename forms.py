from django import forms
from crudapp2.models import Library
class LibraryForm(forms.ModelForm):    #### create fields according to fields in model(database)
    class Meta :
        model=Library
        fields='__all__'     ####   meta means data about data ,first letter must be uppercase ,to get all details in db table
