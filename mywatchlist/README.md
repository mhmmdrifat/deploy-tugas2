# Link Deploy
https://patwatchlist.herokuapp.com/mywatchlist/



## perbedaan antara JSON, XML, dan HTML
- HTML: HTML dapat didefinisikan suatu bahasa markup. Dengan HTML kita dapat membuat halaman statis kita sendiri. HTML digunakan untuk menampilkan data bukan untuk mengangkut data. HTML adalah kombinasi dari Hypertext dan bahasa Markup. Hypertext mendefinisikan link antara halaman web.<br />

- XML: XML merupakan markup language yang digunakan untuk menyederhanakan proses penyimpanan dan pengiriman data antarserver. File XML digunakan untuk membuat format informasi umum serta menjadi sarana untuk membagikan format dan data yang digunakan di World Wide Web, intranet, dan di platform lain yang menggunakan teks ASCII standar. XML sendiri sering dianggap mirip dengan HTML. Baik XML dan HTML mengandung simbol-simbol markup yang berfungsi untuk mendeskripsikan konten sebuah halaman atau file.<br />

- JSON: JSON atau JavaScript Object Notation Berbeda dengan XML (extensive markup language) dan format lainnya yang memiliki fungsi serupa, JSON memiliki struktur data yang sederhana dan mudah dipahami. Itulah mengapa JSON sering digunakan pada API. JSON sendiri terdiri dari dua struktur, yaitu Kumpulan value yang saling berpasangan. Dalam JSON, contohnya adalah object dan daftar value yang berurutan, seperti array.<br />

Perbedaan signifikan dari JSON, XML dan HTML antaralain:
- JSON hanya mendukung encoding UTF-8, sedangkan XML mendukung berbagai macam encoding.
- JSON men-support array sedangkan XML tidak
- HTML digunakan untuk menyusun teks pada halaman web agar ditampilkan dengan tepat di browser web. XML umumnya digunakan untuk menyusun data atau pesan. Sedangkan JSON digunakan untuk merepresentasikan data sebagai pasangan key-value.

## Data Delivery
Data-delivery sangat penting di dalam proses kerja platform karena pada suatu platform seringkali terdapat pertukaran data antara user atau clients dan juga server. Data delivery diperuntukkan untuk memudahkan suatu platform dalam melakukan pengiriman data. Data tersebut tentu memerlukan berbagai format dalam pertukarannya. Format yang seringkali digunakan antara lain adalah HTML, JSON, maupun XML. Jika tidak ada mekanisme tersebut, maka data dari database tidak bisa ditampilkan.

## Implementasi
- Membuat aplikasi mywatchlist dengan `python manage.py startapp mywatchlist`
- Menambahkan path('mywatchlist/', include('mywatchlist.urls')) kedalam list urlpatterns yang ada pada file urls.py dan berada di dalam folder project_django
- Membuat model MyWatchList didalam models.py pada project mywatchlist(membuat field dan data type)
- Membuat initial data pada initial_mywatchlist_data.json yang ada pada fixtures 
- Membuat method pada views.py yang ada di folder mywatchlist
- Memasukan semua path pada list urlpatterns yang ada di urls.py di forlder mywatchlist

  ```
  path('', isi_watchlist, name='isi_watchlist'),
  path('html/', isi_watchlist, name='isi_watchlist'),
  path('xml/', isi_watchlist_xml, name='isi_watchlist_xml'),
  path('json/', isi_watchlist_json, name='isi_watchlist_json'),
  path('json/<int:id>', isi_watchlist_json_by_id, name='isi_watchlist_json_by_id'),
  path('xml/<int:id>', isi_watchlist_xml_by_id, name='isi_watchlist_xml_by_id'),
  ```
- Menambahkan `python manage.py loaddata initial_mywatchlist_data.json` pada procfile

# Postman
## HTML
![image](https://user-images.githubusercontent.com/112569220/191601019-13e5cf20-be33-44cf-be11-37a42fb98672.png)
## XML
![image](https://user-images.githubusercontent.com/112569220/191601119-9bbbee4a-b305-420e-aad1-973faba0d466.png)
## JSON
![image](https://user-images.githubusercontent.com/112569220/191601197-d5499f6d-47f0-4350-8178-a0a46a82e79a.png)


