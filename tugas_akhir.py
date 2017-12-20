def menu():
	print("===================== Menu Pilihan =====================")
	print("--------------------------------------------------------")
	print("1. Perkalian")
	print("2. Upah Karyawan")
	print("3. Biodata")
	print("4. Menghitung Saldo")
	print("5. Calender")
	print("6. Keluar Dari Program")
	print("--------------------------------------------------------")
	pilih = int(input("Masukkan pilihan : "))
	return pilih
	
def perkalian():
	print("\n")
	print("----------------------- Perkalian ----------------------")
	print("--------------------------------------------------------")
	num = int(input("Masukkan angka perkalian: ")) 
	print("--------------------------------------------------------")
	print("Tabel perkalian")
	for i in range(1,11):  
		print(num,"x",i,"=",num*i)
	print("--------------------------------------------------------\n")
	print("\n")

def upah_karyawan():
	print("\n")
	print("------- Menghitung upah kerja karyawan perminggu -------")
	print("--------------------------------------------------------")
	nama = str(input("Nama Anda: "))
	jkerja = int(input("Masukan Jam Kerja: "))
	upahperjam = int(input("Upah Per Jam: Rp."))
	if(jkerja<=24):
		upahtotal = (jkerja*upahperjam)*7
	else:
		upahtotal = jkerja*upahperjam+24*upahperjam
	print("Upah kerja dalkam 1 minggu: Rp.",upahtotal)
	print("--------------------------------------------------------")
	print("Karyawan",nama,"menerima upah perminggu: Rp.",upahtotal)
	print("--------------------------------------------------------\n")
	print("\n")
	
def biodata():
	print("\n")
	print("------------------------ Biodata -----------------------")
	print("--------------------------------------------------------")
	nama= str(input("Masukan Nama Anda: "))
	alamat= str(input("Masukan Alamat: "))
	ttl= str(input("Masukan Tempat Tanggal Lahir Anda: "))
	jk= str(input("Jenis Kelamin: "))
	agama= str(input("Masukan Agama: "))
	pekerjaan= str(input("Pekerjaan: "))
	hoby= str(input("Masukan Hoby: "))
	km= str(input("Kata Mutiara: "))
	print("--------------------------------------------------------\n")

	print("--------------------- Biodata Anda ---------------------")
	print("--------------------------------------------------------")
	print("Nama:",nama)
	print("Alamat:",alamat)
	print("Tempat Tanggal Lahir:",ttl)
	print("Jenis Kelamin:",jk)
	print("Agama:",agama)
	print("Pekerjaan:",pekerjaan)
	print("Hoby:",hoby)
	print("Kata Mutiara:",km)
	print("--------------------------------------------------------\n")
	print("\n")
	
def menghitung_saldo():
	print("\n")
	print("------------0=[]==> MENGHITUNG SALDO <==[]=0------------")
	print("--------------------------------------------------------")
	tabungan = int(input("Masukkan jumlah tabungan: "))
	lama = int(input("Masukkan jumlah lama menabung (bulan): "))
	 
	if tabungan < 1000000 :
		sukuBunga = 0.03
		saldoAkhir = (tabungan * sukuBunga) * lama + tabungan
		print("")
		print("Karena tabungan anda dibawah Rp. 1.000.000, bunga yang anda dapatkan adalah 3%")
		print("")
		print("Maka setelah menabung selama",lama,"bulan, saldo anda adalah Rp.",saldoAkhir)
 
	elif tabungan > 1000000 :
		 sukuBunga = 0.04
		 saldoAkhir = (tabungan * sukuBunga) * lama + tabungan
		 print("")
		 print("Karena tabungan anda diatas Rp. 1.000.000, bunga yang anda dapatkan adalah 4%")
		 print("")
		 print("Maka setelah menabung selama",lama,"bulan, saldo anda adalah Rp.",saldoAkhir) 
	print("--------------------------------------------------------\n")
	print("\n")
	
def calender():
	print("\n")
	print("----------------------- Calender -----------------------")
	print("--------------------------------------------------------")
	import calendar  
	 
	yy = int(input("Masukan Tahun: "))  
	mm = int(input("Masukan Bulan: "))  
	  
	print(calendar.month(yy,mm)) 
	print("--------------------------------------------------------\n")
	print("\n")
	
print("\n")           
print(">>>>>>>>>>>> Selamat Datang Di Program Kami <<<<<<<<<<<<")
print("\n")

pilih = True
while(pilih<6):
	pilih = menu()
	if(pilih==1):
		perkalian()
	elif(pilih==2):
		upah_karyawan()
	elif(pilih==3):
		biodata()
	elif(pilih==4):
		menghitung_saldo()
	elif(pilih==5):
		calender()
	else:
		print("\n")           
		print(">>>>>>> Trimakasih Telah Mengunjungi Program Kami <<<<<<")
		print("\n")
