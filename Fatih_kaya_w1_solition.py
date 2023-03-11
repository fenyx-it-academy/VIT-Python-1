#cevap 1:
pi = 3.14
radius = int(input("Dairenin Yarıçapını 'cm' olarak girin: "))
circle_area = pi*(radius**2)
print(f" Dairenin Alani {circle_area} cm2'dir.", "-"*len("Dairenin Alani {circle_area} cm2'dir."), sep="\n")

# cevap 2:
name = input("Adınızı girin: ")
lname = input("Soyadınızı girin: ")
print(f"Merhaba {lname}   {name}")

# cevap 3:
name = input("Adınızı girin: ")
lname = input("Soyadınızı girin: ")
addres = input("Adresinizi girin: ")
print(name, lname, addres, "*"*len(addres), sep="\n")

# cevap 4:
second = int(input("Toplam Saniyeyi giriniz: "))
remain_1 = second%86400
remain_2= remain_1%3600
print(f"{second} saniye = {second//86400} gün {remain_1//3600} saat {remain_2//60} dakika {remain_2%60} saniye'dir. ")

# cevap 5:
name = input("Ad ve Soyad giriniz: ")
space = len(name)*" "
print (f"""
       I********I 
       I  {space}  I
       I  {name }  I
       I  {space}  I 
       I********I """)

# cevap 6:
print("Log on! olmak için aşağıdaki Formu doldurunuz.")
name = input("Adınız? : ")
print(f"Adınız '{name}' olarak kaydedildi...")
lname = input("Soyadınız? : ")
print(f"""
Merhaba  {name} {lname}. 
Şimdi diğer bilgilerinizi girmenizi isteyeceğiz.
      """)
age= input("Yaşınız? : ")
print(f"Yaşınız '{age}' olarak kaydedildi...")
gender= input("Cinsiyetiniz? : ")
print(f"Cinsiyetiniz '{gender}' olarak kaydedildi...")
country=input("Memleketiniz? : ")
print(f"{name}, Sadece 1 soru kaldı. Sonra işleminiz bitecek!")
addres = input("Adresinizi sadece şehir olarak giriniz? : ")
print(f"""
Kayıt işleminiz başarılı bir şekilde gerçekleşti....
Lütfen bilgilerinizi kontrol ediniz.
    Ad: {name}
    Soyad: {lname}
    Yaş: {age}
    Cinsiyet: {gender}
    Memleket: {country}
    Adres: {addres}
""")
