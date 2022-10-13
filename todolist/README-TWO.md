# asynchronous programming & synchronous programming

- Asynchronous programming adalah sebuah sistem yang dapat diupdate atau diubah tanpa harus dijalankan berulang kali. 
Hal ini dikarenakan sistemnya dapat multitasking dan menjalankan beberapa hal sekaligus.

- Synchronous programming adalah programming untuk sebuah aplikasi atau sistem yang tidak dapat diubah di pertengahan proses. 
Hal ini dikarenakan metode pemanggilan function atau request yang hanya bisa dilakukan satu persatu (synchronous).

# Event-Driven Programming
- Event-driven programming adalah dimana program bergantung pada 'peristiwa/event' yang terjadi pada sistem atau aplikasi. 
Event yang dimaksud dapat berupa perubahan waktu, button click, button hover, key press, dan lain -lain.

# asynchronous programming pada AJAX
Penerapan asynchronous programming AJAX ada penerapannya dalam tugas ini, yakni mengupdate cards yang tertampil di homepage tanpa harus mereload homepage tersebut.
Hal ini dicapai dengan mengambil data dari database dengan dalil asynchronus.

# Implementasi 
- Membuat method baru pada views yang berupa show_json
- Menambahkan path baru pada urls.py
- Membuat Fungsi create_cards untuk ditampilkan pada homepage
- Membuat views baru pada views.py dan path baru di urls untuk routing view tersebut
