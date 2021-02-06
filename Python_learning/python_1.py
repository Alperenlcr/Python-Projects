""" operatorler,degiskenler
# // tamsayi bolmesi, ** us alma
a=10
b=2
print(a**b)
print(a//b)
print(b/a)
"""
"""  bazi string ozellikleri
string = "this is string"
no = " isn't "
place = string.find(" is ")
len_place = len(" is ")
print(string[0:place]+no+string[place+len_place:])
name = "alperen olcer"
print(name.replace("alperen","kerim"))
names = "alp,eren,alper,alperen"
surnames = "x,y,z,t"
print(names[0:3]+" "+surnames[0])
"""
""" veri donusumleri
sayi_int = 15
print(sayi_int)
print(sayi_int*3)
print(type(sayi_int))
print(str(sayi_int)*3)
char = 'c' # string
string = "string"
floatt = 5.5
print(type(char)) # string
print(type(string))
print(type(floatt))
"""
""" print function
a=1
b=2
c=3
print(a,b,c,sep="/") #separate
print(a,end=" aaa ")
print(b,"\n",c,sep="")
isim = "alperen"
soyad = "olcer"
print("merhaba",isim,soyad,"bey")
print("merhaba {} {} bey".format(isim,soyad))
print("merhaba %s %s bey" % (isim,soyad))
dosya = open("text.txt","w")
print("hello there",file=dosya)
str = "yildizli parametreler"
print(*str,sep=".")
"""
"""     list
a = list()
names = ["alp","eren","kerim","al","pe","ren"]
print(type(a),type(names))
print(len(names),names,sep="-->")
names.remove("kerim")
print(len(names),names,sep="-->")
print(names[0:3],names[:6:2],names[::-1],sep="///")
names[0] = "alperen"
print(names)
#string i liste dondurme
str = "hello"
str = list(str)
print(str,type(str))#end
names_2 = ["futbol","voleybol","basketbol"]
names = names + names_2
print(names)
print(names_2 * 3)
names_2.append("masatenisi")    #ekleme
print(names_2)
names_2.pop(0)      #cikarma
print(names_2)
names.sort()    #siralama
print(names)
numbers = [25,2,4,1,2,7,27,5227,52,7,42,3]
numbers.sort(reverse=True)      #siralama
print(numbers)
###
users = ["good","night","gofret"]
passwords = [46,64,85]
all = [users,passwords]
print(all,all[0],all[1],all[0][2],all[1][2],sep="___")
"""
"""     tuple
#tuple nesnesinde icindekilerin degistirilmesine izin vermez.
#sadece okuma
a = (0,0,0,0,"alp",321,"sa","as",22,0)
b = tuple()
print(type(a),type(b))
print(a.index(22))
print(a.count("ali"),a.count(0))
print(a.__contains__("alp"),a.__contains__("ali"))
"""
"""     dict 
# dictionary = {anahtar objesi : deger objesi, ...}
people = {"alperen": 19, "zeynep": [18, "or", 20], "no one": "not exist", "ekleme": ["ekl", "enti"]}
people["ekleme"] += ["hello"]
people["ekleme"].pop(1)
print(people["zeynep"], people,type(people), sep="\t")
copy_people = people.copy()
people.clear()
print(people,copy_people,sep=" /-/ ")
"""
# input function always takes string input
# example_1
# example_2
# example_3
# example_4
# AND , OR pythonda and , or olarak kullaniliyor.
""" if-else-elif
(if or else or elif) (kosul) :
    (islemler)
(cikinca burdan devam)
"""
# example_5
"""     for loop
a = 1 in (0,1,2,3,4)
b = "a" in "hello alperen"
c = 2 in [1,3,5,7,9]
print(a,b,c)
sayilar = [0,1,2,3,4,5,6,7,8,9]
for i in sayilar:
    print(i**2,end=" ")
list = [(1,2),(3,4),(5,6),(7,8),(9,10)]
print()
for i,j in list:
    print(i,j)
oynatma_listesi = {"Barış Manço": "Kara Sevda",
                   "Neşet Ertaş": "Yazımı Kışa Çevirdin",
                   "Hadise": "Sıfır Tolerans",
                   "Merve Özbey": "Vicdanın Affetsin",
                   "Aleyna Tilki": "Yalnız Çiçek" }
for i in oynatma_listesi.values():
    print("-",i)
for j in oynatma_listesi.keys():
    print("-",j)
for i in oynatma_listesi.items():
    print(i)
"""
"""     while
while (kosul):
    (islemler)
    ++
"""
# example_6
"""     range function
# range(parametre:bitis)
for i in range(10):
    print(i)
# range(parametre:baslangıc,parametre:bitis)
for i in range(5,15):
    print(i)
# range(parametre:baslangıc,parametre:bitis,parametre:artıs)
for i in range(20,10,-2):
    print(i)
"""
# example_7
# break and continue dan sonra iki nokta vs. yok
"""     list comprehension (tanimlama)
sayilar = []
for i in range(1,10000):
    if i % 6 == 0:
        sayilar.append(i)
print(*sayilar)
sayilar_2 = list(x for x in range(1,10000) if x % 6 == 0)
print(sayilar_2)
kisiler = ["Ali","veli","ahmet","alper","Omer"]
kopya_kisiler = [kisi for kisi in kisiler]
a_ile_baslayanlar = [i for i in kisiler if i[0] == "A" or i[0] == "a"]
print(kisiler,kopya_kisiler,a_ile_baslayanlar,sep="\n")
"""


