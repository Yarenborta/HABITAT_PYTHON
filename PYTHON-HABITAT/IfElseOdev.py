###ÖDEV-1###
#Bir otoparkın ücret tarifesi aşağıdaki gibidir: 1 saate kadar: 5 TL
#1-5 saat arası: Saat başı 4 TL
#5 saatten fazla: Saat başı 3 TL
#Buna göre kullanıcının girdiği otoparkta kalınan saat süresine göre ödenecek miktarı bularak ekrana yazdırınız.

print("Otoparın ücret tarifesi 1saat 5TL'dir.1-5 saat arası 4TL'dir. 5'ten fazla ise 3Tl'dir ")
time=float(input("Aracın parkta kalma süresi="),)
if time==1:
   park_ucreti=time*5
   print("Park ücteriniz=",park_ucreti,"'dır")
elif time>1 and time<5:
   park_ucreti=time*3
   print("Park ücteriniz=",park_ucreti,"'dır")
else:
   park_ucreti=time*5
   print("Park ücteriniz=",park_ucreti,"'dır")

###################### ÖDEV-2 ##############
# Üçgenler kenar uzunluklarına göre üçe ayrılmaktadır: Eşkenar, İkizkenar ve Çeşitkenar. Kullanıcının girdiği 3 kenar uzunluğuna göre üçgenin türünü ekrana yazdırınız.

#side_1=float(input("Please enter the first sides of the triangle:  "))
#side_2=float(input("Please enter the second sides of the triangle: "))
#side_3=float(input("Please enter the third sides of the triangle:  "))

if side_1==side_2 and side_1==side_3:
   print("That triangle is isosceles triangle.")
elif side_1==side_3 and side_2==side_3:
   print("That triangle is equilateral triangle.")
elif side_1!=side_2 and side_1!=side_3 and side_2!=side_3:
   print("That triangle is scalene triangle")
else:
   print("Please enter valid value for triangle")

############ÖDEV-3##########
#Kullanıcıdan adını, maaşını ve çalışma yılını girmesini isteyiniz. 0-5 yıl arası çalışanlara %10; 6-10 yıl arası çalışanlara %15; 11 ve daha fazla yıl çalışanlara %25 zam yapılmaktadır. Buna göre “Sayın …………….., zamlı maaşınız …….. TL” çıktısı veren kodu yazınız.

name=input("Please enter your name= ")
salary=float(input("Please enter your salary="))
experience=float(input("How long do you work on this company? = "))
if experience==0 and experience<=5:
   salary=salary+(salary*0.10)
   print("Dear ",name, "your increased salary is",salary,"TL.")
elif experience<=6 and experience>=10:
   salary=salary+(salary*0.15)
   print("Dear ",name, "your increased salary is",salary,"TL.")
else:
   salary=salary+(salary*0.25)
   print("Dear ",name, "your increased salary is",salary,"TL.")


#########ÖDEV-4###########3
#4-	Girilen üç sayıdan en büyüğünü bulan kodu yazınız.

number_1=float(input("Please enter first number"))
number_2=float(input("Please enter second number"))
number_3=float(input("Please enter third number"))
if number_1>number_2 and number_1>number_3:
   print("First number is bigger than others.")
elif number_2>number_1 and number_2>number_3:
   print("Second number is bigger than others.")
elif number_3>number_1 and number_3>number_2:
   print("Third number is bigger than others.")
else:
   print("All entered values ​​are equal.")

######ÖDEV-5#########
#5-	Kullanıcıya sinema ya da tiyatro tercihi sorulsun. Sinema izlemek için 15 TL, tiyatro için 10 TL ödenmesi gerekmedir. Öğrencilere %50 indirim yapıldığı düşünülerek öğrenci ise indirim yapılan; öğrenci değilse indirimsiz tutarı hesaplayarak ekrana yazdıran kodu yazınız.

