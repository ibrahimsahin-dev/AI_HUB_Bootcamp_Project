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
    
    
    print("\n Oyunu Sonlandırmak için 'q' tuşuna basınız.\n")
        
 
    secim_oyun = input("Taş kağıt makas oyununu oynamak için 'Taş', 'Kağıt' veya 'Makas'dan 1'ini seçiniz:")    
    while(kazanan==0):#taş kağıt makas oyunu 
        if secim_oyun == "Taş":
            bilgisayar_secimi_oyun = random.choice(tas_kagit_makas)
            if bilgisayar_secimi_oyun == "Taş":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
                print("Berabere \n şimdi tekrar seçiniz.")
                secim_oyun = input()
                
            elif bilgisayar_secimi_oyun == "Kağıt":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
                print("Kaybettiniz \n şimdi bilgisayarın karakterini seçiyor.")
                kazanan = -1
                break
            elif bilgisayar_secimi_oyun == "Makas":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
                print("Kazandınız \n şimdi karakterinizi seçebilirsiniz.")
                kazanan = 1
                break   
        elif secim_oyun == "Kağıt":
            bilgisayar_secimi_oyun = random.choice(tas_kagit_makas)
            if bilgisayar_secimi_oyun == "Taş":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
                print("Kazandınız \n şimdi karakterinizi seçebilirsiniz.")
                kazanan = 1
                break
            elif bilgisayar_secimi_oyun == "Kağıt":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
                print("Berabere \n şimdi tekrar seçiniz.")
                secim_oyun = input()
            elif bilgisayar_secimi_oyun == "Makas":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
                print("Kaybettiniz \n şimdi bilgisayarın karakterini seçiyor.")
                kazanan = -1
                break
        elif secim_oyun == "Makas":
            bilgisayar_secimi_oyun = random.choice(tas_kagit_makas)
            if bilgisayar_secimi_oyun == "Taş":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
                print("Kaybettiniz \n şimdi bilgisayarın karakterini seçiyor.")
                kazanan = -1
                break
            elif bilgisayar_secimi_oyun == "Kağıt":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
                print("Kazandınız \n şimdi karakterinizi seçebilirsiniz.")
                kazanan = 1
                break
            elif bilgisayar_secimi_oyun == "Makas":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
                print("Berabere \n şimdi tekrar seçiniz.")
                secim_oyun = input()
        elif secim_oyun == "q":
            i = 0
            break
        else:
            print("Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.")
            secim_oyun = input()
    
    
    
    
    
    if(i==0):
        break
        
    print("Mevcut karakterler\n")
    for karakter in mevcut_karakterler:
        print(karakter)
    
    while (kazanan==1):
        print("Karakterinizi seçiniz.")
        karakter_secimi = input()
        if karakter_secimi == "Dev":
            mevcut_karakterler.remove("Dev")
            bilgisayar_secimi_oyun = random.choice(mevcut_karakterler)
            print("Dev karakteri seçildi.")
            print("Dev karakterinin canı: ", dev)
            print("Dev karakterinin silahları: ", "Demir Yumruk", "Balta", "Balyoz")
            print("Bilgisayarının karakteri: ", bilgisayar_secimi_oyun)
            kazanan=3
        elif karakter_secimi == "Büyücü":
            mevcut_karakterler.remove("buyucu")
            bilgisayar_secimi_oyun = random.choice(mevcut_karakterler)
            print("buyucu karakteri seçildi.")
            print("buyucu karakterinin canı: ", buyucu)
            print("buyucu karakterinin silahları: ", "Ateş küre", "Can içeçeği", "Buz oku")
            print("Bilgisayarının karakteri: ", bilgisayar_secimi_oyun)
            kazanan=3
        elif karakter_secimi == "Şovalye":
            mevcut_karakterler.remove("Şovalye")
            bilgisayar_secimi_oyun = random.choice(mevcut_karakterler)
            print("Şovalye karakteri seçildi.")
            print("Şovalye karakterinin canı: ", sovalye)
            print("Şovalye karakterinin silahları: ", "Kralın Kılıçı", "Topuz", "Kalkan")
            print("Bilgisayarının karakteri: ", bilgisayar_secimi_oyun)
            kazanan=3

        elif karakter_secimi == "Ejderha":
            mevcut_karakterler.remove("Ejderha")
            bilgisayar_secimi_oyun = dev
            print("Ejderha karakteri seçildi.")
            print("Ejderha karakterinin canı: ", ejderha)
            print("Ejderha karakterinin silahları: ", "Ateş baskını", "Rüzgar", "Işın gözler")
            print("Bilgisayarının karakteri: ", bilgisayar_secimi_oyun)
            kazanan=3
        else:
            print("Hatalı giriş yaptınız.")
            karakter_secimi = input()
            kazanan=1

    
    while (kazanan==-1):
        print("\n\n\nBilgisayarın karakteri seçiliyor.")
        bilgisayar_secimi_oyun = random.choice(mevcut_karakterler)
        print("Bilgisayarın karakteri seçildi.")
        if(bilgisayar_secimi_oyun=="Dev"):
            print("Dev karakteri seçildi.")
            print("Dev karakterinin silahları: ", "Demir Yumruk", "Balta", "Balyoz")
            print("Bilgisayarının karakterinin canı: ", dev)
        elif(bilgisayar_secimi_oyun=="buyucu"):
            print("buyucu karakteri seçildi.")
            print("buyucu karakterinin silahları: ", "Ateş küre", "Can içeçeği", "Buz oku")
            print("Bilgisayarının karakterinin canı: ", buyucu)
        elif(bilgisayar_secimi_oyun=="Şovalye"):
            print("Şovalye karakteri seçildi.")
            print("Şovalye karakterinin silahları: ", "Kralın Kılıçı", "Topuz", "Kalkan")
            print("Bilgisayarının karakterinin canı: ", sovalye)
        elif(bilgisayar_secimi_oyun=="Ejderha"):
            print("Ejderha karakteri seçildi.")
            print("Ejderha karakterinin silahları: ", "Ateş baskını", "Rüzgar", "Işın gözler")
            print("Bilgisayarının karakterinin canı: ", ejderha)
        
        mevcut_karakterler.remove(bilgisayar_secimi_oyun)
        print("Mevcut karakterler\n")
        for karakter in mevcut_karakterler:
            print(karakter)
        print("Karakterinizi seçiniz.")
        karakter_secimi = input()
        while(karakter_secimi not in mevcut_karakterler):
    
            if karakter_secimi == "Dev":
                print("Dev karakteri seçildi.")
                print("Dev karakterinin canı: ", dev)
                print("Dev karakterinin silahları: ", "Demir Yumruk", "Balta", "Balyoz")
            elif karakter_secimi == "buyucu":
                print("buyucu karakteri seçildi.")
                print("buyucu karakterinin canı: ", buyucu)
                print("buyucu karakterinin silahları: ", "Ateş küre", "Can içeçeği", "Buz oku")
            elif karakter_secimi == "Şovalye":
                print("Şovalye karakteri seçildi.")
                print("Şovalye karakterinin canı: ", sovalye)
                print("Şovalye karakterinin silahları: ", "Kralın Kılıçı", "Topuz", "Kalkan")
            elif karakter_secimi == "Ejderha":
                print("Ejderha karakteri seçildi.")
                print("Ejderha karakterinin canı: ", ejderha)
                print("Ejderha karakterinin silahları: ", "Ateş baskını", "Rüzgar", "Işın gözler")
            else:
                print("Hatalı giriş yaptınız.")
                karakter_secimi = input()
    print("\n\n\n\n ############# Savaş başlıyor ############# \n")

    takip=0
    while(dev>0 and buyucu>0 and sovalye>0 and ejderha>0):
        print("İlk vuruş için taş kağıt makas oyunu oynayınız.")
        secim_oyun = input(" 'Taş', 'Kağıt' veya 'Makas'tan 1'ini seçiniz veya çıkmak için q ye basınız:")    
        while(takip==0):#taş kağıt makas oyunu 
            if secim_oyun == "Taş":
                bilgisayar_secimi_oyun = random.choice(tas_kagit_makas)
                if bilgisayar_secimi_oyun == "Taş":
                    print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
                    print("Berabere \n şimdi tekrar seçiniz.")
                    secim_oyun = input()
                    
                elif bilgisayar_secimi_oyun == "Kağıt":
                    print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
                    print("Kaybettiniz Bilgisayarınız atak yapıyor.")
                    takip = -1
                    break
                elif bilgisayar_secimi_oyun == "Makas":
                    print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
                    print("Kazandınız şimdi atak yapabilirsiniz.")
                    takip = 1
                    break   
            elif secim_oyun == "Kağıt":
                bilgisayar_secimi_oyun = random.choice(tas_kagit_makas)
                if bilgisayar_secimi_oyun == "Taş":
                    print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
                    print("Kazandınız şimdi atak yapabilirsiniz.")
                    takip = 1
                    break  
                elif bilgisayar_secimi_oyun == "Kağıt":
                    print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
                    print("Berabere \n şimdi tekrar seçiniz.")
                    secim_oyun = input()
                elif bilgisayar_secimi_oyun == "Makas":
                    print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
                    print("Kaybettiniz Bilgisayarınız atak yapıyor.")
                    takip = -1
                    break
            elif secim_oyun == "Makas":
                bilgisayar_secimi_oyun = random.choice(tas_kagit_makas)
                if bilgisayar_secimi_oyun == "Taş":
                    print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
                    print("Kaybettiniz Bilgisayarınız atak yapıyor.")
                    takip = -1
                    break
                elif bilgisayar_secimi_oyun == "Kağıt":
                    print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
                    print("Kazandınız şimdi atak yapabilirsiniz.")
                    takip = 1
                    break  
                elif bilgisayar_secimi_oyun == "Makas":
                    print("Bilgisayarın seçimi: ", bilgisayar_secimi_oyun)
                    print("Berabere \n şimdi tekrar seçiniz.")
                    secim_oyun = input()
            elif secim_oyun == "q":
                i = 0
                break
            else:
                print("Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.")
                secim_oyun = input()
        
        if(i==0):
            break

    
        
    