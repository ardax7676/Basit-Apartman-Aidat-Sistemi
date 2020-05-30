import sqlite3 as sql
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

if __name__ != "__main__":
    kat1daire1 = Uye("Kemal","Cansever")
    kat1daire2 = Uye("Mehmet","Gül")
    kat1daire3 = Uye("Mustafa","Karataş")
    kat2daire4 = Uye("Abdullah","Dal")
    kat2daire5 = Uye("Hakan","Fidan")
    kat2daire6 = Uye("Goktug","Kızıl")
    kat3daire7 = Uye("Recep","İvedik")
    kat3daire8 = Yonetici("Kamil","Çiçek")
    kat3daire9 = Uye("Arda","Çiçek")
    kat4daire10 = Uye("Ali","Cihat")
    kat4daire11 = Uye("Ozlem","Budanur")
    kat4daire12 = Uye("Celal","Kurt")
    kat5daire13 = Uye("Berk","Sarıtaş")
    kat5daire14 = Uye("Buğra","Aksoy")
    kat5daire15 = Uye("Muhammed","Katılmış")
    kat6daire16 = Uye("Serdar","Yurtseven")