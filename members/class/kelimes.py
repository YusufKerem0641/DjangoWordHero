import sys,os
sys.path.append(os.getcwd())
import kelim

with open("kelimler5","r") as dosya:
    kelimeler=dosya.read()
kelimeler = kelimeler.split(",")

kelimeBulma = kelim.KelimeBulma()
kelimeBulma.kelimeListesiAl(kelimeler)
kelimeBulma.harfAl("a",1)
kelimeBulma.bulunanKelimlerManager()
kelimeBulma.printer()