import mysql.connector
from prettytable import PrettyTable
def print_error_message(hatakodu):
    if hatakodu.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Hata: Kullanıcı adı veya şifre hatalı.")
    elif hatakodu.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
        print("Hata: Belirtilen veritabanı bulunamadı.")
    elif hatakodu.errno == mysql.connector.errorcode.ER_HOST_NOT_PRIVILEGED:
        print("Hata: MySQL sunucusuna bağlanma izniniz yok.")
    elif hatakodu.errno == mysql.connector.errorcode.CR_CONN_HOST_ERROR:
        print("Hata: Sunucuya bağlanılamadı.")
    else:
        print("Bilinmeyen bir hata oluştu:", hatakodu)
def mySQL_db_connect(host1,user1,password1,database1):
    global db_connect 
    try:
        db_connect = mysql.connector.connect(
            host=host1,
            user=user1,
            password=password1,
            database=database1)
        print("MySQL veritabanına başarıyla bağlanıldı...")
    except mysql.connector.Error as error:
        print_error_message(error)
mySQL_db_connect("localhost","root","","randevu")
print ("= RANDEVU VERME =")
imlec=db_connect.cursor()
#Hastalar listeleniyor:
sorgu = "SELECT tc_kimlik, ad, soyad FROM hasta"
imlec.execute(sorgu)
veriler1 = imlec.fetchall()
tablo1 = PrettyTable()
tablo1.field_names = ["TC Kimlik No", "Adı", "Soyadı"]
for veri1 in veriler1:
    tablo1.add_row(veri1)
tablo1.align = "l"
print(tablo1)
sorgu = "SELECT doktor.id,doktor.ad,doktor.soyad,bolum.ad FROM doktor LEFT JOIN bolum ON doktor.bolum_id=bolum.id"
imlec.execute(sorgu)
veriler1 = imlec.fetchall()
tablo1 = PrettyTable()
tablo1.field_names = ["Doktor ID", "Adı", "Soyadı", "Bölümü"]
for veri1 in veriler1:
    tablo1.add_row(veri1)
tablo1.align = "l"
print(tablo1)
print("Günler: (Pazartesi-1, Salı-2, Çarşamba-3, Perşembe-4, Cuma-5, Cumartesi-6, Pazar-7)")
tablo2 = PrettyTable()
tablo2.field_names = ["Randevu No", "Saat"]
tablo2.add_row(["1","09:00"])
tablo2.add_row(["2","10:00"])
tablo2.add_row(["3","11:00"])
tablo2.add_row(["4","13:00"])
tablo2.add_row(["5","14:00"])
tablo2.add_row(["6","15:00"])
tablo2.add_row(["7","16:00"])
tablo2.align = "l"
print(tablo2)
hastaTCKNO = input("Hangi hasta için randevu alınacak (TCKNO)=?")
doktorID = input("Hangi doktordan randevu alınacak (ID)=?")
gunNo = input("Hangi gün=?")
saatNo = input("Hangi saat=?")
#Bu doktor için uygun zaman tablosunda kayıt var mı?
sorgu = f"SELECT * FROM doktor_uygun_gunler WHERE doktorID={doktorID} AND gunNo={gunNo} AND saatNo={saatNo} AND uygun=0"
imlec.execute(sorgu)
kontrolVerisi = imlec.fetchall()
if kontrolVerisi:
    print ("Randevu için uygundur.")
    #Bu doktor için uygunluk durumuna 1 ver ki bir daha randevu verilemesin:
    guncelleSorgu = f"UPDATE doktor_uygun_gunler SET uygun=1 WHERE doktorID={doktorID} AND gunNo={gunNo} AND saatNo={saatNo}"
    imlec.execute(guncelleSorgu)
    randevuSorgu = f"""
        INSERT INTO randevular (hasta, doktor, gun, saatNo)
        VALUES ('{hastaTCKNO}', {doktorID}, {gunNo}, {saatNo})
        """
    imlec.execute(randevuSorgu)
    print ("Randevu verilmiştir...")
else:
    print ("Seçilen bilgiler randevu için uygun değildir...")
imlec.close()
db_connect.commit()
db_connect.close()