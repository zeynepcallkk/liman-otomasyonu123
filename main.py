import tkinter as tk
from tkinter import Tk
import time

# pencere oluşturma
pencere = Tk()

# pencere başlığı verme
pencere.title("LİMAN OTOMASYONU")

# pencere boyutlandırma
pencere.attributes('-fullscreen', True)

# pencereden çıkış tuşu için fonksiyon tanımlama
def kapat(event):
    pencere.destroy()

#çıkış tuşunu esc olarak ayarlama
pencere.bind("<Escape>", kapat)


# menüye saniye sayacı ekleme
saniye_sayaci = 0
def update_saniye():
    global saniye_sayaci
    saniye_sayaci += 1
    sayac.config(text=f"Saniye: {saniye_sayaci}")
    pencere.after(1000, update_saniye)  # Her 1 saniyede bir günceller


sayac = tk.Label(pencere, text="0", font=("Times New Roman", 12), fg="black")
sayac.grid(row=0, column=0, padx=5, pady=0)
update_saniye()


#tir için sınıf oluşturma
class Tir:

    with open('olaylar.csv', 'r') as dosya:
        # Dosya okunur ve her satır eleman olarak listeye eklenir
        tir_liste1 = [satir.split(",") for satir in dosya.readlines()]
        # Başlıklar olan ilk eleman listeden atılır
        tir_liste1.pop(0)
        # Maliyet kısmının sonunda oluşan '\n' ifadesinden kurtulma
        for i in tir_liste1:
            i[6] = i[6][:-1]

    #tır listesine erişim fonskiyonu
    def tir_liste(listet=tir_liste1):
        return listet


    #tır bilgisi sorgulama fonksiyonu
    def tir_sorgulama(plaka, bilgiler=tir_liste1):
        tbilgiler = {}
        for liste in bilgiler:
            if plaka in liste:
                print(liste)
                tbilgiler['Plaka'] = str(plaka)
                tbilgiler['Yükün gideceği ülke'] = liste[2]
                tbilgiler['20 tonluk konteynır adet'] = liste[3]
                tbilgiler['30 tonluk konteynır adet'] = liste[4]
                tbilgiler['Yük miktarı'] = liste[5]
                tbilgiler['Maliyet'] = liste[6]
                break
        # plakasına göre sorgulanan tır için sözlük oluşturulur
        # sözlük menüye yazılır
        label_listesi = []  # Label'ları tutacak liste
        row_index = 4  # Başlangıç satırı
        for anahtar, deger in tbilgiler.items():
            yazi = f"{anahtar} : {deger}"
            label = tk.Label(pencere, text=yazi)
            label.grid(row=row_index, column=1, padx=0, pady=0)
            label_listesi.append(label)
            row_index += 1

    # tirları geliş zamanına göre bir sözlüğe ekleme
    def gelis_zamani_t(liste = tir_liste()):
        gelmis_tir={}

        for tirlar in liste:
            if tirlar[0] in gelmis_tir:
                gelmis_tir[tirlar[0]].append(tirlar)
            else:
                gelmis_tir[tirlar[0]] = [tirlar]
        sirali_tir_liste = {}
    # sözlüğe eklenmiş tırların aynı zamanda gelenlerini
    # sorted ile plaka numarasına göre küçükten büyüğe sıralama

        for anahtar, deger in gelmis_tir.items():
            sirali_deger = sorted(deger, key=lambda x: int(((x[1]).split("_"))[-1]))
            sirali_tir_liste[anahtar] = sirali_deger

        return sirali_tir_liste


class Gemi:
    with open('gemiler.csv', 'r') as dosya:
        # Dosya okunur ve her satır eleman olarak listeye eklenir
        gemi_liste = [satir.split(",") for satir in dosya.readlines()]
        # Başlıklar olan ilk eleman listeden atılır
        gemi_liste.pop(0)
        # Maliyet kısmının sonunda oluşan '\n' ifadesinden kurtulma
        for i in gemi_liste:
            i[3] = i[3][:-1]

    #gemi bilgisi sargulama fonksiyonu
    def gemi_sorgulama(plaka, bilgiler=gemi_liste):
        gbilgiler = {}
        for satir in bilgiler:
            if plaka == satir[1]:
                gbilgiler['Gemi Adı'] = str(plaka)
                gbilgiler['Yükün gideceği ülke'] = satir[3]
                gbilgiler['Kapasite'] = satir[2]
                break

    #sorgulanan gemi numarasına göre verileri yazdırır
        label_listesi = []  # Label'ları tutacak liste
        row_index = 4  # Başlangıç satırı
        for anahtar, deger in gbilgiler.items():
            yazi = f"{anahtar} : {deger}"
            label = tk.Label(pencere, text=yazi)
            label.grid(row=row_index, column=2, padx=0, pady=0)
            label_listesi.append(label)
            row_index += 1


