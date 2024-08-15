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
    if(silah_ismi=="Demir Yumruk"):
        return Demir_Yumruk
    elif(silah_ismi=="Balta"):
        return Balta
    elif(silah_ismi=="Balyoz"):
        return Balyoz
    elif(silah_ismi=="Ateş küre"):
        return Ateş_küre
    elif(silah_ismi=="Can içeçeği"):
        return Can_içeçeği
    elif(silah_ismi=="Buz oku"):
        return Buz_oku
    elif(silah_ismi=="Kralın Kılıcı"):
        return Kralın_Kılıcı
    elif(silah_ismi=="Topuz"):
        return Topuz
    elif(silah_ismi=="Kalkan"):
        return Kalkan
    elif(silah_ismi=="Ateş baskını"):
        return Ateş_baskını
    elif(silah_ismi=="Rüzgar"):
        return Rüzgar
    elif(silah_ismi=="Işın gözler"):
        return Işın_gözler






dev=0
buyucu=0
sovalye=0
ejderha=0

kazanan = 0
#Silahlar
Demir_Yumruk = random.randint(10, 15)
Balta = random.randint(15, 20)
Balyoz = random.randint(20, 25)
Ateş_küre = random.randint(10, 15)
Can_içeçeği = random.randint(15, 20)
Buz_oku = random.randint(20, 25)
Kralın_Kılıcı = random.randint(10, 15)
Topuz = random.randint(15, 20)
Kalkan = random.randint(20, 25)
Ateş_baskını = random.randint(10, 15)
Rüzgar = random.randint(15, 20)
Işın_gözler = random.randint(20, 25)
#silah listesi
silahlar = ["Demir Yumruk", "Balta", "Balyoz", "Ateş küre", "Can içeçeği", "Buz oku", "Kralın Kılıcı", "Topuz", "Kalkan", "Ateş baskını", "Rüzgar", "Işın gözler"]
tas_kagit_makas = ["Taş", "Kağıt", "Makas"]
mevcut_karakterler = ["Dev", "buyucu", "Şovalye", "Ejderha"]
asil_karakterler = ["Dev", "buyucu", "Şovalye", "Ejderha"]
#karakterler ve silahları
dev_silahlar = ["Demir Yumruk", "Balta", "Balyoz"]
buyucu_silahlar = ["Ateş küre", "Can içeçeği", "Buz oku"]
sovalye_silahlar = ["Kralın Kılıcı", "Topuz", "Kalkan"]
ejderha_silahlar = ["Ateş baskını", "Rüzgar", "Işın gözler"]

