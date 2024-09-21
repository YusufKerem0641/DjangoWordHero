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
def gunBul(gunNo):
    match gunNo:
        case "1": gun="Pazartesi"
        case "2": gun="Salı"
        case "3": gun="Çarşamba"
        case "4": gun="Perşembe"
        case "5": gun="Cuma"
        case "6": gun="Cumartesi"
        case _: gun="Pazar"
    return (gun)
def saatBul(saatNo):
    match saatNo:
        case "1": saat="09:00"
        case "2": saat="10:00"
        case "3": saat="11:00"
        case "4": saat="13:00"
        case "5": saat="14:00"
        case "6": saat="15:00"
        case _: saat="16:00"
    return (saat)
mySQL_db_connect("localhost","root","","randevu")
print ("= RANDEVU SORGULAMA =")
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
hastaTCKNO = input("Hangi hastanın randevu bilgileri isteniyor (TCKNO)=?")
sorgu = "SELECT randevular.gun,randevular.saatNo,doktor.ad, doktor.soyad FROM randevular LEFT JOIN doktor ON randevular.doktor=doktor.id"
imlec.execute(sorgu)
veriler = imlec.fetchall()
tablo = PrettyTable()
tablo.field_names = ["Gün", "Saat", "Doktorun Adı", "Doktorun Soyadı"]
for veri in veriler:
    tablo.add_row([gunBul(veri[0]),saatBul(veri[1]),veri[2],veri[3]])
tablo.align = "l"
print(tablo)
imlec.close()
db_connect.close()