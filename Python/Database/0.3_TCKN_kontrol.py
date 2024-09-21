import random 
def TCkno_kontrol(tckn):
    #Sayı ve 11 hane olması:
    if not tckn.isdigit() or len(tckn) != 11: return False
    #Hanelerinden sayı listesi oluşturulması:
    haneler = [int(hane) for hane in tckn]
    #0 ile başlamıyor olsun:
    if haneler[0] == 0: return False
    #Birinci kural kontrolü:
    if sum(haneler[0:10]) % 10 != haneler[10]: return False 
    #İkinci kural kontrolü:
    if (7*sum(haneler[0:9:2]) - sum(haneler[1:9:2])) % 10 != haneler[9]: return False 
    #Bütün olumsuzluklar geçildi ise:
    return True 

TC_kno = input("Lütfen T.C. Kimlik Numarasını Giriniz: ") 
if TCkno_kontrol(TC_kno): print("Girilen T.C. Kimlik Numarası geçerlidir.")
else: print("Girilen T.C. Kimlik Numarası geçersizdir.")