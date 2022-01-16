#####number_1=int(input("lütfen birinci sayıyı giriniz: "))
#####number_2=int(input("lütfen ikinci sayıyı giriniz: "))
#####number_3=int(input("lütfen üçüncüsayıyı giriniz: "))
#####ort = (number_1+number_2+number_3)/3
#####if ort<50 :
 #####   print("kaldınız.")
 #####   if ort <=25 :
 #####       print("notunuz düşük")       
#####else :
    #####print("geçtiniz")
    #####print(ort)

#vize=float(input("Vize notunuz: "))
#final=float(input("final notunuz: "))
#sonuc=(vize*0.4)+(final*0.6)
#if sonuc >= 60:
 #   print("Dersten geçtiniz. Ortalamanız :",sonuc)
#else:
 #   print("Dersten kaldınız. Ortalamanız: ",sonuc)

#vize=float(input("Vize notunuz: "))
#final=float(input("final notunuz: "))
#sonuc=(vize*0.4)+(final*0.6)
#if sonuc >= 60 and float(final)>=60:
#    print("Dersten geçtiniz. Ortalamanız :",sonuc)
#else:
#    print("Dersten kaldınız. Ortalamanız: ",sonuc)




#vize=float(input("Vize notunu giriniz: "))
#final=float(input("final notunu giriniz: "))
#gecmeNotu=(vize*0.4)+(final*0.6)
#if final >=60 :
#    if gecmeNotu<60: # Bu if kısmı üstteki if final notunu kapsıyor. final notu 60tan küçükse hemen alttaki if değeri çalışır.
#        print("Kaldınız.", gecmeNotu)
#    else:
#        print("geçtiniz ", gecmeNotu)
#else: #bu da final kısmı 60dan büyük eşit değil ise çalışır diğer ifin içindeki ifi çalıştırmadan buraya bakar
#    print("Kaldınız")

#sayi=float(input("lütfen bir sayı giriniz."))
#if sayi<1 and sayi>100:
#    print("HATALI GİRİŞ", sayi)
#else:
#    pass

#parola=input("Lütfen bir parola oluşturunuz: ")
#uzunluk=len(parola) #Karakter sayısını saymamız gerektiği için len uzantısıyla bu değeri görebildik.
#if uzunluk<8:
#    print("parolanız zayıf")
#else:
#    print("parolanız güçlü")


sinav_notu=int(input("Lütfen sınav notunuzu giriniz: ")) 
if sinav_notu >=80 and sinav_notu<=100:
    sinav_notu=sinav_notu + 10 #sinav_notu += 10 da aynı anlama gelir.
    print("Sınav sonucunuz=",sinav_notu)
elif sinav_notu >60 and sinav_notu<80 :
    sinav_notu=sinav_notu + 5
    print("Sınav sonucunuz=",sinav_notu)
elif sinav_notu<=45:
    sinav_notu=sinav_notu - 5 #sinav_notu -= 5 de aynı anlama
    print("Sınav sonucunuz=",sinav_notu)
elif sinav_notu>100:
    print("Geçersiz not girdiniz.")
else:
    print(sinav_notu)

 
