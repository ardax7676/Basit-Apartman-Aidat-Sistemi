import sqlite3 as sql
class Kayit:
    __uyeler = list()
    __isimler = list()
    _isim = list()

    def __init__(self,isim = ""):
        self.isim = isim.lower()
        self.fatura = 0
    def kullaniciAdiOlustur(self):
       self._isim.clear()
       for harf in self.isim:
           self._isim.append(str(ord(harf)))
    def __kayit(self):
        self.kullaniciAdiOlustur()
        if "".join(self._isim) not in self.__uyeler:
            self.__uyeler.append("".join(self._isim))
            self.__isimler.append(self.isim)
            self.__veritabaninaKaydet()
    def __veritabaninaKaydet(self):
        vt = sql.connect("users.sqlite")
        cs = vt.cursor()
        cs.execute("CREATE TABLE IF NOT EXISTS users (isim,username,aidat)")
        cs.execute("SELECT * from users")
        bilgiler = cs.fetchone()
        try:
            if self.isim not in bilgiler:
                veri = (self.isim, self.__uyeler[self.__isimler.index(self.isim)], self.fatura)
                cs.execute("INSERT INTO users values (?,?,?)", veri)
                vt.commit()
                vt.close()
                print("Kayıt Edildi")
            else:
                vt.close()
        except:
            veri = (self.isim, self.__uyeler[self.__isimler.index(self.isim)],self.fatura)
            cs.execute("INSERT INTO users values (?,?,?)", veri)
            vt.commit()
            print("Kayıt Edildi")
            vt.close()

