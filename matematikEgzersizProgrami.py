import os
import time
import random
import sqlite3

egzersizAyarlari = {"İşlem": "+", "Soru Sayısı": 15, "Basamak Sayısı": 2, "Negatif Sayilar": False}

def dbEgzersizlerTablosuOlustur():
    baglanti = sqlite3.connect("matematikAlistirmaProgramiVeriTabani.db")
    cursor = baglanti.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS egzersizler (ID INTEGER PRIMARY KEY AUTOINCREMENT, DogruSayisi int, YanlisSayisi int, Sure int)")
    baglanti.commit()

    baglanti.close()


def dbEgzersizGecmisiEkle(dogruSayisi, yanlisSayisi, sure):
    baglanti = sqlite3.connect("matematikAlistirmaProgramiVeriTabani.db")
    cursor = baglanti.cursor()

    cursor.execute("INSERT INTO egzersizler (DogruSayisi, YanlisSayisi, Sure) VALUES (?,?,?)", (dogruSayisi,yanlisSayisi,sure))
    baglanti.commit()

    baglanti.close()

def dbEgzersizVerileriniAl():
    baglanti = sqlite3.connect("matematikAlistirmaProgramiVeriTabani.db")
    cursor = baglanti.cursor()

    cursor.execute("SELECT * FROM egzersizler")
    return cursor.fetchall()

    baglanti.close()

def egzersizeBaslaSayfasi():
    sorular = list()

    for i in range(1,egzersizAyarlari["Soru Sayısı"]+1):

        os.system("cls")
        sayi1 = -random.randint(10**(egzersizAyarlari["Basamak Sayısı"] - 1),(10 ** egzersizAyarlari["Basamak Sayısı"]) - 1) if random.randint(0,1) == 0 and egzersizAyarlari["Negatif Sayilar"] else random.randint(10**(egzersizAyarlari["Basamak Sayısı"] - 1),(10 ** egzersizAyarlari["Basamak Sayısı"]) - 1)
        sayi2 = -random.randint(10**(egzersizAyarlari["Basamak Sayısı"] - 1),(10 ** egzersizAyarlari["Basamak Sayısı"]) - 1) if random.randint(0,1) == 0 and egzersizAyarlari["Negatif Sayilar"] else random.randint(10**(egzersizAyarlari["Basamak Sayısı"] - 1),(10 ** egzersizAyarlari["Basamak Sayısı"]) - 1)
        cevap = 0

        if egzersizAyarlari["İşlem"] == "+":
            cevap = sayi1+sayi2

        elif egzersizAyarlari["İşlem"] == "-":
            cevap = sayi1-sayi2

        elif egzersizAyarlari["İşlem"] == "*":
            cevap = sayi1*sayi2

        while True:

            try:
                print(f"""
    {i}.soru

    {sayi1} {egzersizAyarlari["İşlem"]} {sayi2} = ? 

                        """)
                sureBaslangic = time.time()

                cevapGiris = int(input("    Cevabınız: "))

                sorular.append([cevapGiris == cevap, time.time() - sureBaslangic])

                if cevapGiris == cevap:
                    mesajVer("  Verdiğiniz cevap doğru!")

                else:
                    mesajVer(f"    Verdiğiniz cevap yanlış!\n   Doğru cevap: {cevap}")

                break

            except:
                mesajVer("    Hata! Sadece sayı belirtin!")

    toplamDogru = 0
    toplamYanlis = 0
    toplamSure = 0

    for i in sorular:

        if i[0]:
            toplamDogru+=1

        else:
            toplamYanlis+=1

        toplamSure += i[1]

    dbEgzersizGecmisiEkle(toplamDogru,toplamYanlis,toplamSure)

    os.system("cls")
    print(f"""

        Egzersiz Sonuçları
    
    Toplam Doğru: {toplamDogru} tane
    Toplam Yanlış: {toplamYanlis} tane
    Toplam Süre: {toplamSure:.2f} saniye
    
    %{(toplamDogru/(toplamDogru+toplamYanlis))*100:.2f} doğru
    %{(toplamYanlis/(toplamDogru+toplamYanlis))*100:.2f} yanlış
    
    Bir soruya ortalama {toplamSure/(toplamDogru+toplamYanlis):.2f} saniye ayırdınız.
    
    10 saniye içinde geri dönülüyor!
    Sonucunuz geçmişe kayıt edildi!
    """)
    time.sleep(10)

def islemDegistir():
    while True:
        os.system("cls")

        yeniIslem = input("Çıkmak için 'Q'\nBir işlem seçin (+,-,*) : ")

        if yeniIslem in ["+","-","*"]:
            egzersizAyarlari["İşlem"] = yeniIslem
            break

        elif yeniIslem.upper() == "Q":
            mesajVer("  Geri gidiliyor...")
            break

        else:
            mesajVer("  Hata! (+,-,*) arasından bir tane seçin!")

