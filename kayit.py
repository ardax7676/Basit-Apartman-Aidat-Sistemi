import sqlite3 as sql
from time import sleep
class Uye:
    parolalar = list()
    __isimler = list()
    _isim = list()
    def __init__(self,isim = ""):
        self.isim = isim.lower()
        self.fatura = 0
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
                kod += 0
            self.parolalar.append(kod[:20])
            self.__isimler.append(self.isim)
            self.__veritabaninaKaydet()
    def __veritabaninaKaydet(self):
        vt = sql.connect("users.sqlite")
        cs = vt.cursor()
        cs.execute("CREATE TABLE IF NOT EXISTS users (isim,parola,aidat)")
        cs.execute("SELECT * from users")
        bilgiler = cs.fetchone()
        try:
            if self.isim not in bilgiler:
                veri = (self.isim, self.parolalar[self.__isimler.index(self.isim)], self.fatura)
                cs.execute("INSERT INTO users values (?,?,?)", veri)
                vt.commit()
                vt.close()
                print("Üye Başarıyla Eklendi")
                print("Üye Parolanız:",self.parolalar[self.__isimler.index(self.isim)])
                print("-"*100)
            else:
                vt.close()
        except:
            veri = (self.isim, self.parolalar[self.__isimler.index(self.isim)],self.fatura)
            cs.execute("INSERT INTO users values (?,?,?)", veri)
            vt.commit()
            print("Üye Başarıyla Eklendi")
            print("Üye Parolanız:",self.parolalar[self.__isimler.index(self.isim)])
            print("-"*100)
            vt.close()

class Yonetici:
    admin = list()
    admin_name = list()
    def __init__(self,isim=""):
        self.isim = isim.lower()
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
        print("Yönetici Başarıyla Eklendi")
        print("Yönetici Parolanız:", self.admin[:20])
        print("-" * 100)

if __name__ == "__main__":
    while True:
        islem = input("Yapmak istediğiniz işlemi giriniz\nYönetici eklemek için 1\nÜye eklemek için 2\nÇıkmak için q yazınız\n>> ")
        if islem == "1":
            isim = input("Yöneticinin ismi: ")
            sleep(0.5)
            Yonetici(isim)
            print()
        elif islem == "2":
            isim = input("Üyenin ismi: ")
            sleep(0.5)
            Uye(isim)
            print()
        elif islem == "q":
            print("Hoşçakal...")
            sleep(1.5)
            break
        else:
            print("Yanlış Giriş Yapıldı")
            break