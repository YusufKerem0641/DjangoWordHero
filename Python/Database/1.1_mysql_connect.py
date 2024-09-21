import mysql.connector
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
    print("MySQL bağlantı hatası: {}".format(error))