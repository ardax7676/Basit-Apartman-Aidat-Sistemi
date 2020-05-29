class Yonetim:
    __uyeler = []
    def __init__(self,isim = ""):
        self.isim = isim
        self.__kayit()

    def __kayit(self):
        _isim = []
        for harf in self.isim:
            _isim.append(str(ord(harf)))
        self.__uyeler.append("".join(_isim))
        print("Kayıt Yapıldı")

    @classmethod
    def uyeleriGoruntule(cls):
        return cls.__uyeler

