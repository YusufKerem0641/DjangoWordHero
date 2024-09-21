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
menu = PrettyTable()
menu.field_names = ["SEÇENEKLER"]
menu.align="l"
menu.add_row(["1-Film Bilgisi Girişi"])
menu.add_row(["2-Film Yorumu Girişi"])
menu.add_row(["3-Eleştirmen Girişi"])
menu.add_row(["4-Yönetmen Girişi"])
menu.add_row(["5-Yapımcı Girişi"])
menu.add_row(["6-Yayıncı Girişi"])
print(menu)
secim = input("Seçiminiz=?")
match secim:
    case "1":
        print ("Film Bilgisi Girişi")
        filmAdi = input("Film Adı=?")
        yapimYili = input("Yapım Yılı=?")
        yonetmen = input("Yönetmen ID=?")
        yapimci = input("Yapımcı ID=?")
        yayinSirketi = input("Yayın Şirketi ID=?")
        sorgu = f"""
        INSERT INTO filmBilgi (filmAdi, yapimYili, yonetmen, yapimci, yayinSirketi)
        VALUES ('{filmAdi}', '{yapimYili}', '{yonetmen}', '{yapimci}', '{yayinSirketi}')
        """
    case "2":
        print ("Film Yorumu Girişi")
        sorgu = "SELECT filmBilgi.filmID, filmBilgi.filmAdi, yonetmen.yonetmenAdi FROM filmbilgi LEFT JOIN yonetmen ON filmBilgi.yonetmen=yonetmen.yonetmenID"
        imlec.execute(sorgu)
        veriler = imlec.fetchall()
        tablo = PrettyTable()
        tablo.field_names = ["Film ID", "Film Adı", "Yönetmeni"]
        for veri in veriler:
            tablo.add_row(veri)
        tablo.align = "l"
        print(tablo)
        imlec.close()
        filmID = input("Film ID=?")
        elestirmenID = input("Eleştirmen ID=?")
        yildizSayisi = input("Yıldız Sayısı (1-10)=?")
        yorum = input("Yorum=?")
        sorgu = f"""
        INSERT INTO filmYorum (filmID, elestirmenID, yildizSayisi, yorum)
        VALUES ('{filmID}', '{elestirmenID}', '{yildizSayisi}', '{yorum}')
        """
    case "3":
        print ("Eleştirmen Girişi")
        elestirmenAdi = input("Eleştirmen Adı=?")
        sorgu = f"""
        INSERT INTO elestirmen (elestirmenAdi)
        VALUES ('{elestirmenAdi}')
        """
    case "4":
        print ("Yönetmen Girişi")
        yonetmenAdi = input("Yönetmen Adı=?")
        sorgu = f"""
        INSERT INTO yonetmen (yonetmenAdi)
        VALUES ('{yonetmenAdi}')
        """
    case "5":
        print ("Yapımcı Girişi")
        yapimciAdi = input("Yapımcı Adı=?")
        sorgu = f"""
        INSERT INTO yapimci (yapimciAdi)
        VALUES ('{yapimciAdi}')
        """
    case _:
        print ("Yayın Şirketi Girişi")
        yayinciAdi = input("Yayın Şirketi Adı=?")
        sorgu = f"""
        INSERT INTO yayinci (yayinciAdi)
        VALUES ('{yayinciAdi}')
        """
imlec.execute(sorgu)
imlec.close()
db_connect.commit()
db_connect.close()