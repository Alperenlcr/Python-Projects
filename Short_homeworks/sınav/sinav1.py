from random import randrange
def matris_olustur(n):
    matris = []
    for i in range(n):
        satir = []
        for j in range(n):
            satir.append(chr(randrange(65,65+26)))
        matris.append(satir)
    return matris


def arama(matris, kelime, boyut, amac):
    say = 0
    indexler = []
    satir_index = 0
    sutun_index = 0
    # satir stringler
    for satir in matris:
        string = "".join(satir)
        say += string.count(kelime)
        bas = 0
        for i in range(len(string)):
            if string[bas:].find(kelime) == i:
                indexler.append(([satir_index, i], [satir_index, i + len(kelime)-1]))
                bas += i+1            
        satir_index += 1

    # sutun stringler
    for j in range(len(matris[0])):
        string = ""
        for i in range(len(matris)):
            string += matris[i][j]
        say += string.count(kelime)
        for i in range(len(string)):
            if string[bas:].find(kelime) == i:
                indexler.append(([i, sutun_index], [i + len(kelime)-1, sutun_index]))
                bas += i+1            
        sutun_index += 1


    if say == 0:
            if amac:
                print("Adet : 0 , en yakin kelime : ", arama(matris, kelime[:-1], boyut, 0))
            else:
                return arama(matris, kelime[:-1], boyut, 0)
    elif amac == 0:
        return kelime
    else:
        print(indexler)
        print("Adet :", say)
        print("Konum : ", end="")
        for l in indexler:
            print(l[0], "-", l[1], end=" , ")
    

boyut = int(input("Matris boyutu : "))
matris = matris_olustur(boyut)
for i in matris:
    for j in i:
        print(j, end=" ")
    print()
kelime = input("Aranacak kelimeyi giriniz : ")
arama(matris, kelime, boyut, 1)