# -*- coding: utf-8 -*-
#Gerekli kütüphaneleri içe aktarma
from Tkinter import *
import os
from tkFileDialog import *
import getpass

#Etkinleştirme için anahtarı tanımlama
anahtar = "83545-92736-18593"
#Anahtarın etkinleştirilip etkinleştirilmediğinin kaydını tutan dosyayı okuma
anahtar_etkin = open("anahtar_etkin.txt", "r")
etkin_mi = anahtar_etkin.read()
#Eğer etkin değilse:
if etkin_mi == 0 or etkin_mi == "0" or etkin_mi == "0\n":
	#Etkinleştirme penceresini ayarlama
	etkinlestir = Tk()
	etkinlestir.geometry("+350+250")
	etkinlestir.title("Lisans Etkinlestir")
	etkin_etiket = Label(etkinlestir, text="Lutfen lisans anahtarini yazin:")
	etkin_etiket.pack()
	etkin_giris = Entry()
	etkin_giris.pack()
	#Hizmet şartlarını kabul etme kutularının değerlerini atama ve paketleme
	var1 = IntVar()
	var2 = IntVar()
	kutu1 = Checkbutton(text="Hizmet sartlarini okudum ve kabul ediyorum", variable=var1)
	kutu2 = Checkbutton(text="Hizmet sartlarini okumadim ama kabul ediyorum", variable=var2)
	kutu1.pack()
	kutu2.pack()
	#Etkinleştirme komutu
	def etkin():
		#Yazılan veriyi okuma
		yazilan = etkin_giris.get()
		#Yazılan veri anahtar ile aynı ise:
		if yazilan == anahtar:
			if var1.get() == 1 or var2.get() == 1:
				#Kayıt dosyasını aç
				yeni_etkin = open("anahtar_etkin.txt", "w")
				#Kayıt dosyasının değerini 1 olarak ata ve sonra dosyayı kapat
				yeni_etkin.write("1")
				yeni_etkin.close()
				#Etkinleştirmenin tamamlandığını bildiren geri bildirim penceresini ayarlama
				etkin_toplevel = Toplevel()
				etkin_toplevel.geometry("+370+270")
				etkin_toplevel.title("Etkinlestirildi")
				#Geri bildirim penceresini kapatma düğmeleri
				tamamdir = Label(etkin_toplevel, text="Etkinlestirme islemi tamamlandi.\nLutfen uygulamayi yeniden baslatin.")
				tamamdir.pack()
				etkin_kapat = Button(etkin_toplevel, text="Tamam", command=etkinlestir.quit, bg="dark blue", fg="white")
				etkin_kapat.pack()
			#Hizmet şartları kabul edilmediyse:
			else:
				#Hatayı gösteren geri bildirim penceresi
				kabul_hata = Toplevel()
				kabul_hata.title("Hizmet kosullari")
				kabul_hata.geometry("+370+270")
				kabul_etiket = Label(kabul_hata, text="Lutfen hizmet kosullarini kabul edin")
				kabul_etiket.pack()
				kabuledilmedi_dm = Button(kabul_hata, text="Tamam", fg="white", bg="dark blue", command=kabul_hata.destroy)
				kabuledilmedi_dm.pack()
		#Girilen veri anahtara eşit değilse:
		else:
			hata_toplevel = Toplevel()
			hata_toplevel.geometry("+370+270")
			hata_toplevel.title("Etkinlestirilemedi :(")
			tamamdegil = Label(hata_toplevel, text="Bir hata olustu :( Kodu dogru \nyazdiginizdan ve aralara '-' isareti \nkoydugunuzdan emin olun.")
			tamamdegil.pack()
			hata_toplevel_kapat = Button(hata_toplevel, text="Tamam", command=hata_toplevel.destroy, bg="dark blue", fg="white")
			hata_toplevel_kapat.pack()
	#Etkinleştirme komutunu çalıştıran düğme
	etkin_dugme = Button(etkinlestir, text="Etkinlestir", command=etkin, bg="dark blue", fg="white")
	etkin_dugme.pack()
	anahtar_etkin.close()
	mainloop()
