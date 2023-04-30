from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect ,render

import os
from .function import *

def index(request):
    if request.method == 'POST':

        template = loader.get_template('index.html')
        harfSayisi = request.POST['harf-sayi']
        olmayanHarfSayisi = request.POST['olmayan-harf-sayi']
        if not (harfSayisi == "" or olmayanHarfSayisi == ""):
            print(os.getcwd())
            with open(os.getcwd()+r"\members\class\kelimler"+str(harfSayisi), "r") as dosya:
                kelimeler = dosya.read()
            kelimeler = kelimeler.split(",")
            kelimeBulma = KelimeBulma()
            kelimeBulma.kelimeListesiAl(kelimeler)

            kelimeBulma.olmayanHarflerSet(olmayanHarfSayisi.split(","))
            print(olmayanHarfSayisi.split(","))

            sayiTekrar = 0
            while True:
                sayiTekrar += 1
                try:
                    harf = request.POST['harf'+str(sayiTekrar)]
                    yeri = int(request.POST['yeri' + str(sayiTekrar)]) - 1
                    yeriDegil = request.POST['yeri-degil' + str(sayiTekrar)]
                except:
                    break
                print("harf",yeri,harf)
                if harf == "" or yeri == "":
                    break
                if yeriDegil == "":
                    kelimeBulma.harfAl(harf, yeri)
                else:
                    kelimeBulma.harfAl(harf, yeri,int(yeriDegil) - 1)
            kelimeBulma.bulunanKelimlerManager() # bu kelimelerden kurralları uygular
            kelimeBulma.olmayanHarflerManager() #bu listeden olmayan harfleri çıkarır
            data = kelimeBulma.tahminiKelimelerGet()
            print(data)
        else:
            data = ["Hata oluştu"]
        context = {
            'data': data,
        }
        response = HttpResponse(template.render(context, request))
        return HttpResponse(response)
    else:
        template = loader.get_template('index.html')
        response = HttpResponse(template.render({}, request))
        return response

def kelimtwo():
    pass

def kelim(request):
    if request.method == 'POST':

        template = loader.get_template('index.html')
        harfSayisi = request.POST['harf-sayi']
        olmayanHarfSayisi = request.POST['olmayan-harf-sayi']
        if not (harfSayisi == "" or olmayanHarfSayisi == ""):
            with open(os.getcwd()+r"\members\class\kelimler"+str(harfSayisi), "r") as dosya:
                kelimeler = dosya.read()
            kelimeler = kelimeler.split(",")
            kelimeBulma = KelimeBulma()
            kelimeBulma.kelimeListesiAl(kelimeler)

            kelimeBulma.olmayanHarflerSet(olmayanHarfSayisi.split(","))
            print(olmayanHarfSayisi.split(","))

            sayiTekrar = 0
            while True:
                sayiTekrar += 1
                try:
                    harf = request.POST['harf'+str(sayiTekrar)]
                    yeri = int(request.POST['yeri' + str(sayiTekrar)]) - 1
                    yeriDegil = request.POST['yeri-degil' + str(sayiTekrar)]
                except:
                    break
                print("harf",len(harf),harf)
                if harf == "" or yeri == "":
                    break
                if yeriDegil == "":
                    kelimeBulma.harfAl(harf, yeri)
                else:
                    kelimeBulma.harfAl(harf, yeri,int(yeriDegil) - 1)
            kelimeBulma.bulunanKelimlerManager() # bu kelimelerden kurralları uygular
            kelimeBulma.olmayanHarflerManager() #bu listeden olmayan harfleri çıkarır
            data = kelimeBulma.tahminiKelimelerGet()
            print(data)
        else:
            data = ["Hata oluştu"]
        context = {
            'data': data,
        }
        response = HttpResponse(template.render(context, request))
        return response
    else:
        template = loader.get_template('index.html')
        response = HttpResponse(template.render({}, request))
        return response
# Create your views here.
