#Savaş arenası oyunu
#Oyuncuların karakterleri savaşarak birbirlerini yok etmeye çalıştığı bir oyundur.
#Karakterlerin savaşırken kullandığı silahlar ve canları vardır.
#Karakterlerin ikisinin canı bittiğinde oyun sona erer.
#Karakterlerin silahları ve vuruş önceliği taş kağıt makas oyunuyla belirlenir.
#Oyuncular taş kağıt makas oyunu oynayarak karakterleri belirler.
#Karakterlerin var sayılan silahları vardır.
#4 karakter vardır ve bunlar dev, buyucu, şovalye, ejderhadır.
import random


def karakter_secimi_fonksiyonu(karakter_ismi, karakter_cani):
    if(karakter_ismi=="Dev"):
        karakter_cani = random.randint(100, 125)
    elif(karakter_ismi=="buyucu"):
        karakter_cani = random.randint(50, 75)
    elif(karakter_ismi=="Şovalye"):
        karakter_cani = random.randint(75, 100)
    elif(karakter_ismi=="Ejderha"):
        karakter_cani = random.randint(125, 150)
    return karakter_cani

def atak(silah_ismi):
    if(silah_ismi=="Demir yumruk"):
        return Demir_yumruk
    elif(silah_ismi=="Balta"):
        return Balta
    elif(silah_ismi=="Balyoz"):
        return Balyoz
    elif(silah_ismi=="Ates kure"):
        return Ates_kure
    elif(silah_ismi=="Can icecegi"):
        return Can_icecegi
    elif(silah_ismi=="Buz oku"):
        return Buz_oku
    elif(silah_ismi=="Kralin kilici"):
        return Kralin_kilici
    elif(silah_ismi=="Topuz"):
        return Topuz
    elif(silah_ismi=="Kalkan"):
        return Kalkan
    elif(silah_ismi=="Ates baskini"):
        return Ates_baskini
    elif(silah_ismi=="Ruzgar"):
        return Ruzgar
    elif(silah_ismi=="Isın gozler"):
        return Isın_gozler






dev=0
buyucu=0
sovalye=0
ejderha=0

kazanan = 0
#Silahlar
Demir_yumruk = random.randint(10, 15)
Balta = random.randint(15, 20)
Balyoz = random.randint(20, 25)
Ates_kure = random.randint(25, 40)
Can_icecegi = random.randint(20, 40)
Buz_oku = random.randint(20, 25)
Kralin_kilici = random.randint(10, 15)
Topuz = random.randint(15, 20)
Kalkan = random.randint(20, 25)
Ates_baskini = random.randint(10, 15)
Ruzgar = random.randint(15, 20)
Isın_gozler = random.randint(20, 25)
#silah listesi
silahlar = ["Demir yumruk", "Balta", "Balyoz", "Ates kure", "Can icecegi", "Buz oku", "Kralin kilici", "Topuz", "Kalkan", "Ates baskini", "Ruzgar", "Isın gozler"]
tas_kagit_makas = ["Taş", "Kağıt", "Makas"]
mevcut_karakterler = ["Dev", "buyucu", "Şovalye", "Ejderha"]

#karakterler ve silahları
dev_silahlar = ["Demir yumruk", "Balta", "Balyoz"]
buyucu_silahlar = ["Ates kure", "Can icecegi", "Buz oku"]
sovalye_silahlar = ["Kralin kilici", "Topuz", "Kalkan"]
ejderha_silahlar = ["Ates baskini", "Ruzgar", "Isın gozler"]

