from random import randint
from json import dumps, loads


def dosya_okuma():
    # veri tabani var mi diye kontrol edilmiyor var oldugu biliniyor.
    # bu fonksiyonda veri tabanindaki bilgiler okuyor ve donduruluyor.
    # kodun ilk basinda cagiriliyor.
    try:
        fp = open("veriler.json", "r")
        data = loads(fp.readline())
    except:
        fp = open("veriler.json", "w")
        data = []
    # try-except in amaci eger veriler dosyasi yoksa olusturmaktir.
    fp.close()
    return data


def ekleme():
    # hesap olusturulur. Kart numarasi verilir.
    ekran_temizleme()
    print("\nBankamizi tercih ettiginiz icin tesekkur ederiz.")
    print("Yeni hesap icin istenilen bilgileri giriniz lutfen.")
    yeni_dict = {
        "isim": "isim1",
        "soyad": "soyad1",
        "kartNo": 0,
        "sifre": "sifre1",
        "paraMiktari": 0
    }

    # yeni kartNo olusturma
    yeni_kartNo = randint(100, 999)
    while yeni_kartNo in kartNolar:
        yeni_kartNo = randint(100, 999)
    kartNolar.append(yeni_kartNo)

    # bilgileri alma
    yeni_dict["isim"] = input("Isminizi giriniz : ")
    yeni_dict["soyad"] = input("Soyadinizi giriniz : ")
    yeni_dict["sifre"] = input("Sifre olusturunuz : ")
    yeni_dict["kartNo"] = yeni_kartNo
    print("Kart numaraniz (unutmayin): ", yeni_kartNo)
    input("\nGecmek icin entera basiniz.")
    print("Guvenlik acisindan olusturdugunuz sifreyi girmeniz gerekmektedir.")
    data.append(yeni_dict)
    return yeni_kartNo


def guncelleme():
    # istenilen bilginin guncellenmesi
    # once dict i aramamiz lazim
    ekran_temizleme()
    guncellecek_dict = arama(kartNo)
    print("Hesap bilgilerinizden isim, soyad veya sifreyi guncelleyebilirsiniz.")
    tur = int(input("Hesap bilgilerinizden kac tanesini guncellemek istiyorsunuz : "))
    for i in range(tur):
        key = input("isim, soyad, sifre ... bu ucunden guncellemek istediginizi yaziniz : ")
        value = input("Yeni {} : ".format(key))
        guncellecek_dict[key] = value


def silme():
    i = 0
    cik = 0
    for dict in data:
        for key, value in dict.items():
            if key == "kartNo" and value == kartNo:
                data.pop(i)
                cik = 1
                break
        if cik:
            break
        i += 1


def arama(fkartNo):
    for dict in data:
        for key, value in dict.items():
            if key == "kartNo" and value == fkartNo:
                return dict


def yazdirma():
    # kartNo ya gore arayip buldugumuz kisinin dictionary sini yazdiracak.
    dict = arama(kartNo)
    for key, value in dict.items():
            print("{} : {}".format(key, value))
    input("gecmek icin entera basiniz.")


def dosya_yazma():
    # bu fonksiyon kodun sonunda cagirilir ve verilerin son hali json dosyasina kaydedilir.
    fp = open("veriler.json", "w")
    fp.writelines(dumps(data))
    fp.close()


def ekran_temizleme():
    print("\n"*40)


def giris():
    # kullanici hesap numarasi giris yapar

    print("\t\t***\tBANKAMATIK\t***\n")
    fkartNo = int(input("3 rakamli kart numaranizi giriniz. (Yeni hesap acmak icin 000 giriniz): "))
    while fkartNo not in kartNolar and fkartNo != 0:
        print("Girdiginiz kart numarasi bankamizda bulunmamaktadir. Tekrar giriniz.")
        fkartNo = int(input("3 rakamli kart numaranizi giriniz. (Yeni hesap acmak icin 000 giriniz): "))

    if fkartNo == 0:
        fkartNo = ekleme()

    return fkartNo


