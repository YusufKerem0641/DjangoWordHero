import random
a=int(input("Sayı tutma alt sınırı: "))
b=int(input("Sayı tutma üst sınırı: "))
print (str(a)+" ile "+str(b)+" arasında bir sayı tutun ve bana söylemeyin :)") 
tahmin=random.randrange(a,b)
print(tahmin)
sonuc=input("Doğru mu? (E)vet / (K)üçük / (B)üyük").upper()
while sonuc!="E":
    if sonuc=="K":
        b=tahmin
    elif sonuc=="B":
        a=tahmin
    tahmin=random.randrange(a,b)
    print(tahmin)
    sonuc=input("Doğru mu? (E)vet / (K)üçük / (B)üyük").upper()
print("Buldum! :))")
