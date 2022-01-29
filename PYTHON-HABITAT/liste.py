
      #LİSTE KAVRAMI

# sehirler=["Ankara","Bursa","Çanakkkale","Denzli","Eskişehir"]
# print(sehirler[2])

ders=['k','o','d','l','a','m','a']
print(ders[-1])
print(ders[-4])
print(ders[-3])

asal_sayilar=[2,3,5,7,11,13,17,19,23]
print(asal_sayilar[1:4]) #lisetenin 1.indeksinden başlayarak 4.indekse kadar al ama 4.indeksi alma.
                         # yani 3,5,7

asal_sayilar=[2,3,5,7,11,13,17,19,23]
print(asal_sayilar[5:]) #5. indeksten başlayıp en sona kadar yazdır.

asal_sayilar=[2,3,5,7,11,13,17,19,23]
print(asal_sayilar[:5]) # başlangıcı 0. indektsyen başlatığ 5.indikse kadar yazdır.

asal_sayilar=[2,3,5,7,11,13,17,19,23]
print(asal_sayilar[0:6:2]) #0.indekten başlayıp 6. indekse kadar 2'şer atlayarak yazdır.
                           # 2, 5, 11, 

tek_sayilar=[3,5,7,11,13,17,19]
print(tek_sayilar[0:6])
print(tek_sayilar[2:5])
print(tek_sayilar[3:8])
print(tek_sayilar[:5])
print(tek_sayilar[3:])
print(tek_sayilar[0:8:2])
print(tek_sayilar[::3])

sayi=[20,40,60,80]
print(len(sayi)) # sayı listesinin uzunluğunu yazdır len:4

renkler=["mavi","yeşi,","kırmızı","mor"]
print("mavi"in renkler) #mavi renkler listesinin içinde var mı ? -TRUE

# FONKSİYONLAR: append, exbend, insert, remove, pop, clear, index, count, sort, reverse, copy, del 

#1.append:listenin SONUNA eleman EKLER.
donanim=["yazıcı","klavye","işlemci","bellek","sabit disk","bellek"]
donanim.append("bellek") # listenin EN SONUNA BELLEK yazdır.

#2.extend: listeleri birleştirir.
donanim=["yazıcı","klavye","işlemci","bellek","sabit disk","bellek"]
yazilim=["işletim sistemi","web tarayıcısı"]
donanim.extend(yazilim) #donanımı yazılım ile birleştir.
# ya da  print(donanim+yazilim) olarak da yazılabilir.

#3.insert: listenin istenilen yerine eleman ekler
donanim=["yazıcı","klavye","işlemci","bellek","sabit disk","bellek"]
print(2,"tarayıcı") # 2. indeks tarayıcı olsun geri kalan veriler devam etsin. yerine geçilen veri YOK OLMAZ

#4.remove: listeden değeri verilen eleman silinir
donanim=["yazıcı","klavye","işlemci","bellek","sabit disk","bellek"]
donanim.remove("klavye") # klavye verisini sildir.

#5.pop: listede verilen indeks numarasına göre siler
donanim=["yazıcı","klavye","işlemci","bellek","sabit disk","bellek"]
donanim.pop(1) # donanımda 1. indeksi sildir.
print(donanim)
donanim.pop() # parantezi boş brakırsak son elemanı siler.

#6.clear: listenin tüm elemanını siler.
donanim=["yazıcı","klavye","işlemci","bellek","sabit disk","bellek"]
donanim.clear()
print(donanim)

#7.indeks: listenin içinde istenilen elemanın kaçıncı indekste olduğunu bulur
donanim=["yazıcı","klavye","işlemci","bellek","sabit disk","bellek"]
print(donanim.index("klavye"))

#8.count: Listede kaç belirtilen elemandan kaç tane olduğunu bulur
donanim=["yazıcı","klavye","işlemci","bellek","sabit disk","klavye"]
say=donanim.count("klavye") # donanım listesinde kaç tane klavye yazıldığını buldur
print(say)

#9.sort: listenin elemanların sıralar.
donanim=["yazıcı","klavye","işlemci","bellek","sabit disk","bellek"]
donanim.sort()
print(donanim) 

#10.reverse: sondan başa sıralar
donanim=["yazıcı","klavye","işlemci","bellek","sabit disk","bellek"]
donanim.reverse()

#11.copy: listeyi yeni bir liste olarak kopyalar
donanim=["yazıcı","klavye","işlemci","bellek","sabit disk","bellek"]
yeni_donanim=donanim.copy()
print(yeni_donanim) #donanımı yeni donanım adı altında yeniden kopyaladı

#12.del: istenilen indeksin elemanını siler.
donanim=["yazıcı","klavye","işlemci","bellek","sabit disk","bellek"]
del donanim[2]
print(donanim)
#pop, remove, del fonksiyonları silme işlemi yapar. remove fonksiyonunda verilen değer silinirken pop ve delde indekse göre silme işlemi yapar.

takimlar=["gs","fb","bjk"]
takimlar.append("ts")
print(takimlar)

sebzeler=["lahana","marul","pırasa","ıspanak","fasulye"]
sebzeler.insert(2,"patlıcan")
print(sebzeler)

iller1=["Ankara","İstanbul","Amasya","Kahramanmaraş"]
iller2=iller1.copy()
print(iller2) 

takimlar=["GS","FB","BJK","TS","FB","FB"]
say=takimlar.count("FB")
say_1=takimlar.count("GS")
say_2=takimlar.count("aa")
print(say,say_1,say_2)

sehir1=["Adana","Ankara","Artvin","Amasya","Ağrı"]
sehir2=["Burdur","Balıkesir,""Bursa"]
sehir1.extend(sehir2)
print(sehir1)
sehir2.sort()
print(sehir2)

