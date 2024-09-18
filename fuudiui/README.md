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