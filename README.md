# TUGAS 2
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
- lalu, saya membuat direktori template di dalam main. Di dalam folder baru ini, saya membuat .html yang beirsi template untk dimasukkan variabel nama_aplikasi, nama, dan kelas yang nantinya akan di set di views.py

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

# TUGAS 3
Q : Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
A : Data delivery penting karena platform butuh ngirim dan nerima data biar semua fitur bisa jalan sesuai rencana. Misal, kalo platformnya web atau aplikasi, data delivery ini bikin kita bisa dapet info user, kirim data dari server ke client, dan sebaliknya. Tanpa data delivery, aplikasi tidak akan bisa interaktif dan data yang ditampilin bisa jadi tidak up-to-date.

Q : Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
A : A: JSON dianggap lebih baik dibandingkan XML  karena strukturnya yang lebih sederhana dan lebih mudah dibaca oleh manusia. JSON memiliki format yang lebih ringkas dan tidak perlu banyak tag seperti XML. Selain itu, JSON juga lebih cepat di parsing sama banyak bahasa pemrograman, jadi buat lebih banyak orang akan memilihj JSON karena rasanya lebih praktis dan efisien.



Q : Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
A : is_valid() dipake untuk ngecek apakah data yang diisi di form udah sesuai aturan yang kita tetapkan atau belum. Method ini nge-validasi input berdasarkan rules yang ada di form, misalnya ngecek tipe data, panjang karakter, atau format yang sesuai. Tanpa is_valid(), kita tidak bisa yakin data yang masuk itu valid atau nggak, yang bisa jadi nambahin bug atau error di web kita.

Q : Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
A : csrf_token dibutuhin buat ngelindungin aplikasi dari serangan CSRF (Cross-Site Request Forgery). CSRF itu serangan di mana penyerang mencoba melakukan aksi tanpa izin dengan memanfaatkan sesi pengguna yang sedang aktif.Misalnya, user lagi login di sebuah aplikasi, dan tanpa disadari, user meng-klik link atau mengunjungi situs berbahaya yang sudah diset oleh penyerang buat kirim request palsu ke aplikasi tadi. Kalau tidak ada csrf_token, request palsu ini bisa diterima dan dieksekusi seolah-olah itu beneran dari user asli, kayak transfer uang atau ubah data penting. Dengan csrf_token, setiap form submission harus menyertakan token unik yang di-generate khusus buat sesi itu, jadi kalau request datang tanpa token atau dengan token yang salah, server bakal tolak requestnya.

Q : Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- CP 1 Membuat input form untuk menambahkan objek model pada app sebelumnya.
A :  Pertama, bikin form di forms.py dalam app yang udah ada. Di forms.py udah ada ProductForm, yang pake ModelForm buat model Product. Jadi form ini udah otomatis masukin field kayak name, price, dan description

Di views.py, ada fungsi create_product_entry yang nge-handle request buat nampilin form dan nyimpen data. Di sini dicek kalo request-nya POST dan form valid pake is_valid(). Kalo valid, form bakal di-save dan user bakal di-redirect ke halaman utama.

Template create_product.html buat nampilin form. Di dalamnya, form dirender pake {{ form.as_table }} dan dikirim lewat POST. Lalu masukin {% csrf_token %} agar aman dari CSRF.

- CP 2 Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
A : Pertama, buat 4 fungsi di views.py
show_xml dan show_json buat nampilin semua objek.
show_xml_by_id dan show_json_by_id buat nampilin objek berdasar ID.

lalu serialize data -> pake Django serializers buat ubah data jadi XML atau JSON, kayak serializers.serialize("xml", data) buat XML.

terakhir, cek akses URL /xml/, /json/, /xml/<id>/, /json/<id>/, terus cek kalo datanya muncul sesuai format yang diminta. Misal, kalo ngeakses pake ID, harusnya yang muncul data sesuai ID itu aja.

- CP 3 Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
A : Di urls.py, tambahin path buat semua views tadi:

path('create-product-entry', create_product_entry, name='create_product_entry') buat form input produk.
path('xml/', show_xml, name='show_xml') dan path('json/', show_json, name='show_json') buat nampilin data dalam XML dan JSON.
path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id') dan path('json/<str:id>/', show_json_by_id, name='show_json_by_id') buat nampilin data berdasar ID.

lalu, kita tingal tes akses tiap URL sesuai path yang udah dibikin dan memastikan semuanya memberikan respons yang benar