sebzeler=["Lahana","Marul","Pırasa","Ispanak","Fasulye"]
iller=["Sİvas","Samsun","Sakarya","Sinop","Adana","Ankara"]
print(sebzeler.index("Ispanak"))
print(iller.index("Adana"))
#lower/upper ile büyük küçük duyarlılığını ayarlayabiliriz

liste1=[1,2,3,4,5]
liste2=liste1.copy() #liste2=liste1 de aynı şey demek.
liste1[0]=10 # yzarsak #liste2=liste1 de 2.listeye 10 olarak değiştirmez ama ilk listede biz 10 olarak değiştirdiğimiz için sadece ilk liste değişir.
print(liste2)

#ama böyle ise listede değiştirğini anlayıp direkt çıktıyı değiştirecektir ve liste 2 yi değişmiş haliyle yazacaktır
liste1=[1,2,3,4,5]
liste1[0]=10
liste2=liste1.copy()
print(liste2)


cars=["BMW","Mercedes","Opel","Mazda"]
print(cars)
#
print(len(cars))
#
print(cars[0], cars[-1])
#
cars[-1]="Toyota"
print(cars)
#
print("Mercedes"in cars)
#
print(cars[-2])
#
print(cars[:3])
#
print(cars[-2:-5:-1])
#
cars[-2:]="Renault","Toyota"
print(cars)
#
cars.append("Audi"+"Nissan")
print(cars)
#
#ya da ;
cars_2=["Audi","Nissan"]
#
cars.extend(cars_2)
print(cars)
#
del cars[-1]
print(cars)
#
cars.reverse()
print(cars)
#
cars.sort()
print(cars)
#
#print(dir(list)): birden fazla olan listeleri gösterir.

liste=["ağaç","yapral","toprak","su","ateş"]
liste.clear()
print(liste)

sebzeler=["tarhana","marul","pırasa","ıspanak","fasulye"]
sebzeler.pop(2)
print(sebzeler)

tek_sayilar=[1,3,5,7,9]
cift_sayilar=[2,4,6,8]
tek_sayilar.append(cift_sayilar)
print(tek_sayilar)
#eğer bir grup halinde değilde o grubun içide sayılarmış gibi göstermek istersek APPEND eklemeliyiz
tek_sayilar.extend(cift_sayilar)
print(tek_sayilar)

#Tuple (Demet) Veri tipi: yeni eleman ekleme ya da silmeye izin vermiyor

birimler=("bit","inç","byte","hertz","piksel")
print(birimler)
print(birimler[3])
print(birimler[-2])
print(birimler[1:3])
###
birimler_liste=list(birimler)#burada tuple listeye çevrildi
birimler_liste[2]="mega byte"#listenin indeksi 2 olan elamanına değiştirildi
print(birimler_liste)
# tuple genelde değişmeyen şeylerde kullanılır. Aylar, yıllar, günlerde gibi
#gunler=("Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar")
say=birimler.count("piksel")
print(say)
print(birimler.index("byte"))

  ##DICTIONARY TIPI {}
  #sozluk_adi={anahtar:deger}
sozluk={"Mesleğiniz":"Öğrenci","Alanınız":"Bilişim","Yaşadığınız Yer":"Ankara"}
print(sozluk)
print(sozluk.keys())
print(sozluk.values())

donanim={"Türü":"RAM","Tipi":"DDR4","Kapasitesi":"8GB"}
print(donanim["Türü"])
print("Türü" in donanim)
# ##
donanim["Hızı"]="2400 MHZ" # burada ekleme işlemi yapılmış oluyor.
print(donanim)
# ##
donanim.pop("Kapasitesi") #burada silme işlemi yapılır.
# ##
del donanim #sözlüğü tamamen siler.
print(donanim)
# ##
donanim.clear()
print(donanim)
# ##
yeni_donanim=donanim.copy()
print(yeni_donanim)
# ## 
donanim_1={"Türü":"Sabit Disk","Tipi":"SSD","Kapasitesi":"1 TB"}
donanimlarim={"donanim":donanim,"donanim_1":donanim_1}
print(donanimlarim)
##
#Tuple de remove and pop kullanamayız

kod=("Python","C++","Java")
print(kod)

kod={"Python","C++","Java"} # bu set tir yani kümedir.
print(type(kod))

## SET (KÜME) VERİ TİPİ
 # küme olduğu için içerideki değerleri her daim bir defa sayar
 # genelede matematik fonksiyonlarında kullanılır.
sayilar={1,2,3,4,5} # sayilar={1,2,3,4,5,5,5,5,5,6,6,6}
                    # print(sayilar) derek çıktısı: {1,2,3,4,5,6} olacaktır. yani 5 i bir defa 6yı bir defa yazdıracaktır bize.
sayilar.add(6)
print(sayilar)
# ## birden fazla sayı eklemek istersek
sayilar.update([6,7,8])
print(sayilar)
#  ## silmek için remove VE discard
sayilar.discard(3) # 1,2,3,4,5 teki 3 değerini siliyor
print(sayilar)

dersler=("Python","C++ Dersleri","Java","C++ Dersleri")
# print(dersler[2]) # index numarası istenirse her zaman [] şeklinde yazmamız gerek
dersler2=list(dersler)
dersler2[2]="C#"
print(dersler2)
##
for eleman in dersler: # elemanı derslerin İÇİNDE döndür.
    print(eleman)
##
if "Python Dersleri" in dersler: # "Python Dersleri", derlser İÇERİSNDEYSE EĞER
    print("Aradığınız değerler Tuple içinde mevcut")
##
print(len(dersler))
## ya da bu şekilde yazdırabiliriz.
print("Dersler isimli tuple",len(dersler),"içeriyor")