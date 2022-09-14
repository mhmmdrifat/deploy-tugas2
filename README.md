# Link HerokuApp

https://patkatalog.herokuapp.com/katalog/


## Bagan Request Client
![image](https://user-images.githubusercontent.com/112569220/190210075-4198ca22-dee4-4ab0-9550-7fb948599125.png)

Request yang diminta user akan diproses oleh middlewares yang akan diteruskan ke URL router. Kemudian, URLs akan mengarahkan request ke views.py. Setelah function terpanggil, Method yang ada di views.py akan mencetak data-data di katalog.html. Kemudian, database akan mereturn response ke user.

## Virtual Environment

Virtual Environment adalah sebuah wadah untuk menampung libraries serta modul dalam suatu proyek pekerjaan agar terisolasi. Ketika kita mengerjakan beberapa aplikasi/proyek dengan modul yang sama akan tetapi membutuhkan versi berbeda, disinilah kita membutuhkan virtualenv. Secara keseluruhan, Virtual Environment menjadi sangat berguna saat mengerjakan proyek yang berbeda. Tentu saja, jika proyek Anda tidak bergantung pada packages, tidak diperlukan banyak version dan package.

## Implementasi
-Clone repository template dan kemudian menjalankan virtual env sekaligus mengistall segala requirements yang dibutuhkan.
-Membuat method di views.py yang akan mengambil data dari models sekaligus mengubah nama menjadi "Muhammad Rifat Fadhillah" dan student id (NPM) menjadi "2106752470"
-Merender data-data tersebut di katalog.html. Pada katalog.html membuat fields yang bersesuaian dengan data yang ada pada views.py 
-Melakukan routing method show_katalog di urls.py
-Step terakhir adalah dengan melakukan deployment ke HerokuApp dengna memasukan API key dan nama aplikasi yang baru di daftarkan ke dalam secret github dengan format HEROKU_API_KEY untuk API key dan HEROKU_APP_NAME untuk nama aplikasi yang sudah didaftarkan pada HerokuApp
