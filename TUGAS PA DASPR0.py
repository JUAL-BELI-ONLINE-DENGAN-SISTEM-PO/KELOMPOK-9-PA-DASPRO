import json
import pwinput
from prettytable import PrettyTable
from datetime import datetime
import os
import re
os.system("cls")

# Nama file untuk penyimpanan data
USERS_FILE = 'users.json'
PRODUCTS_FILE = 'products.json'

# Fungsi untuk membaca data pengguna dari file JSON
def baca_users():
    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"users": []}

# Fungsi untuk membaca data produk dari file JSON
def baca_products():
    try:
        with open(PRODUCTS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"products": []}

# Fungsi untuk menyimpan data pengguna ke file JSON
def simpan_users(data):
    try:
        with open(USERS_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        print("Data produk telah disimpan ke file.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data produk: {e}")

# Fungsi untuk menyimpan data produk ke file JSON
def simpan_products(data):
    try:
        with open(PRODUCTS_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        print("Data produk telah disimpan ke file.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data produk: {e}")

# Fungsi registrasi pembeli
def registrasi():
    data = baca_users()
    print("\n+-------------------------------------------------------+")
    print("|              REGISTRASI AKUN PEMBELI                  |")
    print("+-------------------------------------------------------+")
    while True:
        try:
            username = input("Masukkan username: ")
            if username == "":
                print("-> INPUT HARUS DI ISI")
                print("-> SILAKAN COBA LAGI!\n")
                continue
            elif any(x.isdigit() for x in username):  # Cek apakah ada angka dalam username
                print("----Maaf username anda salah, username tidak boleh ada angkanya----")
                continue
            

            # Cek apakah username sudah ada di dalam data json
            for user in data["users"]:
                    if user["username"] == username:
                        print("-> MAAF USERNAME TELAH TERDAFTAR, SILAKAN COBA USERNAME LAIN\n")
                        while True:
                            try:
                                print("+-----------------------------------------------------+")
                                print("|1. Login Akun                                        |")
                                print("|2. Registrasi Akun Baru                              |")
                                print("+-----------------------------------------------------+")
                                pilihan = input("Masukan pilihan anda : ")
                                if pilihan == "1":
                                    login("buyer")  
                                    return
                                elif pilihan == "2":
                                    print("\n-> SILAHKAN REGISTRASI USERNAME YANG BARU")
                                    registrasi()  
                                    return
                                else:
                                    print("\n-> PILIHAN TIDAK TERSEDIA, SILAKAN COBA LAGI\n")
                                    continue
                            except ValueError:
                                    print("Input tidak valid. Masukkan angka yang sesuai.")
                                    continue
                            except (KeyboardInterrupt, EOFError) as e :
                                    print("\n-> Terjadi kesalahan input. Program dihentikan.")
                                    return None
                            except Exception as e:
                                    print(f"\n-> Terjadi kesalahan: {e}")
                                    return None 
                        break
            

            # Jika username belum terdaftar, lanjutkan ke pengisian password
            while True:
                try:
                    password = pwinput.pwinput("Masukkan password: ")
                    if password == "":
                        print("-> INPUT HARUS DI ISI!")
                        print("-> MOHON MAAF COBA LAGI!\n")
                        continue

                    # Cek apakah password mengandung angka dan huruf
                    if not re.match(r'^(?=.*[a-zA-Z])(?=.*\d)', password):  # Password harus ada angka dan hurufnya
                        print("-> PASSWORD HARUS MENGANDUNG ANGKA DAN HURUF!")
                        continue

                    break

                except ValueError:
                        print("Input tidak valid")
                        continue
                except KeyboardInterrupt:
                    print("\n-> Proses pengisian password dibatalkan.")
                    break 
                except (EOFError) as e:
                    print("\n-> Terjadi kesalahan input. Program dihentikan.")
                    break
                except Exception as e:
                    print(f"\n-> Terjadi kesalahan: {e}")
                    break

            # Saldo e-money
            saldo_emoney = 0

            # Input saldo tunai awal
            while True:
                try:
                    saldo_tunai = input("Masukkan saldo tunai awal (Rp): ").strip()
                
                    # Cek jika input kosong
                    if not saldo_tunai:
                        print("-> Saldo tunai tidak boleh kosong. Masukkan saldo yang valid.")
                        continue

                    saldo_tunai = int(saldo_tunai)

                    # Cek apakah saldo negatif
                    if saldo_tunai < 0:
                        print("-> Saldo tunai tidak bisa negatif. Masukkan saldo yang valid.")
                        continue
                        
                    break

                except ValueError:
                    print("-> Saldo tunai harus berupa angka. Masukkan saldo yang valid.")
                    continue
                except (KeyboardInterrupt, EOFError) as e :
                    print("\n-> Terjadi kesalahan input. Program dihentikan.")
                    break  
                except Exception as e:
                    print(f"\n-> Terjadi kesalahan: {e}")
                    break  

            # Menambah pengguna baru ke dalam data
            data["users"].append({
                "username": username,
                "password": password,
                "role": "buyer",
                "saldo_e_money": saldo_emoney,  
                "saldo_tunai": saldo_tunai     
            })
                
            simpan_users(data)
            print("\n            --- REGISTRASI AKUN BERHASIL ---           \n")
            break  # Keluar dari loop ketika registrasi berhasil

        except (KeyboardInterrupt, EOFError) as e :
            print("\n-> Terjadi kesalahan input. Program dihentikan.")
            break  
        except Exception as e:
            print(f"\n-> Terjadi kesalahan: {e}")
            break  

# Fungsi login
def login(role):
    data = baca_users()
    print("\n+---------------------------------------------+")
    print("|                 LOGIN AKUN                  |")
    print("+---------------------------------------------+")
    while True:
        try:
            username = input(">> Masukkan username: ").strip()
            password = pwinput.pwinput(">> Masukkan password: ").strip()
    
            # Cek apakah username dan password ada di dalam data
            user_found = False  # Flag untuk memastikan apakah user ditemukan
            for user in data["users"]:
                if user["username"] == username and user["password"] == password and user["role"] == role:
                    print(f"~~~~ Selamat Anda Berhasil Login Sebagai {role} !!! ~~~~")

                    if role == "admin":
                        menu_admin()
                        return None
                    
                    elif role == "buyer":
                        menu_buyer(username)
                        return None
                    
                elif user["username"] == username:  # Username ditemukan tapi password salah
                    user_found = True  # Menandakan username ditemukan tapi password salah

            # Jika username ditemukan tapi password salah
            if user_found:
                print("-> Password salah. Silakan coba lagi.")
            else:
                print("-> Username tidak ditemukan. Silakan coba lagi.")
            
            # Setelah gagal login, beri pilihan apakah ingin mencoba lagi atau kembali ke menu utama
            while True:
                try:
                    Lanjut = input("\n>> Apakah anda ingin kembali ke menu utama? (ya/tidak) : ")
                    if Lanjut.lower() == "ya":
                        return None  # Kembali ke menu utama
                    elif Lanjut.lower() == "tidak":
                        break  # Coba login lagi
                    else:
                        print("\n-> HANYA KETIK ya/tidak")
                        continue

                except (KeyboardInterrupt, EOFError) as e:
                    print("\n-> Terjadi kesalahan input. Program dihentikan.")
                    return None 
                except Exception as e:
                    print(f"\n-> Terjadi kesalahan: {e}")
                    return None
                
        except ValueError:
            print("Input tidak valid. Silakan coba lagi.")
            continue  # Coba lagi jika ada error input
        except (KeyboardInterrupt, EOFError) as e:
            print("\n-> Terjadi kesalahan input. Program dihentikan.")
            break  # Keluar dari loop jika ada gangguan input
        except Exception as e:
            print(f"\n-> Terjadi kesalahan: {e}")
            break  # Keluar dari loop jika terjadi error lain



# Fungsi untuk menambah produk (khusus admin)
def tambah_produk():
    data = baca_products()
    while True:
        try:
            print("=======================================================")
            print("|                                                     |")
            print("|          --- MENAMBAHKAN PRODUK BARU ---            |")
            print("|                                                     |")
            print("=======================================================")
            nama_produk = input("Nama produk: ")

            # Cek apakah produk dengan nama yang sama sudah ada
            if any(product["nama"].lower() == nama_produk.lower() for product in data["products"]):
                print("-> Produk dengan nama yang sama sudah ada. Tidak bisa menambah produk baru dengan nama yang sama.")
                continue
            
            if not nama_produk.strip():  # Cek jika nama produk kosong atau hanya spasi
                print("-> Nama produk tidak boleh kosong.")
                continue  # Kembali ke awal dan meminta input ulang

            # Validasi harga
            while True:
                harga = input("Harga: ")
                try:
                    harga = int(harga)  # Mengkonversi harga ke integer
                    if harga <= 0:
                        print("Harga harus lebih besar dari 0.")
                        continue
                    break
                except ValueError:
                    print("-> Harga harus berupa angka. Silakan coba lagi.")
                except (KeyboardInterrupt, EOFError) as e:
                    print("\n-> Terjadi kesalahan input. Program dihentikan.")
                    return  # Keluar dari loop jika ada gangguan input
                except Exception as e:
                    print(f"\n-> Terjadi kesalahan: {e}")
                    return  # Keluar dari loop jika terjadi error lain

            # Validasi stok
            while True:
                stok = input("Stok: ")
                try:
                    stok = int(stok)  # Mengkonversi stok ke integer
                    if stok < 0:
                        print("Stok tidak bisa negatif. Silakan coba lagi.")
                        continue
                    break
                except ValueError:
                    print("-> Stok harus berupa angka. Silakan coba lagi.")
                except (KeyboardInterrupt, EOFError) as e:
                    print("\n-> Terjadi kesalahan input. Program dihentikan.")
                    return  # Keluar dari loop jika ada gangguan input
                except Exception as e:
                    print(f"\n-> Terjadi kesalahan: {e}")
                    return  # Keluar dari loop jika terjadi error lain
            
            # Validasi pre-order (yes/no)
            while True:
                pre_order_input = input("Pre-order (yes/no): ").lower()
                if pre_order_input == "yes":
                    pre_order = True
                    break
                elif pre_order_input == "no":
                    pre_order = False
                    break
                else:
                    print("-> Input tidak valid! Harap masukkan 'yes' atau 'no'.")
                

            # Menambahkan input untuk tanggal ketersediaan produk
            if pre_order:
                while True:
                    tanggal_ketersediaan = input("Tanggal ketersediaan produk (YYYY-MM-DD): ")
                    try:
                        # Validasi format tanggal
                        datetime.strptime(tanggal_ketersediaan, "%Y-%m-%d")
                        break
                    except ValueError:
                        print("-> Tanggal tidak valid. Format yang benar adalah YYYY-MM-DD.")
                    except (KeyboardInterrupt, EOFError) as e:
                        print("\n-> Terjadi kesalahan input. Program dihentikan.")
                        return  # Keluar dari loop jika ada gangguan input
                    except Exception as e:
                        print(f"\n-> Terjadi kesalahan: {e}")
                        return  # Keluar dari loop jika terjadi error lain
            else:
                tanggal_ketersediaan = "Tersedia Sekarang"

            data["products"].append({
            "nama": nama_produk,
            "harga": harga,
            "stok": int(stok),
            "pre_order": pre_order,
            "tanggal_ketersediaan": tanggal_ketersediaan,
            "deskripsi": input("Deskripsi: ")
            })
        
            simpan_products(data)
            print("\n        --- Produk berhasil ditambahkan!---       \n")

            while True:
                try:
                    pilihan = input("Apakah anda ingin menambahkan produk lagi? (ya/tidak) : ")
                    if pilihan == "ya":
                        break
                    elif pilihan == "tidak":
                        return
                    else:
                        print("\n-> MAAF PILIHAN TIDAK ADA, SILAKAN COBA LAGI")
                except ValueError:
                    print("\n-> TOLONG MASUKAN INPUT DENGAN BENAR")
                    print("-> SILAHKAN COBA LAGI\n")
                except (KeyboardInterrupt, EOFError) as e:
                    print("\n-> Terjadi kesalahan input. Program dihentikan.")
                    return  # Keluar dari loop jika ada gangguan input
                except Exception as e:
                    print(f"\n-> Terjadi kesalahan: {e}")
                    return  # Keluar dari loop jika terjadi error lain
                
        except ValueError:
            print("\n-> INPUT TIDAK VALID")
            break
        except (KeyboardInterrupt, EOFError) as e:
            print("\n-> Terjadi kesalahan input. Program dihentikan.")
            break  # Keluar dari loop jika ada gangguan input
        except Exception as e:
            print(f"\n-> Terjadi kesalahan: {e}")
            break  # Keluar dari loop jika terjadi error lain
    
                

# Fungsi untuk menampilkan produk
def lihat_produk():
    data = baca_products()

    if not data["products"]:
        print("Tidak ada produk yang tersedia.")
        return
    
    table = PrettyTable()
    table.field_names = ["No", "Nama Produk", "Harga", "Stok", "Status", "Tanggal Ketersediaan", "Deskripsi"]

    # Tampilkan tanggal ketersediaan jika produk adalah pre-order
    for i, produk in enumerate(data["products"], start=1):
        status = "Pre-order" if produk["pre_order"] else "Ready stock"
        tanggal_ketersediaan = produk["tanggal_ketersediaan"] if produk["pre_order"] else "Tersedia Sekarang"

        table.add_row([i, produk['nama'], produk['harga'], produk['stok'], status, tanggal_ketersediaan, produk['deskripsi']])

    print("\n                       ------------------------------------------- Daftar Produk ------------------------------------------         \n")
    print(table)


# Fungsi untuk mengupdate produk
def update_produk():
    data = baca_products()
    
    if not data["products"]:
        print("\n-> Tidak ada produk yang tersedia untuk diupdate.\n")
        menu_admin() 
        return 
    
    lihat_produk()
    
    while True:
        try:
            print("=======================================================")
            print("|                                                     |")
            print("|          --- MEMPERBARUI DATA PRODUK ---            |")
            print("|                                                     |")
            print("=======================================================")
            pilihan = input("Pilih nomor produk yang ingin diupdate (1 - {}): ".format(len(data["products"])))
            
            # Mengecek apakah input valid dan berada dalam range produk yang ada
            if not pilihan.isdigit():
                print("-> Harap masukkan nomor yang valid.")
                continue
                
            pilihan = int(pilihan) - 1  # Konversi pilihan ke indeks (dimulai dari 0)
            
            if 0 <= pilihan < len(data["products"]):
                produk = data["products"][pilihan]
                print(f"Update produk {produk['nama']}")

                # Update detail produk
                produk["nama"] = input(f"Nama produk ({produk['nama']}): ") or produk["nama"]
                
                # Validasi harga agar hanya menerima angka saja
                while True:
                    try:
                        harga = input(f"Harga ({produk['harga']}): ")
                        if harga:
                            produk["harga"] = int(harga)
                        else:
                            produk["harga"] = produk["harga"]
                        break
                    except ValueError:
                        print("-> Harga harus berupa angka. Silakan coba lagi.")
                        continue
                    except (KeyboardInterrupt, EOFError) as e:
                        print("\n-> Terjadi kesalahan input. Program dihentikan.")
                        return                     
                    except Exception as e:
                        print(f"\n-> Terjadi kesalahan: {e}")
                        return

                # Validasi stok agar hanya menerima angka saja
                while True:
                    try:
                        stok = input(f"Stok ({produk['stok']}): ")
                        if stok:
                            produk["stok"] = int(stok)
                        else:
                            produk["stok"] = produk["stok"]
                        break
                    except ValueError:
                        print("-> Stok harus berupa angka. Silakan coba lagi.") 
                    except (KeyboardInterrupt, EOFError) as e:
                        print("\n-> Terjadi kesalahan input. Program dihentikan.")
                        return  # Keluar dari fungsi update_produk
                    except Exception as e:
                        print(f"\n-> Terjadi kesalahan: {e}")
                        return  # Keluar dari fungsi update_produk

                    
                
                # Mengupdate pre-order status
                while True:
                    try:
                        pre_order = input(f"Pre-order (yes/no, saat ini {'yes' if produk['pre_order'] else 'no'}): ").lower()
                        if pre_order in ["yes", "no"]:
                            produk["pre_order"] = pre_order == "yes"
                            # Update tanggal ketersediaan berdasarkan pre-order
                            if produk["pre_order"]:  # Jika pre-order masih aktif
                                while True:
                                    tanggal = input(f"Masukkan tanggal ketersediaan untuk produk {produk['nama']} (format: YYYY-MM-DD): ")
                                    try:
                                        datetime.strptime(tanggal, "%Y-%m-%d")  # Validasi format tanggal pre order
                                        produk["tanggal_ketersediaan"] = tanggal
                                        break
                                    except ValueError:
                                        print("-> Format tanggal tidak valid. Harap gunakan format YYYY-MM-DD.")
                                    except (KeyboardInterrupt, EOFError) as e:
                                        print("\n-> Terjadi kesalahan input. Program dihentikan.")
                                        return # Keluar dari loop jika ada gangguan input
                                    except Exception as e:
                                        print(f"\n-> Terjadi kesalahan: {e}")
                                        return # Keluar dari loop jika terjadi error lain

                            else:  # Jika bukan pre-order, set tanggal ketersediaan menjadi "Tersedia sekarang"
                                produk["tanggal_ketersediaan"] = "Tersedia sekarang"
                                print(f"tanggal_ketersediaan setelah update: {produk['tanggal_ketersediaan']}")
                                break
                        else:
                            print("-> Pilihan tidak valid. Harap masukkan 'yes' atau 'no'.")
                    except (KeyboardInterrupt, EOFError) as e:
                        print("\n-> Terjadi kesalahan input. Program dihentikan.")
                        return
                    except Exception as e:
                        print(f"\n-> Terjadi kesalahan: {e}")
                        return


                produk["deskripsi"] = input(f"Deskripsi ({produk['deskripsi']}): ") or produk["deskripsi"]
                
                simpan_products(data)
                print("\n-> -----SELAMAT DATA PRODUK BERHASIL DIPERBARUI!-----")
                

                # Tanyakan apakah ingin mengupdate produk lagi
                while True:
                    try:
                        pilihan = input("Apakah anda ingin mengupdate produk lagi? (ya/tidak) : ").lower()
                        if pilihan == "ya":
                            update_produk()  # Memanggil ulang fungsi untuk mengupdate produk lagi
                            return  # Agar tidak terus berada di loop yang sama
                        elif pilihan == "tidak":
                            return # Kembali ke menu admin jika selesai
                        else:
                            print("Pilihan tidak valid. Harap masukkan 'ya' atau 'tidak'.")
                    except (KeyboardInterrupt, EOFError) as e:
                        print("\n-> Terjadi kesalahan input. Program dihentikan.")
                        return
                    except Exception as e:
                        print(f"\n-> Terjadi kesalahan: {e}")
                        return

            else:
                print("-> Nomor produk tidak valid, silakan pilih nomor yang tersedia.")
        
        except ValueError:
            print("\n-> INPUT TIDAK VALID. Silakan coba lagi.")
            break
        except (KeyboardInterrupt, EOFError) as e:
            print("\n-> Terjadi kesalahan input. Program dihentikan.")
            break  # Keluar dari loop jika ada gangguan input
        except Exception as e:
            print(f"\n-> Terjadi kesalahan: {e}")
            break  # Keluar dari loop jika terjadi error lain


# Fungsi untuk menghapus produk
def delete_produk():
    data = baca_products()

    # Cek apakah ada produk yang tersedia untuk dihapus
    if not data["products"]:
        print("\n-> Tidak ada produk yang tersedia untuk dihapus.\n")
        menu_admin()  # Kembali ke menu admin jika tidak ada produk didalam data
    
    lihat_produk()

    while True:
        try:
            print("=======================================================")
            print("|                                                     |")
            print("|          --- MENGHAPUS DATA PRODUK     ---          |")
            print("|                                                     |")
            print("=======================================================")
            

            # Memvalidasi input: pastikan input adalah angka
            pilihan = input("Pilih nomor produk yang ingin dihapus: ")
            if not pilihan.isdigit():
                print("-> Harap masukkan nomor yang valid.")
                continue
            
            pilihan = int(pilihan) - 1  # Konversi pilihan ke indeks (dimulai dari 0)
    
            if 0 <= pilihan < len(data["products"]):
                produk = data["products"].pop(pilihan)
                simpan_products(data)
                print(f"------Produk {produk['nama']} berhasil dihapus!------")

                while True:
                    try:
                        pilihan = input("Apakah anda ingin menghapus produk lagi? (ya/tidak) : ")
                        if pilihan == "ya":
                            break
                        elif pilihan == "tidak":
                            return
                        else:
                            print("Pilihan tidak valid.")
                    except ValueError:
                        print("Tolong masukkan input dengan benar! Silahkan coba kembali")
                    except (KeyboardInterrupt, EOFError) as e:
                        print("\n-> Terjadi kesalahan input. Program dihentikan.")
                        return
                    except Exception as e:
                        print(f"\n-> Terjadi kesalahan: {e}")
                        return


            else:
                print("-> Nomor produk tidak valid. Silakan pilih nomor yang ada.")

        except ValueError:
            print("\n-> DATA TIDAK DITEMUKAN")
            print("-> SILAHKAN COBA LAGI\n")
        except (KeyboardInterrupt, EOFError) as e:
            print("\n-> Terjadi kesalahan input. Program dihentikan.")
            break  # Keluar dari loop jika ada gangguan input
        except Exception as e:
            print(f"\n-> Terjadi kesalahan: {e}")
            break  # Keluar dari loop jika terjadi error lain


def beli_produk():
    data = baca_products()  
    lihat_produk()  # Tampilkan produk

    while True:
        try:
            pilihan = input("Pilih nomor produk yang ingin dibeli: ")

            # Validasi input agar hanya angka yang diterima
            if not pilihan.isdigit():
                print("-> Harap masukkan nomor yang valid.")
                continue
            
            pilihan = int(pilihan) - 1  # Mengkonversi ke indeks produk (dimulai dari 0)
            
            if 0 <= pilihan < len(data["products"]):
                produk = data["products"][pilihan]

                # Informasi produk pre-order atau ready stock
                if produk["pre_order"]:
                    print(f"Produk ini akan tersedia pada {produk['tanggal_ketersediaan']}.")
                    print("Pembelian Anda akan diproses setelah produk tersedia.")
                else:
                    print(f"Produk {produk['nama']} tersedia dengan stok {produk['stok']}.")
                
                # Proses pembelian (bisa dilakukan meskipun pre-order)
                while True:
                    try:
                        jumlah = input("Masukkan jumlah pembelian: ")

                        if not jumlah.isdigit() or int(jumlah) <= 0:
                            print("-> Jumlah pembelian tidak valid. Harap masukkan angka positif.")
                            continue
                        jumlah = int(jumlah)

                        if produk["pre_order"] or produk["stok"] >= jumlah:  
                            
                            simpan_products(data)  # Simpan data produk yang sudah diperbarui
                            pembayaran(produk, jumlah)  # Lanjutkan ke pembayaran
                            
                            # Hanya simpan produk setelah pembayaran jika produk ready stock
                            if not produk["pre_order"]:
                                simpan_products(data)  # Simpan produk yang sudah diperbarui setelah pembayaran

                            break  # Keluar dari loop jika selesai membeli produk

                    except ValueError:
                        print("-> INPUT TIDAK VALID. Harap masukkan angka yang sesuai.")
                        continue  # Mengulangi input jumlah jika input tidak valid

                # Tanyakan apakah ingin membeli lagi
                while True:
                    try:
                        beli_lagi = input(">> Apakah ingin membeli produk lagi? (ya/tidak) : ").lower()
                        if beli_lagi == "ya":
                            print("\n-> SILAKAN BELI PRODUK LAGI")
                            break  # Kembali ke awal loop untuk membeli produk lagi
                        elif beli_lagi == "tidak":
                            print("---------- Terima kasih telah berbelanja ^-^ ----------")
                            return  # Keluar dari fungsi jika tidak ingin membeli lagi
                        else:
                            print("\n-> INPUT YANG DIMASUKKAN SALAH. Harap ketik 'ya' atau 'tidak'.")
                            continue

                    except ValueError:
                        print("-> INPUT TIDAK VALID.")
                        continue  # Mengulangi input produk atau jumlah ketika input tidak valid
                    except (KeyboardInterrupt, EOFError) as e:
                        print("\n-> Terjadi kesalahan input. Program dihentikan.")
                        return
                    except Exception as e:
                        print(f"\n-> Terjadi kesalahan: {e}")
                        return

            else:
                print("-> Pilihan produk tidak valid. Harap pilih produk yang ada.")
                continue  # Jika pilihan produk tidak valid, kembali ke pilihan produk

        except ValueError:
            print("Tolong masukkan input dengan benar! Silahkan coba kembali")
            continue  # Mengulangi pilihan produk jika input tidak valid
        except (KeyboardInterrupt, EOFError) as e:
            print("\n-> Terjadi kesalahan input. Program dihentikan.")
            break  # Keluar dari loop jika ada gangguan input
        except Exception as e:
            print(f"\n-> Terjadi kesalahan: {e}")
            break  # Keluar dari loop jika terjadi error lain



# Fungsi Pembayaran
def pembayaran(produk, jumlah):
    data = baca_products()
    produk['harga'] = int(produk['harga'])
    total_harga = produk['harga'] * jumlah 
    total_harga = int(total_harga)
    print(f">> Total pembayaran : Rp {total_harga}")

    

    with open("invoice-transaksi.txt", "a") as invoice:
        print("+----------------------INVOICE PEMBELIAN---------------------+", file=invoice)
        print(f" Nama Produk          : {produk['nama']}", file=invoice)
        print(f" Harga per Produk     : Rp {produk['harga']}", file=invoice)
        print(f" Jumlah Pembelian     : {jumlah}", file=invoice)
        print(f" Total Harga          : Rp {total_harga}", file=invoice)
        print("+-------------------------------------------------------------+", file=invoice)  

        if produk["pre_order"]:
            print(f" Status               : {produk['pre_order']}", file=invoice)
            print(f" Tanggal Ketersediaan : {produk['tanggal_ketersediaan']}", file=invoice)
        print("+-------------------------------------------------------------+", file=invoice)    
        print("\n           ---SILAKAN LAKUKAN PEMBAYARAN---             \n")

    print("+-----------------------------------------------------+")
    print("|                  METODE PEMBAYARAN                  |")
    print("+-----------------------------------------------------+")
    print("|1. E-Money                                           |")
    print("+-----------------------------------------------------+")
    
    while True:
        try:
            pilihan = int(input(">> Masukkan metode pembayaran: "))
            
            if pilihan == 1:  # Pembayaran E-Money
                username = input("Masukkan username Anda: ").strip()

                # Cek apakah username valid
                if not is_username_valid(username):
                    print("-> Username tidak valid. Silakan coba lagi.")
                    continue  # Meminta username yang valid
            
                # Cari saldo E-Money pengguna
                saldo_terpakai = cari_saldo(username)
            
                if saldo_terpakai >= total_harga:
                    saldo_terpakai -= total_harga  # Kurangi saldo e-money pengguna
                
                    # Update saldo e-money di data pengguna
                    update_saldo(username, saldo_terpakai)
                
                    with open("struk-pembayaran.txt", "a") as struk:
                        print("+-------------------STRUK PEMBELIAN--------------------+", file=struk)
                        print(f" Nama Produk          : {produk['nama']}", file=struk)
                        print(f" Harga per Produk     : Rp {produk['harga']}", file=struk)
                        print(f" Jumlah Pembelian     : {jumlah}", file=struk)
                        print(f" Total Harga          : Rp {total_harga}", file=struk)
                        print(f" E-Money Terpakai     : Rp {total_harga}", file=struk)
                        print(f" Sisa Saldo E-Money   : Rp {saldo_terpakai}", file=struk)
                        print("+-----------------------------------------------------+\n", file=struk)
                
                    print("\n             ---PEMBAYARAN BERHASIL---               \n")
                    # Kurangi stok setelah pembayaran berhasil

                    produk["stok"] -= jumlah
                    simpan_products(data)  # Simpan data produk terbaru
                    break  # Jika Pembayaran berhasil, keluar dari loop
                else:
                    saldo_kurang = total_harga - saldo_terpakai
                    print(f">> Saldo e-money kurang sebesar Rp {saldo_kurang}")
                    print("\n                 ---PEMBAYARAN GAGAL---                 \n")
                    break

            else:
                print("\n-> PILIHAN TIDAK TERSEDIA")
                print("\n-> SILAKAN COBA LAGI\n")
                continue
        except ValueError:
            print("-> INPUT TIDAK VALID. Harap masukkan angka yang sesuai.") 
            continue


# Fungsi untuk memeriksa apakah username valid
def is_username_valid(username):
    data = baca_users()  
    for user in data["users"]:
        if user["username"] == username:
            return True
    return False

# Fungsi untuk mencari saldo pengguna (e-money)
def cari_saldo(username):
    data = baca_users()  
    for user in data["users"]:
        if user["username"] == username:
            return user["saldo E-Money"] 
    return 0  # Jika tidak ditemukan, return 0

# Fungsi untuk memperbarui saldo e-money pengguna
def update_saldo(username, saldo_baru):
    data = baca_users()  
    for user in data["users"]:
        if user["username"] == username:
            user["saldo E-Money"] = saldo_baru 
            simpan_users(data)  
            return
    print("Pengguna tidak ditemukan.")
                
# Fungsi untuk mengecek saldo pengguna
def cek_saldo(username):
    data = baca_users()
    for user in data["users"]:
        if user["username"] == username:
            print(f"Saldo e-money Anda: Rp {user['saldo_e_money']}")
            return user['saldo_e_money']
    print("---------- Maaf Pengguna tidak ditemukan, Silakan coba lagi!!!----------")
    return 0

# Fungsi untuk top up saldo pengguna
def top_up(username):
    data = baca_users()
    
    # Tampilkan pilihan top-up
    while True:
        print("+-----------------------------------------------------+")
        print("|                   TOP UP E-MONEY                    |")
        print("+-----------------------------------------------------+")
        print("|1. Rp 500.000                                        |")
        print("|2. Rp 1.000.000                                      |")
        print("|3. Rp 5.000.000                                      |")
        print("|4. Rp 7.000.000                                      |")
        print("|5. Rp 10.000.000                                     |")
        print("+-----------------------------------------------------+")
        
        try:

            pilihan_topup = int(input("\n>> Masukkan pilihan top up e-money: "))
            
            # Mengecek apakah pilihan yang dimasukkan valid
            if pilihan_topup not in [1, 2, 3, 4, 5]:
                print(">> Pilihan tidak valid. Silakan pilih angka 1 hingga 5.")
                continue
            
            # Menentukan jumlah top-up berdasarkan pilihan yang ada
            if pilihan_topup == 1:
                jumlah_top_up = 500000
            elif pilihan_topup == 2:
                jumlah_top_up = 1000000
            elif pilihan_topup == 3:
                jumlah_top_up = 5000000
            elif pilihan_topup == 4:
                jumlah_top_up = 7000000
            elif pilihan_topup == 5:
                jumlah_top_up = 10000000

            # Cari pengguna berdasarkan username
            for user in data["users"]:
                if user["username"] == username:
                    saldo_tunai = user["saldo_tunai"]

                    # Mengecek apakah saldo tunai cukup untuk top-up
                    if saldo_tunai >= jumlah_top_up:
                        # Mengurangi saldo tunai dan menambah saldo e-money
                        user["saldo_tunai"] -= jumlah_top_up
                        user["saldo_e_money"] += jumlah_top_up

                        simpan_users(data)  # Simpan data pengguna yang telah diperbarui
                        print("======================================================================")
                        print(f"Top-up berhasil! Saldo e-money Anda sekarang: Rp {user['saldo_e_money']}")
                        print(f"Saldo tunai Anda sekarang: Rp {user['saldo_tunai']}")
                        print("=======================================================================")
                        return  # Keluar dari fungsi setelah berhasil top-up
                    else:
                        print("=======================================================================")
                        print(f">> Saldo tunai Anda tidak cukup. Anda memerlukan Rp {jumlah_top_up - saldo_tunai} lebih.")
                        print("=======================================================================")
                        return  # Keluar jika saldo tunai tidak cukup

            # Jika pengguna tidak ditemukan
            print("Pengguna tidak ditemukan.")
            return  # Keluar dari fungsi jika pengguna tidak ditemukan
            
        except ValueError:
            print("Masukkan pilihan yang valid.")
        except (KeyboardInterrupt, EOFError) as e:
            print("\n-> Terjadi kesalahan input. Program dihentikan.")
            return
        except Exception as e:
            print(f"\n-> Terjadi kesalahan: {e}")
            return



# Fungsi menu admin
def menu_admin():
    while True:
        try:
            print("+-----------------------------------------------------+")
            print("|                     MENU ADMIN                      |")
            print("+-----------------------------------------------------+")
            print("|1. Tambah Produk                                     |")
            print("|2. Lihat Produk                                      |")
            print("|3. Update Produk                                     |")
            print("|4. Delete Produk                                     |")
            print("|5. Logout                                            |")
            print("+-----------------------------------------------------+")

            pilihan = int(input("Masukkan menu yang dipilih:"))
        
            if pilihan == 1:
                os.system("cls")
                tambah_produk()
            elif pilihan == 2:
                os.system("cls")
                lihat_produk()
            elif pilihan == 3:
                os.system("cls")
                update_produk()
            elif pilihan == 4:
                os.system("cls")
                delete_produk()
            elif pilihan == 5:
                os.system("cls")
                print("Logout berhasil.")
                break
            else:
                print("Pilihan tidak valid.")
                print("-> SILAHKAN COBA LAGI\n")
        except ValueError:
            print("\n-> TOLONG MASUKAN INPUT DENGAN BENAR")
            print("-> SILAHKAN COBA LAGI\n")

        except (KeyboardInterrupt, EOFError) as e:
            print("\n-> Terjadi kesalahan input. Program dihentikan.")
            return
        except Exception as e:
            print(f"\n-> Terjadi kesalahan: {e}")
            return

        

# Fungsi menu pembeli
def menu_buyer(username):
    while True:
        try:
            print("+-----------------------------------------------------+")
            print("|                    MENU PEMBELI                     |")
            print("+-----------------------------------------------------+")
            print("|1. Lihat Produk                                      |")
            print("|2. Beli Produk                                       |")
            print("|3. Cek Saldo E-Money                                 |") 
            print("|4. Top Up Saldo E-Money                              |") 
            print("|5. Logout                                            |")               
            print("+-----------------------------------------------------+")
        
            pilihan = int(input("Masukkan Menu Yang Ingin Dipilih:"))

            if pilihan == 1:
                os.system("cls")
                lihat_produk()
            elif pilihan == 2:
                os.system("cls")
                beli_produk()
            elif pilihan == 3:
                os.system("cls")
                cek_saldo(username)
            elif pilihan == 4:
                os.system("cls")
                top_up(username)
            elif pilihan == 5:
                os.system("cls")
                print("Logout berhasil.")
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("\n-> TOLONG MASUKAN INPUT DENGAN BENAR")
            print("-> SILAHKAN COBA LAGI\n")

        except (KeyboardInterrupt, EOFError) as e:
            print("\n-> Terjadi kesalahan input. Program dihentikan.")
            return
        except Exception as e:
            print(f"\n-> Terjadi kesalahan: {e}")
            return

        

# Main Program
def main():
    while True:
        try:
            print("+-------------------------------------------------------+")
            print("|            --- Sistem Jual Beli Online ---            |")
            print("|            SELAMAT DATANG DI ELECTROSPHERE            |")   
            print("|               Toko Elektronik Terpercaya              |")
            print("+-------------------------------------------------------+")
            print("|1. Login sebagai Admin                                 |")
            print("|2. Login sebagai Pembeli                               |")
            print("|3. Registrasi Pembeli                                  |")
            print("|4. Keluar                                              |")
            print("+-------------------------------------------------------+")
            pilihan = input(">>> Masukkan Menu Yang Ingin Dipilih <<< : ")
            os.system("cls")
        
            if pilihan == "1":
                print("=========================================================")
                print("--------------- ANDA MASUK SEBAGAI ADMIN --------------\n")
                print("-------------SILAKAN LOGIN TERLEBIH DAHULU-------------\n")
                print("=========================================================")
                if login("admin"):
                    menu_admin()
            elif pilihan == "2":
                print("=========================================================")
                print("------------- ANDA MASUK KE SEBAGAI PEMBELI -------------\n")
                print("-------------SILAKAN LOGIN TERLEBIH DAHULU---------------\n")
                print("=========================================================")
                username = login("buyer")
                if username:
                    menu_buyer(username)
            elif pilihan == "3":
                registrasi()
            elif pilihan == "4":
                print("----------------------------------------------------")
                print("Baiklah, terimakasih sudah mengunjungi toko kami ^-^")
                print("----------------------------------------------------")
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("\n-> TOLONG MASUKAN INPUT DENGAN BENAR")
            print("-> SILAHKAN COBA LAGI\n")

        except (KeyboardInterrupt, EOFError) as e:
            print("\n-> Terjadi kesalahan input. Program dihentikan.")
            return
        except Exception as e:
            print(f"\n-> Terjadi kesalahan: {e}")
            return



# Buat admin default jika belum ada
def buat_admin_default():
    data = baca_users()
    admin_ada = any(user["role"] == "admin" for user in data["users"])
    if not admin_ada:
        data["users"].append({"username": "admin", "password": "admin123", "role": "admin", "email": "admin@example.com", "phone": "08123456789"})
        simpan_users(data)

# Eksekusi program utama
buat_admin_default()
main()