from prettytable import PrettyTable
import mysql.connector
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
mySQL_db_connect("localhost","root","","deneme")
    
imlec=db_connect.cursor()
# Sorguyu çalıştır:
sorgu = "SELECT * FROM kullanici"
imlec.execute(sorgu)

# Verileri al:
veriler = imlec.fetchall()
# Tabloyu oluştur:
tablo = PrettyTable()
tablo.field_names = ["ID", "Ad", "Soyad", "eposta"]
# Tabloyu yazdır:
for veri in veriler:
    tablo.add_row(veri)
print(tablo)
print(tablo.get_string(fields=["ID", "eposta"]))
# Bağlantıyı kapat:
imlec.close()
db_connect.close()