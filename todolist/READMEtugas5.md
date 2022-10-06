# Link Deployment
https://pbp-tugas2-audrey.herokuapp.com/todolist/

# Perbedaan dari Inline, Internal dan External CSS
Inline merupakan css yang harus di definisikan terlebih dahulu di tiap elemen yang kita buat di file html kita, internal merupakan kode yang dituliskan di dalam file html kita sendiri di bagian header. Sedangkan pada external, kita perlu import filenya terlebih dahulu dengan melakukan ```<link rel="stylesheet" href="tugas.css"/>``` yang diletakan setelah tag ```tag```.

# Kelebihan dan Kekurangan dari Masing-Masing Style
- Inline, kekurangannya menghabiskan waktu yang ekstra karena harus apply satu persatu ke elemen dan membuat kode menjadi kurang rapi. Kelebihannya adalah _quickfix_, karena saat terdapat error, dapat dengan cepat ditemukan karena hanya menerapkan di 1 elemen.
- Internal, kekurangannya tidak efisien ketika ingin dipakai pada banyak file html, kelebihannya adalah bisa untuk mengatur 1 halaman.
- External, kekurangannya kurang efektif apabila hanya diterapkan sedikit. Kelebihannya adalah bisa digunakan untuk banyak file.

# Apa Itu tag HTML5?
Digunakan untuk menunjukkan elemen-elemen yang ada dalam suatu halaman website dengan tag <> dan </>. Kedua tag tersebut berisi inisial yang mewakili sebuah elemen halaman. Contohnya seperti <p>, <p> merepresentasi sebuah paragraf yang dapat langsung diketik pada sebuah text editor. Untuk memakainya dengan benar, kita perlu memasukkan teks di antara tag <p> dan </p>. Dengan demikian, kita dapat membuat sebuah paragraf.

# Banyak Tipe CSS Selector
Tipe CSS selector bergantung kepada _styling purpose_. CSS _selectors_ memilih elemen pada HTML bergantung pada masing-masing _id, class, type, attribute etc_.
Berikut merupakan macam-macam tipe _selectors_:
- Element Selector
- Id Selector
- Class Selector
- Universal Selector
- Group Selector
- Attribute Selector

# Cara Mengimplementasikan _Checklist_
1. Mengaktifkan virtual environment dengan cara menjalankan ```python -m venv env``` dan ```source env/bin/activate``` di terminal.
2. Kustomisasi halaman _login, register, createtask_ dan halaman utama menjadi semenarik mungkin. 
3. Membuat _task_ agar masuk ke dalam _card_. Untuk membuat card terlihat rapi, saya menambahkan _container_.
4. Menjalankan server dengan ```python3 manage.py runserver```.
5. Melakukan deployment dengan cara _add, commit,_ dan _push_ perubahan.