from django.shortcuts import render
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage

# Uploads file to /media directory
def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'file.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'file.html')


def notes(request):
    return render(request, 'note.html')