def istifleme(tir=Tir.tir_liste()):
    istif_alanlari = [0, 0]  # İstif alanlarındaki toplam tonajı temsil eder

    # Listedeki plaka numarasının sayı kısmına göre liste elemanlarını sıralar
    sirali_liste = sorted(tir, key=lambda x: int(((x[1]).split("_"))[-1]))

    # Kapasiye kontrolü ile alana istif yapılır
    for i in range(len(istif_alanlari)):
        if istif_alanlari[i] < 750:
            for tir in sirali_liste:
                istif_alanlari[i] += int(tir[5])
                if istif_alanlari[i] > 750:
                    istif_alanlari[i] -= int(tir[5])
                    print(f"{i + 1}. istif alanı doldu !")
                    break
                print(istif_alanlari)

ssayac = 0
labels= []
def tir_gelisi():
    global tir_label_frame
    global tir_canvas
    global tir_label_inside
    global ssayac

    ssayac += 1
    print(ssayac)

    # Tir modülünden liste al
    liste = Tir.gelis_zamani_t()

    for anahtart, degert in liste.items():
        if int(anahtart) == ssayac:
            for tirlar in degert:
                print(tirlar)
                text = tirlar
                label = tk.Label(tir_label_inside, text=text, font=("Times New Roman",15))
                label.pack()
                labels.append(label)
                tir_label_inside.update_idletasks()

    # Canvas içeriğinin boyutunu güncelle
                tir_canvas.update_idletasks()
                tir_canvas.config(scrollregion=tir_canvas.bbox("all"))

    # En üstteki etiketi göster
                tir_canvas.yview_moveto(0)

    # Önceki etiketleri aşağı kaydır
                tir_canvas.yview_scroll(1, "units")
                if len(labels) > 9:  # Önceki etiketlerin sayısını sınırlandırma
                    labels[0].destroy()
                    del labels[0]

    tir_label_inside.after(1000, tir_gelisi)
    
#Tir listesinin olacağı label frame oluşturma
tir_label_frame = tk.LabelFrame(pencere, text="Tır Listesi")
tir_label_frame.grid(row=1, column=0, padx=10, pady=10)

tir_scrollbar = tk.Scrollbar(tir_label_frame)
tir_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tir_canvas = tk.Canvas(tir_label_frame, yscrollcommand=tir_scrollbar.set)
tir_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

tir_scrollbar.config(command=tir_canvas.yview)

tir_label_inside = tk.Frame(tir_canvas)
tir_canvas.create_window((0, 0), window=tir_label_inside, anchor=tk.NW)



scrollbar = tk.Scrollbar(pencere)
istif2_label_frame = tk.LabelFrame(pencere, text="İstif Alanı 2")
istif2_label_frame.grid(row=1, column=2, padx=10, pady=10)
istif2_canvas = tk.Canvas(istif2_label_frame, yscrollcommand=scrollbar.set)
istif2_scrollbar = tk.Scrollbar(istif2_label_frame, orient=tk.VERTICAL, command=istif2_canvas.yview)
istif2_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
istif2_canvas.config(yscrollcommand=istif2_scrollbar.set)


gemi_label_frame = tk.LabelFrame(pencere, text="Gemi Listesi")
gemi_label_frame.grid(row=1, column=3, padx=10, pady=10)
gemi_canvas = tk.Canvas(gemi_label_frame, yscrollcommand=scrollbar.set)
gemi_scrollbar = tk.Scrollbar(gemi_label_frame, orient=tk.VERTICAL, command=gemi_canvas.yview)
gemi_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
gemi_canvas.config(yscrollcommand=gemi_scrollbar.set)

istif1_label_frame = tk.LabelFrame(pencere, text="İstif Alanı 1")
istif1_label_frame.grid(row=1, column=1, padx=10, pady=10)
istif1_canvas = tk.Canvas(istif1_label_frame, yscrollcommand=scrollbar.set)
istif1_scrollbar = tk.Scrollbar(istif1_label_frame, orient=tk.VERTICAL, command=istif1_canvas.yview)
istif1_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
istif1_canvas.config(yscrollcommand=istif1_scrollbar.set)


istif1_label_inside = tk.Label(istif1_label_frame, text="")
istif1_label_inside.pack(padx=100, pady=100)
istif2_label_inside = tk.Label(istif2_label_frame, text="")
istif2_label_inside.pack(padx=100, pady=100)


tir_sorgula = tk.Entry()
tir_sorgula.grid(row=3, column=1, padx=00, pady=00)
tir_sorgulama_butonu = tk.Button(text="Tır Bilgisi Sorgula", command=lambda: Tir.tir_sorgulama(tir_sorgula.get()))
tir_sorgulama_butonu.grid(row=2, column=1, padx=10, pady=10)

gemi_label_inside = tk.Label(gemi_label_frame, text="")
gemi_label_inside.pack(padx=150, pady=100)
gemi_sorgula = tk.Entry()
gemi_sorgula.grid(row=3, column=2, padx=00, pady=00)
gemi_sorgulama_butonu = tk.Button(text="Gemi Bilgisi Sorgula", command=lambda: Gemi.gemi_sorgulama(gemi_sorgula.get()))
gemi_sorgulama_butonu.grid(row=2, column=2, padx=10, pady=10)


tir_gelisi()

pencere.mainloop()