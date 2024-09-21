import random
def TCkno_olustur():
    #İlk 9 haneyi rastgele oluştur:
    haneler = [random.randint(0, 9) for _ in range(9)]
    #İlk haneyi sıfırdan farklı yap:
    haneler[0] = random.randint(1, 9)
    hane10 = (7*sum(haneler[0:9:2]) - sum(haneler[1:9:2])) % 10
    haneler.append(hane10)  
    hane11 = sum(haneler[:10]) % 10    
    tck_no = ''.join(map(str, haneler)) + str(hane11)
    return tck_no

print("Oluşturulan T.C. Kimlik Numarası:",TCkno_olustur())