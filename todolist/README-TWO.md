# Perbedaan Antara _Asynchronous_ dengan _Synchronous_ Programming
_Asynchronous_ merupakan komunikasi web yang memiliki tipe komunikasi parsial. Penerimaan _request_ dari _user_ kepada server akan diterima lalu dikirimkan _response_ yang sifatnya parsial dan tidak merubah keseluruhan isi dari aplikasi. Sehingga, _user_ hanya akan menerima _response_ berupa page yang hanya dapat dilihat oleh _user_, namun, _user_ tetap bisa berinteraksi dengan aplikasi tanpa menunggu _response_ dari server.

_Synchronous_ merupakan tipe komunikasi permanen. Permintaan _user_ akan diterima dan diberi _response_ yang akan memperbaharui isi dari aplikasi, lalu memberikannya kepada _user_. _Synchronous_ akan membuat _user_ menunggu _response_ dari server dan membuat _user_ tidak dapat berinteraksi selama proses menunggu _response_ dari server.

# Apa Itu Paradigma _Event-Driven Programming_?
Sebuah sistem objek yang saling berinteraksi dengan menggunakan mekanisme pesan yang dikontrol oleh suatu komponen berbeda bernama event dispatcher. 

# Penerapan _Asynchronous Programming_ Pada AJAX
_Asynchronous programming_ pada AJAX membuat website tidak memerlukan reload saat merubah data. AJAX akan mengumpulkan perintah yang akan dijalankan lalu mengirimnya ke server agar datanya diubah menjadi asynchronous. 

# Cara Pengimplementasian Checklist
1. Mengaktifkan virtual environment dengan cara menjalankan ```python -m venv env dan source env/bin/activate``` di terminal.
2. Membuat fungsi show_json pada views.py yang yang mengembalikan seluruh data _task_ dalam bentuk JSON.
3. Routing path /todolist/json.
4. Mengambil task menggunakan AJAX GET dengan menambahkan ```$.get()...``` pada todolist.html.
5. Membuat tombol untuk menambahkan _task_ dengan membuka sebuah modal dengan _form_ pada todolist.html.
6. Membuat fungsi baru pada views.py untuk menambahkan _task_ ke dalam database.
7. _Routing path_ /todolist/add yang mengarah ke fungsi yang telah dibuat pada views.py.
8. Menghubungkan _form_ modal dengan path /todolist/add.
9. Setelah _task_ berhasil ditambahkan, maka modal akan ditutup dengan ```data-bs-dismiss="modal"```.
10. Menjalankan server dengan ```python3 manage.py runserver```.
11. Melakukan deployment dengan cara _add, commit_, dan _push_ perubahan.
