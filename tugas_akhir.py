def menu():
	print("--------------------------------------------------------")
	print("1. Perkalian")
	print("--------------------------------------------------------\n")
	
def perkalian():
	print("--------------------------------------------------------")
	num = int(input("Masukkan angka perkalian: ")) 
	print("--------------------------------------------------------")
	print("Tabel perkalian")
	for i in range(1,11):  
		print(num,'x',i,'=',num*i)

print("\n")
print("--------------------------------------------------------")           
print("<<<<<<<<<<<< Selamat Datang Di Program Kami >>>>>>>>>>>>")
print("--------------------------------------------------------")
menu()
pilih = int(input("Masukkan pilihan : "))

if(pilih==1):
	perkalian()
else:
	print("")
	print("--------------------------------------------------------")           
	print("<<<<<< Trimakasih Telah Mengunjungi Program Kami >>>>>>>")
	print("--------------------------------------------------------")