# Bagan Request Client ke Web Aplikasi Berbasis Django
Di bawah ini merupakan bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya.
![Bagan_Audrey](/Bagan_Audrey.png)


# Proses Yang Terjadi Pada Bagan, Kaitan Antara urls.py, views.py, models.py, & Berkas html
Berdasarkan nomor-nomor yang ada pada bagan, berikut merupakan penjelasannya:
1. _Controller_ menerima permintaan dari user melalui web _browser_.
2. _Controller_ mencari URL yang cocok dengan permintaan dari user dan mengeksekusi fungsi milik objek.
3. Presentation _object_ mendefinisikan template agar dapat digunakan untuk membangun sebuah halaman web, dengan memanggil fungsi model yang sesuai, yang mengirim kembali data tersebut. Data yang dikembalikan akan ditampilkan dan dikirim ke template.
4. Data _object_ terhubung dengan inti dari aplikasi CostGlue melalui API CostGlue, yang berperan untuk menerima kembali data serta laporan status yang diminta.
5. Halaman web dibentuk berdasarkan yang template yang telah dipilih dan dengan data yang diserahkan dari _object presentation_.
6. Halaman HTML yang ditampilkan di web _browser_ merupakan hasil dari permintaan user.

Sehingga, dari proses di atas, urls.py, views.py, models.py, & html jelas berkaitan antar satu sama lain.

# Mengapa Kita Menggunakan Virtual Environment? 
Virtualenv digunakan untuk mengatur _packages_ Python di berbagai proyek yang berbeda. Menggunakan virtualenv memungkinkan kita untuk menghindari pemakaian _packages_ Python secara global, yang dapat merusak _system tools_ ataupun proyek lain.

# Apakah Tetap Dapat Membuat Aplikasi Web Berbasis Django Tanpa Menggunakan Virtual Environment?
Ya, tanpa menggunakan virtualenv, kita tetap dapat membuat aplikasi web berbasis Django. Namun, saat memulai dengan proyek baru atau menginstal beberapa _software_, kita tidak dapat mengetahui apakah versinya terbaru, apakah ada kontradiksi dengan _packages_ atau versi python yang lain, atau bahkan jika _packages_ itu ada sama sekali. Disorganisasi semacam itu dapat menyebabkan masalah, dan hal tersebut tentunya tidak hanya mengganggu proyek yang sedang kita buat, namun juga membuat kita kehilangan banyak waktu yang seharusnya dapat digunakan untuk sesuatu yang lebih produktif.


# Pengimplementasian Poin 1 Sampai Poin 4
Poin Pertama
1. Membuat repositori baru agar dapat di kloning ke perangkat saya untuk dapat menggunakan template yang telah disediakan. Repositori tersebut saya namakan Tugas-2---Audrey.
2. Membuka folder yang telah berhasil saya kloning melalui VSCode dan mengerjakannya sesuai perintah. 
3. Menjalankan perintah 
```shell 
python manage.py makemigrations 
``` 
untuk mempersiapkan migrasi skema model ke dalam database Django lokal dan perintah 
```shell 
python manage.py migrate 
``` 
untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal. Lalu, menjalankan perintah 
```shell
python manage.py loaddata initial_wishlist_data.json 
```
agar  data tersebut masuk ke dalam database Django lokal.
4. Membuat sebuah fungsi yang menerima parameter _request_ dan mengembalikan _render_ dengan cara menambahkan kode berikut ke dalam views.py yang ada pada folder katalog:

```python
def show_katalog(request):
    return render(request, "katalog.html", context)
```
Poin Kedua
1. Melakukan _routing_ terhadap fungsi _views_ yang telah di buat pada urls.py dalam folder katalog. Isi dari urls.py tersebut adalah sebagai berikut:
```python
from django.urls import path
from katalog.views import show_katalog

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]
```
2. Mendaftarkan aplikasi katalog ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode berikut pada variabel urlpatterns:
```python
path('katalog/', include('katalog.urls')),
```
3. Menjalankan 
```shell
python manage.py _runserver_ 
```
di terminal untuk menjalankan proyek Django tersebut.

Poin Ketiga
1. Mencari variabel-variabel yang harus di isi sesuai dengan diri sendiri.
2. Menyimpan semua perubahan.

Poin Keempat
1. Melakukan _add-commit-push_.
2. Copy API key akun Heroku milik saya lalu memasukannya ke _secrets_ di Github.
3. _Rerun workflow_.