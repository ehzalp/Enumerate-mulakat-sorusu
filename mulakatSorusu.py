############################
# ENUMERATE mülakat sorusu
############################
#divide_students fonksiyonu yazınız
#çift indexte yer alan öğrencileri bir listeye alınız
#tek indekste yer alan öğrencileri başka bir listeye alınız
#fakakt bu iki liste tek bir liste olarak return olmalı

students = ["John", "Mark", "Venessa", "Mariam"]


def divide_students(students):
    groups = [[], []] #öğrencilere işlem yapıldıktan sonra grup listesinin içerisinde indexlere göre eleman gönderiminde kullanılacak listelerin tek bir liste olarak tanımlanması
    for index, student in enumerate(students): #enumerate ile indeks üzerinde işlem yapma
        if index % 2 == 0: #indeksi çift olan elemanları 1. gruba ekleme işlemi
            groups[0].append(student)
        else: #çift olmayanları ikinci gruba ekleme işlemi
            groups[1].append(student)
    print(groups)
    return groups #iki listenin tek bir liste olarak tanımlanmasıyla return etme 