i = 1
while(i):
    print("Taş kağıt makas oyunu oynayarak karakterinizi seçin.\n")
    
    
    print("\n Oyunu Sonlandırmak için 'q' tuşuna basınız.\n")
        
    mevcut_karakterler = ["Dev", "buyucu", "Şovalye", "Ejderha"]
    kazanan = 0
    secim_oyun = input("Taş kağıt makas oyununu oynamak için 'Taş', 'Kağıt' veya 'Makas'dan 1'ini seçiniz:")    
    while(kazanan==0):#taş kağıt makas oyunu 
        bilgisayar_secimi = random.choice(tas_kagit_makas)
        if secim_oyun == "Taş":
            
            if bilgisayar_secimi == "Taş":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                print("Berabere \n şimdi tekrar seçiniz.")
                secim_oyun = input()
                
            elif bilgisayar_secimi == "Kağıt":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                print("Kaybettiniz \nŞimdi bilgisayarınız karakterini seçiyor.\n")
                
                kazanan = -1
                break
            elif bilgisayar_secimi == "Makas":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                print("Kazandınız \nŞimdi karakterinizi seçebilirsiniz.\n")
                kazanan = 1
                break   
        elif secim_oyun == "Kağıt":
            
            if bilgisayar_secimi == "Taş":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                print("Kazandınız \nŞimdi karakterinizi seçebilirsiniz.\n")
                kazanan = 1
                break
            elif bilgisayar_secimi == "Kağıt":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                print("Berabere \n şimdi tekrar seçiniz.")
                secim_oyun = input()
            elif bilgisayar_secimi == "Makas":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                print("Kaybettiniz \nŞimdi bilgisayarınız karakterini seçiyor.\n")
                kazanan = -1
                break
        elif secim_oyun == "Makas":
            
            if bilgisayar_secimi == "Taş":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                print("Kaybettiniz \nŞimdi bilgisayarınız karakterini seçiyor.\n")
                kazanan = -1
                break
            elif bilgisayar_secimi == "Kağıt":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                print("Kazandınız \nŞimdi karakterinizi seçebilirsiniz.\n")
                kazanan = 1
                break
            elif bilgisayar_secimi == "Makas":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi)
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
        
    print("Mevcut karakterler")
    for karakter in mevcut_karakterler:
        print(karakter)
    
    while (kazanan==1):
        
        print("Karakterinizi seçiniz.")
        karakter_secimi = input()
        while(karakter_secimi not in mevcut_karakterler):
            print("Hatalı giriş yaptınız.")
            karakter_secimi = input()
        
        if karakter_secimi == "Dev":
            oyuncunun_karakteri = karakter_secimi_fonksiyonu(karakter_secimi, dev)
            mevcut_karakterler.remove("Dev")

            print("Dev karakterinin canı: ", oyuncunun_karakteri)
            print("Dev karakterinin silahları: ", "Demir yumruk\t", "Balta\t\t", "Balyoz")
            
            
            kazanan=3
        elif karakter_secimi == "buyucu":
            oyuncunun_karakteri = karakter_secimi_fonksiyonu(karakter_secimi, buyucu)
            mevcut_karakterler.remove("buyucu")

            print("Büyücü karakterinin canı: ", oyuncunun_karakteri)
            print("Büyücü karakterinin silahları: ", "Ates kure\t", "Can icecegi\t\t", "Buz oku")         
            kazanan=3
        elif karakter_secimi == "Şovalye":
            oyuncunun_karakteri = karakter_secimi_fonksiyonu(karakter_secimi, sovalye)
            mevcut_karakterler.remove("Şovalye")

            print("Şovalye karakterinin canı: ", oyuncunun_karakteri)
            print("Şovalye karakterinin silahları: ", "Kralin kılıcı\t", "Topuz\t\t", "Kalkan")
            
            kazanan=3

        elif karakter_secimi == "Ejderha":
            oyuncunun_karakteri = karakter_secimi_fonksiyonu(karakter_secimi, ejderha)
            mevcut_karakterler.remove("Ejderha")

            print("Ejderha karakterinin canı: ", oyuncunun_karakteri)
            print("Ejderha karakterinin silahları: ", "Ates baskini\t", "Ruzgar\t\t", "Isın gozler\t")
            
            kazanan=3
        
        bilgisayar_secimi_oyun = random.choice(mevcut_karakterler)
        if(bilgisayar_secimi_oyun=="Dev"):
            bilgisayarin_karakteri = karakter_secimi_fonksiyonu(bilgisayar_secimi_oyun, dev)
        elif(bilgisayar_secimi_oyun=="buyucu"):
            bilgisayarin_karakteri = karakter_secimi_fonksiyonu(bilgisayar_secimi_oyun, buyucu)
        elif(bilgisayar_secimi_oyun=="Şovalye"):
            bilgisayarin_karakteri = karakter_secimi_fonksiyonu(bilgisayar_secimi_oyun, sovalye)
        elif(bilgisayar_secimi_oyun=="Ejderha"):
            bilgisayarin_karakteri = karakter_secimi_fonksiyonu(bilgisayar_secimi_oyun, ejderha)
        print("Bilgisayarın karakteri seçildi.", bilgisayar_secimi_oyun)
        print("Bilgisayarın karakterinin canı: ", bilgisayarin_karakteri)


    
    while (kazanan==-1):     
        bilgisayar_secimi_oyun = random.choice(mevcut_karakterler)
        print("Bilgisayarın ", bilgisayar_secimi_oyun, " karakterini seçti.")
        if(bilgisayar_secimi_oyun=="Dev"):
            bilgisayarin_karakteri = karakter_secimi_fonksiyonu(bilgisayar_secimi_oyun, dev)
            print("Dev karakterinin silahları: ", "Demir yumruk\t", "Balta\t", "Balyoz")
            print("Bilgisayarının karakterinin canı: ", bilgisayarin_karakteri)
            kazanan =3
        elif(bilgisayar_secimi_oyun=="buyucu"):
            bilgisayarin_karakteri = karakter_secimi_fonksiyonu(bilgisayar_secimi_oyun, buyucu)

            print("buyucu karakterinin silahları: ", "Ates kure\t", "Can icecegi\t", "Buz oku")
            print("Bilgisayarının karakterinin canı: ", bilgisayarin_karakteri)
            kazanan=3

        elif(bilgisayar_secimi_oyun=="Şovalye"):
            bilgisayarin_karakteri = karakter_secimi_fonksiyonu(bilgisayar_secimi_oyun, sovalye)

            print("Şovalye karakterinin silahları: ", "Kralin kilici\t", "Topuz\t", "Kalkan")
            print("Bilgisayarının karakterinin canı: ", bilgisayarin_karakteri)
            kazanan=3

        elif(bilgisayar_secimi_oyun=="Ejderha"):
            bilgisayarin_karakteri = karakter_secimi_fonksiyonu(bilgisayar_secimi_oyun, ejderha)

            print("Ejderha karakterinin silahları: ", "Ates baskini\t", "Ruzgar\t", "Isın gozler")
            print("Bilgisayarının karakterinin canı: ", bilgisayarin_karakteri)
            kazanan=3

        
        mevcut_karakterler.remove(bilgisayar_secimi_oyun)
        print("Mevcut karakterler\n")
        for karakter in mevcut_karakterler:
            print(karakter)
        print("Karakterinizi seçiniz.")
        karakter_secimi = input()
        while(karakter_secimi not in mevcut_karakterler):
            print("Hatalı giriş yaptınız.")
            karakter_secimi = input()
            
        if karakter_secimi == "Dev":
            oyuncunun_karakteri = karakter_secimi_fonksiyonu(karakter_secimi, dev)
            mevcut_karakterler.remove("Dev")
            
            print("Dev karakteri seçildi.")
            print("Dev karakterinin canı: ", oyuncunun_karakteri)
            print("Dev karakterinin silahları: ", "Demir yumruk\t", "Balta\t", "Balyoz")
        elif karakter_secimi == "buyucu":
            oyuncunun_karakteri = karakter_secimi_fonksiyonu(karakter_secimi, buyucu)
            mevcut_karakterler.remove("buyucu")
            
            print("buyucu karakteri seçildi.")
            print("buyucu karakterinin canı: ", oyuncunun_karakteri)
            print("buyucu karakterinin silahları: ", "Ates kure\t", "Can icecegi\t", "Buz oku")
        elif karakter_secimi == "Şovalye":
            oyuncunun_karakteri = karakter_secimi_fonksiyonu(karakter_secimi, sovalye)
            mevcut_karakterler.remove("Şovalye")
            
            print("Şovalye karakteri seçildi.")
            print("Şovalye karakterinin canı: ", oyuncunun_karakteri)
            print("Şovalye karakterinin silahları: ", "Kralin kilici\t", "Topuz\t", "Kalkan")
        elif karakter_secimi == "Ejderha":
            oyuncunun_karakteri = karakter_secimi_fonksiyonu(karakter_secimi, ejderha)
            mevcut_karakterler.remove("Ejderha")
            
            print("Ejderha karakteri seçildi.")
            print("Ejderha karakterinin canı: ", oyuncunun_karakteri)
            print("Ejderha karakterinin silahları: ", "Ates baskini", "Ruzgar", "Isın gozler")

          
    print("\n\n\n\n ############# Savaş başlıyor ############# \n")

    takip=0
    while(oyuncunun_karakteri>0 and bilgisayarin_karakteri>0):
        print("\n \t Mevcut can durumu \n Sizin canınız: ", oyuncunun_karakteri)
        print("\n Bilgisayarın canı: ", bilgisayarin_karakteri)
        
        print("İlk vuruş için taş kağıt makas oyunu oynayınız.")
        secim_oyun = input(" 'Taş', 'Kağıt' veya 'Makas'tan 1'ini seçiniz veya çıkmak için q ye basınız:")    
        while(takip==0):#taş kağıt makas oyunu
            bilgisayar_secimi = random.choice(tas_kagit_makas) 
            if secim_oyun == "Taş":
                
                if bilgisayar_secimi == "Taş":
                    print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                    print("Berabere \n şimdi tekrar seçiniz.")
                    secim_oyun = input()
                    takip=0
                    
                elif bilgisayar_secimi == "Kağıt":
                    print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                    print("Kaybettiniz Bilgisayarınız atak yapıyor.")
                    takip = -1
                    
                elif bilgisayar_secimi == "Makas":
                    print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                    print("Kazandınız şimdi atak yapabilirsiniz.")
                    takip = 1
                     
            elif secim_oyun == "Kağıt":
                
                if bilgisayar_secimi == "Taş":
                    print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                    print("Kazandınız şimdi atak yapabilirsiniz.")
                    takip = 1
                      
                elif bilgisayar_secimi == "Kağıt":
                    print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                    print("Berabere \n şimdi tekrar seçiniz.")
                    secim_oyun = input()
                    takip=0

                elif bilgisayar_secimi == "Makas":
                    print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                    print("Kaybettiniz Bilgisayarınız atak yapıyor.")
                    takip = -1
                    
            elif secim_oyun == "Makas":
                
                if bilgisayar_secimi == "Taş":
                    print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                    print("Kaybettiniz Bilgisayarınız atak yapıyor.")
                    takip = -1
                    
                elif bilgisayar_secimi == "Kağıt":
                    print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                    print("Kazandınız şimdi atak yapabilirsiniz.")
                    takip = 1
                      
                elif bilgisayar_secimi == "Makas":
                    print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                    print("Berabere \n şimdi tekrar seçiniz.")
                    secim_oyun = input()
            elif secim_oyun == "q":
                i = 0
                break
            else:
                print("Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.")
                secim_oyun = input()
        
        
        if(takip==1):
            print("Silahınızı seçiniz.")
            if(karakter_secimi=="Dev"):
                print("Demir yumruk\t", "Balta\t", "Balyoz")
            elif(karakter_secimi=="buyucu"):
                print("Ates kure\t", "Can icecegi\t", "Buz oku")
            elif(karakter_secimi=="Şovalye"):
                print("Kralin kilici\t", "Topuz\t", "Kalkan")
            elif(karakter_secimi=="Ejderha"):
                print("Ates baskini\t", "Ruzgar\t", "Isın gozler")
            karakterin_silahi = input()
            while(karakterin_silahi not in silahlar):
                print("Hatalı giriş yaptınız.")
                karakterin_silahi = input()
            if(karakterin_silahi=="Can icecegi"):
                oyuncunun_karakteri = oyuncunun_karakteri + Can_icecegi
                print("Canınız arttı. Yeni canınız: ", oyuncunun_karakteri)
            else:
                hasar=atak(karakterin_silahi)
                print("Verilen Hasar: ", hasar, "\n")
                bilgisayarin_karakteri = bilgisayarin_karakteri - hasar
        if(takip==-1):
            if(bilgisayar_secimi_oyun=="Dev"):
                bilgisayarin_silahi = random.choice(dev_silahlar)
            elif(bilgisayar_secimi_oyun=="buyucu"):
                bilgisayarin_silahi = random.choice(buyucu_silahlar)
            elif(bilgisayar_secimi_oyun=="Şovalye"):
                bilgisayarin_silahi = random.choice(sovalye_silahlar)
            elif(bilgisayar_secimi_oyun=="Ejderha"):
                bilgisayarin_silahi = random.choice(ejderha_silahlar)
            print("Bilgisayarın silahı: ", bilgisayarin_silahi)
            if(bilgisayarin_silahi=="Can icecegi"):
                bilgisayarin_karakteri = bilgisayarin_karakteri + Can_icecegi
                print("Bilgisayarın canı arttı. Yeni canı: ", bilgisayarin_karakteri)
            else:
                hasar2=atak(bilgisayarin_silahi)
                print("Alınan Hasar: ", hasar2, "\n")
                oyuncunun_karakteri = oyuncunun_karakteri - hasar2
        takip=0
        if(i==0):
            break
        
    print("Oyun bitti.")
    if(oyuncunun_karakteri>bilgisayarin_karakteri):
        print("Oyunu kazandınız.")
    else:
        print("Oyunu kaybettiniz.")
    print("Oyunu tekrar oynamak için 1'e basınız.")
    print("Oyundan çıkmak için q'ya basınız.")
    secim = input()
    if(secim=="q"):
        i=0
    elif(secim=="1"):
        i=1
    else:
        print("Hatalı giriş yaptınız.")
        i=0
        break       
            
                

   
        
    