# example_8
# example_9
"""     functions
def yazdirma(sayi, yazi):
    for i in range(sayi):
        print(yazi)
yazdirma(5, "Selam")
def switch(a, b):
    temp = a
    a = b
    b = temp
def ebob(a, b):
    if a < b:
        switch(a, b)
    for i in range(1,b+1):
        if b % i == 0 and a % i == 0:
            deger = i
    return deger
a = int(input("sayi 1 : "))
b = int(input("sayi 2 : "))
print(ebob(a, b))
"""
# parametre cesitleri : 1. Normal parametre 2.Yldizli parametre
# 3.Varsayilan parametre 4. **Degerler (dict mantigi)(keywords)
"""
def topla(*sayilar):
    sum = 0
    for sayi in sayilar:
        sum += sayi
    print(sum)
topla(1,2,3,4,11,2,33,44,55,78)

def kuvvet_al(sayi,kuvvet = 2):
    return sayi ** kuvvet
print(kuvvet_al(3,4))
print(kuvvet_al(3))

def degerleri_goster(**degerler):
    for anahtar,deger in degerler.items():
        print(anahtar,deger)
degerleri_goster(alp = "eren", zey = "nep", ker = "im", al = "beni")
"""
# fonksiyon icinde uretilen degiskenler local dir disinda is yapmaz.
# en soldaki (maindeki) her degisken globaldir.
# fonksiyon icinde uretilen bir degiskeni global yapabiliriz. global degisken seklinde

