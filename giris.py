import kayit
import sqlite3 as sql
from sys import exit as cikis
parola = input("Lütfen parolanızı giriniz: ")
vt = sql.connect("admin.sqlite")
cs = vt.cursor()
cs.execute("SELECT * FROM admin WHERE parola =(?)",(parola,))
admin_bilgisi = cs.fetchone()
if parola in admin_bilgisi:
    class AdminPanel:
        def __init__(self):
            pass
    admin = AdminPanel()
    emir = input("Yönetici Hesabıyla Giriş Yaptınız\nLütfen Yapmak İstediğiniz İşlemi Giriniz\n>> ")
elif parola in kayit.Uye.parolalar:
    class UyePanel:
        def __init__(self):
            pass
    uye = UyePanel()
    emir = input("Üye Hesabıyla Giriş Yaptınız\nLütfen Yapmak İstediğiniz İşlemi Giriniz\n>> ")
else:
    print("Girdiğiniz parola hatalı!")
    cikis()