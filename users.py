import sqlite3 as sql

class User:
    __uyeler = []
    __isimler = []
    def __init__(self,isim = ""):
        self.isim = isim
        self.__kayit()

    def __kayit(self):
        _isim = []
        for harf in self.isim:
            _isim.append(str(ord(harf)))
        self.__uyeler.append("".join(_isim))
        self.__isimler.append(self.isim)
        self.__veritabaninaKaydet()

    def __veritabaninaKaydet(self):
        vt = sql.connect("users.sqlite")
        cs = vt.cursor()
        cs.execute("CREATE TABLE IF NOT EXISTS users (isim,username)")
        cs.execute("SELECT * from users")
        bilgiler = cs.fetchone()
        try:
            if self.isim not in bilgiler:
                veri = (self.isim,self.__uyeler[self.__isimler.index(self.isim)])
                cs.execute("INSERT INTO users values (?,?)",veri)
                vt.commit()
                vt.close()
                print("Kayıt Edildi")
            else:
                vt.close()
        except:
            veri = (self.isim, self.__uyeler[self.__isimler.index(self.isim)])
            cs.execute("INSERT INTO users values (?,?)", veri)
            vt.commit()
            vt.close()
            print("Kayıt Edildi")
            vt.close()
    @classmethod
    def uyeleriGoruntule(cls):
        return cls.__uyeler