else:
	#Pencereyi ayarlama
	pen = Tk()
	#Pencere rengi
	pen.tk_setPalette("#c0defa")
	#Pencere boyutları
	pen.geometry("660x400+150+30")
	#Pencere başlığı
	baslik = pen.title("Not Defteri 4")
	#Pencere simgesi
	simge = PhotoImage(file="nd_ikon.gif")
	pen.tk.call('wm', 'iconphoto', pen._w, simge)
	#Metin kutusu için dikey bir kaydırma çubuğu oluşturma
	cubuk = Scrollbar(pen)
	cubuk.pack(side=RIGHT, fill=Y)
	#Metin kutusunu oluşturma ve kaydırma çubuğuna bağlama
	metin = Text(yscrollcommand=cubuk.set, bg="white", undo=1)
	metin.pack(expand=1, fill=BOTH)
	#Kaydetme komutunu ayarlama
	def kaydet():
		#Metni okuma ve kaydetme için işlem başlatma
		yazi = metin.get(1.0, END)
		islem = asksaveasfile(mode="w", defaultextension=".txt")
    islem.write(yazi)
    islem.close()
		#Geri bildirim penceresi
    pen2 = Toplevel()
    pen2.geometry("280x50+280+320")
    baslik2 = pen2.title("Kaydedildi")
    simge7 = PhotoImage(file="nd_kaydedildi.gif")
    pen2.tk.call('wm', 'iconphoto', pen2._w, simge7)
    kaydedildi = Label(pen2, text="Dosya basariyla kaydedildi.")
    kaydedildi.pack()
    kaydedildi_kapat = Button(pen2, text="Tamam", command=pen2.destroy, bg="light green", fg="dark blue")
    kaydedildi_kapat.pack()
	#Yedekleme komutu
	def yedekle():
		#Metni okuma
		yedeklenecek = metin.get(1.0, END)
		#Ve metni yedekleme dosyasına yazma
		yedek_ac = open("yedek_dosya.txt", "w")
		yedek_ac.write(yedeklenecek)
		yedek_ac.close()
	#Yedeği yükleme komutu
	def yedek_yukle():
		#Yedeğin yazılı olduğu dosyayı okuyup aktarma ve kapatma
		acilacak = open("yedek_dosya.txt", "r")
		yedek_metin = acilacak.read()
		#Yedek metin yoksa yedek olmadığını gösteren geri bildirim
		if yedek_metin == "" or yedek_metin == " " or yedek_metin == "	":
			metin.delete(1.0, END)
			metin.insert(END, "Su anda hicbir yedeginiz yok. Bir metni yedeklemek icin 'Yedekler' menusuden 'Yedekle'ye tikalyin(Bu islemi yaptiginizda daha onceden bir yedeginiz varsa silinir.")
		#Yedek varsa içe aktarma
		else:
			metin.delete(1.0, END)
			metin.insert(END, yedek_metin)
			acilacak.close()
	#Dosya açma komutu
	def dosya_ac():
		#Dosyayı okuma, içe aktarma ve kapatma
		dosya_adi = askopenfilename()
		dosya = open(dosya_adi, "r")
		dosya_icerik = dosya.read()
		dosya.close()
		duzenle = open(dosya_adi, "a")
		metin.delete(1.0, END)
		metin.insert(END, dosya_icerik)
		duzenle.close()
	#Yardım menüsünün komutu
	def destek():
		pen3 = Toplevel()
		pen3.geometry("300x170+180+280")
		baslik3 = pen3.title("Yardim")
		simge3 = PhotoImage(file="nd_yardim_destek.gif")
		pen3.tk.call('wm', 'iconphoto', pen3._w, simge3)
		#Yardım metni
		yardim_metni = Label(pen3, text="Ustteki buyuk kutucuga kaydedilecek metni yazin.\nDosya kaydetmek icin dosyanin adini\n'Dosya Adi' yazan yere yazin.\nDaha sonra 'Kaydet'e basin ve klasor secin.\nDosyayi varolan baska bir dosyanin\nuzerine yazmak icin 'Uzerine Kaydet'e basin\nDosya acmak icin 'Dosya Ac' dugmesine basip\ndosya secin.", fg="blue")
		yardim_metni.pack()
		yardim_kapat = Button(pen3, text="Yardim'i Kapat", command=pen3.destroy, fg="dark blue", bg="light green")
		yardim_kapat.pack()
	#Hakkında menüsünün komutu
	def hakkinda():
		pen6 = Toplevel()
		baslik6 = pen6.title("Hakkinda")
		simge6 = PhotoImage(file="nd_yardim_destek.gif")
		pen6.tk.call('wm', 'iconphoto', pen6._w, simge6)
		surum = Label(pen6, text="Not Defteri Uygulamasi - Surum 4.x", fg="blue")
		surum.pack()
		hakkinda_yazi = Label(pen6, text="Cetin Yazilim 2014", fg="dark green")
		hakkinda_yazi.pack()
		lisans_etiket = Label(pen6, text="Cetin Yazilim'in Lisansli urunudur", fg="blue")
		lisans_etiket.pack()
		hakkinda_kapat = Button(pen6, text="Hakkinda'yi Kapat", command=pen6.destroy, bg="red", fg="white")
		hakkinda_kapat.pack()
	#Menüleri ayarlama
	#Menü çubuğu oluştur
	menu = Menu(pen)
	#Menü çubuğunu pen penceresine tuttur
	pen.config(menu=menu)
	#Menü çubuğu menülerini oluştur
  dosyaislemleri = Menu(menu, tearoff=0)
	yedeklemeler = Menu(menu, tearoff=0)
	yardim = Menu(menu, tearoff=0)
	#Menüleri göster
  menu.add_cascade(label="Dosya", menu=dosyaislemleri)
	menu.add_cascade(label="Yedekler", menu=yedeklemeler)
	menu.add_cascade(label="Yardim", menu=yardim)
	#Menülere komutları tuttur
  dosyaislemleri.add_command(label="Kaydet", command=kaydet)
  dosyaislemleri.add_command(label="Dosya Ac", command=dosya_ac)
  dosyaislemleri.add_command(label="Kapat", command=pen.quit)
	yardim.add_command(label="Yardim", command=destek)
	yardim.add_command(label="Hakkinda", command=hakkinda)
	yedeklemeler.add_command(label="Yedekle", command=yedekle)
	yedeklemeler.add_command(label="Yedegi Yukle", command=yedek_yukle)
	#Kaydırma çubuğunu tamamla
	cubuk.config(command=metin.yview)
	#Grafiksel döngü oluştur
	mainloop()