tercih=input("Vakit geçirmek için hangisini tercih edersiniz? Sinema/Tiyatro")
ogrenci=input("Öğrenci misiniz? EVET/HAYIR")
if tercih=="Sinema":
    if ogrenci== "EVET":
        ucret=15-(15*0.2)
        print("Öğrenci olduğunuzdan dolayı ücretiniz= ",ucret, "TL'dir.")
    else:
        print("Ücretiniz 15 TL'dir.")
elif tercih=="Tiyatro":
    if ogrenci=="EVET":
        ucret=10-(10*0.2)
        print("Öğrenci olduğunuzdan dolayı ücretiniz= ",ucret, "TL'dir.")
    else:
        print("Ücretiniz 10 TL'dir.")
else:
    print("Lütfen geçerli bir tercih giriniz.")


# tercih=input("Which do you prefer to pass the time? Cinema/Theatre")
# ogrenci=input("Are you a student ? YES/NO")
# if tercih=="Cinema":
#     if ogrenci== "YES":
#         ucret=15-(15*0.2)
#         print("Your pay for being a student is ",ucret, "TL.")
#     else:
#         print("your pay is 15 TL.")
# elif tercih=="Theatre":
#     if ogrenci=="YES":
#         ucret=10-(10*0.2)
#         print("Your pay for being a student is ",ucret, "TL.")
#     else:
#         print("your pay is 15 TL.")
# else:
#     print("Please enter valid prefering.") 


#################### ÖDEV-6 ################
#6-	Girilen sayı hem 3 hem de 5’e tam bölünüyorsa “15’e tam bölünür.”; bölünmüyorsa “15’e tam bölünmez.” çıktıları veren kodu yazınız.

number=int(input("Please enter a value"))
if number%3==0 and number%5==0:
    print("The entered value is divisible by 15.")
else:
    print("The entered value is not divisible by 15.")

##########ÖDEV-7############
#7-	Bir hava yolu firması en fazla 20 kilogram bagaj hakkı vermektedir. 20 kilogramdan sonraki her kilogram için 10 TL ek ücret almaktadır. Buna göre bagajı 20 kg ya da daha az olan yolculara “Herhangi bir ücret ödemeniz gerekmiyor.”; 20 kg’den fazla olanlar için de ne kadar ek ücret ödeneceğini hesaplayarak “Fazla bagaj için ….. TL ödemelisiniz.” çıktılarını veren kodu yazınız. Not: Bu soruda kilogram hesabında sadece tam sayıları dikkate alınız. Örneğin 28,70 kilogram olan bagaj için sadece 8 kg için ek ücret ödenmesi yeterlidir.

kilo=float(input("Bagaj ağırlığınızı giriniz (kg): "))
if kilo<=20:
    print("Herhangi bir ücret ödemeniz gerekmiyor.")
else:
    ucret=int(kilo+((kilo-20)*10))
    print("Fazla bagaj hakkı için ",ucret, "TL ödemelisiniz.")

################ÖDEV-8############3
#8-	Kullanıcıdan iki sınav ve bir performans notu girmesini isteyiniz. Girilen 3 notun ortalaması 50 ve daha büyükse “Başarılı”; değilse “Başarısız” çıktıları veren kodu yazınız. b) Bir üçgenin iç açıları toplamı 180 derecedir. Kullanıcının girdiği üç açı değerine göre “Bu bir üçgendir.” ya da “Bu bir üçgen değildir.” çıktıları veren kodu yazınız.
#A)

sinav_1=float(input("1. sınav notunu giriniz: "))
sinav_2=float(input("2.sınav notunu giriniz: "))
perf=float(input("Performans notunu giriniz: "))
ort=(sinav_1+sinav_2+perf)/3
if ort >=50:
    print("Başarılı.")
else:
    print("Başarısız.")

#B)

aci_1=float(input("İlk açı değerini giriniz: "))
aci_2=float(input("İkinci açı değerini giriniz: "))
aci_3=float(input("Üçüncü açı değerini giriniz: "))
toplam=aci_1+aci_2+aci_3
if toplam==180:
    print("Bu bir üçgendir.")
else:
    print("Bu bir üçgen değildir.")








