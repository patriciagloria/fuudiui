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
