f = open("log.txt", "w")
komut_satiri = "baslangic"
son = 0
while komut_satiri != "exit":
    komut_satiri = input("-> ")
    islemler = komut_satiri.split()

    if '*' in islemler:
        islemler[islemler.index('*')] = str(son)
        #komut_satiri[komut_satiri.find("*")] = str(son)
    f.write(komut_satiri+"\n")
    if islemler[0] == "topla":
        if len(islemler) < 2:
            print("Yetersiz parametre")
        else:
            sum = 0
            for i in islemler[1:]:
                f.write(i+" +")
                sum += int(i)
            f.write(" = "+str(sum)+"\n")
            print(sum)
            son = sum
    elif islemler[0] == "cikar":
        if len(islemler) != 3:
            print("Uygun olmayan parametre")
        else:
            sonuc = int(islemler[1]) - int(islemler[2])
            f.write("{} - {} = {}\n".format(islemler[1], islemler[2], sonuc))
            print(sonuc)
            son = sonuc

    elif islemler[0] == "carp":
        if len(islemler) < 2:
            print("Yetersiz parametre")
        else:
            sonuc = 1
            for i in islemler[1:]:
                f.write(i + " *")
                sonuc *= int(i)
            f.write(" = " + str(sonuc) + "\n")
            print(sonuc)
            son = sonuc

    elif islemler[0] == "bol":
        if len(islemler) != 3:
            print("Uygun olmayan parametre")
        else:
            if islemler[1] == "0":
                print("0 a bolme hatasi")
            else:
                sonuc = int(islemler[1]) / int(islemler[2])
                f.write("{} / {} = {}\n".format(islemler[1], islemler[2], int(sonuc)))
                print(int(sonuc))
                son = sonuc

    elif islemler[0] == "kareal":
        if len(islemler) != 2:
            print("Uygun olmayan parametre")
        else:
            sonuc = int(islemler[1]) ** 2
            f.write("{} ^ 2 = {}\n".format(islemler[1], int(sonuc)))
            print(int(sonuc))
            son = sonuc

f.close()