# lambda functions
"""
# map --> map(fonksiyon,fonksiyona giricek degerler(liste olabilir) ) = sonuc = fonksiyondan cıkan degerler
l = list(map(lambda x : x+2, range(10)))
# x, l listesi olusturulurken tanimlandi kullanildi sonra silindi.
l = [(x+2) for x in range(10)]
# x, l listesi olusturulurken tanimlandi kullanildi sonrasinda da var.
l = []
for x in range(10)
    l.append(x+2)
# x, dongu basinda tanimlandi ve bittikten sonra da var.

"""
"""
fonksiyon = lambda x,y: x * y
toplam = lambda *sayilar: sum(sayilar)
print(fonksiyon(1,4))
print(toplam(45,5,4,3,1,2))
"""
# example_10
# example_11
"""     moduller (bastaci)
import moduller
print(moduller.toplama(2,3))
from moduller import carpma,bolme    # sadece yazdiklarimi aktif hale getirir
print(carpma(5,5))
print(bolme(7,8))
from moduller import *      # butun fonksiyonlari aktif hale getirir
print(cıkarma(3,4))

import random
print("Zar : {}".format(random.randint(1,6)))
"""
# example_12
#   class
"""
class class1():
    def __init__(self):
        print("obje uretildi")
    ogrenci = "alp"
    ogretmen = "eren"
    mevcut = 1
    okul = "hayat"
    def bilgileri_yazdir(self):
        print(self.okul,self.mevcut,self.ogrenci,self.ogretmen)
a12 = class1()
print(a12.okul, a12.mevcut, a12.ogrenci, a12.ogretmen)
print(a12)
a12.bilgileri_yazdir()

class oda():
    def __init__(self,girdi_yatak,girdi_masa,girdi_alan):
        self.yatak = girdi_yatak
        self.masa = girdi_masa
        self.alan = girdi_alan
    def yazdir(self):
        print("onun odasinda {} yatak, {} masa var ve alani {}".format(self.yatak,self.masa,self.alan))
kerim = oda(1,1,20)
kerim.yazdir()
alperen = oda(2,2,30)
alperen.yazdir()

"""
"""
class Sinif:
    def __str__(self):
        return "ogrenci"
sinif = Sinif()
print(sinif)
#__str__ fonksiyonu print ile tetiklenir buna benzer birsürü gomulu fonksiyon vardır.
"""
"""

class sinif:
    def __init__(self,deger = 0):
        self.deger = deger
class1 = sinif(100)
s = input("class name : ")
print(class1.deger)
print(eval(s).deger)
"""
# example_13
""" split()
str = "a,b,c/d,e/f"
bol = "text.txt".split("/")
count = 0
while count < 5:
    print(bol)
    count += 1
    if count == 1:
        bir = bol[0].split(",")
    elif count == 2:
        iki = bol[1].split(",")
    elif count == 3:
        uc = bol[2].split(",")
    else:
        pass
        #print(count)
print(bir,iki,uc,sep="/")
"""
# Kalitim
"""
class Genel:
    pass
def __init__(self,genelozellik1, genelozellik2):
    self.ad = genelozellik1
    self.soyad = genelozellik2
    def genelfonk(self):
        print("Genelin fonksiyonu")
    def aldigini_yazdir(self,al):
        print(al)

class Ozel(Genel):
    def __init__(self,ozellik1,ozellik2):
        super().__init__(ozellik1,ozellik2)

ozel = Ozel(1,2)
ozel.genelfonk()
print(ozel.ad,ozel.soyad)
ozel.aldigini_yazdir("yazi")


class BuyukAnne:
    def __init__(self,gozz,sacc):
        print("BuyukAnne__init__")
        self.sac = sacc
        self.goz = gozz
class Anne(BuyukAnne):
    def __init__(self):
        print("Anne__init__")
        BuyukAnne.__init__(self,buyukanne.goz,buyukanne.sac)
        #super().__init__(buyukanne.goz,buyukanne.sac)
        self.goz = "yesil"
class Cocuk(Anne):
    def __init__(self):
        print("Cocuk__init__")
        Anne.__init__(self)
        #super().__init__()
buyukanne = BuyukAnne("mavi","kumral")
anne = Anne()
cocuk = Cocuk()
print("buyukanne --> goz:{}    sac:{} \nanne     --> goz:{}    sac:{}\ncocuk    --> goz:{}    sac:{}".format(buyukanne.goz,buyukanne.sac,
               anne.goz,anne.sac,
               cocuk.goz,cocuk.sac)
)
"""
# The super() function is used to give access to methods and properties of a parent or sibling class.
# The super() function returns an object that represents the parent class.

# example_14

# example_15

# try-except-finally / raise
"""
# try:
#     islem
# except hata:
#     hatamesaji
# finally:
#     son islem
i = 2
if type(i) != list:
    raise TypeError("i list degil")
# raise hata tipi uretme
"""
# Dosya islemleri

