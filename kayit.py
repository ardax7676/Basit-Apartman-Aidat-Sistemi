import sqlite3 as sql
from time import sleep
class Uye:
    parolalar = list()
    __isimler = list()
    _isim = list()
    def __init__(self,isim = "",soyisim = ""):
        self.isim = isim.lower()
        self.soyisim = soyisim
        self.aidat = dict()
        self.__kayit()
    def kullaniciAdiOlustur(self):
       self._isim.clear()
       for harf in self.isim:
           self._isim.append(str(ord(harf)))
    def __kayit(self):
        self.kullaniciAdiOlustur()
        kod = "".join(self._isim)
        if kod not in self.parolalar:
            while len(kod) < 20:
                kod += "0"
            self.parolalar.append(kod[:20])
            self.__isimler.append(self.isim)
            self.__veritabaninaKaydet()
    def __veritabaninaKaydet(self):
        vt = sql.connect("users.sqlite")
        cs = vt.cursor()
        cs.execute("CREATE TABLE IF NOT EXISTS users (isim,parola)")
        cs.execute("SELECT * from users")
        bilgiler = cs.fetchone()
        try:
            if self.isim not in bilgiler:
                veri = (self.isim, self.parolalar[self.__isimler.index(self.isim)])
                cs.execute("INSERT INTO users values (?,?)", veri)
                vt.commit()
                vt.close()
            else:
                vt.close()
        except:
            veri = (self.isim, self.parolalar[self.__isimler.index(self.isim)])
            cs.execute("INSERT INTO users values (?,?)", veri)
            vt.commit()
            vt.close()

class Yonetici:
    admin = list()
    admin_name = list()
    def __init__(self,isim="",soyisim=""):
        self.isim = isim.lower()
        self.soyisim = soyisim
        self.YoneticiEkle()
    def YoneticiEkle(self):
        self.admin_name.clear()
        for harf in self.isim:
            self.admin_name.append(str(ord(harf)))
        self.admin = "".join(list(reversed(self.admin_name)))
        while len(self.admin) < 20:
            self.admin += "0"
        vt = sql.connect("admin.sqlite")
        cs = vt.cursor()
        cs.execute("CREATE TABLE IF NOT EXISTS admin (isim,parola)")
        cs.execute("INSERT INTO admin VALUES (?,?)",(self.isim,self.admin[:20]))
        vt.commit()
        vt.close()

# Apartman Kaydı Oluşturuluyor #
kat1daire1 = Uye("Kemal")
kat1daire2 = Uye("Mehmet")
kat1daire3 = Uye("Mustafa")
kat2daire4 = Uye("Abdullah")
kat2daire5 = Uye("Hakan")
kat2daire6 = Uye("Goktug")
kat3daire7 = Uye("Recep")
kat3daire8 = Yonetici(isim="Kamil",soyisim="Çiçek")
kat3daire9 = Uye("Arda")
kat4daire10 = Uye("Ali")
kat4daire11 = Uye("Ozlem")
kat4daire12 = Uye("Celal")
kat5daire13 = Uye("Berk")
kat5daire14 = Uye("Buğra")
kat5daire15 = Uye("Muhammed")
kat6daire16 = Uye("Serdar")