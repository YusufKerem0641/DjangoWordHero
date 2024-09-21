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
# Kaydı kullanici tablosundan bul:
id = input("Hangi ID numaralı kayda kişi bilgisi girilecek?")
sorgu1 = f"SELECT * FROM kullanici WHERE ID={id}"
imlec.execute(sorgu1)
veriler = imlec.fetchall()
for veri in veriler:
    print(veri)
#Bulunan kayda kisi tablosunda veri gir:
tckno = input("T.C. Kimlik Numarası=?")
dyil = input("Doğum Yılı=?")
sorgu = f"""
INSERT INTO kisi (kisiID, tckno, dyil)
VALUES ('{id}', '{tckno}', '{dyil}')
"""
imlec.execute(sorgu)
imlec.close()
db_connect.commit()
db_connect.close()