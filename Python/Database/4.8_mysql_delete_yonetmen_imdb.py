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
imlec=db_connect.cursor()
#Önce yönetmenleri gösterelim:
sorgu = "SELECT * FROM yonetmen"
imlec.execute(sorgu)
veriler = imlec.fetchall()
tablo = PrettyTable()
tablo.field_names = ["Yönetmen ID", "Yönetmen"]
for veri in veriler:
    tablo.add_row(veri)
tablo.align = "l"
print(tablo)

yonetmenID = input("Yönetmen ID=?")
cevap = input("Bu yönetmen veritabanından silinecektir. Emin misiniz?(E/H)")
if cevap.upper() == "E":
    sorgu = f"DELETE FROM yonetmen WHERE yonetmenID={yonetmenID}"
    imlec.execute(sorgu)
    imlec.close()
    db_connect.commit()
    print("Silme işlemi gerçekleştirilmiştir...")
    db_connect.close()