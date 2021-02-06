# example_1 --> calculator
"""
print("\tCALCULATOR\n")
sayi1 = float(input("enter a value:"))
operator = input("operator:")
sayi2 = float(input("enter a value"))
if operator == "+":
    print(sayi1+sayi2)
elif operator == "-":
    print(sayi1-sayi2)
elif operator == "*":
    print(sayi1*sayi2)
elif operator == "/":
    print(sayi1/sayi2)
else:
    print("THIS CALCULATOR CAN'T DO YOUR OPERATION")
"""
# example_2 --> hipotenus
"""
import math
a = float(input("ucgenin birinci dik kenarinin uzunlugu : "))
b = float(input("ucgenin ikinci dik kenarinin uzunlugu : "))
print(math.sqrt(a*a+b**2))
"""
# example_3 --> akim
"""
V = float(input("potansiyel : "))
R = float(input("direnc : "))
print("akim :",(V/R))
"""
# example_4 --> dictionary
"""
while True:
    dictionary = dict()
    word = input("word : ")
    meaning = input("meaning : ")
    dictionary[word] = [meaning]
    y_n = input("add another (y,n):")
    if y_n == "n":
        break
print(dictionary)
"""
# example_5 --> bir dosyaya ogrencinin not ortalamasini yazdirma
"""
ad = input("ogrenci : ")
vize = int(input("vize notu : "))
final = int(input("final : "))
donem_sonu_notu = (vize*0.4)+(final*0.6)
if donem_sonu_notu >= 85:
    harf_not = "AA"
elif donem_sonu_notu >= 70:
    harf_not = "BA"
elif donem_sonu_notu >= 60:
    harf_not = "BB"
elif donem_sonu_notu >= 50:
    harf_not = "CB"
elif donem_sonu_notu >= 40:
    harf_not = "CC"
else:
    harf_not = "FF"
# 'a' !!
with open("notlar.txt","a") as dosya:
    dosya.writelines("{} ogrencisinin notu : {} --> {}\n".format(ad,donem_sonu_notu,harf_not))
print(donem_sonu_notu,harf_not)
"""
# example_6 --> yazi-tura
"""
tekrar = int(input("bilgisayar kac kez yazi tura atsin : "))
yazi = 0
tura = 0
import random

parayuzeyi = ("yazi", "tura")
while tekrar > 0:
    tekrar -= 1
    secim = random.choice(parayuzeyi)
    if secim == "yazi":
        yazi += 1
    else:
        tura += 1
print("{} atis icerisinden {} kez yazi, {} kez tura geldi.".format((yazi + tura), yazi, tura))
"""
# example_7 --> asal sayi yazdirma
"""
sinir = int(input("hangi sayiya kadar asal sayilari yazdirayim : "))
list = []
for sayi in range(2, sinir):
    i = 2
    while i <= int(sayi / 2) and sayi % i != 0:
        i += 1
    if i == int(sayi / 2) + 1:
        list.append(sayi)
print("{}'den kucuk asal sayilar --> ".format(sinir), *list)
"""
# example_8 --> faktoriyel
"""
faktoriyeli_alinacak_sayi = int(input("Kac faktoriyel : "))
total = 1
for x in range(1,faktoriyeli_alinacak_sayi+1):
    total *= x
print(faktoriyeli_alinacak_sayi,"! = ",total,sep="")
print("{}! = {}".format(faktoriyeli_alinacak_sayi,total))
"""
# example_9 --> ATM
"""
bakiye = 2000
bilgi = "Alperen Olcer"
while 1:
    islem = int(input("1)Para cekme\n2)Para yatirma\n3)Kart bilgileri\n4)Kart iade\nSeciniz : "))
    if islem == 1:
        miktar = int(input("Cekilecek miktar : "))
        if miktar > bakiye:
            print("Bakiye yetersiz.")
        else :
            bakiye -= miktar
            print("Yeni bakiyeniz : {}".format(bakiye))
    elif islem == 2:
        miktar = int(input("Yatirilacak miktar : "))
        bakiye += miktar
        print("Yeni bakiyeniz : {}".format(bakiye))
    elif islem == 3:
        print(bilgi,bakiye)
    elif islem == 4:
        break
    else:
        print("Islem secemediniz. Tekrar deneyiniz.")
"""
# example_10 --> girilen sayinin tam sayi bolenlerini bulma
"""
def bulma(sayi):
    for i in range(1,sayi+1):
        if  sayi % i == 0:
            dizi.append(i)
    return dizi
dizi = []
sayi = int(input("sayi giriniz : "))
print(bulma(sayi))
"""
# example_11 --> ekok
"""
sayi1 = int(input("Birinci sayi : "))
sayi2 = int(input("Ikinci sayi : "))
carpım = sayi1 * sayi2
for i in range (max(sayi1,sayi2),carpım+1):
    if i % sayi1 == 0 and i % sayi2 == 0:
        print("{} ve {} sayilarinin ekoku : {}".format(sayi1, sayi2, i))
        break
"""
# example_12 --> sayi tahmin oyunu
"""
from random import randint
devam = "e"
while devam == "e":
    print("7 tahmin hakkiniz var.\nSayi (1,100) arasindadir.")
    sayi = randint(1, 100)
    deneme = 1
    while deneme < 8:
        tahmin = int(input("{}. tahmininizi giriniz : ".format(deneme)))
        deneme += 1
        if tahmin > sayi:
            print("Asagi")
        elif tahmin < sayi:
            print("Yukari")
        else:
            print("Tebrikler bildiniz.")
            break
    if deneme == 8:
        print("Bulamadiginiz sayi {} idi".format(sayi))
    devam = input("Tekrar oynamak istiyor musunuz? (e,h): ")
"""
# example_13 --> class sirket dosya
"""
class sirket():

    def __init__(self, calisans = [],butce = 0):
        self.Calisanlar = calisans
        self.butce = butce

    def calisan_sayisi_bul(self):
        return len(self.Calisanlar)

    def calisan_ekleme(self,ekle):
        self.Calisanlar.append(ekle)

    def calisan_cikarma(self, cikar):
        self.Calisanlar.remove(cikar)

    def butce_ekle_cikar(self, sayi):
        self.butce += sayi

    def output(self):
        print("\nCalisanlar :", *self.Calisanlar, sep=",")
        print("butce = {}".format(self.butce))
        print("*************CREATED BYE OUT OF WORLD COMPANY*************")


calisanlarR = []
sirketlerR = []
butcelerR = []
try:
    with open("sirketlerin_bilgileri.txt", "r") as fpr:
        sirketlerin_bilgileri = fpr.read()
    bol = sirketlerin_bilgileri.split("/")
    count = 0
    print(bol)
    while count < 3:
        if count == 0:
            sirketlerR.append(bol[0].split(","))

        elif count == 1:
            workers = bol[1].split(".")
            for i in workers:
                calisanlarR.append(i.split(","))

        elif count == 2:
            butcelerR.append(bol[2].split(","))

        count += 1
    print(sirketlerR,calisanlarR,butcelerR)
    a = 0
    for name in sirketlerR[0]:
        y = name
        vars()[y] = sirket(calisanlarR[a],int(butcelerR[0][a]))
        a += 1
except IOError:
    print("Have not opened yet")
    with open("sirketlerin_bilgileri.txt", "a") as fpr:
        pass
finally:
    fpr.close()

while 1:
    sec = int(input("Var olan sirket uzerinden islem mi yapicaksiniz (1) yoksa yeni sirket bilgileri mi ekleyeceksiniz (2) , cikis icin (3) :"))
    if sec == 1:
        s = input("Sirket adi : ")
        eval(s)
    elif sec == 2:
        y_s = input("Sirket adi : ")
        s = y_s
        s = sirket()
    elif sec == 3:
        break


    while 1:
        if sec == 1:eval(s).output()
        if sec == 2:s.output()
        print("1-Calisan kaydetme       2-Calisan silme     3-Toplam maas",
              "4-Sirket butce ogrenme      5-Butce ekleme      6-Butce silme","\t\t\t\t7-Cikis",sep="\n")
        secim = int(input("Seciniz : "))
        if secim == 1:
            ekle = input("Yeni calisan : ")
            if sec == 1:eval(s).calisan_ekleme(ekle)
            if sec == 2:s.calisan_ekleme(ekle)
        elif secim == 2:
            cikar = input("Silinecek calisan : ")
            if sec == 1:eval(s).calisan_cikarma(cikar)
            if sec == 2:s.calisan_cikarma(cikar)
        elif secim == 3:
            maas = int(input("Ortalama bir calisanin maasi nedir : "))
            if sec == 1:print("Yaklasik toplam maas =", maas * len(eval(s).Calisanlar))
            if sec == 2:print("Yaklasik toplam maas =", maas * len(s.Calisanlar))
        elif secim == 4:
            if sec == 1:print(eval(s).butce)
            if sec == 2:print(s.butce)
        elif secim == 5:
            sayi = int(input("Ne kadar eklenecek : "))
            if sec == 1:eval(s).butce_ekle_cikar(sayi)
            if sec == 2:s.butce_ekle_cikar(sayi)
        elif secim == 6:
            sayi = -int(input("Ne kadar azalacak : "))
            if sec == 1:eval(s).butce_ekle_cikar(sayi)
            if sec == 2:s.butce_ekle_cikar(sayi)
        elif secim == 7:
            if sec == 2:
                sirketlerR[0].append(y_s)
                calisanlarR.append(s.Calisanlar)
                butcelerR[0].append(str(s.butce))
            else:
                i = 0
                while s != sirketlerR[0][i]:
                    i += 1
                calisanlarR[i] = eval(s).Calisanlar
                butcelerR[0][i] = (str(eval(s).butce))
            break


    #print(*sirketlerR[0],*calisanlarR,*butcelerR)

yazilacak = ""
i = 0
for company in sirketlerR[0]:
    yazilacak += company+","
    i += 1
yazilacak = yazilacak[:-1]
yazilacak += "/"
for x in range(0, i):
    for worker in calisanlarR[x]:
        yazilacak += worker+","
    yazilacak = yazilacak[:-1]
    yazilacak += "."
yazilacak = yazilacak[:-1]
yazilacak += "/"
for money in butcelerR[0]:
    yazilacak += money+","
yazilacak += "/"
yazilacak = yazilacak[:-2]
#print(yazilacak)
with open("sirketlerin_bilgileri.txt", "w") as fpw:
    fpw.write(yazilacak)
"""
# example_14 --> basit mp3 calar
"""
import random
import os


class Mp3Calar:
    def __init__(self,sarkilar_g=[], ses_g=50, calan="YOK"):
        self.ses = ses_g
        self.sarkilar = sarkilar_g
        self.calan_sarki = calan

    def sesArttir(self):
        if self.ses == 100:
            print("Max ses duzeyi")
        else:
            self.ses += 10

    def sesAzalt(self):
        if self.ses == 0:
            print("Min ses duzeyi")
        else:
            self.ses -= 10
    def SarkiSec(self):
        sarki = input("Calacak sarki : ")
        while self.sarkilar.count(sarki) == 0 and sarki != "-":
            sarki = input("Sectiginiz sarki listede yok tekrar girin (cikmak icin '-') : ")
        self.calan_sarki = sarki

    def rastgeleSarkiSec(self):
        self.calan_sarki = random.choice(self.sarkilar)


choice = 1
mp3 = Mp3Calar()
while choice != 7:
    choice = int(input("Sarki listesi : {}\n".format(mp3.sarkilar) +
                       "Suan calan sarki : {}\n".format(mp3.calan_sarki) +
                       "Ses : {}\n".format(mp3.ses) +
                       "1-Sarki sec\n"
                       "2-Ses arttir\n"
                       "3-Ses azalt\n"
                       "4-Rastgele sarki sec\n"
                       "5-Sarki ekle\n"
                       "6-Sarki sil\n"
                       "7-Kapat\n"
                       "Seciniz : "))

    if choice == 1:
        mp3.SarkiSec()
    elif choice == 2:
        mp3.sesArttir()
    elif choice == 3:
        mp3.sesAzalt()
    elif choice == 4:
        mp3.rastgeleSarkiSec()
    elif choice == 5:
        sarki = "1"
        print("Sarki eklemeyi bitirdiginizde '-' giriniz.")
        while sarki != "-":
            sarki = input("Yeni Sarki : ")
            if mp3.sarkilar.count(sarki) == 1:
                print("Sarki zaten bulunmakta.")
                continue
            mp3.sarkilar.append(sarki)
        mp3.sarkilar.pop()
    elif choice == 6:
        sarki = "1"
        print("Sarki silmeyi bitirdiginizde '-' giriniz.")
        while sarki != "-":
            sarki = input("Sarki listesi : {}".format(mp3.sarkilar) + "\nSilinecek Sarki : ")
            try:
                mp3.sarkilar.remove(sarki)
            except:
                pass
    os.system("clear")
"""
# example_15 --> X-O-X Game
"""
class Game:
    def __init__(self):
        self.table = {
            11: "-", 12: "-", 13: "-",
            21: "-", 22: "-", 23: "-",
            31: "-", 32: "-", 33: "-"}
        self.bitmedi = 1

    def hamleal(self, sira):
        print("\nHamle sirasi O")
        satir = int(input("satir : "))
        sutun = int(input("sutun : "))
        key = satir*10 +sutun
        while self.table[key] != "-":
            print("DOLU")
            satir = int(input("satir : "))
            sutun = int(input("sutun : "))
            key = satir * 10 + sutun
        self.table[key] = sira
    def bitti_mi(self):
        if self.table[11] == self.table[12] == self.table[13] != "-":
            self.bitmedi = 0
        elif self.table[21] == self.table[22] == self.table[23] != "-":
            self.bitmedi = 0
        elif self.table[31] == self.table[32] == self.table[33] != "-":
            self.bitmedi = 0
        elif self.table[11] == self.table[21] == self.table[31] != "-":
            self.bitmedi = 0
        elif self.table[12] == self.table[22] == self.table[32] != "-":
            self.bitmedi = 0
        elif self.table[13] == self.table[23] == self.table[33] != "-":
            self.bitmedi = 0
        elif self.table[11] == self.table[22] == self.table[33] != "-":
            self.bitmedi = 0
        elif self.table[13] == self.table[22] == self.table[31] != "-":
            self.bitmedi = 0
    def yazdir(self):
        for key, values in self.table.items():
            if int(key) % 10 == 1:
                print("\n",end="")
            print("{}  ".format(values), end="")

xox = Game()
sira = 1
while xox.bitmedi:
    xox.yazdir()
    if sira % 2 == 1:
        xox.hamleal("O")
    else:
        xox.hamleal("X")
    xox.bitti_mi()
    sira += 1

xox.yazdir()
"""
# example_16 --> Uyelik sistemi (json)
"""
import json
from time import sleep
from random import randint


class Kullanici:
    
    def __init__(self):
        global dosya
        try:
            dosya = open("uyeler.json", "r")
            self.uyeler = json.load(dosya)
        except FileNotFoundError:
            dosya = open("uyeler.json", "w")
            self.uyeler = {"kullanicilar": []}
            json.dump(self.uyeler, dosya)
        finally:
            dosya.close()
        self.menu()

    def menu(self):
        while 1:
            print("*********HOS GELDINIZ*********")
            print("1-Giris yap", "2-Kayit ol", "3-Cikis", sep="\n")
            secim = input("Isleminiz : ")

            while secim != '1' and secim != '2' and secim != '3':
                secim = input("1,2,3 girebilirsiniz sadece\nIsleminiz : ")

            if secim == '1':
                self.giris_yap()
            elif secim == '2':
                self.kayit_ol()
            elif secim == '3':
                self.cikis()
                break
            # print(self.uyeler)
            
    def giris_yap(self):
        ad = input("Kullanici adi : ")

        if len(self.uyeler["kullanicilar"]) == 0:
            print("Kayit olun.")
            return 0
        yok = 1
        while yok:
            for j in range(len(self.uyeler["kullanicilar"])):
                if ad == self.uyeler["kullanicilar"][j]["ad"]:
                    yok = 0
                    sifre = input("Sifre : ")
                    kalan_hak = 3
                    while sifre != self.uyeler["kullanicilar"][j]["sifre"]:
                        sifre = input("Yanlıs sifre / kalan deneme hakkiniz: {}\nSifrenizi unutmus iseniz 0 giriniz.\nSifre : ".format(kalan_hak))
                        kalan_hak -= 1
                        if kalan_hak == 0:
                            kalan_hak = 3
                            print("5 saniye bekleme...")
                            sleep(5)

                        if sifre == "0":
                            self.sifre_unuttum(j)
                            sifre = input("Mailinize gonderilen yeni sifrenizi giriniz : ")
                    print("Giris yaptiniz. MERHABA {}!!!".format(ad))
                    break
            if yok:
                ad = input("Kayitli oldugunuza emin misiniz ? Degilseniz 'g' giriniz. Tekrardan kullanici adi : ")
                if ad == 'g':
                    return 0

    def kayit_ol(self):
        key = 0

        ad = input("Kullanici adi : ")
        ad = self.var_mi(ad,key)
        key +=1
        sifre = input("Sifre : ")
        sifre = self.var_mi(sifre,key)
        key +=1
        mail = input("Mail : ")
        mail = self.var_mi(mail,key)

        self.uyeler["kullanicilar"].append({"ad": ad, "sifre": sifre, "mail": mail})

    def var_mi(self, string,key):
        keys = ["ad","sifre","mail"]
        broke = 1
        if len(self.uyeler["kullanicilar"]) == 0:
            return string
        while broke:
            for j in range(len(self.uyeler["kullanicilar"])):
                if string == self.uyeler["kullanicilar"][j][keys[key]]:
                    string = input("Girdiginiz kullanici {}i zaten var. Baska {} adi : ".format(keys[key], keys[key]))
                    break
                if j == len(self.uyeler["kullanicilar"]) - 1:
                    broke = 0
        return string

    def sifre_unuttum(self, sira):
        sifre = randint(1000, 100000)
        self.uyeler["kullanicilar"][sira]["sifre"] = str(sifre)
        with open("mail.txt", "a") as dosya:
            dosya.write("{} mailinize OUTofWORLD@gmail.com 'dan yeni bir mail geldi :\n\nYeni sifreniz : {}\nIYI GUNLER {}\n\n\n".format(
                self.uyeler["kullanicilar"][sira]["mail"], sifre, self.uyeler["kullanicilar"][sira]["ad"]))

    def cikis(self):
        with open("uyeler.json", "w") as dosya:
            json.dump(self.uyeler, dosya)


kullanici = Kullanici()
"""
# example_17 --> universite sistemi SQL
"""
import sqlite3


class Sistem:

    def __init__(self):
        self.baglanti = sqlite3.connect("universite_V_T.db")
        self.imlec = self.baglanti.cursor()
        self.imlec.execute("CREATE TABLE IF NOT EXISTS ogrenciler(ad TEXT, bolum TEXT, numara INT)")
        self.menu()

    def ogrenci_ekle(self):
        ad, bolum, numara = input("AD ve SOYAD : "), input("BOLUM : "), int(input("NUMARA : "))
        self.imlec.execute("INSERT INTO ogrenciler VALUES('{}','{}',{})".format(ad,bolum,numara))
        self.baglanti.commit()

    def ogrenci_sil(self):

        self.imlec.execute("DELETE FROM ogrenciler WHERE numara = {}".format(int(input("SILENECEK OGRENCININ NUMARASI : "))))
        self.baglanti.commit()

    def bilgi_degistirme(self):
        kisi_num = int(input("Bilgisi guncellenecek ogrencinin numarasi : "))
        degisecek = int(input("Neyi degistirmek istiyorsunuz (1-AD ve SOYAD , 2-BOLUM , 3-NUMARA)")) - 1
        secenekler = ["ad", "bolum", "numara"]
        yeni = input("Yeni {} : ".format(secenekler[degisecek]))
        try:
            self.imlec.execute("UPDATE ogrenciler SET '{}' = {} WHERE numara = {}".format(secenekler[degisecek], yeni, kisi_num))
        except sqlite3.OperationalError:
            self.imlec.execute("UPDATE ogrenciler SET '{}' = '{}' WHERE numara = {}".format(secenekler[degisecek], yeni, kisi_num))
        finally:
            self.baglanti.commit()

    def ogrencileri_gor(self):

        self.imlec.execute("SELECT * FROM ogrenciler")
        for ogrenci in enumerate(self.imlec.fetchall(), 1):
            print(ogrenci[0], ogrenci[1][0], ogrenci[1][1], ogrenci[1][2])

    def menu(self):
        while True:
            secim = input("\n1-Ogrenci ekle\n2-Ogrenci sil\n3-Ogrencileri goruntele\n4-Ogrenci bilgilerini degistir\n5-Cikis\nSECINIZ : ")
            if secim == '1':
                self.ogrenci_ekle()
            elif secim == '2':
                self.ogrenci_sil()
            elif secim == '3':
                self.ogrencileri_gor()
            elif secim == '4':
                self.bilgi_degistirme()
            else:
                break


usis = Sistem()
"""
# example_18 --> https://www.youtube.com/watch?v=jbQxr_zdPcQ&list=PLK6Whnd55IH5i1klkNSBDasIaO77l-Bm9&index=49
"""
kisiler = ["ali","veli","busra","sema","ALI","VEli","    BusrA     ","sEmAnuR"]
for i in range(len(kisiler)):
    kisiler[i] = kisiler[i].strip().lower()
for j in set(kisiler):
    if kisiler.count(j) > 1:
        print(j.capitalize())

def reverse_int(sayi):
    liste = list(str(sayi))
    liste.reverse()
    return int( "".join(liste) )
sayi = int(input("sayi gir : "))
print(reverse_int(sayi))

def move_zeros(liste):
    ilk = len(liste)
    while True:
        try:
            liste.remove(0)
        except ValueError:
            break
    son = len(liste)
    for i in range(ilk-son):
        liste.append(0)
        print(liste)
    return liste
liste = [15,42,53,68,9,0,4,20,0,0,1,0,2,44,45,3]

# print(move_zeros(liste))
print("*************************")
j = 0
for i in range(0, len(liste)):
    print(i)
    if liste[i] == 0:
        #print(liste)
        deger = liste[i]
        liste.remove(deger)
        liste.append(deger)
        j += 1
print(j)
print(liste)

# string = "selam bu python learning icinden examples_free"
string = "pijamalı hasta yağız şoföre çabucak güvendi"
def pangram_mi(paragraf):
    if len(set(paragraf)) > 29:
        return True
    else:
        return False
print(pangram_mi(string))
"""
# example_19 --> https://www.youtube.com/watch?v=4-0tLD_WftM&list=PLK6Whnd55IH5i1klkNSBDasIaO77l-Bm9&index=51&t=704s
"""
def convert_tr(metin):
    tr = ["i","ğ","ü","ç","ş","ö"]
    en = ["ı","g","u","c","s","o"]
    for x in range(6):
        metin = metin.lower().replace(tr[x],en[x])
    metins = metin.split(". ")
    for i in range(len(metins)):
         metins[i] = metins[i].capitalize()
    metin = " ".join(metins)
    return metin

string = "Sevgi, nesnel olduğu gibi öznel olarak da varlık'ın ölçütüdür; hakikatin ve gerçekliğin ölçütüdür. Sevginin olmadığı yerde hakikat da yoktur."
print(convert_tr(string))

def clear_numbers(yazi:str):
    for i in yazi:
        try:
            int(i)
            yazi = yazi.replace(i,"")
        except ValueError:
            pass

    return yazi
print(clear_numbers("asd67as46a4f 421 asc 217 das d a21d 1a 21s"))

def first_repeat(metin):
    liste = []
    for i in metin:
        liste.append(i)
    a = 0
    for i in liste:
        a += 1
        for j in liste[a:]:
            if i == j:
                return i
    return "0"
print(first_repeat("hajvsxawıdas"))

def maxc(yazi:str):
    kume = set(yazi)
    max_index = 0
    index = 0
    kume = list(kume)
    for i in kume:
        if yazi.count(i) > yazi.count(kume[max_index]):
            max_index = index
        index += 1
    return kume[max_index]
print(maxc("ascasvxzxkvweyıbldsşvbsıvcyhsdkv ywıecvzxc"))

def clear_list(liste:list):
    return list(set(liste))
liste = [1,2,2,4,24,2,10,45,5,24,2,42,542,12,7,53,12,5,42,7542]
print(clear_list(liste))
"""
