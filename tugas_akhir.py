def menu():
	print("--------------------------------------------------------")
	print("1. Perkalian")
	print("2. Keluar Dari Program")
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

print("\n")
print("--------------------------------------------------------")           
print("<<<<<<<<<<<< Selamat Datang Di Program Kami >>>>>>>>>>>>")
print("--------------------------------------------------------")

pilih = True
while(pilih<2):
	pilih = menu()
	if(pilih==1):
		perkalian()
	else:
		print("")
		print("--------------------------------------------------------")           
		print("<<<<<< Trimakasih Telah Mengunjungi Program Kami >>>>>>>")
		print("--------------------------------------------------------")