def soruSayisiDegistir():
    while True:
        try:
            os.system("cls")

            yeniSoruSayisi = input("Çıkmak için 'Q'\nYeni soru sayısı (1 ile 200 arası) : ")

            if yeniSoruSayisi.upper() == "Q":
                mesajVer("    Geri gidiliyor...")
                break

            elif int(yeniSoruSayisi) > 0 and int(yeniSoruSayisi) <= 200:
                egzersizAyarlari["Soru Sayısı"] = int(yeniSoruSayisi)
                break

            else:
                mesajVer("  Hata! Soru sayısı 1 ile 200 arası olmalı!")

        except:
            mesajVer("  Hata! Lütfen bir sayı belirtin")

def basamakSayisiDegistir():
    while True:
        try:
            os.system("cls")

            yeniBasamakSayisi = input("Çıkmak için 'Q'\nYeni basamak sayısı (1 ile 12 arası) : ")

            if yeniBasamakSayisi.upper() == "Q":
                mesajVer("    Geri gidiliyor...")
                break

            elif int(yeniBasamakSayisi) > 0 and int(yeniBasamakSayisi) <= 11:
                egzersizAyarlari["Basamak Sayısı"] = int(yeniBasamakSayisi)
                break

            else:
                mesajVer("  Hata! Basamak sayısı 1 ile 12 arası olmalı!")

        except:
            mesajVer("  Hata! Lütfen bir sayı belirtin")

def egzersizAyarlariSayfasi():
    while True:
        os.system("cls")
        print(f"""

           Egzersiz Ayarları

       A - İşlem: {egzersizAyarlari["İşlem"]}
       B - Soru sayısı: {egzersizAyarlari["Soru Sayısı"]}
       C - Basamak sayısı: {egzersizAyarlari["Basamak Sayısı"]}
       D - Negatif sayılar: {"Aktif" if egzersizAyarlari["Negatif Sayilar"] else "Aktif değil"}
       Q - Geri git

           """)
        secenek = input("   Bir seçenek seçin:")

        if secenek.upper() == "A":
            islemDegistir()

        elif secenek.upper() == "B":
            soruSayisiDegistir()

        elif secenek.upper() == "C":
            basamakSayisiDegistir()

        elif secenek.upper() == "D":
            egzersizAyarlari["Negatif Sayilar"] = not egzersizAyarlari["Negatif Sayilar"]

        elif secenek.upper() == "Q":
            mesajVer("  Geri gidiliyor...")
            break

        else:
            mesajVer("  Hata! Geçerli bir seçenek seçin")

def yeniEgzersizSayfasi():
    while True:
        os.system("cls")
        print("""

       Yeni Egzersiz

        A - Başla
        B - Ayarlar
        Q - Geri git
    
        """)
        secenek = input("   Bir işlem seçin:")

        if secenek.upper() == "A":
            egzersizeBaslaSayfasi()

        elif secenek.upper() == "B":
            egzersizAyarlariSayfasi()

        elif secenek.upper() == "Q":
            mesajVer("  Geri gidiliyor...")
            break

def egzersizGecmisiSayfasi():
    while True:
        os.system("cls")
        print("    Egzersiz Geçmişi")

        for satir in dbEgzersizVerileriniAl():
            print(f"""
            
    - {satir[0]} numaralı egzersiz -
    
    Toplam Doğru: {satir[1]} tane
    Toplam Yanlış: {satir[2]} tane
    Toplam Süre: {satir[3]:.2f} saniye
    
    %{(satir[1]/(satir[1]+satir[2]))*100:.2f} doğru
    %{(satir[2]/(satir[1]+satir[2]))*100:.2f} yanlış
    
    Bir soruya ortalama {satir[3]/(satir[1]+satir[2]):.2f} saniye ayırdınız.
    
    ------------------------------------------------------
    
            """)

        secim = input("    Çıkmak için 'Q' yazın: ")

        if secim.upper() == "Q":
            mesajVer("     Geri dönülüyor...")
            break

        else:
            mesajVer("     Hata! Lütfen geçerli bir seçim yapın!")

def mesajVer(mesaj):
    os.system("cls")
    print(mesaj)
    time.sleep(0.75)

dbEgzersizlerTablosuOlustur()
while True:
    os.system("cls")
    print("""
    
    Basit Matematik Egzersiz Programı
    
        A - Yeni egzersiz
        B - Egzersiz geçmişi
        Q - Çıkış yap
    
    """)
    secenek = input("   Bir işlem seçin:")

    if secenek.upper() == "A":
        yeniEgzersizSayfasi()

    elif secenek.upper() == "B":
        egzersizGecmisiSayfasi()

    elif secenek.upper() == "Q":
        mesajVer("  Programdan çıkılıyor...")
        exit()

    else:
        mesajVer("    Hata! Geçerli bir seçenek seçin")