Q : BUKTI POSTMAN
A : 
![](https://drive.google.com/drive/folders/12QARfz82-MZwKnaSW74mKAjs8bU3RwUU?usp=sharing)

# TUGAS 4
1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
perbedaanya adalah HttpResponseRedirect() menerima parameter URL. Berbeda dengan redirect() yang dapat menerima mode, view name, dan juga bisa URL sama seperti HttpResponse. Dalam program ini, HttpResponseRedirect dibantu menggunakan reverse(). reverse() adalah yang bertugas untuk mencari tau URL dari suatu view, barulah URL dari reverse ini di pass ke HttpResponseRedirect(). Contohnya, kita bisa redirect('main:login') atau bisa juga HttpResponseRedirect('main:login')

2. Jelaskan cara kerja penghubungan model Product dengan User!
Cara kerja penghubungan model dengan User adalah dengan membuat user sebagai foreign key di model *Product* kita, sehingga setiap *Product Instance* itu linked ke *User instance*. Untuk secara teknis, akan dijelaskan di nomor 5 di *checkpoint* ke-3

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authetication adalah pemeriksaan/verifikasi. Contohnya, ketika kita login kita akan ditanya username dan password. Jika Username tidak ada di data ataupun password yang dimasukkan salah, maka user tidak bisa login/ lanjut ke step berikutnya. 

Setelah authentication, maka ada authorization. Authorization ini adalah yang mengontrol akses apa yang diberikan terhadap user yang TELAH diverifikasi. Dalam program ini, user bisa add entry product.

Authentication selalu lebih dulu dibandingkan authorization. Dalam Django, cara mengimplementasikannya adalah dengan cara import dari *django.contribu.auth* yaitu Authentication Form. 
*form = AuthenticationForm(request)*

Lalu untuk Authorization, dalam program ini adalah **hanya user yang terverifikasi** yang bisa akses ke halaman main (show_main)
Karena itu, di views.py kita import *from django.contrib.auth.decorators import login_required* dan menambahkan *@login_required* di atas fungsi show_main

4.  Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang udah login dengan pake session. Jadi, pas kita login, Django bikin session yang dihubungin sama cookie di browser kita. Cookie ini nyimpen ID session, jadi tiap kali kita akses halaman, Django bisa tau itu kita karena cookie tersebut dikirim lagi ke server.

Selain itu, cookies digunakan untuk menyimpan preferensi user sehingga cookies bisa tau apa yang user ini biasa set sehingga tidak perlu berkali-kali. Misalnya, user A biasa memakai bahasa inggris. Dengan cookies, maka web dapat '*mengingat*' preferensi bahasa dari user A. 

Tidak semua cookies aman digunakan karena bisa dicuri datanya atau bisa jadi ada yang menyusupkan script jahat di dalam cookies, serangan CSRF atau pencurian data. Karena itu, perlu set cookies dengan benar dan memasang flag HttpOnly atau Secure agar data lebih aman.

5. Jelaskan cara kamu mengimplementasikan semua *checklist* diatas

- Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
Caranya, pertama kita harus membuat form registrasi terlebih dahulu. Kita harus mengimport User Creation Form dan messages yang sudah tersedia dari django. 

### Registrasi
Setelah itu, kita membuat fungsi register di views.py. Guna dari fungsi ini adalah untuk menghasilkan form regist secara otomatis dengan *form = UserCreationForm(request.POST)* dan mengyimpan akun pengguna ketika data disubmit di form. Setelah membuat fungsi ini di views.py, kita -> membuat template dari register (dengan *register html*) ->mendaftarkan fungsi register dan pathnya pada *urls.py* 

Setelah membuat form registrasi, maka kita bisa melanjutkan ke login dan logout

### Login
Buka views.py dan import authenticate, login , dan Authentication Form. Ini adalah fungsi dari Django sehingga kita bisa melakukan autentikasi dan login dengan hanya memakai (tidak perlu dari awal). 

Lalu -> buat fungsi login_user di views.py. pada login_user, form akan kita autentikasi / validasi apakah pengguna dapat login dengan username dan password yang benar (*form = AuthenticationForm(data=request.POST)*) Jika benar, kita akan memakai *login(request, user)* untuk login.

Setelah membuat fungsi ini di views.py, kita -> membuat template dari login (dengan *login.html*) ->mendaftarkan fungsi login dan pathnya pada *urls.py* 


### Logout
Buka views.py dan import logout. *logout(request)* ini akan digunakan agar sesi yang saat ini dihapus. Lalu, buat fungsi logout_user. Pada fungsi ini, kita akan mengimplementasikan logout dan redirect user ke halaman login dengan *return redirect('main:login')* ini adalah cara untuk menginstruksikan browser untuk pergi ke url yang ditentukan oleh *login* view di aplikasi main

### Tambahan 
agar halaman main (show_main) HANYA dapat diakses dengan login terlebih dahulu, maka kita harus merestriksi halaman main. Caranya adalah dengan import *login_required* pada views.py, lalu **sebelum** fungsi show_main, maka kita menambahkan *@login_required(login_url='/login')*


- Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
Untuk membuat akun, maka kita menjalankan virtual environment -> python -m venv env ->  env\Scripts\activate -> python manage.py runserver. lalu buka [localhost](http://localhost:8000/) dan buat 2 akun pengguna dan 3 dummy data.

- Menghubungkan model Product dengan User.
Tujuan kita menghubungkan model Product dengan User adalah agar main page hanya menampilkan data milik user tersebut. Cara menghubungkan model product dengan user adalah : 
1 - ke models.py lalu import *user*, dan masukkan data *user = models.ForeignKey(User, on_delete=models.CASCADE)* ke dalam class Product

2 - setelah itu, ke views.py. di dalam fungsi create_product_entry, setelah kita memastikan bahwa formnya valid, kita menahan agar form jangan di save dlu dengan perintah *product_entry = form.save(commit=False)*, lalu set agar *product.user = request.user*. Gunanya adalah agar program mengetahui bahwa user yang saat ini sedang log in adalah user yang terkait dengan product saat ini (product user). Setelah itu, barulah kita save form nya dengan product_entry.save()

3 - kemudian di dalam fungsi show_main, kita memfilter data yang ditujukkan dengan : *product_entries = Product.objects.filter(user=request.user)*

4- karena kita mengupdate model, maka jangan lupa untuk migrate dengan
*python manage.py makemigrations*
*python manage.py migrate*

- Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
cara menampilkan informasi pengguna yang sedang login adalah dengan -> views.py, lalu di context name, kita ubah jadi *'nama' : request.user.username,*. 

Selain itu, kita akan menambahkan informasi last login pada page main. Caranya adalah dengan bantuan *cookies*. 
Import yang telah kita perlukan (datetime, HttpResponseRedirect, reverse). Lalu, kita akan  : 
->  set cookies ketika user login *response = HttpResponseRedirect(reverse("main:show_main"))*
*response.set_cookie('last_login', str(datetime.datetime.now()))*
->  menampilakn data last_login di halaman show_main dengan request cookies *'last_login': request.COOKIES['last_login']*
-> hapus cookies saat logout.*response = HttpResponseRedirect(reverse('main:login'))*
*response.delete_cookie('last_login')*

Setelah mengatur semua fungsi, kita tinggal menambahkan tampilan *sesi terakhir login* pada *main.html*

# TUGAS 5

1.  Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Saat ada beberapa CSS selector yang berlaku untuk satu elemen HTML, browser menentukan mana yang diterapkan berdasarkan specificity dan urutan penulisannya. Specificity diukur berdasarkan jenis selector yang digunakan, di mana selector dengan spesifisitas lebih tinggi akan memiliki prioritas lebih tinggi. Sebagai contoh, selector ID (#id) memiliki prioritas lebih tinggi dibandingkan dengan selector kelas (.class) atau tag (div).

Selain specificity, jika dua selector memiliki tingkat prioritas yang sama, maka yang ditulis terakhir dalam file CSS akan diutamakan. Inline styles yang ditulis langsung di atribut style pada elemen HTML memiliki prioritas tertinggi dibandingkan selector lainnya. Dengan memahami urutan prioritas ini, pengembang dapat menulis CSS yang lebih efektif dan menghindari konflik antar gaya yang diterapkan pada elemen yang sama.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design penting dalam pengembangan aplikasi web karena pengguna mengakses internet melalui berbagai perangkat dengan ukuran layar yang berbeda, seperti smartphone, tablet, dan desktop. Dengan menerapkan responsive design, tampilan website dapat menyesuaikan secara otomatis sehingga tetap nyaman dan mudah digunakan di semua perangkat. Ini meningkatkan pengalaman pengguna dan memastikan bahwa konten dapat diakses dengan baik tanpa perlu zoom atau scroll berlebihan.

Contoh aplikasi yang sudah menerapkan responsive design adalah Instagram dan Twitter, di mana antarmuka mereka secara dinamis menyesuaikan dengan ukuran layar perangkat yang digunakan. Sebaliknya, banyak website lama perusahaan atau beberapa forum online masih menggunakan layout tetap yang tidak responsif, membuat navigasi dan membaca konten menjadi sulit di perangkat mobile. Implementasi responsive design membantu memastikan bahwa aplikasi web tetap relevan dan kompetitif di era perangkat mobile yang terus berkembang.
3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin, border, dan padding adalah tiga properti CSS yang digunakan untuk mengatur ruang di sekitar elemen, namun masing-masing memiliki fungsi yang berbeda. Margin mengatur ruang di luar border elemen, berfungsi sebagai jarak antara elemen satu dengan lainnya. Misalnya, margin: 20px; akan memberikan ruang 20 piksel di sekitar elemen tersebut. Border adalah garis pembatas di sekitar elemen yang dapat diatur ketebalan, gaya, dan warnanya, seperti border: 2px solid black;.

Sementara itu, padding mengatur ruang di dalam border elemen, antara border dan konten elemen. Contohnya, padding: 15px; akan memberikan ruang 15 piksel di dalam elemen tersebut. 
4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox dan Grid adalah dua teknik layout di CSS yang sangat membantu saya dalam mengatur elemen-elemen di halaman web dengan lebih mudah dan fleksibel. Flexbox (Flexible Box Layout) dirancang untuk mengatur elemen dalam satu arah, baik itu secara horizontal maupun vertikal. Misalnya, saat saya ingin membuat navigasi yang rapi atau menyusun item dalam satu baris yang dapat menyesuaikan ukuran layar, Flexbox adalah pilihan yang tepat. Dengan Flexbox, saya bisa dengan mudah mengatur jarak antar elemen, menyelaraskan posisi mereka, dan memastikan semuanya tetap teratur meski ukuran layar berubah-ubah.

Di sisi lain, Grid Layout menawarkan kemampuan yang lebih powerful karena memungkinkan saya mengatur elemen dalam dua dimensi sekaligus, yaitu baris dan kolom. Ini sangat berguna ketika saya ingin membuat layout yang lebih kompleks seperti halaman utama dengan header, sidebar, konten utama, dan footer. Grid memudahkan penempatan elemen di area tertentu tanpa harus repot mengatur posisi satu per satu. Dengan Grid, saya bisa menciptakan desain yang lebih terstruktur dan responsif, memastikan tampilan web tetap menarik di berbagai perangkat. Kombinasi Flexbox dan Grid memungkinkan saya untuk membangun layout yang fleksibel dan terorganisir dengan baik tanpa banyak kesulitan.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

-  Implementasikan fungsi untuk menghapus dan mengedit product.
Caranya adalah dengan pertama-tama menambahkan dahulu taiwind ke aplikasi, lalu buat fungsi edit_product di views.py dan juga membuat edit_product.html. Lalu, atur urlnya dan juga menambahkan button pada main.html. Begitu juyga dengan delete. Saya membuat terlebih dahulu delete_product di views, lalu atur url dan buat button di main.html

-  Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma)
Saya bisa mulai dengan menambahkan file CSS eksternal untuk bg login ke dalam HTML, lalu menulis aturan-aturan gaya untuk mengubah warna, font, margin, padding, dan elemen lainnya. Misalnya, dengan mengubah properti background-color atau font-family, saya dapat memberikan nuansa yang berbeda pada halaman web. Selain itu, saya juga  menggunakan selektor kelas dan ID untuk menargetkan elemen tertentu dan menerapkan gaya yang lebih spesifik.  Kustomisasi ini memungkinkan saya untuk menciptakan tampilan yang unik dan sesuai dengan identitas merek atau preferensi pribadi.

# TUGAS 6
Q : Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
A : Dengan JavaScript, saya bisa membuat halaman web yang interaktif dan dinamis. Misalnya, saat saya ingin menambahkan efek animasi, validasi form di sisi pengguna, atau membuat konten yang bisa berubah tanpa perlu me-refresh seluruh halaman, JavaScript lah yang memungkinkan hal itu. Selain itu, JavaScript juga mendukung komunikasi asinkron dengan server melalui teknologi seperti AJAX. Ini memungkinkan saya untuk mengambil data dari server dan memperbarui bagian tertentu dari halaman tanpa harus memuat ulang seluruh halaman. Hasilnya, pengalaman pengguna jadi lebih mulus dan responsif.


Q : Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
A : Pengambilan data selesai sebelum melanjutkan eksekusi kode berikutnya. Ini memastikan bahwa kita mendapatkan respons dari server sebelum mencoba memprosesnya, sehingga mencegah error akibat data yang belum tersedia.

Jika kita tidak menggunakan await, kode akan berjalan secara asinkron dan mungkin mencoba memproses respons sebelum data diterima, yang dapat menyebabkan error atau hasil yang tidak diinginkan. Tanpa await, fetch() mengembalikan Promise yang belum terpenuhi, sehingga data yang kita harapkan mungkin belum siap saat kita mencoba menggunakannya.

Q :  Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
A : Kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST karena Django secara default menerapkan perlindungan CSRF pada semua request POST. Jika kita tidak menonaktifkan perlindungan ini atau tidak mengirim token CSRF dengan benar, request AJAX kita akan ditolak oleh server.

Dengan menambahkan @csrf_exempt, kita memberitahu Django untuk tidak memeriksa token CSRF pada view tersebut, sehingga request AJAX bisa diproses. Namun, penting untuk diingat bahwa ini dapat membuka celah keamanan, jadi sebaiknya tetap mengirim token CSRF dalam request AJAX dan tidak menggunakan @csrf_exempt jika memungkinkan.

Q : Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Melakukan pembersihan data input di backend sangat penting karena kita tidak bisa sepenuhnya mengandalkan frontend untuk validasi data. Pengguna bisa memanipulasi frontend atau mengirim request langsung ke server tanpa melalui interface yang kita sediakan, sehingga data berbahaya bisa masuk jika hanya melakukan validasi di frontend.

Dengan memvalidasi dan membersihkan data di backend, kita memastikan bahwa semua data yang masuk aman dan sesuai dengan yang diharapkan, terlepas dari bagaimana data tersebut dikirim. Ini membantu mencegah berbagai serangan seperti SQL Injection atau Cross-Site Scripting (XSS) yang dapat membahayakan aplikasi kita.

Q : Mengimplementasikan checklist : 
- AJAX GET
 1. Ubahlah kode cards data mood agar dapat mendukung AJAX GET.
ntuk mendukung AJAX GET pada produk, saya sudah menambahkan elemen kosong di halaman utama di dalam main.html untuk menampung daftar produk. Ini dilakukan dengan menggunakan elemen <div id="product_entry_cards"></div>. Kontainer ini akan diisi secara dinamis setelah data produk diambil menggunakan AJAX. Selanjutnya, saya akan menulis fungsi JavaScript di dalam main.html yang menggunakan fetch() untuk mengambil data produk dari server dan memasukkannya ke dalam elemen ini tanpa perlu reload halaman. Disini dapat terlihat dari main.html dibagian async function getProductEntries() dan async function refreshProductEntries().

 2. Lakukan pengambilan data mood menggunakan AJAX GET. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.
Untuk memastikan data yang diambil hanyalah produk milik pengguna yang login, saya akan menggunakan fetch() untuk melakukan request GET ke endpoint yang mengembalikan daftar produk berdasarkan request.user. Di server-side, di views.py, query sudah difilter untuk hanya mengambil produk milik pengguna yang login. Fungsi show_json() akan memastikan bahwa hanya data yang relevan dengan pengguna tersebut yang dikembalikan.
def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

Setelah mendapatkan respons JSON dari server, JavaScript akan memproses data tersebut dan menampilkan produk-produk yang sesuai ke dalam elemen #product_entry_cards. Dengan ini, produk-produk langsung ditampilkan di halaman tanpa perlu reload seluruh halaman.
- AJAX POST
 1. Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan mood.
Untuk membuat tombol yang membuka modal, saya sudah menambahkan tombol ini di bagian sidebar dalam main.html:
<button onclick="showModal()" class="w-32 h-12 bg-[#ec6841] rounded-lg flex items-center justify-center cursor-pointer">
    <span class="text-[#fbe6d2] font-bold">Add New Product by AJAX</span>
</button>
Tombol ini akan memanggil fungsi showModal() yang akan membuka modal produk menggunakan JavaScript. Fungsi showModal() mengubah tampilan modal dari hidden menjadi terlihat dengan animasi, seperti berikut:
function showModal() {
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');
    modal.classList.remove('hidden');
    setTimeout(() => {
      modalContent.classList.remove('scale-95', 'opacity-0');
      modalContent.classList.add('scale-100', 'opacity-100');
    }, 50);
}

2. Modal di-trigger dengan menekan suatu tombol pada halaman utama. Saat penambahan mood berhasil, modal harus ditutup dan input form harus dibersihkan dari data yang sudah dimasukkan ke dalam form sebelumnya. Jika penambahan gagal, tampilkan pesan error.
Setelah pengguna menambahkan produk melalui form di modal, saya menggunakan fungsi addProductEntry() yang menangani request AJAX. Jika produk berhasil ditambahkan, modal akan ditutup dan form akan dibersihkan menggunakan kode berikut:
async function addProductEntry() {
    const csrftoken = getCSRFToken();
    try {
      const response = await fetch("{% url 'main:add_product_entry_ajax' %}", {
        method: "POST",
        body: new FormData(document.getElementById('productEntryForm')),
        headers: {
          'X-CSRFToken': csrftoken,
          'Accept': 'application/json',
        }
      });

      if (response.status === 201) {
        await refreshProductEntries();
        document.getElementById("productEntryForm").reset(); 
        hideModal();  // Tutup modal setelah berhasil
      } else {
        const errorData = await response.json();
        console.error('Failed to add product entry:', errorData);
      }
    } catch (error) {
      console.error('Error:', error);
    }
}

 3. Buatlah fungsi view baru untuk menambahkan mood baru ke dalam basis data.
 Untuk membuat fungsi view yang menambahkan produk baru, kita ke file views.py. 
 @csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    user = request.user

    if not price:
        return HttpResponse(b"Price is required.", status=400)

    try:
        price = float(price)
    except ValueError:
        return HttpResponse(b"Invalid price value.", status=400)

    new_product = Product(name=name, description=description, price=price, user=user)
    new_product.save()

    return HttpResponse(b"CREATED", status=201)



 4. Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.
 Di file urls.py, kita bisa membuat path baru yang mengarah ke view untuk menambahkan product dengan menambahkan baris path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),


 5. Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.
 Form yang ada di dalam modal bisa dihubungkan dengan path /create-ajax/ melalui penggunaan AJAX, dalam hal ini menggunakan addProductEntry()  yang mengirimkan data form menggunakan fetch()
 fetch("{% url 'main:add_product_entry_ajax' %}", {
    method: "POST",
    body: new FormData(document.getElementById('productEntryForm')),
    headers: {
      'X-CSRFToken': csrftoken,
      'Accept': 'application/json',
    }
});


 6. Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar mood terbaru tanpa reload halaman utama secara keseluruhan.
 Untuk menampilkan daftar menu terbaru tanpa me-refresh seluruh halaman, kita bisa menggunakan AJAX GET untuk mengambil data terbaru dan menampilkannya secara dinamis di halaman. async function refreshProductEntries() {
    try {
      const productEntries = await getProductEntries();
      let htmlString = "";
      if (productEntries.length === 0) {
        document.getElementById("no_products_message").classList.remove("hidden");
        document.getElementById("product_entry_cards").classList.add("hidden");
      } else {
        document.getElementById("no_products_message").classList.add("hidden");
        document.getElementById("product_entry_cards").classList.remove("hidden");
        productEntries.forEach((item) => {
          const name = DOMPurify.sanitize(item.fields.name);
          const price = DOMPurify.sanitize(item.fields.price);
          const description = DOMPurify.sanitize(item.fields.description);
          htmlString += `
            <div class="bg-[#fffaf2] border-4 border-[#ec6841] rounded-xl p-6 flex flex-col items-center space-y-4 shadow-md">
              <h3 class="text-xl font-semibold text-center">${name}</h3>
              <div class="w-full bg-[#FFC24C] rounded-lg p-4 text-center">
                <p class="text-gray-800">${description}</p>
              </div>
              <div class="flex items-center justify-between w-full mt-4">
                <span class="text-[#ec6841] text-lg font-bold">${price}</span>
              </div>
            </div>
          `;
        });
      }
      document.getElementById("product_entry_cards").innerHTML = htmlString;
    } catch (error) {
      console.error('Error refreshing product entries:', error);
    }
}