# dosya = open( dosyaAdi , islem ("r","w","a","a+") , encoding=("utf-8"...) )
# dosya.close()
# dosya.read(n --> int kac karakter (eger bossa hepsi) )
# dosya.readline() bulundugu satir bitine kadar veya icine girilen deger kadar okur
# dosya.readlines() her satiri bir listenin elemani yapar
# dosya.tell() dosya pointerinin nerede oldugunu soyler
# dosya.seek() dosya pointerinin yerini degistirir
# dosya.write() dosyaya yazar
# dosya.writelines(list) listedekinleri yazar arka arkaya
# "a" da iken dosya.write() dosyanin sonuna yazar
# with open(dosyaAdi , islem ("r","w","a","a+") , encoding=("utf-8"...) ) as dosya:
#     islemler
# bloktan cıkınca otomatik dosyayi kapatir

# map

# Syntax :
# map(funct, iterbl)
# Parameters :
# funct : The function which is going to execute for each iterable
# iterbl : A sequence or collection of iterable objects which is to be mapped exp: list, tuple...
"""
def fonk(x):
    return x**2
print(list(map(fonk, [1,2,3,4,5])))
print(list(map( lambda x: x**3, [1,2,3,4,5])))
"""
# zip() fonksiyonu iki diziyi eşleştirmemizi kolaylaştırır.
"""
kelimeler = ["kalem", "bilgisayar", "fare"]
ingilizceleri = ("pencil", "computer", "mouse")
print(list(zip(kelimeler, ingilizceleri)))
"""
# enumrate(iter, start=0) fonksiyonu girdiğimiz parametrenin elemanlarını numaralandırır.
"""
ogrenciListesi = ["alperen","kemal","zehra","zeynep","orkun"]
print(list(enumerate(ogrenciListesi, start=1)))
"""
# filter(func, iter) fonksiyonu bir dizi içinden belirlediğimiz koşulu tutan elemanların süzebilmemize yarar.
"""
def cift(x):
    return x % 2 == 0
liste = [i for i in range(20)]
print(list(filter(cift, liste)))

# list of letters
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(letter in vowels):
        return letter

filteredVowels = filter(filterVowels, letters)
print(list(filteredVowels))
"""
# all(iter) fonksiyonu bir dizinin icindeki tüm degerler True ise True, degilse False degeri dondurur.
"""
liste = [0,1,2,3,4] # 0 değeri False, 1 ve diğer tüm sayılar True değerindedir.
print(all(liste))

liste = [1,2,3,"Mert",4]
print(all(liste))

liste = [1,"",3,"Mert",4] # boşluk False değerindedir.
print(all(liste))

liste = [1,None,3,"Mert",4] # None False değerindedir.
print(all(liste))
"""
# any(iter) fonksiyonu ise en az bir deger True ise True degilse False dondurur.
"""
liste = [0,1,2,3,0,False,""]
print(any(liste))

liste = [False,0,"",None]
print(any(liste))

liste = [1,"",3,"Mert",False]
print(any(liste))
"""

# json --> genelde dictionary objelerini saklamada kullanılan dosya turu
"""
import json

veriler = {
"kullanicilar":[
    {
    "ad":"alperen",
    "sifre":123
    },
    {
    "ad":"rover",
    "sifre":321
    }
]
}
print(veriler)
with open("veriler.json","w") as dosya:
    json.dump(veriler,dosya)

with open("veriler.json","r") as dosya:
    okunanlar = json.load(dosya)
print(okunanlar)
"""
# example_16

# string functions
"""
string = "CYV  ASCCI   V2zx c  kSDf 73q7 8czc-cas  dc"
print(string)
print(string.upper())
print(string.lower())
# "...".strip("...") girdigin karakterlerden stringin icinde sagdan ve soldan olanlari siler olmayan denk gelirse ilerlemez
print(string.strip("Cc"))
# "...".replace(old,new,how_many)
print(string.replace("ASCCI","HEy"))
# "...".startswith(string or tupple) sameway .endswith()
print(string.startswith(("C","cc","ASD")))
print(string.endswith(("C","cc","ASD")))
print(string.split("  "))
print(string.find("V",4,15))
print(string.count("C"))
print("*".join(string.split()))
"""

