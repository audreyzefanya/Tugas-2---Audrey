# Perbedaan antara JSON, XML, dan HTML
JSON, XML serta HTML memiliki beberapa perbedaan. Perbedaan tersebut dapat dilihat pada tabel berikut:
![tabel_perbedaan](/tabel_perbedaan.jpg)

# Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Karena dalam kesatuan platform, pertukaran data user dengan data yang ada di server pasti terjadi. Data delivery mempermudah kita untuk melakukan pertukaran data. Pertukaran (kirim dan menerima) data bisanya menggunakan format JSON, XML, ataupun HTML agar data yang dik kirim dapat diterima dengan baik oleh user serta mudah dipahami.



# Cara mengimplementasikan masing-masing checklist
1. Membuat aplikasi 'mywatchlist' dengan cara menjalankan 
```shell
python manage.py startapp mywatchlist
```
di folder root.

2. Menambahkan 
```shell 
path('mywatchlist/', include('mywatchlist.urls')) 
``` 
untuk menghubungkan urlpatterns yang ada pada project_django dengan mywatchlist.

3. Menambahkan mywatchlist pada 
installed_app yang ada di setting.py.

4. Melakukan path route pada mywatchlist/urls.py agar terhubung dengan fungsi yang akan dijalankan dalam mywatchlist/views.py

5. Membuat model data pada mywatchlist/models.py dengan fields watched, title, rating, release_date dan review.

6. Melakukan command 
``` python
python manage.py makemigrations 
```
dan 
```python
python manage.py migrate
```

7. Menambahkan 10 data untuk objek MyWatchList dengan membuat folder fixtures dan file baru dengan format .json

8. Jalankan perintah 
```python
python manage.py loaddata initial_wishlist_data.json 
```
untuk memasukkan data tersebut ke dalam database Django lokal.

9. Add, commit, dan push perubahan.

# Mengakses 3 URL menggunakan Postman