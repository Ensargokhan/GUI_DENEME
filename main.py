import cv2 as cv
import tkinter as Tk
from PIL import ImageTk, Image
from tkinter .ttk import Combobox

form = Tk.Tk()
form.title("LİHA İHA YER İSTASYANU")
form.geometry("1920x1080")
form.state("zoomed")
form.configure(background= "#2C2C2C")

def pencereyi_ortala(pencere):
    form.update_idletasks()
    genislik = pencere.winfo_width()
    yukseklik = pencere.winfo_height()
    ekran_genislik = form.winfo_screenwidth()
    ekran_yukseklik = form.winfo_screenheight()
    x_konum = (ekran_genislik - genislik) // 2 
    y_konum = (ekran_yukseklik - yukseklik) // 2 
    form.geometry('{}x{}+{}+{}'.format(genislik, yukseklik, x_konum, y_konum))

cerceve_baslik = Tk.Frame(form, width=720, height=100,  bg=form.cget('bg'), borderwidth=10, relief="sunken")
cerceve_baslik.place(x=600, y=10)

baslik_etiketi = Tk.Label(form, text="LİVA İHA YER İSTASYONU",font="Times 20 bold",bg="#2C2C2C",height=2,width=40)
baslik_etiketi.place(x=640,y=26)

img = Image.open("ahter_logo.jpg")

def update_frame():
    success, frame = cap.read()

    if success:
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        img = Image.fromarray(rgb_frame)
        imgtk = ImageTk.PhotoImage(image=img)

        label.imgtk = imgtk
        label.configure(image=imgtk)

    label.after(10, update_frame)

icon = Image.open("ahter_logo.jpg")
photo = ImageTk.PhotoImage(icon)
form.wm_iconphoto(False,photo)

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 720)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

cerceve_kamera = Tk.Frame(form, width=688, height=527, bg="#2C2C2C", borderwidth=20, relief="sunken")
cerceve_kamera.place(x=1040, y=254)

label = Tk.Label(form,width=640,height=480,bg="#2C2C2C")
label.place(x=1060,y=275)

