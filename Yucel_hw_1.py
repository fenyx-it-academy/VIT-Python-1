#Dairenin alani?
#import math

#print("Dairenin alanini bulalim")
#r=float(input("Lutfen yaricapi giriniz: "))
#alan=float((math.pi)*((2*r)**2))
#sonuc=str("Dairenin alani:{} cm2'dir.".format(alan))
#print(sonuc,"\n","_"*len(sonuc))

#Selamlama

#name=input("What is your name?: ")
#surname=input("What is your surname?: ")
#print("Merhaba", surname, name, sep="   ")

#Kisisel Bilgiler

#name=input("What is your name?: ")
#surname=input("What is your surname?: ")
#adress=input("What is your adress?: ")
#print(name,surname,adress,"*"*len(adress), sep="\n")

#Saniye 

#time=int(input("input time in seconds: "))
#day=time//(60*60*24)
#time2=time%(60*60*24)
#hour=time2//(60*60)
#time3=time2%(60*60)
#minutes=time3//60
#time4=time3%60
#second=time4
#print(time,"is", day, "day", hour, "hour", minutes, "minutes", second, "second")


#Karvizit yapalim!

#name=input("What is your name?: ")
#surname=input("What is your surname?: ")


#print(*"II", sep="*"*((len(name+surname)+3)))
#print(*"II", sep=" "*((len(name+surname)+3)))
#print(*"II", sep=" "*((len(name+surname)+3)))
#print("I",name,surname,"I")
#print(*"II", sep=" "*((len(name+surname)+3)))
#print(*"II", sep=" "*((len(name+surname)+3)))
#print(*"II", sep="*"*((len(name+surname)+3)))


#LET'S GO!
com_les="matematik"
com_city="amsterdam"
com_hobby="gezmek"
com_age= 25
print("Hadi tanisalim!")
name=input("Senin adin ne?: ")
print("Merhaba ", name)

while True:
    user=input("Daha yakindan tanisalim mi? (yes/no) ")
    if user.lower()=="yes":
        print("Bakalim ne kadar benziyoruz?")
        age=int(input("Yasiniz nedir?: "))
        if age<25:
            print("Benden kucuksun:)")
        elif age==25:
            print("Bu ne tesaduf ayni yastayiz!!!")
        else:
            print("Benden buyuksunuz.")
        les=input("En sevdigin ders nedir?: ")
        if les.lower()=="matematik":
            print("Inanamiyorum bende cok severim")
        else:
            print("Ben matematik dersini seviyordum")   
        city=input("Hollandanin hangi sehrinde yasiyorsun?: ")  
        if city.lower()=="amsterdam":   
            print("Gercekten mi, bende", com_city, "'da yasiyorum")
        else:
            print("Oraya gitmedim hic")  
        hobby=input("En sevdiginiz hobiniz bedir?: ") 
        if hobby.lower()=="gezmek":
            print("Gercekten ortak yanlarimiz cok:)", "Seninle konusmak guzeldi", sep="\n")
            
        else:
            print("Birgun bende yapmak istiyorum")    
                 
                
    else:
        print("Bir dahaki sefer gurusmek uzere :(")    
    break





