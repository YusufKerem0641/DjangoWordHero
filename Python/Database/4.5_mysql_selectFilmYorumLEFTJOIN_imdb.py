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
        print("MySQL veritabanına başarıyla bağlanıldı.")
    except mysql.connector.Error as error:
        print_error_message(error)

mySQL_db_connect("localhost","root","","imdb")
print ("= Film Yorumu Görüntüleme =")
imlec1=db_connect.cursor()
sorgu1 = "SELECT filmbilgi.filmID,filmbilgi.filmAdi,filmBilgi.yapimYili,yonetmen.yonetmenAdi,yapimci.yapimciAdi,yayinci.yayinciAdi FROM filmbilgi LEFT JOIN yonetmen ON filmbilgi.yonetmen=yonetmen.yonetmenID LEFT JOIN yapimci ON filmbilgi.yapimci=yapimci.yapimciID LEFT JOIN yayinci ON filmbilgi.yayinSirketi=yayinci.yayinciID"
imlec1.execute(sorgu1)
veriler1 = imlec1.fetchall()
tablo1 = PrettyTable()
tablo1.field_names = ["Film ID", "Film Adı", "Yapım Yılı", "Yönetmeni", "Yapımcısı", "Yayıncısı"]
for veri1 in veriler1:
    tablo1.add_row(veri1)
tablo1.align = "l"
print(tablo1)
imlec1.close()

imlec2=db_connect.cursor()
secimID = input("Hangi film (ID)=?")
sorgu2 = f"SELECT filmyorum.yorumID, elestirmen.elestirmenAdi, filmyorum.yildizSayisi, filmyorum.yorum FROM filmyorum LEFT JOIN elestirmen ON filmyorum.elestirmenID=elestirmen.elestirmenID WHERE filmyorum.filmID = {secimID}"
imlec2.execute(sorgu2)
veriler2 = imlec2.fetchall()
tablo2 = PrettyTable()
tablo2.field_names = ["Yorum ID", "Eleştirmen", "Yıldız Sayısı", "Yorum"]
for veri2 in veriler2:
    tablo2.add_row(veri2)
tablo2.align = "l"
print(tablo2)
imlec2.close()
db_connect.close()