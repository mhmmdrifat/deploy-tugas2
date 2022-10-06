# Link Deploy
https://patwatchlist.herokuapp.com/todolist/

## Kegunaan `{% csrf_token %}` pada elemen `<form>`
CSRF token adalah Cross-Site Request Forgery, Token CSRF adalah unique, secret, unpredictable yang dihasilkan oleh aplikasi sisi server 
dan dikirimkan ke klien sedemikian rupa sehingga disertakan dalam permintaan HTTP berikutnya yang dibuat oleh klien. Saat permintaan selanjutnya dibuat, 
aplikasi sisi server memvalidasi bahwa permintaan tersebut menyertakan token yang diharapkan dan menolak permintaan jika token tidak ada atau tidak valid.
sehingga jika `{% csrf_token %}` dihapus aplikasi tidak akan bisa memverivikasi HTTP request dan akan menghasilkan HTTP request kita di batalkan.

## Apakah kita dapat membuat elemen `<form>` secara manual tanpa menggunakan generator seperti `{{ form.as_table }}`
kita dapat membuat elemen `<form>` secara manual dengan menggunakan wrapper dan setelah itu kita menentukan attribut method dan action dengan value yang sesuai. attribut action digunakan untuk menspesifikasikan endpoint request yang akan diberikan. 
attribut method digunakan untuk menspesifikasi HTTP method yang akan digunakan untuk mengirim request ke server.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
saat user melakukan submit form, HTTP akan melakukan request ke server dengan method dan action yang ada pada form. kemudian action akan memetakan request ke URL,
sesuai dengan yang ada pada urls.py. kemudian akan dilanjutkan ke method yang sesuai di views.py yang kemudian akan men render data di html.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- membuat aplikasi kedalam settings.py dan urls.py pada django project. 
- membuat file html yang diperlukan, models, dan routing urls.py serta mengimplementasikan method register, login, dan logout pada views.py. 
- membuat kelas taskform yang akan membuat form untuk create-task. memunculkan data pada todolist.html.
- mengimplementasikan update task dan delete task untuk menghapus dan memperbaharui task.
