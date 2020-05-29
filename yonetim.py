import users
class Yonetim:
    admin = list()
    admin_name = list()
    def __init__(self,isim=""):
        self.isim = isim.lower()
    def YoneticiEkle(self):
        self.admin_name.clear()
        for harf in self.isim:
            self.admin_name.append(str(ord(harf)))
        self.admin = "".join(list(reversed(self.admin_name)))
        print("Yönetici Başarıyla Eklendi")
a = Yonetim("kamil")
a.YoneticiEkle()