i = 1
while(i):
    print("Taş kağıt makas oyunu oynayarak karakterinizi seçin.\n")
    
    
    print("\n Oyunu Sonlandırmak için 'q' tuşuna basınız.\n")
        
 
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
                print("Kaybettiniz \n şimdi bilgisayarın karakterini seçiyor.")
                kazanan = -1
                break
            elif bilgisayar_secimi == "Makas":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                print("Kazandınız \n şimdi karakterinizi seçebilirsiniz.")
                kazanan = 1
                break   
        elif secim_oyun == "Kağıt":
            
            if bilgisayar_secimi == "Taş":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                print("Kazandınız \n şimdi karakterinizi seçebilirsiniz.")
                kazanan = 1
                break
            elif bilgisayar_secimi == "Kağıt":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                print("Berabere \n şimdi tekrar seçiniz.")
                secim_oyun = input()
            elif bilgisayar_secimi == "Makas":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                print("Kaybettiniz \n şimdi bilgisayarın karakterini seçiyor.")
                kazanan = -1
                break
        elif secim_oyun == "Makas":
            
            if bilgisayar_secimi == "Taş":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                print("Kaybettiniz \n şimdi bilgisayarın karakterini seçiyor.")
                kazanan = -1
                break
            elif bilgisayar_secimi == "Kağıt":
                print("Bilgisayarın seçimi: ", bilgisayar_secimi)
                print("Kazandınız \n şimdi karakterinizi seçebilirsiniz.")
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
        
    print("Mevcut karakterler\n")
    for karakter in mevcut_karakterler:
        print(karakter)
    
    while (kazanan==1):
        print("Karakterinizi seçiniz.")
        karakter_secimi = input()
        if karakter_secimi == "Dev":
            oyuncunun_karakteri = karakter_secimi_fonksiyonu(karakter_secimi, dev)
            mevcut_karakterler.remove("Dev")
            
            print("Dev karakteri seçildi.")
            print("Dev karakterinin canı: ", oyuncunun_karakteri)
            print("Dev karakterinin silahları: ", "Demir Yumruk", "Balta", "Balyoz")
            
            
            kazanan=3
        elif karakter_secimi == "buyucu":
            oyuncunun_karakteri = karakter_secimi_fonksiyonu(karakter_secimi, buyucu)
            mevcut_karakterler.remove("buyucu")
           
            print("buyucu karakteri seçildi.")
            print("buyucu karakterinin canı: ", oyuncunun_karakteri)
            print("buyucu karakterinin silahları: ", "Ateş küre", "Can içeçeği", "Buz oku")         
            kazanan=3
        elif karakter_secimi == "Şovalye":
            oyuncunun_karakteri = karakter_secimi_fonksiyonu(karakter_secimi, sovalye)
            mevcut_karakterler.remove("Şovalye")
            
            print("Şovalye karakteri seçildi.")
            print("Şovalye karakterinin canı: ", oyuncunun_karakteri)
            print("Şovalye karakterinin silahları: ", "Kralın Kılıçı", "Topuz", "Kalkan")
            
            kazanan=3

        elif karakter_secimi == "Ejderha":
            oyuncunun_karakteri = karakter_secimi_fonksiyonu(karakter_secimi, ejderha)
            mevcut_karakterler.remove("Ejderha")
            
            print("Ejderha karakteri seçildi.")
            print("Ejderha karakterinin canı: ", oyuncunun_karakteri)
            print("Ejderha karakterinin silahları: ", "Ateş baskını", "Rüzgar", "Işın gözler")
            
            kazanan=3
        while(karakter_secimi not in asil_karakterler):
            print("Hatalı giriş yaptınız.")
            karakter_secimi = input()
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
        print("\n\n\nBilgisayarın karakteri seçiliyor.")
        bilgisayar_secimi_oyun = random.choice(mevcut_karakterler)
        
        print("Bilgisayarın karakteri seçildi.")
        if(bilgisayar_secimi_oyun=="Dev"):
            bilgisayarin_karakteri = karakter_secimi_fonksiyonu(bilgisayar_secimi_oyun, dev)
            print("Dev karakteri seçildi.")
            print("Dev karakterinin silahları: ", "Demir Yumruk", "Balta", "Balyoz")
            print("Bilgisayarının karakterinin canı: ", bilgisayarin_karakteri)
            kazanan =3
        elif(bilgisayar_secimi_oyun=="buyucu"):
            bilgisayarin_karakteri = karakter_secimi_fonksiyonu(bilgisayar_secimi_oyun, buyucu)
            print("buyucu karakteri seçildi.")
            print("buyucu karakterinin silahları: ", "Ateş küre", "Can içeçeği", "Buz oku")
            print("Bilgisayarının karakterinin canı: ", bilgisayarin_karakteri)
            kazanan=3

        elif(bilgisayar_secimi_oyun=="Şovalye"):
            bilgisayarin_karakteri = karakter_secimi_fonksiyonu(bilgisayar_secimi_oyun, sovalye)
            print("Şovalye karakteri seçildi.")
            print("Şovalye karakterinin silahları: ", "Kralın Kılıçı", "Topuz", "Kalkan")
            print("Bilgisayarının karakterinin canı: ", bilgisayarin_karakteri)
            kazanan=3

        elif(bilgisayar_secimi_oyun=="Ejderha"):
            bilgisayarin_karakteri = karakter_secimi_fonksiyonu(bilgisayar_secimi_oyun, ejderha)
            print("Ejderha karakteri seçildi.")
            print("Ejderha karakterinin silahları: ", "Ateş baskını", "Rüzgar", "Işın gözler")
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
            print("Dev karakterinin silahları: ", "Demir Yumruk", "Balta", "Balyoz")
        elif karakter_secimi == "buyucu":
            oyuncunun_karakteri = karakter_secimi_fonksiyonu(karakter_secimi, buyucu)
            mevcut_karakterler.remove("buyucu")
            
            print("buyucu karakteri seçildi.")
            print("buyucu karakterinin canı: ", oyuncunun_karakteri)
            print("buyucu karakterinin silahları: ", "Ateş küre", "Can içeçeği", "Buz oku")
        elif karakter_secimi == "Şovalye":
            oyuncunun_karakteri = karakter_secimi_fonksiyonu(karakter_secimi, sovalye)
            mevcut_karakterler.remove("Şovalye")
            
            print("Şovalye karakteri seçildi.")
            print("Şovalye karakterinin canı: ", oyuncunun_karakteri)
            print("Şovalye karakterinin silahları: ", "Kralın Kılıcı", "Topuz", "Kalkan")
        elif karakter_secimi == "Ejderha":
            oyuncunun_karakteri = karakter_secimi_fonksiyonu(karakter_secimi, ejderha)
            mevcut_karakterler.remove("Ejderha")
            
            print("Ejderha karakteri seçildi.")
            print("Ejderha karakterinin canı: ", oyuncunun_karakteri)
            print("Ejderha karakterinin silahları: ", "Ateş baskını", "Rüzgar", "Işın gözler")

          
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
                print("Demir Yumruk", "Balta", "Balyoz")
            elif(karakter_secimi=="buyucu"):
                print("Ateş küre", "Can içeçeği", "Buz oku")
            elif(karakter_secimi=="Şovalye"):
                print("Kralın Kılıçı", "Topuz", "Kalkan")
            elif(karakter_secimi=="Ejderha"):
                print("Ateş baskını", "Rüzgar", "Işın gözler")
            karakterin_silahi = input()
            while(karakterin_silahi not in silahlar):
                print("Hatalı giriş yaptınız.")
                karakterin_silahi = input()
            bilgisayarin_karakteri = bilgisayarin_karakteri - atak(karakterin_silahi)
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
            oyuncunun_karakteri = oyuncunun_karakteri - atak(bilgisayarin_silahi)
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
            
                

   
        
    