def sifre_alma():
    # sifre kontrolu
    dict = arama(kartNo)
    sifre = input("Sifre : ")
    i = 0
    while sifre != dict["sifre"]:
        i += 1
        if i == 3:
            print("3 kez yanlis sifre girdiniz. Eger sifrenizi unutmus iseniz en yakin banka subemize gidiniz.")
            exit(1)
        else:
            sifre = input("Yanlis sifre girdiniz. Tekrar deneyiniz : ")


def para_cekme():
    dict = arama(kartNo)
    print("Mevcut paraniz :", dict["paraMiktari"], "TL")
    cekilecek = int(input("Cekmek istediginiz para miktarini giriniz : "))
    while dict["paraMiktari"] < cekilecek:
        print("Hesabinizda {} TL para bulunmamaktadir.".format(cekilecek))
        cekilecek = int(input("Cekmek istediginiz para miktarini giriniz : "))
    dict["paraMiktari"] -= cekilecek


def para_yukleme():
    dict = arama(kartNo)
    print("Mevcut paraniz :", dict["paraMiktari"], "TL")
    eklenecek = int(input("Yukleyeceginiz para miktarini giriniz : "))
    dict["paraMiktari"] += eklenecek


def havale(fkartNo):
    kartNo2 = int(input("Havale yapilacak kart numarasi giriniz : "))
    while kartNo2 not in kartNolar:
        print("Bankamizda {} kart numarali bir hesap bulunmamaktadir.".format(kartNo2))
        kartNo2 = int(input("Havale yapilacak kart numarasini tekrar giriniz : "))

    # lazim bilgileri aliyoruz.
    dict1 = arama(fkartNo)
    dict2 = arama(kartNo2)

    para = int(input("Gonderilecek para miktarini giriniz : "))
    while para > dict1["paraMiktari"]:
        print("Hesabinizda {} TL para bulunmamaktadir. Mevcut bakiyeniz {} TL'dir.".format(para, dict1["paraMiktari"]))
        para = int(input("Gonderilecek para miktarini giriniz : "))

    # islemler
    dict1["paraMiktari"] -= para
    dict2["paraMiktari"] += para


def menu():
    # bankamatikten cikilina kadar menu fonksiyonunda donulur.
    # menu fonksiyonu oteki fonksiyonlari cagirir.
    # secilen islemlere gore hareket eder.

    def menu_yazdirma():
        ekran_temizleme()
        # Kullaniciya bir menu secegeni sunar
        print("\t\t***\tBANKAMATIK\t***")
        print("\n\tHOSGELDINIZ ISLEMINIZI SECINIZ")
        print("\n1) Hesap bilgisi sorgulama")
        print("2) Hesap bilgisi degistirme")
        print("3) Hesap silme")
        print("4) Para yatirma")
        print("5) Para cekme")
        print("6) Havale islemi")
        print("7) Cikis")

    menu_yazdirma()
    secim = input("\nIslem : ")
    # secilen isleme gore fonksiyonlara gonderme
    if secim == '1':
        yazdirma()
        menu()
    elif secim == '2':
        guncelleme()
        menu()
    elif secim == '3':
        silme()
        print("Hesabiniz silinmistir.")
    elif secim == '4':
        para_yukleme()
        menu()
    elif secim == '5':
        para_cekme()
        menu()
    elif secim == '6':
        havale(kartNo)
        menu()

# data dictionary dizisi olacak
data = dosya_okuma()

# kartNo lari id gibi kullanıcaz o yuzden kod boyu lazim olacaktir. dizide tutucaz degeerleri
kartNolar = []
for dict in data:
    for key, value in dict.items():
        if key == "kartNo":
            kartNolar.append(value)

kartNo = giris()
sifre_alma()
menu()
dosya_yazma()
print("\n\n\t\tIYI GUNLER")


# ornek data
# data = [
#     {
#         "isim": "isim1",
#         "soyad": "soyad1",
#         "kartNo": 123,
#         "sifre": "sifre1",
#         "paraMiktari": 3000
#     },
#     {
#         "isim": "isim2",
#         "soyad": "soyad1",
#         "kartNo": 234,
#         "sifre": "sifre2",
#         "paraMiktari": 4600
#     }
# ]