import random
a=int(input("Sayı tutma alt sınırı: "))
b=int(input("Sayı tutma üst sınırı: "))
sayi=random.randrange(a,b)
tahmin=int(input(str(a)+" ile "+str(b)+" arasında bir sayı tahmin edin: "))
while sayi!=tahmin:
    if tahmin<sayi:
        print ("Tuttuğum sayı daha büyük bir sayı")
    elif tahmin>sayi:
        print ("Tuttuğum sayı daha küçük bir sayı")
    tahmin=int(input("Tekrar Sayı giriniz: "))
print("Tebrikler! Sayıyı doğru tahmin ettiniz...")
