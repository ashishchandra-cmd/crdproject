from django.shortcuts import render , redirect
from curdapp.forms import UserForm
from curdapp.models import User

# Create your views here.
def insert_view(request):
    ulist=User.objects.all() 
    if request.method=='POST':
        fr=UserForm(request.POST)
        if fr.is_valid():
            nm=fr.cleaned_data['name']
            em=fr.cleaned_data['email']
            ph=fr.cleaned_data['phone']
            pwd=fr.cleaned_data['password']
            reg=User(name=nm,email=em,phone=ph,password=pwd)
            reg.save()
            fr=UserForm()
    else:
        fr=UserForm()        
    return render(request,'insertshow.html',{'form':fr, 'ulist':ulist})
def delete_view(request,id):
    if request.method=='POST':
        del2=User.objects.get(pk=id)
        del2.delete()
    return redirect('/insert')

def update_view(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fr=UserForm(request.POST,instance=pi)
        if fr.is_valid():
            fr.save()
    else:
        pi=User.objects.get(pk=id)
        fr=UserForm(instance=pi)
    return render(request,'update.html',{'form':fr})



