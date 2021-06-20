from random import randint


def harita_olustur(kenar):
    # matris yapisi     [[mayin olma durumu, karakter ile gosterimi]]
    harita = []
    for i in range(kenar):
        sutun = []
        for j in range(kenar):
            sutun.append([False, "?"])
        harita.append(sutun)
    return harita


def mayinlari_ekle(harita, kenar, mayin_sayisi):
    print("Oyundaki Mayin Sayisi : ", mayin_sayisi)
    for i in range(mayin_sayisi):
        x = randint(0, kenar-1)
        y = randint(0, kenar-1)
        harita[x][y][0] = True


def hamle_al(kenar, harita, mod):
    satir = int(input("\nLutfen satir numarasi giriniz : "))
    sutun = int(input("Lutfen sutun numarasi giriniz : "))
    if mod == 1:
        if sutun > kenar or satir > kenar or sutun <= 0 or satir <= 0 or harita[satir-1][sutun-1][1] != "?":
            print("O koordinatlari secemezsiniz. Tekrar seciniz.")
            return hamle_al(kenar, harita, mod)
    else:
        if sutun > kenar or satir > kenar or sutun <= 0 or satir <= 0 or "*" in harita[satir-1][sutun-1][1]:
            print("O koordinatlari secemezsiniz. Tekrar seciniz.")
            return hamle_al(kenar, harita, mod)
    return satir, sutun


def hamle_oyna(sutun, satir, harita, kenar, mod):
    # oynanacak hamle mayina mi denk geliyor ?
    if harita[satir][sutun][0]:
    	# acik_mod fonksiyonundan ilk defa mi geliyor buraya
        if mod == 2 and harita[satir][sutun][1] != "X":
            harita[satir][sutun][1] = "X"
            return
        else:
            if mod == 1:
                oyun_bitti(harita, kenar+1)
            print("Maalesef kaybettiniz.")
            exit(1)
    index = 0
    # mayinsayda bakilacak indexler listesi, duruma gore gerekli olan kullaniliyor
    # [sol ust kose, sag ust kose, sol alt kose, sag alt kose, ust kenar, sag kenar, alt kenar, sol kenar, ortalar]
    bakilacak = [
        [(1, 0), (0, 1), (1, 1)],
        [(1, 0), (0, -1), (1, -1)],
        [(-1, 0), (0, 1), (-1, 1)],
        [(-1, 0), (0, -1), (-1, -1)],
        [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1)],
        [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0)],
        [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)],
        [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0)],
        [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    ]
    if satir == 0 and sutun == 0:
        index = 0
    elif satir == 0 and sutun == kenar:
        index = 1
    elif satir == kenar and sutun == 0:
        index = 2
    elif satir == kenar and sutun == kenar:
        index = 3
    elif satir == 0:
        index = 4
    elif sutun == kenar:
        index = 5
    elif satir == kenar:
        index = 6
    elif sutun == 0:
        index = 7
    else:
        index = 8
    count = mayin_say(bakilacak[index], satir, sutun, harita)
    if mod == 1:
        harita[satir][sutun][1] = str(count)
    else:
        if harita[satir][sutun][1] == "?":
            harita[satir][sutun][1] = str(count)
        else:
            harita[satir][sutun][1] = "*"+harita[satir][sutun][1]


def mayin_say(dizi, satir, sutun, harita):
    count = 0
    for x, y in dizi:
        if harita[satir+x][sutun+y][0]:
            count += 1
    return count


def yazdir(harita, kenar):
    print("\n****************************************\n\n     ", end="")
    for i in range(kenar):
        if i<10:
            print(" ", end="")
        print(i+1, end="   ")
    sayac = 1
    print()
    for i in range(kenar+1):
        print("-----", end="")
    print()
    for i in harita:
        if sayac<10:
            print(" ", end="")
        print(sayac, end=" |  ")
        sayac += 1
        for j in i:
            if "*" not in j[1]:
                print(" ", end="")
            print(j[1], end="   ")
        print()


def acik_mod(harita, kenar):
    for i in range(kenar):
        for j in range(kenar):
            hamle_oyna(i, j, harita, kenar-1, mod)


def oyun_bitti(harita, kenar):
    for i in range(kenar):
        for j in range(kenar):
            if harita[i][j][0]:
                harita[i][j][1] = "X"
    yazdir(harita, kenar+1)


# oyun modu secilir
mod = 0
while mod > 2 or mod < 1:
    mod = int(input("Gizli mod icin 1 , acik mod icin 2 giriniz : "))

# haritanin boyu alinir
kenar = 3
first = False
while kenar < 10:
    if first:
        print("9'dan buyuk deger girmeniz gerekiyor! Tekrar giriniz.")
    first = True
    kenar = int(input("Boyut giriniz (en az 10) : "))

# harita olusturulur
matris = harita_olustur(kenar)
# mayin sayisi hesaplanir
mayin_sayisi = int(kenar*kenar*0.3)
# mayin sayisi kadar rastgele mayin eklenmesi icin fonksiyona gonderilir
mayinlari_ekle(matris, kenar, mayin_sayisi)

# acik mod istenmis ise harita guncellenir
if mod == 2:
    acik_mod(matris, kenar)
# outputa harita yazdirilir
yazdir(matris, kenar)
i=0
# oyun max toplam alan - mayin sayisi kadar oynanabilir.
tur = kenar*kenar - mayin_sayisi
# mayinsiz alan kalmayana kadar dongude donulur
while i<tur:
    i+=1
    # kullanicidan hamle alinir
    satir, sutun = hamle_al(kenar, matris, mod)
    # alinan hamle oynanir
    hamle_oyna(sutun-1, satir-1, matris, kenar-1, mod)
    # hamle_oyna'da guncellenen matris ekrana yazdirilir
    yazdir(matris, kenar)
# oyun bittiginde mayinli harita ekrana yazdirilir
oyun_bitti(matris, kenar)
# kazanma mesaji
print("Tebrikler Kazandiniz.")
