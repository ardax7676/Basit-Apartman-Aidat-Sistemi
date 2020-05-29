import kayit
import sqlite3 as sql
from sys import exit as cikis
parola = input("Lütfen parolanızı giriniz: ")
vt = sql.connect("admin.sqlite")
cs = vt.cursor()
cs.execute("SELECT * FROM admin WHERE parola =(?)",(parola,))
admin_bilgisi = cs.fetchone()
if admin_bilgisi == None:
    vt = sql.connect("admin.sqlite")
    cs = vt.cursor()
    cs.execute("SELECT * FROM admin WHERE parola =(?)", (parola,))
    admin_bilgisi = cs.fetchone()
    print("Bir Hata Oluştu Lütfen Tekrar Deneyiniz")
else:
    if parola in admin_bilgisi:
        class AdminPanel:
            def __init__(self):
                pass
            def aidatEkle(self,ay="",miktar=0,kat=1,daire=1):
                if kat == "1" and daire == "1":
                    kayit.kat1daire1.aidat[ay] = miktar
                elif kat == "1" and daire == "2":
                    kayit.kat1daire2.aidat[ay] = miktar
                elif kat == "1" and daire == "3":
                    kayit.kat1daire3.aidat[ay] = miktar
                elif kat == "2" and daire == "4":
                    kayit.kat2daire4.aidat[ay] = miktar
                elif kat == "2" and daire == "5":
                    kayit.kat2daire5.aidat[ay] = miktar
                elif kat == "2" and daire == "6":
                    kayit.kat2daire6.aidat[ay] = miktar
                elif kat == "3" and daire == "7":
                    kayit.kat3daire7.aidat[ay] = miktar
                elif kat == "3" and daire == "8":
                    kayit.kat3daire8.aidat[ay] = miktar
                elif kat == "3" and daire == "9":
                    kayit.kat3daire9.aidat[ay] = miktar
                elif kat == "4" and daire == "10":
                    kayit.kat4daire10.aidat[ay] = miktar
                elif kat == "4" and daire == "11":
                    kayit.kat4daire11.aidat[ay] = miktar
                elif kat == "4" and daire == "12":
                    kayit.kat4daire12.aidat[ay] = miktar
                elif kat == "5" and daire == "13":
                    kayit.kat5daire13.aidat[ay] = miktar
                elif kat == "5" and daire == "14":
                    kayit.kat5daire14.aidat[ay] = miktar
                elif kat == "5" and daire == "15":
                    kayit.kat5daire15.aidat[ay] = miktar
                elif kat == "6" and daire == "16":
                    kayit.kat6daire16.aidat[ay] = miktar
                else:
                    print("Yanlış Bilgiler Girildi")

        admin = AdminPanel()
        emir = input("Yönetici Hesabıyla Giriş Yaptınız\nLütfen Yapmak İstediğiniz İşlemi Giriniz\n>> ")
        if emir == "1":
            kat = input("kat:")
            daire = input("daire:")
            ay = input("ay:")
            miktar = input("miktar:")
            admin.aidatEkle(ay,miktar,kat,daire)
            print("Aidat Başarılı Bir Şekilde Eklendi")

    elif parola in kayit.Uye.parolalar:
        class UyePanel:
            def __init__(self):
                pass
            def aidatGoruntule(self,kat=1,daire=1):
                print("Fatura")
        uye = UyePanel()
        emir = input("Üye Hesabıyla Giriş Yaptınız\nLütfen Yapmak İstediğiniz İşlemi Giriniz\n>> ")
        if emir == "1":
            kat = input("kat:")
            daire = input("daire:")
            uye.aidatGoruntule(kat,daire)
    else:
        print("Girdiğiniz parola hatalı!")
        cikis()