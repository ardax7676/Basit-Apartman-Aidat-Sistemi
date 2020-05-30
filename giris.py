import kayit
import sqlite3 as sql
import time
from sys import exit as cikis
vt = sql.connect("admin.sqlite")
cs = vt.cursor()
cs.execute("SELECT * FROM admin")
admin_bilgisi = cs.fetchone()
if admin_bilgisi == None:
    pass
else:
    while True:
        parola = input("Lütfen parolanızı giriniz: ")
        if parola in admin_bilgisi:
            class AdminPanel:
                def __init__(self):
                    pass
                def aidatEkle(self,ay="",miktar=0,kat=1,daire=1):

                    if kat == "1" and daire == "1":
                        kayit.kat1daire1.aidat[ay] = miktar
                        print("Aidat Başarılı Bir Şekilde Eklendi")
                    elif kat == "1" and daire == "2":
                        kayit.kat1daire2.aidat[ay] = miktar
                        print("Aidat Başarılı Bir Şekilde Eklendi")
                    elif kat == "1" and daire == "3":
                        kayit.kat1daire3.aidat[ay] = miktar
                        print("Aidat Başarılı Bir Şekilde Eklendi")
                    elif kat == "2" and daire == "4":
                        kayit.kat2daire4.aidat[ay] = miktar
                        print("Aidat Başarılı Bir Şekilde Eklendi")
                    elif kat == "2" and daire == "5":
                        kayit.kat2daire5.aidat[ay] = miktar
                        print("Aidat Başarılı Bir Şekilde Eklendi")
                    elif kat == "2" and daire == "6":
                        kayit.kat2daire6.aidat[ay] = miktar
                        print("Aidat Başarılı Bir Şekilde Eklendi")
                    elif kat == "3" and daire == "7":
                        kayit.kat3daire7.aidat[ay] = miktar
                        print("Aidat Başarılı Bir Şekilde Eklendi")
                    elif kat == "3" and daire == "8":
                        kayit.kat3daire8.aidat[ay] = miktar
                        print("Aidat Başarılı Bir Şekilde Eklendi")
                    elif kat == "3" and daire == "9":
                        kayit.kat3daire9.aidat[ay] = miktar
                        print("Aidat Başarılı Bir Şekilde Eklendi")
                    elif kat == "4" and daire == "10":
                        kayit.kat4daire10.aidat[ay] = miktar
                        print("Aidat Başarılı Bir Şekilde Eklendi")
                    elif kat == "4" and daire == "11":
                        kayit.kat4daire11.aidat[ay] = miktar
                        print("Aidat Başarılı Bir Şekilde Eklendi")
                    elif kat == "4" and daire == "12":
                        kayit.kat4daire12.aidat[ay] = miktar
                        print("Aidat Başarılı Bir Şekilde Eklendi")
                    elif kat == "5" and daire == "13":
                        kayit.kat5daire13.aidat[ay] = miktar
                        print("Aidat Başarılı Bir Şekilde Eklendi")
                    elif kat == "5" and daire == "14":
                        kayit.kat5daire14.aidat[ay] = miktar
                        print("Aidat Başarılı Bir Şekilde Eklendi")
                    elif kat == "5" and daire == "15":
                        kayit.kat5daire15.aidat[ay] = miktar
                        print("Aidat Başarılı Bir Şekilde Eklendi")
                    elif kat == "6" and daire == "16":
                        kayit.kat6daire16.aidat[ay] = miktar
                        print("Aidat Başarılı Bir Şekilde Eklendi")
                    else:
                        print("Yanlış Bilgiler Girildi")
                    print()

            admin = AdminPanel()
            while True:
                emir = input("Yönetici Hesabıyla Giriş Yaptınız\nLütfen Yapmak İstediğiniz İşlemi Giriniz\nAidat eklemek için 1 yazınız\n>> ")
                if emir == "1":
                    kat = input("kat:")
                    daire = input("daire:")
                    ay = input("ay:")
                    miktar = input("miktar:")
                    admin.aidatEkle(ay,miktar,kat,daire)
                else:
                    break

        elif parola in kayit.Uye.parolalar:
            class UyePanel:
                def __init__(self):
                    pass
                def aidatGoruntule(self,ay):
                    if parola == "10710110997108000000":
                        print("Hoşgeldin",kayit.kat1daire1.isim.capitalize(),kayit.kat1daire1.soyisim)
                        print(kayit.kat1daire1.aidat.get(ay,"Bir Hata Oluştu"))
                    elif parola == "10910110410910111600":
                        print("Hoşgeldin", kayit.kat1daire2.isim.capitalize(), kayit.kat1daire2.soyisim)
                        print(kayit.kat1daire2.aidat.get(ay,"Bir Hata Oluştu"))
                    elif parola == "10911711511697102970":
                        print("Hoşgeldin", kayit.kat1daire3.isim.capitalize(), kayit.kat1daire3.soyisim)
                        print(kayit.kat1daire3.aidat.get(ay,"Bir Hata Oluştu"))
                    elif parola == "97981001171081089710":
                        print("Hoşgeldin", kayit.kat2daire4.isim.capitalize(), kayit.kat2daire4.soyisim)
                        print(kayit.kat2daire4.aidat.get(ay,"Bir Hata Oluştu"))
                    elif parola == "10497107971100000000":
                        print("Hoşgeldin", kayit.kat2daire5.isim.capitalize(), kayit.kat2daire5.soyisim)
                        print(kayit.kat2daire5.aidat.get(ay,"Bir Hata Oluştu"))
                    elif parola == "10311110711611710300":
                        print("Hoşgeldin", kayit.kat2daire6.isim.capitalize(), kayit.kat2daire6.soyisim)
                        print(kayit.kat2daire6.aidat.get(ay,"Bir Hata Oluştu"))
                    elif parola == "11410199101112000000":
                        print("Hoşgeldin", kayit.kat3daire7.isim.capitalize(), kayit.kat3daire7.soyisim)
                        print(kayit.kat3daire7.aidat.get(ay,"Bir Hata Oluştu"))
                    elif parola == "":
                        print("Hoşgeldin", kayit.kat3daire8.isim.capitalize(), kayit.kat3daire8.soyisim)
                        print(kayit.kat3daire8.aidat.get(ay,"Bir Hata Oluştu"))
                    elif parola == "97114100970000000000":
                        print("Hoşgeldin", kayit.kat3daire9.isim.capitalize(), kayit.kat3daire9.soyisim)
                        print(kayit.kat3daire9.aidat.get(ay,"Bir Hata Oluştu"))
                    elif parola == "97108105000000000000":
                        print("Hoşgeldin", kayit.kat4daire10.isim.capitalize(), kayit.kat4daire10.soyisim)
                        print(kayit.kat4daire10.aidat.get(ay,"Bir Hata Oluştu"))
                    elif parola == "11112210810110900000":
                        print("Hoşgeldin", kayit.kat4daire11.isim.capitalize(), kayit.kat4daire11.soyisim)
                        print(kayit.kat4daire11.aidat.get(ay,"Bir Hata Oluştu"))
                    elif parola == "99101108971080000000":
                        print("Hoşgeldin", kayit.kat4daire12.isim.capitalize(), kayit.kat4daire12.soyisim)
                        print(kayit.kat4daire12.aidat.get(ay,"Bir Hata Oluştu"))
                    elif parola == "98101114107000000000":
                        print("Hoşgeldin", kayit.kat5daire13.isim.capitalize(), kayit.kat5daire13.soyisim)
                        print(kayit.kat5daire13.aidat.get(ay,"Bir Hata Oluştu"))
                    elif parola == "98117287114970000000":
                        print("Hoşgeldin", kayit.kat5daire14.isim.capitalize(), kayit.kat5daire14.soyisim)
                        print(kayit.kat5daire14.aidat.get(ay,"Bir Hata Oluştu"))
                    elif parola == "10911710497109109101":
                        print("Hoşgeldin", kayit.kat5daire15.isim.capitalize(), kayit.kat5daire15.soyisim)
                        print(kayit.kat5daire15.aidat.get(ay,"Bir Hata Oluştu"))
                    elif parola == "11510111410097114000":
                        print("Hoşgeldin", kayit.kat6daire16.isim.capitalize(), kayit.kat6daire16.soyisim)
                        print(ay+":",kayit.kat6daire16.aidat.get(ay,"Bir Hata Oluştu"))
                    else:
                        print("Yanlış Bilgiler Girildi")
                    print()
            uye = UyePanel()
            while True:
                emir = input("Üye Hesabıyla Giriş Yaptınız\nLütfen Yapmak İstediğiniz İşlemi Giriniz\nAidatlarınızı Görüntülemek İçin 1 Yazınız\n>> ")
                if emir == "1":
                    ay = input("Aidat miktarını öğrenmek istediğiniz ayı giriniz: ")
                    uye.aidatGoruntule(ay=ay)
                else:
                    break
        elif parola == "q":
            print("Hoşçakal...")
            time.sleep(1)
            cikis()
        else:
            print("Girdiğiniz parola hatalı!")
            cikis()