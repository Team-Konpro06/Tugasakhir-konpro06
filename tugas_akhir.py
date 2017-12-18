def menu():
	print("--------------------------------------------------------")
	print("1. Perkalian")
	print("2. Upah Karyawan")
	print("3. Biodata")
	print("4. Keluar Dari Program")
	print("--------------------------------------------------------\n")
	pilih = int(input("Masukkan pilihan : "))
	return pilih
	
def perkalian():
	print("--------------------------------------------------------")
	num = int(input("Masukkan angka perkalian: ")) 
	print("--------------------------------------------------------")
	print("Tabel perkalian")
	for i in range(1,11):  
		print(num,'x',i,'=',num*i)
	print("--------------------------------------------------------\n")

def upah_karyawan():
	print("Menghitung upah kerja karyawan perminggu")
	print("")
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
	
def biodata():
	print("")
	print("--------------------------------------------------------")
	print("======================== Biodata =======================")
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

	print("--------------------------------------------------------")
	print("===================== Biodata Anda =====================")
	print("--------------------------------------------------------")
	print("Nama: ",nama)
	print("Alamat: ",alamat)
	print("Tempat Tanggal Lahir: ",ttl)
	print("Jenis Kelamin: ",jk)
	print("Agama: ",agama)
	print("Pekerjaan: ",pekerjaan)
	print("Hoby: ",hoby)
	print("Kata Mutiara: ",km)
	print("--------------------------------------------------------\n")
	
print("\n")
print("--------------------------------------------------------")           
print("<<<<<<<<<<<< Selamat Datang Di Program Kami >>>>>>>>>>>>")
print("--------------------------------------------------------")

pilih = True
while(pilih<4):
	pilih = menu()
	if(pilih==1):
		perkalian()
	elif(pilih==2):
		upah_karyawan()
	elif(pilih==3):
		biodata()
	else:
		print("")
		print("--------------------------------------------------------")           
		print("<<<<<< Trimakasih Telah Mengunjungi Program Kami >>>>>>>")
		print("--------------------------------------------------------")