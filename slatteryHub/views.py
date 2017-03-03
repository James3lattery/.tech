from django.shortcuts import render
from .forms import newNote
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.edit import UpdateView, DeleteView
from .models import note
from .forms import uploadImage

def upload(request):
    return render(request, 'file.html')


def notes(request):
    from .models import note
    template = loader.get_template('note.html')
    me = request.user
    my_notes = note.objects.filter(owner=me)
    if request.method == 'POST':
        form = newNote(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.postDate = timezone.now()
            note.pinned = False
            note.save()
            return HttpResponseRedirect('/notes/')
        else:
            return render(request, 'fail.html')
    form = newNote(request.POST)
    context = {
        'my_notes': my_notes,
        'form': form
    }
    return HttpResponse(template.render(context, request))


class noteUpdate(UpdateView):
    model = note
    fields = ['title', 'content']
    template_name = 'note_edit.html'
    success_url = '/notes'


class noteDelete(DeleteView):
    model = note
    success_url = '/notes/'
    template_name = 'note_delete.html'


def skyward(request):
    return render(request, 'skyward.html')


def images(request):
    if request.method == 'POST':
        form = uploadImage(request.POST)
        if form.is_valid():
            image = form.save(commit=False)
            image.owner = request.user
            image.image = request.FILES['image']
            image.save()
            return HttpResponseRedirect('/images/')
        else:
            return render(request, 'fail.html')
    return render(request, 'images.html')
