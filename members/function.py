class KelimeBulma():
    kelimelerListe = []
    bilinenHarfSozluk = {}
    yeriBelliOlmayan = {}
    tahminiKelimeler = []
    yeriOlmayan = {}
    olmayanHarfler = []

    def __init__(self):
        self.kelimelerListe = []
        self.bilinenHarfSozluk = {}
        self.yeriBelliOlmayan = []
        self.tahminiKelimeler = []
        self.yeriOlmayan = {}
        self.olmayanHarfler = []

    def kelimeListesiAl(self,kelimelerListe):# hangi kelimlerden seçilecekse o listeyi alır
        self.kelimelerListe = kelimelerListe

    def harfAl(self,bilinenHarf,bilinenHarfYeri,yeriOlmayanYeri = 0):#harfleri ve yerlerini almak için kullanılır
        self.bilinenHarfSozluk[bilinenHarfYeri] = bilinenHarf
        if bilinenHarfYeri == -1:
            self.yeriBelliOlmayan.append([bilinenHarf, yeriOlmayanYeri])

    def bulunanKelimlerManager(self):# olan harfli kelimeleri bulmak için kullanılır
        print(self.yeriBelliOlmayan)
        for kelime in self.kelimelerListe:
            hata = False
            for x in self.bilinenHarfSozluk:
                if x == -1:
                    for yeriBelliOlmayanHarf in self.yeriBelliOlmayan:
                        harfYeri = kelime.find(yeriBelliOlmayanHarf[0])
                        if harfYeri == -1 or kelime[yeriBelliOlmayanHarf[1]] == yeriBelliOlmayanHarf[0]:
                            hata = True
                            break
                else:
                    if not kelime[x] == self.bilinenHarfSozluk[x]:
                        hata = True
                        break
            if not hata:
                self.tahminiKelimeler.append(kelime)

    def olmayanHarflerSet(self,olmayanHarfler):
        self.olmayanHarfler = olmayanHarfler

    def olmayanHarflerManager(self):#olmayan harfleri listeden çıkarmak için kullanılır
        for olmayanHarf in self.olmayanHarfler:
            if olmayanHarf == "":
                break
            index = 0
            while index < len(self.tahminiKelimeler):
                if self.tahminiKelimeler[index].find(olmayanHarf) != -1:
                    self.tahminiKelimeler.remove(self.tahminiKelimeler[index])
                    index -= 1
                index += 1

    def tahminiKelimelerGet(self):#çıkan sonuçtaki kelimleri liste halinde verir
        return self.tahminiKelimeler

    def printer(self):# çıkan sonuçtaki kelimleri konsola yazdırır
        for tahminiKelime in self.tahminiKelimeler:
            print(tahminiKelime)
