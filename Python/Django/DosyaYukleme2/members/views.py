from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members
from .models import File
from django.shortcuts import redirect ,render
from .forms import UploadFileForm
from .function import *
from datetime import date

def index(request):
    template = loader.get_template('index.html')
    a=pageControl(request)
    context = {'contr':True,}
    return HttpResponse(template.render(context, request))

def hakkimizda(request):
    template = loader.get_template('hakkimizda.html')
    return HttpResponse(template.render({}, request))

def login(request):
    if request.method == 'POST':
        template = loader.get_template('login.html')
        x = request.POST['Name']
        y = request.POST['Password']
        data = Members.objects.filter(user=x, password=y).values()
        if len(data) == 1:
            context = {
                'data': data[0],
            }
            print(data)
            response = redirect('/members/')
            response.set_cookie('user', x)
            response.set_cookie('Securityint', data[0]["Securityint"])
        else:
            context = {
                'girdimi': 'Hatalı Giriş \n',
            }
            response = HttpResponse(template.render(context, request))
        return response
    else:
        template = loader.get_template('login.html')
        response = HttpResponse(template.render({}, request))
        return response

def upload(request):
    if not pageControl(request):
        return redirect('/members/login/')
    if request.method == 'POST':
        student = UploadFileForm(request.POST, request.FILES)
        if student.is_valid():
            uzanti = request.FILES['file'].name.split(".")[-1]
            switcher = {
                "txt": 1,
                "pptx": 2,
                "docx": 3,
                "xxls": 4,
            }
            try:
                uzantilar = switcher[uzanti]
            except:
                uzantilar = 5
            user = request.COOKIES.get('user')
            d = date.today()
            instance = File(user=user,category=1,fileType=uzantilar,file=request.FILES['file'],fileName=request.POST['title'],date=d,info="dosya")
            instance.save()
            return redirect('/members/')
    else:
        student = UploadFileForm()
        return render(request, "upload.html", {'form': student})


def search(request,searchData):
    if request.method == 'POST':
        data = File.objects.get(id=request.POST['download'])
        response = HttpResponse(data.file.chunks())
        uzanti = data.file.name.split(".")[-1]
        response['Content-Disposition'] = 'attachment; filename=%s' % data.fileName + "." + uzanti
        return response

    else:
        template = loader.get_template('dosya.html')
        data = File.objects.filter(fileName__icontains=searchData).values()
        return HttpResponse(template.render({'data':data},request))

def searchCategory(request,searchData):
    if request.method == 'POST':
        data = File.objects.get(id=request.POST['download'])
        response = HttpResponse(data.file.chunks())
        uzanti = data.file.name.split(".")[-1]
        response['Content-Disposition'] = 'attachment; filename=%s' % data.fileName + "." + uzanti
        return response

    else:
        switcher = {
            "dersler": 1,
            "odev": 2,
            "sunum": 3,
            "proje": 4,
            "not": 5,
            "diger": 6
        }
        template = loader.get_template('dosya.html')
        data = File.objects.filter(category=switcher[searchData]).values()
        return HttpResponse(template.render({'data':data},request))

def exits(request):
    response=redirect('/members/')
    response.delete_cookie('user')
    response.delete_cookie('Securityint')
    return response
# Create your views here.
