from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Members, File

def pageControl(request):
    value1 = request.COOKIES.get('user')
    if value1 is None:
        return False
    else:
        value2 = request.COOKIES.get('Securityint')
        data = Members.objects.filter(user=value1, Securityint=value2).values()
        if len(data) == 1:
            return True
        else:
            return False

def download(id):
    data = File.objects.get(id=id)
    response = HttpResponse(data.file.chunks())
    uzanti = data.file.name.split(".")[-1]
    response['Content-Disposition'] = 'attachment; filename=%s' % data.fileName + "." + uzanti
    return response