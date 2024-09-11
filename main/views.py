from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import notes
from .forms import NoteForm
from django.contrib.auth import get_user_model



@login_required(login_url='/accounts/login')
def home(request,*args,**kwargs):
    User = request.user
    user_notes = notes.objects.filter(user=User)
    context = {
        "notes":user_notes
    }
    return render(request,'home.html',context=context)




@login_required(login_url='/accounts/login')
def create_note(request, *args, **kwargs):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)  # Do not save yet, we need to add the user first
            note.user = request.user        # Set the user field
            note.save()                     # Now save the note with the user field set
            return redirect('/')
        else:
            context = {
                'form': form
            }
            return render(request, 'note.html', context=context)
    else:
        form = NoteForm()
        context = {
            "form": form
        }
        return render(request, 'note.html', context=context)
