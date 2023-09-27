from django.shortcuts import render,redirect
from crudapp2.models import Library             ### importing library model or class
from crudapp2.forms import LibraryForm          ### importing libraryform model ,,,,to get details from user and also for updating

def get_view(request):                          ### this function is for retrieving
    data=Library.objects.all()                  ### it will get all the datas in library model
    context={'data':data}                       ### for giving retrived data to index.html file 
    return render(request,'crudapp2/index.html',context)                                                                                       ########SIMULTANEOUSLY CHECK URL,HTML FILES
# Create your views here.
def create_view(request):                       ### this function is for creating the data or getting the data(information) from users
    form=LibraryForm()                            ### saving library form in one object ,like fields will display
    if request.method == 'POST' :               ### these post is html form post,checking the condition
        form=LibraryForm(request.POST)           ### details in this under post will be saved
        if form.is_valid():                        ### checking data in form ,this is django form function
            form.save()                            ### it will saved
            return redirect('/check')             ###redirecting to main page where data are displayed
    return render(request,'crudapp2/forms.html',{'form':form})    
def delete_view(request,id):                   ###   this is for deleting data ,id is must
    member=Library.objects.get(id=id)           #### library model's id by using dict get method
    member.delete()                             ### deleting alll data in given id
    return redirect('/check')                   ### redircting to main page
def update_view(request,id):                      ### UPDATING DATA IN FIELDS,ID IS MUST
    member=Library.objects.get(id=id)
    if request.method == 'POST' :
        form=LibraryForm(request.POST,instance=member)   ### SAME AS FORM BUT INSTANCE IS MUST ,IT WILL HOLD THE PARTICULAR ID
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request,'crudapp2/update.html',{'member':member})     
