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
try:
    db_connect = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="deneme")
    print("MySQL veritabanına başarıyla bağlanıldı.")
    db_connect.close()
    print("MySQL veritabanı bağlantısı kapatıldı.")
except mysql.connector.Error as error:
    print_error_message(error)
except Exception:
    print("Bilinmeyen Hata")