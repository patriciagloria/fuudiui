Q: Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

A : 
Checklist 1 : Membuat Proyek Django baru
- Cara saya membuat proyek Django baru adalah dengan membuat direktori di lokal terlebih dahulu, baru setelah itu saya akan membuat virual environmentnya. Setelah itu, saya akan menyiapkan dependencies Django supaya saya bisa akses library, framework, dan package. Dependencies saya buat dengan meng copy requirements.txt, lalu diinstall. Setelah menginstall semua yang saya perlukan, saya menbuat proyek dengan nama fuudiui dengan menjalankan perintah django-admin startproject fuudiui . 

Selanjutnya, karena yang mengakses apliaksi web hanya jaringan saya saja, maka saya memasukkan allowed_host nya adalah ["localhost", "127.0.0.1"]. 

Akhirnya, project dengan nama fuudiui pun selesai.

Checklist 2 : Membuat aplikasi dengan nama main pada proyek tersebut.
- di dalam proyek, ada aplikasi. aplikasi ini untuk melakukan tuga yang lebih kecil dri proyek sehingga lebih mudah dikelola. Proyek sendiri berisi banyak aplikasi. 

- Cara membuat aplikasi adalah dengan membuat direktori baru main dengan cara python manage.py startapp main. 

Checklist 3 :  Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- Karena aplikasi main ini adalah bagian dari proyek, maka main di dafttarkan dulu di baigan settings.py pada proyek (installed_apps)


Chekclist 4 : Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
name
price
description
- di dalam struktur app, ada models.py
- lalu,  kita ubah models.py nya sesuai keinginan kita. karena disini diwajibkan namanya Product, maka kita membuat fungsi dengan nama Product, lalu mendefinisikan setiap atribut wajib dengan fieldnya masing masing (di sini, saya menggunakan CharField untuk nama, TextField untuk desc, dan DeicnalField untuk nomor)

Checklist 5 : Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- lalu, saya membuat direktori template di dalam main. Di dalam folder baru ini, saya membuat .html yang beirsi template untk dimasukkan variabel nama_aplikasi, nama, dan npm yang nantinya akan di set di views.py

Checklist 6 : Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

- urls pada proyek dan pada aplkasi harus dipetakan supaya 
- urls pada app itu untuk mengatur rute URL di dalam aplikasi main. di dalamnya kita akan memetakan fungsi show_main dari views.py agar variabel yang sudah di set di views.py bisa ditampilkan sesuai template html
- polanya kita atur dengan import path (urlpatterns = 
urlpatterns = [
    path('', show_main, name='show_main'),
])

- lalu, kita buka urls di proyek, dan di urlspatterns nya kita tambahkan path ->  urlspatterns = [   path('', include('main.urls')),]

* notes disini kita menggunakan include agar kita impor rute URL APLIKASI ke PROYEK

* pathnya stirng kosong agar halaman main bisa diakses langsungg

Checklist 7 : Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- buat proyek baru di pws -> simpan credentias, lalu tambahkan url deploymen PWS ke allowed host karena sekarang web pbp juga bisa akses
- trus git add, git commit, git push, isi informasi yang diminta di pws, lalu ubah branchjadi main dan selesaii


Q: Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

A : 

[ Client ] 
     |
     | HTTP Request
     v
[ Django Server ]
     |
     | maps request
     v
[ urls.py ]
     |
     | determines function
     v
[ views.py ]
     |
     | processes request
     v
[ models.py ]
     |
     | pake Django ORM
     v
[ Database ]
     |
     | data retrieval/processing
     v
[ views.py ]
     |
     | renders HTML dgn data yg sudah di set
     v
[ HTML Template ]
     |
     | return HTML response
     v
[ Client ]

- penjelasan 
Bagan sederhana dari request client ke web aplikasi berbasis Django menggambarkan alur mulai dari client yang mengirimkan request HTTP ke server Django. Pertama, request diterima oleh Django dan dipetakan melalui urls.py, yang berfungsi sebagai peta rute untuk menentukan fungsi apa yang harus dijalankan dari views.py. views.py kemudian memproses request tersebut, dan jika diperlukan data dari database, ia akan memanggil models.py untuk berinteraksi dengan database menggunakan ORM Django. Setelah data diproses, views.py mengembalikan respon dalam bentuk halaman HTML, di mana data tersebut dirender menggunakan template dari berkas HTML yang sesuai. Hasil akhirnya adalah respon HTML yang dikirimkan kembali ke client sebagai tampilan akhir dari aplikasi.

Q: Jelaskan fungsi git dalam pengembangan perangkat lunak!

A : Git berfungsi sebagai sistem kontrol versi yang membantu pengembang perangkat lunak untuk melacak perubahan dalam kode sumber selama pengembangan. Dengan Git, pengembang dapat bekerja secara kolaboratif, mengelola versi kode yang berbeda, dan menggabungkan perubahan dari berbagai kontributor tanpa kehilangan atau menimpa kode yang sudah ada. Ini penting dalam pengembangan perangkat lunak modern karena memungkinkan pengelolaan kode secara efisien dan aman.

Q: Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

A : Django sering dijadikan framework awal untuk pembelajaran pengembangan perangkat lunak karena struktur dan dokumentasinya yang jelas. Django juga menggunakan pola MVC (Model-View-Controller) yang membantu pemahaman tentang pemisahan logika bisnis dan tampilan, yang merupakan dasar dari banyak framework lain. Selain itu, Django relatif mudah digunakan untuk pemula tetapi cukup kuat untuk proyek skala besar, membuatnya ideal sebagai pengenalan bagi pemula.


Q: Mengapa model pada Django disebut sebagai ORM?

A : Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai jembatan antara database relasional dan kode Python. ORM memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek Python, tanpa perlu menulis SQL langsung. Ini mempermudah pengelolaan data karena pengembang cukup bekerja dengan objek dan metode dalam bahasa yang sudah mereka kenal, sementara ORM mengurus penerjemahan operasi-operasi ini ke dalam query SQL yang sesuai.