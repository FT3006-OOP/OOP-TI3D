Class adalah Prototipe yang ditentukan pengguna untuk objek yang mendefinisikan atribut dari suatu objek atau rancangan/blue print dari sebuah objek
Instance adalah Objek individu dari class tertentu, dengan salinan class dengan nilai sebenarnya 
Hubungan antara class dan instance adalah class adalah cetak biru yang digunakan untuk menggambarkan bagaimana membuat sesuatu, instance adalah objek yang dibuat dari cetak biru tersebut
Sintaks python untuk menentukan class baru adalah class PythonclassName:
konvensi ejaan untuk nama class adalah PythonclassName()
bagaimana memberi instantiate, atau membuat instance dari sebuah class dengan cara menggunakan nama class diikuti dengan tanda kurung. jika nama classnya Hero(), maka Heronya adalah - my_class = Hero()
bagaimana mengakses atribut dan prilaku instance class yaitu Dengan notasi titik contohnya instance_name.attribute_name
metode adalah jenis fungsi yang didefinisikan didalam suatu class
tujuan self adalah setiap metode merujuk pada instance class yang menurut konvensi diberi nama self. Dalam __init__metode ini, self mengacu pada objek yang baru dibuat; sementara dalam metode lain, selfmengacu pada contoh yang metode namanya disebut. Untuk lebih lanjut tentang __init__vs self atau untuk  memanggil sebuah variabel dan sebuah method yang ada pada dirinya sendiri
tujuan dari __init__ metode adalah menginisialisasi sebuah instance dari suatu class