# set kume
"""
kume = {"ali","veli","ali","ayse"}
print(type(kume))
print(kume)
# set(iterable object)
print(set("ali veli ali ayse"))
kume.add("alp")
print(kume)
kume.discard("ali")
print(kume)
kume2 = {"ali","veli","ali","ayse"}
# kume fark kume2
print(kume.difference(kume2))
print(kume - kume2)
# farki kumeye atama
kume.difference_update(kume2)
print(kume,kume2)
A = {1,2,3,4,5}
B = {3,4,5,6,7}
print(A.intersection(B)) # A kesisim B
print(A & B)
print(A.isdisjoint(B))  # ayrik kume mi
print(A.issubset(B))    # A B nin alt kumesi mi
print(A.union(B))       # birlesim
print(A | B)
print(A ^ B) # (A U B) - (A kesisim B)
"""

# SQLite veri tabani
# SQL commands
"""
import sqlite3

with sqlite3.connect("veriTabani.db") as baglanti:

    imlec = baglanti.cursor()

    # imlec.execute("CREATE TABLE IF NOT EXISTS ekip(isim TEXT, yas INT, cinsiyet TEXT)")
    #
    # imlec.execute("INSERT INTO ekip VALUES('kerim',27,'erkek')")
    # imlec.execute("INSERT INTO ekip VALUES('sue',34,'kadin')")
    # imlec.execute("INSERT INTO ekip VALUES('ali',0,'erkek')")

    #imlec.execute("UPDATE ekip SET yas = 11 WHERE isim = 'ali'")

    imlec.execute("SELECT * FROM ekip")
    #imlec.execute("SELECT isim,yas FROM ekip")
    #imlec.execute("SELECT * FROM ekip WHERE yas<20")

    #imlec.execute("DELETE FROM ekip WHERE isim='ali'")

    for veri in imlec.fetchall():
        print(veri)
    baglanti.commit()
print("bitti")
"""
# example_17

# Decorator
# her sey obje fonksiyonlarda dahil bu yuzden fonksiyonlara parametre olarak baska bir fonksiyon gonderilebilir.
"""
def kareal(sayi):
    return sayi**2
def fonksiyonugoster(kareal, sayi):
    print(kareal)
    print(fonksiyonugoster)
    print(kareal(sayi))
sayi = int(input("sayi : "))
fonksiyonugoster(kareal, sayi)

def MAP(fonk, iter):
    liste = []
    for i in iter:
        liste.append(fonk(i))
    return liste

print(MAP(kareal, [1,2,3,4,5,6]))

def a(fonk):
    print("a calisti")
    def b():
        print("b calisti")
        fonk()
    return b
def yazi():
    print("aaaaa")
def yazi2():
    print("bbbbb")
c = a(yazi)
print(c)
print("******")
c()
print("////////")
d = a(yazi2)
print(d)
print("*****")
d()

def f1(func):
    def g():
        print("STARTED")
        func()
        print("ENDED")
    return g

@f1
def f2():
    print("in f2")

f2()


import time

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print("function took :", time.time() - before, "seconds")
    return wrapper

@timer
def fonksiyon():
    sum = 0
    for i in range(100):
        sum += i
    print(sum)

fonksiyon()
"""
# example_18

# os library some functions
"""
import os
liste = os.listdir()
print(liste)
#os.remove(file)
"""

# iterable --> tekrarlanabilir
# buraya yazmadim ama iterable objeler classlar uzerinden obje uretildigini basitce gosteren objelerdir
# ayni sekilde list, tuple, set ... de classlar uzerinden uretilen objelerdir
"""
list = [x for x in range(15)]
iterasyon = iter(list)
while True:
    try:
        print(next(iterasyon))
    except StopIteration:
        break
"""

# example_19

# Generator -> C deki dinamik hafiza kullanimi ile benzer mantıga dayaniyor
"""
def sayi_arttir():
    a = 1
    yield a
    a += 1
    yield a
    a += 1
    yield a

print(sayi_arttir())

for i in sayi_arttir():
    print(i)
# her girdiginde kaldigi yerden (yield) devam ediyor
f = sayi_arttir()
while True:
    try:
        print(next(f))
    except StopIteration:
        break
"""