# Görüntüyü yeniden boyutlandırın ve yeni bir değişkende saklayın
resized_image = img.resize((300,200), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

# Tk.Label oluştururken yeni_image değişkenini kullanın
imageLabel = Tk.Label(form, image=new_image)
imageLabel.place(x=0, y=0)

#----------------------------------------------------------------------------------------------------

cerceve_harita = Tk.Frame(form, width=705, height=530, bg="#2C2C2C", borderwidth=20, relief="sunken")
cerceve_harita.place(x=310, y=252)

def boyuta_gore_yeniden_boyutlandir(resim_yolu, genislik, yukseklik):
    # Resmi aç
    orijinal_resim = Image.open(resim_yolu)
    # Belirtilen boyuta yeniden boyutlandır
    yeniden_boyutlandirilmis_resim = orijinal_resim.resize((genislik, yukseklik), Image.ANTIALIAS)
    return ImageTk.PhotoImage(yeniden_boyutlandirilmis_resim)

resim_yolu = "harita.jpg"

# Resmi belirli bir boyuta yeniden boyutlandır
yeniden_boyutlandirilmis_resim = boyuta_gore_yeniden_boyutlandir(resim_yolu, 720, 480)

# Resmi etiketin içine yerleştir
label_harita = Tk.Label(form, image=yeniden_boyutlandirilmis_resim,width=655,height=480)
label_harita.place(x=330,y=272)

cerceve_server = Tk.Frame(form, width=290, height=100, bg="#2C2C2C", borderwidth=10, relief="sunken")
cerceve_server.place(x=340, y=130)

label_serve_ip = Tk.Label(form,text="Server IP:",font="Times 14 bold",padx=10, pady=10,bg="#2C2C2C",fg="white").place(x=350,y=145)
label_server_port = Tk.Label(form,text="PORT:",font="Times 14 bold",padx=10, pady=10,bg="#2C2C2C",fg="white").place(x=350,y=175)
portlar = ["com1","com2","com3","com4","com5"]
kutu = Combobox(form,values=portlar,height=3,background="#2C2C2C").place(x=454,y=185)
label_server = Tk.Label(form,text="ip adresi",font="Times 14 bold",bg="white",fg="black").place(x=455,y=155)     #server ip verisinin geliceği yer

cerceve_rasberry = Tk.Frame(form, width=290, height=100, bg="#2C2C2C", borderwidth=10, relief="sunken")
cerceve_rasberry.place(x=660, y=130)

label_rasberry_ip = Tk.Label(form,text="Rasberry IP:",font="Times 14 bold",padx=10, pady=10,bg="#2C2C2C",fg="white").place(x=670,y=145)
label_rasberry_port = Tk.Label(form,text="PORT:",font="Times 14 bold",padx=10, pady=10,bg="#2C2C2C",fg="white").place(x=670,y=175)
portlar = ["com1","com2","com3","com4","com5"]
kutu = Combobox(form,values=portlar,height=3,).place(x=795,y=185)
label_rasberry = Tk.Label(form,text="ip adresi",font="Times 14 bold").place(x=795,y=155)   #rasberry ip geliceği yer

cerceve_baglanti = Tk.Frame(form, width=200, height=100, bg="#2C2C2C", borderwidth=10, relief="sunken")
cerceve_baglanti.place(x=975, y=130)

def baglandi():
    print("Bağlantı Kuruldu")
buton_baglan = Tk.Button(form,text="Bağlan",fg="black",bg="green",font="Times 10 bold",width=10,height=1,command=baglandi).place(x=1037,y=155)
def baglanti_kes():
    print("Bağlantı Kesildi")
buton_baglanti_kes = Tk.Button(form,text="Bağlantı Kes",fg="black",bg="red",font="Times 10 bold",width=10,height=1,command=baglanti_kes).place(x=1037,y=185)

cerceve_yuk_birak = Tk.Frame(form, width=210, height=100, bg="#2C2C2C", borderwidth=10, relief="sunken")
cerceve_yuk_birak.place(x=1200, y=130)

def yuk_birakildi():
    print("Yük Bırakıldı")
buton_yuk_birak = Tk.Button(form,text="Yükü Bırak",fg="white",bg="red",font="Arial 18 bold",width=12,height=2,command=yuk_birakildi).place(x=1212,y=140)

cerceve_tarih_saat = Tk.Frame(form, width=220, height=100, bg="#2C2C2C", borderwidth=10, relief="sunken")
cerceve_tarih_saat.place(x=0, y=230)

label_tarih = Tk.Label(form,text="Tarih:",font="Times 13 bold",bg="#2C2C2C",fg="white").place(x=47,y=255)
label_tarih_veri = Tk.Label(form,text="10.10.10",font="Times 13 bold").place(x=112,y=255) #tarih verisinin geliceği yer

label_saat = Tk.Label(form,text="Saat:",font="Times 13 bold",bg="#2C2C2C",fg="white").place(x=47,y=285)
label_saaat_veri = Tk.Label(form,text="12.20.51",font="Times 13 bold").place(x=112,y=285) #saat verisinin geliceği yer

cerceve_baglanti_suresi = Tk.Frame(form, width=220, height=100, bg="#2C2C2C", borderwidth=10, relief="sunken")
cerceve_baglanti_suresi.place(x=0, y=350)

label_baglanti_suresi = Tk.Label(form,text="Bağlantı süresi:",font="Times 14 bold",bg="#2C2C2C",fg="white").place(x=15,y=390)
label_baglanti_suresi_veri = Tk.Label(form,text="15.25",font="Times 14 bold").place(x=150,y=390) #bağlantı süresi verisinin geliceği yer

cerceve_hiz_irtifa = Tk.Frame(form, width=220, height=100, bg="#2C2C2C", borderwidth=10, relief="sunken")
cerceve_hiz_irtifa.place(x=0, y=470)

label_hiz = Tk.Label(form,text="Hız:",font="Times 14 bold",bg="#2C2C2C",fg="white").place(x=35,y=490)
label_hiz_veri = Tk.Label(form,text="50",font="Times 14 bold").place(x=86,y=490) #hız verisinin geliceği yer
label_kmh = Tk.Label(form,text="km/h",font="Times 14 bold").place(x=111,y=490)

label_irtifa = Tk.Label(form,text="İrtifa:",font="Times 14 bold",bg="#2C2C2C",fg="white").place(x=35,y=525)
labell_irtifa_verisi = Tk.Label(form,text="50",font="Times 14 bold").place(x=90,y=525) #irtifa verisinin geliceği yer
label_metre = Tk.Label(form,text="metre",font="Times 14 bold").place(x=115,y=525)

cerceve_enlem_boylam = Tk.Frame(form, width=220, height=100, bg="#2C2C2C", borderwidth=10, relief="sunken")
cerceve_enlem_boylam.place(x=0, y=590)

label_enlem = Tk.Label(form,text="Enlem:",font="Times 14 bold",bg="#2C2C2C",fg="white").place(x=20,y=610)
labell_enlem_verisi = Tk.Label(form,text="37,871540",font="Times 14 bold").place(x=100,y=610) #enlem verisinin geliceği yer

label_boylam = Tk.Label(form,text="Boylam:",font="Times 14 bold",bg="#2C2C2C",fg="white").place(x=20,y=645)
labell_boylam_verisi = Tk.Label(form,text="32.498914",font="Times 14 bold").place(x=100,y=645) #boylam verisinin geliceği yer

label_info_box = Tk.Label(form,
                          text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Eum, repellendus.\n Lorem ipsum dolor sit amet consectetur adipisicing elit. Eum, repellendus.\n Lorem ipsum dolor sit amet consectetur adipisicing elit. Eum, repellendus.\n Lorem ipsum dolor sit amet consectetur adipisicing elit. Eum, repellendus.",
                          font="Times 14 bold"
                          ,bg="black"
                          ,fg="white"
                          ,width=129
                          ,height=9
                          ,justify="left")
label_info_box.place(x=310,y=800)

update_frame()

form.mainloop()