# latihan01

Cara menggunakan Library Random.uniform dengan Python

1.  Langkah pertama 
     Lalu setelah anda membuka IDLE Python, klik menu file lalu pilih new file (ctrl+N).

![1](https://user-images.githubusercontent.com/46732630/52874052-125be580-3183-11e9-89a7-2216936f8495.png)

2.  Langkah kedua
     Kemudian mulai ketik codingannya text editor python dengan mengetik seperti dibawah ini :

print("==================================================")
print(" Nama  	: Winda Yulianti")
print(" Kelas 	: TI.18.A1")
print(" NIM 	: 311810518")
print("==================================================")

import random
jumlah = int(input("Masukan nilai n: "))
print()
for i in range(jumlah):
	i = random.uniform(0.0,0.5)
	print(i)
print("selesai")

3.  Langkah ketiga

n=input("Masukkan nilai n :") 

Sintaks ini berfungsi untuk memasukkan nilai "n"

for i in range(jumlah):

     Pada sintaks ini akan menampilkan perulangan bilangan random yang nilai nya sesuai dengan nilai n yang di input sebelumnya.

n= random.uniform(0.0, 0.5) 

random.uniform digunakan untuk menampilkan bilangan float random dengan batas awal bilangan x, dan batas akhir bilangan y. Pada sintaks ini akan menampilkan bilangan random yang batas awalnya 0.0, dan batas akhirnya 0.5.

Untuk menjalankannya, klik run lalu klik Run Module F5 lalu simpan dengan membuat nama file lalu tekan ENTER, untuk lebih jelas perhatikan gambar di bawah ini :

![2](https://user-images.githubusercontent.com/46732630/52874832-46d0a100-3185-11e9-84a6-13315ae473dd.png)

3.  Langkah keempat
     Lalu masukkan jumlah (n)nya. Dan tekan enter, lalu akan muncul seperti pada gambar berikut ini :

![3](https://user-images.githubusercontent.com/46732630/52875882-12aaaf80-3188-11e9-87d5-00e217ced848.png)

Selesai

Berikut penjelasan singkat mengenai fungsinya : 

1. While
     Perulangan dilakukan selama keadaan masih TRUE, akan dilakukan pengecekan kondisi terlebih dahulu sebelum blok kode dieksekusi.

2. For
      Eksekusi terhadap blok kode dilakukan berulang kali sesuai dengan variable yang mengatur perulangan.

3. Break
      untuk menghentikan looping ketika terjadi kondisi tertentu.
