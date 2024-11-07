# KELOMPOK-9-PA-DASPRO
# Sistem Jual Beli Online Dengan Sistem Pre Order
# Sistem Informasi Kelas A
Nama Anggota Kelompok 9:
1. Zahraturramadhani
2. Muhammad Rachmad Ramadhan
3. Yardan Raditya Rafi' Widyadhana

![Cuplikan layar 2024-11-07 111511](https://github.com/user-attachments/assets/2ad89afe-e72f-400b-9e9f-b4fc60852096)

Pada awal program akan menampilkan menu awal/utama seperti gambar diatas, Kita diminta untuk menginputkan menu yang ingin dipilih yaitu dari angka (1-4):

1. Jika memilih angka 1 maka akan langsung masuk sebagai admin dan akan diminta untuk login terlebih dahulu menggunakan username dan password yang terdaftar untuk admin.
   
   ![Cuplikan layar 2024-11-07 113104](https://github.com/user-attachments/assets/b4d5fe46-bf31-4522-a63e-c82473905de7)

   >> Output jika admin berhasil untuk login
   
     ![Cuplikan layar 2024-11-07 113324](https://github.com/user-attachments/assets/891a41a2-63f9-44aa-b63d-284373015c4b)

   Ketika admin menginputkan username "admin" dan password "admin123", maka Anda dinyatakan berhasil untuk login sebagai admin. Setelah berhasil login admin akan di arahkan ke menu admin dan di menu admin bisa melakukan CRUD (Create, Read, Update, Delete) produk, serta Logout.

   >> Output jika admin gagal untuk login
   
   ![Cuplikan layar 2024-11-07 125951](https://github.com/user-attachments/assets/acad4700-c1d3-4355-a6e2-97a6a4718efd)
   
   Ketika admin salah menginputkan username dan password, maka admin akan ditanya apakah ingin kembali ke menu utama dengan sistem looping (ya/tidak).
   
   * Jika ya, output nya adalah sebagai berikut:

     ![Cuplikan layar 2024-11-07 130510](https://github.com/user-attachments/assets/38143729-b061-4422-b80f-85598bc4684e)
     
     Ketika admin menginputkan kata ya, maka admin akan di arahkan ke menu utama.

   * Jika tidak, outputnya adalah sebagai berikut:
     
     ![Cuplikan layar 2024-11-07 130832](https://github.com/user-attachments/assets/89110980-6575-4311-a12c-6496fd0b423e)
     
     Ketika admin menginputkan kata tidak, maka admin akan di arahkan untuk input username dan password nya dengan benar.
     

2. Jika memilih angka 2 maka akan langsung masuk sebagai pembeli dan akan diminta untuk login terlebih dahulu menggunakan username dan password yang sudah terdaftar untuk pembeli.
   
   ![Cuplikan layar 2024-11-07 135243](https://github.com/user-attachments/assets/43eaeb40-47d6-43f9-abdf-26cba5cccab7)

    >> Output jika pembeli berhasil untuk login

   ![Cuplikan layar 2024-11-07 135441](https://github.com/user-attachments/assets/88a2770a-e5b2-4597-ac6f-475631d25cee)

    Ketika pembeli menginputkan username dan password yang sudah terdaftar dengan cara registrasi yaitu username "zahratur" dan password "zahra29", maka Anda dinyatakan berhasil untuk login sebagai pembeli. Setelah berhasil login pembeli akan di arahkan ke menu pembeli dan di menu pembeli bisa melakukan lihat produk, beli produk, cek saldo e-money, top up saldo e-money dan juga logout.
   
    >> Output jika pembeli gagal login

    ![Cuplikan layar 2024-11-07 135904](https://github.com/user-attachments/assets/d9d3570b-00e0-4bb6-bfd5-7d8f20941c7d)

    Ketika pembeli salah menginputkan username dan password, maka pembeli akan ditanya apakah ingin kembali ke menu utama dengan sistem looping (ya/tidak).

   * Jika ya, maka output nya adalah sebagai berikut:

     ![Cuplikan layar 2024-11-07 140157](https://github.com/user-attachments/assets/7e9501fd-ebca-4ddc-99d5-3f12c9ed5084)

     Ketika pembeli menginputkan kata ya, maka pembeli akan di arahkan ke menu utama.

   * Jika tidak, maka output nya adalah sebagai berikut:

     ![Cuplikan layar 2024-11-07 140352](https://github.com/user-attachments/assets/6678d964-126a-41ec-8dd2-ac207254ea80)

     Ketika pembeli menginputkan kata tidak, maka admin akan di arahkan untuk input username dan password nya yang sudah terdaftar dengan cara registrasi dengan benar.
     

3. Jika memilih angka 3 maka anda akan masuk ke menu registrasi untuk pembeli, dan pembeli diminta untuk menginputkan username, password, dan juga saldo tunai mereka

   ![Cuplikan layar 2024-11-07 141619](https://github.com/user-attachments/assets/6bf9a9ac-ac3c-4df6-aaa2-03e7004ab256)

   >> Output jika pembeli berhasil untuk registrasi adalah sebagai berikut:

   ![Cuplikan layar 2024-11-07 141905](https://github.com/user-attachments/assets/bd111576-5186-4a57-b269-fbf42cc91d29)

   Ketika pembeli berhasil untuk registrasi maka akan muncul pesan bahwa registrasi akun berhasil dan akan di arahkan kembali ke menu utama untuk melakukan login sebagai admin.
  
   >> Output jika pembeli tidak menginputkan username adalah sebagai berikut:

   ![Cuplikan layar 2024-11-07 142229](https://github.com/user-attachments/assets/3eaac160-79f8-4b8f-afc7-50a8d4c34b8e)

   Ketika pembeli mengosongkan inputan untuk username, maka muncul pesan bahwa input harus diisi dan silakan coba lagi, serta pembeli akan diminta ulang untuk menginputkan username.

   >> Output jika username nya tidak huruf semua, tetapi ada angkanya adalah sebagai berikut:

   ![Cuplikan layar 2024-11-07 143212](https://github.com/user-attachments/assets/e50258ee-f6f6-4dd5-9a30-ba3629b2f1a5)

   Ketika pembeli menginputkan username ada angkanya, maka akan muncul pesan bahwa username tidak boleh ada angkanya, dan pembeli diminta untuk menginputkan username yang sesuai.

   >> Output jika username sudah terdaftar di data adalah sebagai berikut:

   ![Cuplikan layar 2024-11-07 144323](https://github.com/user-attachments/assets/1d0ddd54-85c0-493e-94c2-78bca47b32ac)
  
   Ketika username pembeli sudah terdaftar, maka akan muncul pesan bahwa username sudah terdaftar dan coba username lainnya, serta akan ada pilihan mau login akun atai registrasi akun baru.
  
    * Jika pilih 1, yaitu login akun maka outputnya adalah sebagai berikut:

      ![Cuplikan layar 2024-11-07 144612](https://github.com/user-attachments/assets/a966e6a8-27a3-4c57-ab20-48d0710c8a7d)

      Pembeli disuruh untuk menginputkan username dan password mereka yang sudah terdaftar.
   
   * Jika pilih 2, yaitu registrasi akun baru maka ouputnya adalah sebagai berikut:

     ![Cuplikan layar 2024-11-07 145709](https://github.com/user-attachments/assets/51eac03f-4ba2-423b-b9e6-45b61d9ec709)

     Pembeli diminta untuk menginputkan username dan password baru, serta saldo tunainya.

   >> Output jika pembeli tidak menginputkan password adalah sebagai berikut:

    ![Cuplikan layar 2024-11-07 150124](https://github.com/user-attachments/assets/650a148a-7d8e-4047-8a14-bf6f40de0897)
   
    Ketika pembeli mengosongkan inputan untuk password, maka muncul pesan bahwa input harus diisi dan mohon maaf coba lagi, serta pembeli akan diminta ulang untuk menginputkan usernamenya supaya bisa menginputkan passwordnya.

   >> Output jika pembeli menginputkan password hanya angka saja atau huruf saja adalah sebagai berikut:

    ![Cuplikan layar 2024-11-07 150707](https://github.com/user-attachments/assets/befe5a68-aa4d-4e97-90db-9822e9738cf3)

    Ketika pembeli menginputkan password hanya angka saja atau hanya huruf saja, maka akan muncul pesan bahwa password harus mengandung angka dan huruf, serta pembeli akan diminta ulang untuk menginputkan ulang dari username.

   >> Output ketika pembeli menginputkan saldo < 0 adalah sebagai berikut:
   
   ![Cuplikan layar 2024-11-07 184046](https://github.com/user-attachments/assets/5c964441-5743-45e2-99f6-568d4dc0c47e)

   Ketika pembeli menginputkan saldo tunai kurang dari 0, maka akan muncul pesan bahwa saldo tunai tidak bisa negatif, serta pembeli akan diminta ulang untuk menginputkan kembali username sampai dengan saldo tunai.

   >> Output jika pembeli menginputkan saldo tunai bukan berupa angka tapi huruf adalah sebagai berikut:

   ![Cuplikan layar 2024-11-07 184645](https://github.com/user-attachments/assets/035d9b80-f0a5-4e69-981b-523f2f05dfba)

   Ketika pembeli menginputkan saldo tunai menggunakan huruf bukannya angka, maka akan muncul pesan bahwa saldo tunai harus berupa angka, serta pembeli akan diminta ulang untuk menginputkan kembali username sampai dengan saldo tunai.
   

4. Jika memilih angka 4 maka akan langsung diarahkan untuk keluar dari program.

   ![Cuplikan layar 2024-11-07 190639](https://github.com/user-attachments/assets/f486070a-f2f2-4ab3-9a7f-d95b44b48d01)
   


# MENU-MENU ADMIN (CRUD)

Untuk bisa mengakses menu admin, admin harus melakukan login terlebih dahulu:

![Cuplikan layar 2024-11-07 193232](https://github.com/user-attachments/assets/f699d2a2-ed5c-4d8d-9b73-c42f5822f9ac)

Pada menu admin, terdapat 5 pilihan yang dapat dilakukam oleh seorang admin yaitu: Tambah produk, Lihat Produk, Update Produk, Delete Produk, dan juga logout. Admin dapat menginputkan menu yang diinginkan yaitu dari angka (1-5):

~ Jika admin memilih angka 1, maka admin akan di arahkan untuk ke menu tambah produk

![Cuplikan layar 2024-11-07 195844](https://github.com/user-attachments/assets/d377e756-a999-48c9-a897-612fc31f10f0)

Di tambah produk admin diminta untuk menginputkan



  













  

  

   



   


     

     
     



