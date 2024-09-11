from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import notes

from django.contrib.auth import get_user_model



@login_required(login_url='/accounts/login')
def home(request,*args,**kwargs):
    User = request.user
    user_notes = notes.objects.filter(user=User)
    context = {
        "notes":user_notes
    }
    return render(request,'home.html',context=context)

