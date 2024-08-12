#Savaş arenası oyunu
#Oyuncuların karakterleri savaşarak birbirlerini yok etmeye çalıştığı bir oyundur.
#Karakterlerin savaşırken kullandığı silahlar ve canları vardır.
#Karakterlerin ikisinin canı bittiğinde oyun sona erer.
#Karakterlerin silahları ve vuruş önceliği taş kağıt makas oyunuyla belirlenir.
#Oyuncular taş kağıt makas oyunu oynayarak karakterleri belirler.
#Karakterlerin var sayılan silahları vardır.
#4 karakter vardır ve bunlar dev, buyucu, şovalye, ejderhadır.
import random

dev = random.randint(100, 125)
buyucu = random.randint(50, 75)
sovalye = random.randint(75, 100)
ejderha = random.randint(125, 150)
kazanan = 0

tas_kagit_makas = ["Taş", "Kağıt", "Makas"]
mevcut_karakterler = ["Dev", "buyucu", "Şovalye", "Ejderha"]
i = 1
while(i):
    print("Taş kağıt makas oyunu oynayarak karakterinizi seçin.\n")
    bilgisayar_secimi_oyun = random.choice(tas_kagit_makas)
    
    print("\n Oyunu Sonlandırmak için 'q' tuşuna basınız.\n")
        
 
    secim_oyun = input("Taş kağıt makas oyununu oynamak için 'Taş', 'Kağıt' veya 'Makas'dan 1'ini seçiniz:")    
    while(kazanan==0):#taş kağıt makas oyunu 
        print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
        if secim_oyun == "Taş":
            if bilgisayar_secimi_oyun == "Taş":
                print("Berabere \n şimdi tekrar seçiniz.")
                secim_oyun = input()
                break
            elif bilgisayar_secimi_oyun == "Kağıt":
                print("Kaybettiniz \n şimdi bilgisayarın karakterini seçiyor.")
                kazanan = -1
                break
            elif bilgisayar_secimi_oyun == "Makas":
                print("Kazandınız \n şimdi karakterinizi seçebilirsiniz.")
                kazanan = 1
                break   
        elif secim_oyun == "Kağıt":
            if bilgisayar_secimi_oyun == "Taş":
                print("Kazandınız \n şimdi karakterinizi seçebilirsiniz.")
                kazanan = 1
                break
            elif bilgisayar_secimi_oyun == "Kağıt":
                print("Berabere \n şimdi tekrar seçiniz.")
                secim_oyun = input()
            elif bilgisayar_secimi_oyun == "Makas":
                print("Kaybettiniz \n şimdi bilgisayarın karakterini seçiyor.")
                kazanan = -1
                break
        elif secim_oyun == "Makas":
            if bilgisayar_secimi_oyun == "Taş":
                print("Kaybettiniz \n şimdi bilgisayarın karakterini seçiyor.")
                kazanan = -1
                break
            elif bilgisayar_secimi_oyun == "Kağıt":
                print("Kazandınız \n şimdi karakterinizi seçebilirsiniz.")
                kazanan = 1
                break
            elif bilgisayar_secimi_oyun == "Makas":
                print("Berabere \n şimdi tekrar seçiniz.")
                secim_oyun = input()
        else:
            secim_oyun == "q"
            i = 0
            break
    print("Mevcut karakterler\n")
    for karakter in mevcut_karakterler:
        print(karakter)
    if(kazanan==1):
        print("Karakterinizi seçiniz.")
        karakter_secimi = input()
        if karakter_secimi == "Dev":
            bilgisayar_secimi_oyun = random.choice(mevcut_karakterler)
            print("Dev karakteri seçildi.")
            print("Dev karakterinin canı: ", dev)
            print("Dev karakterinin silahları: ", "Demir Yumruk", "Balta", "Balyoz")
        elif karakter_secimi == "Büyücü":
            bilgisayar_secimi_oyun = random.choice(mevcut_karakterler)
            print("buyucu karakteri seçildi.")
            print("buyucu karakterinin canı: ", buyucu)
            print("buyucu karakterinin silahları: ", "Ateş küre", "Can içeçeği", "Buz oku")
        elif karakter_secimi == "Şovalye":
            bilgisayar_secimi_oyun = random.choice(mevcut_karakterler)
            print("Şovalye karakteri seçildi.")
            print("Şovalye karakterinin canı: ", sovalye)
            print("Şovalye karakterinin silahları: ", "Kralın Kılıçı", "Topuz", "Kalkan")
        elif karakter_secimi == "Ejderha":
            bilgisayar_secimi_oyun = dev
            print("Ejderha karakteri seçildi.")
            print("Ejderha karakterinin canı: ", ejderha)
            print("Ejderha karakterinin silahları: ", "Ateş baskını", "Rüzgar", "Işın gözler")
        
    