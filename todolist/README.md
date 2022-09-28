# Deployment Link


# Kegunaan {% csrf_token %} Pada Elemen, Apa Yang Terjadi Jika Tidak Ada Kode Tersebut?
`{% csrf_token %}` merupakan perintah yang dapat menjalankan token secara acak setiap halaman form muncul. `{% csrf_token %}` dapat mencegah serangan CSRF dengan membuat penyerang tidak mungkin membuat permintaan HTTP yang sepenuhnya valid, dengan begitu, penyerang tidak dapat memprediksi berapa nilai token CSRF _user_ dan membuat permintaan dengan semua parameter yang diperlukan aplikasi untuk memenuhi permintaan tersebut.

Jika tidak ada `{% csrf_token %}` pada elemen, maka penyerang dapat dengan mudah menyerang web yang kita miliki dengan cara mengirim form dari server yang tidak seharusnya. 

# Apakah Kita Dapat Membuat Elemen Tanpa Menggunakan {{ form.as_table }}) ?
Hal tersebut dapat terjadi, dengan cara membuat method form, menambahkan `{% csrf_token %}`, mengatur tipe input, name serta placeholder. 
Berikut contoh penerapannya.
```shell
<form method="post" novalidate>
  {% csrf_token %}

  {{ form.non_field_errors }}

  {% for hidden_field in form.hidden_fields %}
    {{ hidden_field.errors }}
    {{ hidden_field }}
  {% endfor %}

  <table border="1">
    {% for field in form.visible_fields %}
      <tr>
        <th>{{ field.label_tag }}</th>
        <td>
          {{ field.errors }}
          {{ field }}
          {{ field.help_text }}
        </td>
      </tr>
    {% endfor %}
  </table>

  <button type="submit">Submit</button>
</form>
```

# Alur Data dari Submisi, Penyimpanan Data Pada Database, Serta Munculnya Data Yang Telah Disimpan Pada Template HTML
_User_ mengisi data pada form lalu server akan mengecek apakah data yang diisi oleh _user_ valid atau tidak. Setelah di cek, data akan diarahkan menuju `views.py`, disimpan di dalam database, lalu, data baru dapat muncul di halaman html sesaat setelah data tersebut diambil.

# Cara Mengimplementasikan Checklist 
1. Mengaktifkan virtual environment dan membuat aplikasi `todolist` dengan cara menjalankan `python manage.py startapp todolist` pada terminal.
2. Menambahkan `path('todolist/', include('todolist.urls')),` ke urls.py. yang ada di dalam folder     `project django` untuk _routing_ dan menjalankan fungsi `show_todolist` yang ada di `views.py`, folder `todolist`.
3. Membuat _class_ di file `models.py` yang ada di folder `todolist` serta membuat atribut sesuai perintah tugas.
4. Membuat fungsi register, login dan logout lalu menghubungkannya dengan `login.html` dan menambahkan `@login_required(login_url='/todolist/login/')`
5. Menyesuaikan isi dari html seperti membuat tombol, kotak untuk diisi oleh _user_ serta tabel untuk menampilkan data yang telah dimasukkan ke dalam _database_
6. Membuat routing untuk register, login, create_task dsb agar terhubung dengan fungsi yang ada di views.py
7. Menjalankan server dengan `python3 manage.py runserver`
8. Melakukan command `python manage.py makemigrations` dan `python manage.py migrate`
9. Add, commit, dan push perubahan.