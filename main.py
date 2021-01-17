# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger

print("Selamat datang di kalkulator sederhana")
mathArray = []
getInput = True
while getInput:
	  inp = input("Silahkan pilih menu yang anda inginkan" + \
	  	          "\n1. Tambah Operasi Matematika" + \
	  	          "\n2. Lihat Hasil\n")
	  if (int(inp) == 1):
	  	 mathInput = input("Masukan Operasi Matematika : ")
	  	 mathArray.append(mathInput)
	  if (int(inp) == 2):
	  	 print(arithmetic_arranger(mathArray))
	  	 getInput = False

