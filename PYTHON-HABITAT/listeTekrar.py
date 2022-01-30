
ders=["b","İ","l","i","ş","i","m"]
ders.sort()
print(ders)
# ##
ders.reverse()
print(ders)
# ##
a=ders.count("i")
print(a)
# ##
del ders[4:6]
print(ders)
# ##
ders.remove("ş")
ders.pop(4)
print(ders)
# ##
del ders[4:]
ders.append("M")
print(ders)
# ##
alan=ders.copy()
print(alan)
print(ders.index("l"))

sayilar=[35,26,81,64]
sayilar.sort()
print(sayilar)
# ##
sayilar.reverse()
print(sayilar)
# ##
print(sayilar.index(26))
# ## 
ondalikliSayilar=[1.4,6.8]
sayilar.extend(ondalikliSayilar)
print(sayilar)
# ##

meyveler=["elma","çilek","armut"]
alisveris_listesi=["süt","peynir",meyveler]
print(alisveris_listesi)
print(len(alisveris_listesi))
print(alisveris_listesi[0])
print(alisveris_listesi[1])
print(alisveris_listesi[2])
# ya da böyle yazabiliriz tek tek yazıp kodu uzatmamk yerine
for i in alisveris_listesi:
    print(i) # a lışveriş list. içerisinde her elemanı i ye atıyor ve tek tek döndürüryor

bellek=["RAM","ROM"]
ekran_kartlari=["Paylaşımlı","Paylaşımsız"]
sabit_diskler=["SSD"]
birimler=bellek,ekran_kartlari,sabit_diskler # araya + operatörü koysak da çıktımız aynı olacaktır fakat ayrı ayrı liste gibi değilde sanki biirmlerin yeni bir elemanıymış gibi söterir.
print(birimler)

sozluk={"Bilim İnsanı":"Aziz SANCAR","Şair":"Mehmet Akif ERSOY","Astronom":"Ali Kuşçu"}
meslekler=sozluk.copy()
print(meslekler)
# ##
print(sozluk.values())
# ##
sozluk.clear() # sözlüğün içini tamamen siler
print(sozluk)
##
sozluk["Matematikçi"]="Cahit ARF" # burada ekleme işlemi yapılmış oluyor.
print(sozluk)
# ##
print('sanatçılar' in dict.keys(sozluk)) # sözlüğün keys kısmının içinde sanatçılar diye kavram var mı? TRUE/FALSE
# ##
print(sozluk["Şair"]) # diyince values olan Şairin keys değerini yani Mehemt Akif ERSOY u ekrana yazdırır.
# ##
print("Ali Kuşçu" in dict.values(sozluk)) # sözluk değerinde Ali Kuşçu var mı ? TRUE/FALSE
# ## Ya da ;
print("Ali Kuşçu" in sozluk.values())
sozluk["Bilim İnsanı"]="Canan DAĞDEVİREN" # Bilim insanı diye bir keys var ve onun yerine başka bir şey yazmak istersek güncelleme yapar fakat öyle bir eleman yoksa o listenin içine yeni bir eleman ekliyor
print(sozluk)

notlar={"Erdal":83,"Arzu":88,"Yaren":48}
name=input("Adınız: ")
sinav_notu=int(input("Notunuzu giriniz"))
notlar[name]=sinav_notu # kullanıcıdan adını ve sınav notunu istedikten sonra notlar[KEYS]=VALUES şeklinde olduğu için listeye yazdırmış oldu
print(notlar)

ogrenciNotlari={"Arzu":90,"Erdal":60,"Sumeyra":70,"Dua":90,"Meryem":100,"Yaren":90}
top=0
for i,j in ogrenciNotlari.items():
    print("Öğrenci Adı: {0}\t Notu :{1}".format(i,j))
    top+=j
print("Ortalama :{}".format(top/len(ogrenciNotlari)))


notlar={"erdal":{"Mat":45,"Eng":78,"Phys":78,"Science":77},"arzu":{"Mat":45,"Eng":78,"Phys":78,"Science":77}}

onemli_telefonlar={"Acil Çağrı Merkezi":"112","Polis İmdat":"155","Milli Eğitim Bakanlığı İletişim Merkezi":"444 0 632"}
print(onemli_telefonlar.values())
# print(dir(dict))
# print(dir(list))
onemli_telefonlar.pop("Acil Çağrı Merkezi")
print(onemli_telefonlar)
##
if "Sağlık Merkezi" in dict.keys(onemli_telefonlar): #in onemli_telefonlar diye de yazdırabilirdik yani keys dememize gerek yok.
     print("var")
else:
     print("yok")
# ##

#print(dir(set)) yazdırarak kümelerin(Sets) hangi methodları kullanabileceğimizi görebiliyoruz

kume={"Python",'c',4,"Cahit","Python"} # Kümede aynı şeyin birkaç defa yazılmasına rağmen çıktı onu bir defa alır.
# print(len(kume))
kumeler=list(kume) #'set' object is not subscriptable hatası veriyor. Indexleme yapmadığı için indexini okuyabilmek için ÇEVİRME İŞLEMİ yapmamız gerekti. Bunu da LIST e çevirerek yeni bir eleman oluşturduk.
print(kumeler[3])
##

kume={1,2,3,4,5}
kume.add(6)
print(kume)
##
kume_2={7,8,9,10}
kume.update(kume_2)
print(kume)
##
kume={1,2,3,4,5,6}
kume.remove(4)  #4 ü siler.
print(kume)
kume.remove(8) # KeyError: 8 hatası verir çünkü 8 diye bir değer yok kümenin içinde
print(kume)
##
kume.discard(8) # hata vermez kümenin kendisini ekrana yazdırır.
print(kume)
##
# #POP kümlerde İLK ELEMANI SİLMEYE yarar.
kume.pop() # ilk sayıyı tutmaya yarıyor
print(kume) # ilk sayıyı tuttuğumuz için geri kalanları yazdırıyor
print(kume.pop()) # tutulan sayıyı yazdırıyor
##
#print(A.union(B.union(C.union))) 3 kümeyi birleştiriyor.

#intersection= kesişim  -> print(A.intersection(C)); print(A.intersection(b.intersectin(C)))
#frozenset(kısıtlnamış küme): kısıtlı işlemler yapan küme methodu silme,ekleme,değiştirme gibi işlemler falan yapamıyor
#kisitli_kume=frozenset(["Python",3.14,5,'A'])
#print(dir(frozenset))
#print(type(kisitli_kume)) -> <class 'frozenset'>
#frozenset({5,3.14,'Python','A'})
