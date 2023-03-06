######### COZUM-1 ########

# Dairenin alanini hesaplayan bir program yapiyoruz
print('Dairenin alanini hesaplayan programa hosgeldiniz.')

# Kullanicidan int a donusturerek bir input aliyoruz
yaricap = int(input('Dairenin yari capini giriniz: '))
pi = 3.14159
# kullanicidan gelen degeri sonuc adli bir degiskene atiyoruz cunku daha sonra kolaylikla kullanabiliriz
sonuc = ("Girdiginiz yaricap {} birimdir. Buna gore dairenin alani yaklasik olarak: {} birimdir".format(
    yaricap, yaricap * yaricap * pi))
# inputtan gelene gore bir alan hesaplamasi yaparak kullaniciya sonucu donuyoruz
print(sonuc, "\n", '-'*len(sonuc), sep='')
###########################################################################

####### COZUM-2 ########

# Kullanicidan ad ve soyadini alip yer degistirerek yazdiriyoruz

ad = input('Ad: ').upper()
soyad = input('Soyad: ').upper()

print('Merhaba:', soyad + "   " + ad)
###########################################################################

####### COZUM-3 ########

# kullanicidan ad soyad adres alip alta lta yazdiriyoruz en son satirea adres kadar * isareti koyuyoruz

ad = input('Ad: ').upper()
soyad = input('Soyad: ').upper()
adres = input('Adres: ').upper()

print('''
{}
{}
{}
'''.format(ad, soyad, adres))
print('*'*len(adres), sep='')
###########################################################################

####### COZUM-4 ########

# kullanicidan saniye alip gun saat dakika ve saniye olarak ekrana yazdiriyoruz.

saniye = int(input('Lutfen Saniye Giriniz: '))
# dakika saat ve gunu formulize ediyoruz
gun = saniye // 86400
saat = saniye // 3600
saniye = saniye % 3600
dakika = saniye // 60
sonSaniye = saniye % 60
# aldigimiz inputu ilgili formulizasyonlar sonucunda sonuc adli degiskene hesaplamalar yaparak atiyoruz.
# {} ile .format fonksiyonunu kullaniyoruz. boylece gelendegeri istedigimiz noktalara yazdirabiliriz.
# format icindeki her birimi int a cevirerek cikan sonucun float olmasini engellemis oluyoruz
sonuc = ("Girdiginiz {} Saniye : {} Gun,  {} Saat, {} Dakika ve {} Saniye  olarak hesaplanmistir".format(
    saniye, int(gun), int(saat), int(dakika), int(sonSaniye)))
print(sonuc)

###########################################################################

# COZUM-5 ######## *******
# kullanicidan isim ve soyadini alip bir dikdotgenin icine yazdiriyoruz

isim = input('Adiniz: ').upper()
soyisim = input('Soyadiniz: ').upper()

sonuc = ("{} {}".format(isim, soyisim))

print('|', '*'*len(sonuc), "|")
print('|', " "*len(sonuc), "|")
print('|', " "*len(sonuc), "|")
print('|', " "*len(sonuc), "|")
print('|', sonuc, '|')
print('|', " "*len(sonuc), "|")
print('|', " "*len(sonuc), "|")
print('|', " "*len(sonuc), "|")
print('|', '*'*len(sonuc), "|")

###########################################################################

# COZUM-6 ########

# KULLANICIYA SORU SORUP CEVAP VERECEGIMIZ BASIT CHAT PRORRAMI
'''
#her konusmayi bir degiskene atiyoruz bu sekilde baska yerlerdede kolayca kullanabiliriz.
#upper fonksiyonunu kullaniyoruz bu sekilde her cevap buyuk harf olarak donuyor ve karsilastirmalarda sorun yasamiyoruz
ad = input("Merhaba ben 'ROBOFENYX', Peki Sizin Adiniz Nedir?: ").upper()
adCevap = print('ROBOFENYX: Memnun oldum', ad)
yas = print('ROBOFENYX:', ad,
            ', Benim yasim 2 dir, peki sizin yasiniz kacdir?: ')
yasCevap = int(input('Benim yasim ise: ')) # yas cevabini int almamiz lazim o yuzden int kullaniyoruz
#if statement ile bazi dogrulama cevaplari vermesini sagliyoruz.daha eglenceli oluyor.
if yasCevap <= 45:
    yasGenc = print('ROBOFENYX: Ne guzel', yasCevap,
                    'yas daha gencliginizin baharindasiniz, Peki memleket nere', ad, 'Bey?')
else:
    yasYasli = print(
        'ROBOFENYX: Ne guzel omrunuzde ne guzel anilariniz olmustur kimbilir. Hayirli omurler dilerim... Peki memleket nere ?', ad)
memleket = 'MARS'
print('ROBOFENYX: Bu arada benim memleketim', memleket, 'dir')
memleketCevap = input('Benim memleketim ise:').upper()
if memleketCevap == memleket:
    print('ROBOFENYX: Oooo o zaman biz hemseriyiz!')
else:
    print('ROBOFENYX: Hemseri degilmisiz yaw :(')
yazilimDili = 'PYTHON'
yazilim = print('ROBOFENYX: Peki en sevdiginiz yazilim dili nedir?')
yazilimCevap = input('Benim sevdigim yazilim dili: ').upper()
if yazilimCevap == yazilimDili:
    print('Bende', yazilimDili, 'yazilim dilini cok severim gercekten')
else:
    print('Bahsettiginiz', yazilimCevap,
          'yazilim dilini malesef bilmiyorum. Ama onu da ogrenebilirim')
print("ROBOFENYX: Bence bugunluk bu kadar konusma yeter sanirim, benimle konustugun icin tesekkurler baska zaman yine gorusuruz", ad, ":)")'''
