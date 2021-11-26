# ======= F14 - LOAD DATA =======

import argparse
import os

parser = argparse.ArgumentParser(description='Untuk me-load data yang ingin digunakan')
parser.add_argument('dir', type=str, help='Nama folder tempat data yang ingin digunakan', nargs='?', default="")
args = parser.parse_args()

def load():  # Prosedur load data untuk melakukan loading data ke dalam sistem 
    global User
    global Gadget
    global Consumable
    global Consum_hist
    global Gadget_borrow
    global Gadget_return
    global loaded
    if args.dir == "" :  # Apabila saat memberikan command tidak sekaligus memberikan nama folder
        print("\nTidak Ada Nama Folder Yang Diberikan!\n")
        loaded = False
    elif not(os.path.exists(args.dir)):
        print("\nFolder tidak ada!\n")
        loaded = False
    else:
        print("\nLoading...")
        dir = os.getcwd()
        os.chdir(dir + f"/{args.dir}")  # Mengambil data yang akan digunakan yang disimpan pada folder files

        # Mengassign data ke dalam sebuah variabel
        User = csv_list('user.csv')
        Gadget = csv_list('gadget.csv')   
        Consumable = csv_list('consumable.csv')
        Consum_hist = csv_list('consumable_history.csv')
        Gadget_borrow = csv_list('gadget_borrow_history.csv')
        Gadget_return = csv_list('gadget_return_history.csv')

        os.chdir(dir)
        loaded = True
        print("\nSelamat Datang di 'Kantong Ajaib!'\n")

def parser(string, pemisah):
    # Fungsi ini mengubah string menjadi 
    # list yang dipisahkan suatu karakter
    res = []              # list kosong untuk menyimpan hasil
    tmp = ''              # String sementara
    for ch in string:
        if ch == pemisah: # Kalau ketemu pemisah
            res += [tmp]
            tmp  = ''     # Dikosongkan kembali
        else:
            tmp += ch
    res += [tmp]          # Menambahkan bagian terakhir
    return res

def csv_list(filename):
    # Fungsi ini membaca dari file .csv
    # lalu mengubahnya ke bentuk list
    raw = open(filename).read()
    res = []
    for el in parser(raw, '\n'):
        res += [parser(el, ';')]
    return res

load()

# ======= F01 - REGISTER =======

def register():  # Prosedur register

    print("Pastikan username Anda unik !") # Pesan peringatakan untuk user
    nama = input("Masukkan nama: ")
    username = input("Masukkan username: ")

    while Is_Available(username,User) == False : # Apabila username yang diinput tidak unik (sudah ada pada data_username), meminta input hingga unik
        print("Username " + username +" Sudah Terpakai! Silahkan Gunakan Username Lain !") 
        username = input("Masukkan username baru: ") 

    # username yang diinput user sudah unik 
    password = input("Masukkan password: ")
    alamat = input("Masukkan alamat: ")
    data_baru = [str(len(User)), username, nama, alamat, password, 'user']  # Menyimpan data-data baru dalam list data_baru
    User.append(data_baru)  # Menambahkan data baru yang ada di data_baru ke variabel User
    data_username.append(username)
    print()
    print("Selamat User " + username +" Berhasil Terdaftarkan ke Kantong Ajaib !")
    print()

def Is_Available(username,User):  # fungsi untuk memeriksa apakah username yang diinput sudah ada pada data_username
    Bool = True
    for i in range(len(User)):
        if username == data_username[i]:
            Bool = False
    return Bool

# ======= F02 - LOGIN =======
if loaded: # Kalau load sudah benar
    data_username = []  # inisialisasi list kosong
    for i in range(len(User)):  # Mengisi list dengan username milik user dari variabel User
        data_username.append(User[i][1])

    data_password = [] # inisialisasi list kosong
    for i in range(len(User)): # Mengisi list dengan password milik user dari variabel User
        data_password.append(User[i][4])

    data_role = [] # inisialisasi list kosong
    for i in range(len(User)): # Mengisi list dengan role milik user dari variabel User
        data_role.append(User[i][5])

    data_nama = [] # inisialisasi list kosong
    for i in range(len(User)): # Mengisi list dengan nama milik user dari variabel User
        data_nama.append(User[i][2])

def login():
    global role
    global nama
    global logged
    username = input("Masukkan username: ")  
    while Is_Username(username, User) == False : # Jika username yang diinput user salah / tidak terdaftar, meminta input hingga valid
        print("Username Salah! Silahkan masukkan username yang tepat")  
        username = input("Masukkan username: ") 

    # Input username sudah benar
    password = input("Masukkan password: ")  
    while Is_Password(username, password, User) == False:  # Jika password yang diinput salah / tidak sesuai, meminta input hingga valid
        print("Password yang di input salah! ")  
        password = input("Masukkan password: ") 

    # Username dan password user sudah benar dan sesuai
    role = data_role[Get_Position(username, User)]  # Mengambil role dari akun yang digunakan user
    nama = data_nama[Get_Position(username, User)]
    logged = True
    print("Selamat Datang " + role + ' ' + username +" di Kantong Ajaib !") 
    

def Is_Username(username, User):  # Memeriksa apakah username yang diinput user ada pada varibel user melalui data_username
    Bool = False
    Position = 0
    for i in range(len(User)):
        if username == data_username[i]:
            Bool = True
            Position = Position + i
    return(Bool)
    return(Position)

def Get_Position(username, User):  # Mencari posisi username yang sudah divalidasi melalui Is_Username
    Position = 0
    for i in range(len(User)):
        if username == data_username[i]:
            Position = Position + i
    return(Position)

def Is_Password(username, password, User):  # Mmeriksa apakah password yang diinput sudah benar dan sesuai dengan pasangan usernya berdasarkan posisi dari Get_Posisition dan dari data_usernamea
    Bool = False
    for i in range(len(User)):
        if password == data_password[Get_Position(username, User)]:
            Bool = True
    return(Bool)

# ======= F03 - SEARCH RARITY =======

def check_input(rarity_input):
    if rarity_input == 'A' or rarity_input == 'B' or rarity_input == 'C' or rarity_input == 'S':
        return True
    else:
        return False

def input_valid(rarity_input):
    while not (check_input(rarity_input)):
        print("Masukkan rarity salah")
        rarity_input = input ("Masukkan ulang rarity : ")
    return rarity_input

def printGroup(i,arr):
    if arr[i][0][0] == 'G':
        print("Type Item        :  Gadget")
        print("Nama             : ", arr[i][1])
        print("Deskripsi        : ", arr[i][2])
        print("Jumlah           : ", arr[i][3], "buah")
        print("Rarity           : ", arr[i][4])
        print("Tahun Ditemukan  : ", arr[i][5])
        print()
    elif arr[i][0][0] == 'C':
        print("Type Item        :  Consumable")
        print("Nama             : ", arr[i][1])
        print("Deskripsi        : ", arr[i][2])
        print("Jumlah           : ", arr[i][3], "buah")
        print("Rarity           : ", arr[i][4])
        print()
    elif arr[0][1] =='id_peminjam' and len(arr[0])==5:
        print("ID Peminjaman       : ", arr[i][0])
        print("Nama Pengambil      : ", arr[i][1])
        print("Nama Gadget         : ", arr[i][2])
        print("Tanggal Peminjaman  : ", arr[i][3])
        print("Jumlah              : ", arr[i][4])
        print()
    elif arr[0][1] =='id_peminjam' and len(arr[0])==4:
        print("ID Pengembalian       : ", arr[i][0])
        print("Nama Pengambil        : ", arr[i][1])
        print("Nama Gadget           : ", arr[i][2])
        print("Tanggal Pengembalian  : ", arr[i][3])
        print()    
    elif arr[0][1] =='id_pengambil':
        print("ID Pengambilan       : ", arr[i][0])
        print("Nama Pengambil       : ", arr[i][1])
        print("Nama consumable      : ", arr[i][2])
        print("Tanggal Pengambilan  : ", arr[i][3])
        print("Jumlah               : ", arr[i][4])

def searchrarity(Gadget):
    n = len(Gadget)
    found = 0
    rarity_input = str(input("Masukkan rarity : "))
    rarity_input = input_valid(rarity_input)
    print()
    print ("Hasil pencarian :")
    print()
    for i in range (1,n):
        if Gadget[i][4] == rarity_input:
            found += 1
            printGroup(i,Gadget)
    if found == 0:
        print ("Tidak ada gadget yang ditemukan")

# ======= F04 - SEARCH YEAR =======

def printGroup(i,arr):
    if arr[i][0][0] == 'G':
        print("Type Item        :  Gadget")
        print("Nama             : ", arr[i][1])
        print("Deskripsi        : ", arr[i][2])
        print("Jumlah           : ", arr[i][3], "buah")
        print("Rarity           : ", arr[i][4])
        print("Tahun Ditemukan  : ", arr[i][5])
        print()
    elif arr[i][0][0] == 'C':
        print("Type Item        :  Consumable")
        print("Nama             : ", arr[i][1])
        print("Deskripsi        : ", arr[i][2])
        print("Jumlah           : ", arr[i][3], "buah")
        print("Rarity           : ", arr[i][4])
        print()
    elif arr[0][1] =='id_peminjam' and len(arr[0])==5:
        print("ID Peminjaman       : ", arr[i][0])
        print("Nama Pengambil      : ", arr[i][1])
        print("Nama Gadget         : ", arr[i][2])
        print("Tanggal Peminjaman  : ", arr[i][3])
        print("Jumlah              : ", arr[i][4])
        print()
    elif arr[0][1] =='id_peminjam' and len(arr[0])==4:
        print("ID Pengembalian       : ", arr[i][0])
        print("Nama Pengambil        : ", arr[i][1])
        print("Nama Gadget           : ", arr[i][2])
        print("Tanggal Pengembalian  : ", arr[i][3])
        print()    
    elif arr[0][1] =='id_pengambil':
        print("ID Pengambilan       : ", arr[i][0])
        print("Nama Pengambil       : ", arr[i][1])
        print("Nama consumable      : ", arr[i][2])
        print("Tanggal Pengambilan  : ", arr[i][3])
        print("Jumlah               : ", arr[i][4])


def check_input(kategori):
    if not (kategori != "=" or kategori != ">" or kategori != "<" or kategori != "<=" or kategori != ">="):
        return False
    else:
        True

def input_valid(kategori):
    if check_input(kategori):
        while(check_input):
            print("Masukkan salah")
            kategori = input("Masukkan ulang tAnda : ")
    return kategori

def searchyear (Gadget):
    n = len(Gadget)
    tahun_input = input("Masukkan Tahun : ")
    try:
        tahun_input = int(tahun_input)
    except:
        print("Tahun harus berupa angka!")
        return
    kategori = str(input("Masukkan Kategori : "))
    kategori = input_valid(kategori)
    print()
    print ("Hasil pencarian : ")
    print()
    found = 0
    for i in range (1,n):
        if kategori == ">" and int(Gadget[i][5]) > tahun_input:
            printGroup(i,Gadget)
            found += 1
        elif kategori == "<" and int(Gadget[i][5]) < tahun_input:
            printGroup(i,Gadget)
            found += 1
        elif kategori == "=" and int(Gadget[i][5]) == tahun_input:
            printGroup(i,Gadget)
            found += 1
        elif kategori == ">=" and int(Gadget[i][5]) >= tahun_input:
            printGroup(i,Gadget)
            found += 1
        elif kategori == "<=" and int(Gadget[i][5]) <= tahun_input:
            printGroup(i,Gadget)
            found += 1
    if found == 0:
        print ("Tidak ada gadget yang ditemukan")
        print()

# ========= F05 - ADD ITEM =========

def id_exist(id):
    # Fungsi untuk memastikan apakah ID ada

    # Kamus Lokal
    # id   : array of char
    # item : array of array of char

    # Algoritma
    global Gadget
    global Consumable
    if id[0] == 'G':
        for item in Gadget:
            if item[0] == id:
                return True
    elif id[0] == 'C':
        for item in Consumable:
            if item[0] == id:
                return True
    return False

def tambahItem():
    # Menambahkan item ke Gadget atau Consumables

    # Kamus Lokal
    # id, nama, desc, quan, year : array of char
    # rrty                       : char

    # Algoritma
    global Gadget
    global Consumable
    id = input("Masukan ID        : ")
    if id[0] != 'C' and id[0] != 'G':
        print("\nID tidak valid.\n")
    elif id_exist(id):
        print("\nID sudah ada.\n")
    else:
        nama = input("Masukan Nama      : ")
        desc = input("Masukan Deskripsi : ")
        quan = input("Masukan Jumlah    : ")
        if quan.isdigit(): # Tidak bisa negatif
            rrty = input("Masukan Rarity    : ")
            if not(rrty in ['S', 'A', 'B', 'C']):
                print("\nRarity tidak valid.\n")
            elif id[0] == 'G':
                year = input("Masukan Tahun     : ")
                if year.isdigit():
                    Gadget += [[id, nama, desc, quan, rrty, year]]
                    print("\nItem berhasil ditambahkan ke database.\n")
                else:
                    print("\nTahun tidak valid.\n")
            else:
                Consumable += [[id, nama, desc, quan, rrty]]
                print("\nItem berhasil ditambahkan ke database.\n")
        else:
            print("\nJumlah tidak valid.\n")

#======= F06 - DELETE ITEM ========#

def id_find(id):
    # Mencari index ID

    # Kamus Lokal
    # res : integer
    # id  : array of char

    # Algoritma
    global Gadget
    global Consumable
    res = 0
    if id[0] == 'G':
        while Gadget[res][0] != id: # False jika ketemu
            res += 1
    else:
        while Consumable[res][0] != id:
            res += 1
    return res

def hapusItem():
    # Menghapus Item dari gadget atau Consumables

    # Kamus Lokal
    # id, prompt
    # index

    # Algoritma
    global Gadget
    global Consumable
    id = input("Masukan ID: ")
    if not(id_exist(id)):
        print("\nTidak ada item dengan ID tersebut.\n")
    else:
        index = id_find(id)
        if id[0] == 'G':
            prompt = input(f"Apakah Anda yakin ingin menghapus {Gadget[index][1]}? (Y/N): ")
            while prompt.upper() != 'Y' and prompt.upper() != 'N':
                print("\nInput tidak valid.\n")
                prompt = input(f"Apakah Anda yakin ingin menghapus {Gadget[index][1]}? (Y/N): ")
            if prompt.upper() == 'Y':
                Gadget = Gadget[:index] + Gadget[index + 1:]
                print("\nItem telah berhasil dihapus dari database.\n")
            else:
                print("\nPenghapusan Item gagal.\n")
        else:
            prompt = input(f"Apakah Anda yakin ingin menghapus {Consumable[index][1]}? (Y/N): ")
            while prompt.upper() != 'Y' and prompt.upper() != 'N':
                print("\nInput tidak valid.\n")
                prompt = input(f"Apakah Anda yakin ingin menghapus {Consumable[index][1]}? (Y/N): ")
            if prompt.upper() == 'Y':
                Consumable = Consumable[:index] + Consumable[index + 1:]
                print("\nItem telah berhasil dihapus dari database.\n")
            else:
                print("\nPenghapusan Item gagal.\n")

#======= F07 -  CHANGE ITEM =========#

def ubahJumlah():
    # Menambahkan jumlah Gadget atau Consumables

    # Kamus Lokal
    # id, jumlah : array of char
    # id_index   : integer

    global Gadget
    global Consumable
    id = input("Masukan ID     : ")
    if not(id_exist(id)):
        print("\nTidak ada item dengan ID tersebut.\n")
    else:
        id_index = id_find(id)
        jumlah = input("Masukan Jumlah : ")
        try:
            jumlah = int(jumlah)
        except:
            print("\nJumlah tidak valid.\n")
            return
        if id[0] == 'G':
            if (int(Gadget[id_index][3]) + jumlah) >= 0:
                Gadget[id_index][3] = str(int(Gadget[id_index][3]) + jumlah)
                if jumlah >= 0:
                    print(f"\n{jumlah} {Gadget[id_index][1]} berhasil ditambahkan. Stok sekarang: {Gadget[id_index][3]}\n")
                else:
                    print(f"\n{-jumlah} {Gadget[id_index][1]} berhasil dibuang. Stok sekarang: {Gadget[id_index][3]}\n")
            else:
                print(f"\n{Gadget[id_index][1]} Gagal dibuang karena stok kurang. Stok sekarang: {Gadget[id_index][3]}\n")
        elif id[0] == 'C':
            if (int(Consumable[id_index][3]) + jumlah) >= 0:
                Consumable[id_index][3] = str(int(Consumable[id_index][3]) + jumlah)
                if jumlah >= 0:
                    print(f"\n{jumlah} {Consumable[id_index][1]} berhasil ditambahkan. Stok sekarang: {Consumable[id_index][3]}\n")
                else:
                    print(f"\n{-jumlah} {Consumable[id_index][1]} berhasil dibuang. Stok sekarang: {Consumable[id_index][3]}\n")
            else:
                print(f"\n{Consumable[id_index][1]} Gagal dibuang karena stok kurang. Stok sekarang: {Consumable[id_index][3]}\n")

# ======== F08 -  BORROW GADGET ========

def check_id_gadget(input_id):
    checking_id = True
    first_char = input_id[0]
    if (first_char != 'G'):
        checking_id = False
    return checking_id


def pinjamGadget(input_id, Gadget, Gadget_borrow, jmlh_pinjam, tgl_pinjam, nama):
    success = ""
    username = nama
    for i in range(len(Gadget)):
        if (input_id == Gadget[i][0]):
            pick_gadget = Gadget[i]
            if not availableBorrow(nama , pick_gadget[1]):
                success = False
            else :
                if (int(pick_gadget[3]) >= jmlh_pinjam):
                    jumlah = int(pick_gadget[3]) - jmlh_pinjam
                    pick_gadget[3] = str(jumlah)
                    Gadget[i] = pick_gadget
                    success = pick_gadget[1]
                    borrowHistoryGadget(username, pick_gadget[1], tgl_pinjam, jmlh_pinjam, Gadget_borrow)
    return success

def availableBorrow(nama , nama_gadget):
    global Gadget_borrow
    allow = True
    if len(Gadget_borrow) > 1 :       
        for i in range(len(Gadget_borrow)):
            if ((nama == Gadget_borrow[i][1]) and (nama_gadget == Gadget_borrow[i][2]) and (int(Gadget_borrow[i][5]) < 2)):
                allow = False
    return allow


def borrowHistoryGadget(username, nama_gadget, tgl_pinjam, jumlah, Gadget_borrow):
    idBorrow = 1
    if len(Gadget_borrow) > 1:
        idBorrow = len(Gadget_borrow)
    newBorrow = [str(idBorrow), username, nama_gadget, tgl_pinjam, jumlah,'0',jumlah]
    Gadget_borrow.append(newBorrow)

def borrow_gadget():
    input_id = input("Masukkan ID Item   : ")
    tgl_pinjam = input("Tanggal Peminjaman : ")
    jmlh_pinjam = input("Jumlah Peminjaman  : ")

    try: # User tidak bisa diharapkan memasukkan angka
        jmlh_pinjam = int(jmlh_pinjam)
    except:
        print("Jumlah peminjaman harus angka!")
        return

    pinjam_gadget = pinjamGadget(input_id, Gadget, Gadget_borrow, jmlh_pinjam, tgl_pinjam, nama)

    if (check_id_gadget(input_id) == True) and ( pinjam_gadget != ""):
        print(pinjam_gadget,"(",jmlh_pinjam,") - Item berhasil dipinjam!")
    else:
        q = input("Gagal Meminjam Item! Ulangi? (Y/N): ").upper()
        while q != 'Y' and q != 'N':
            q = input("Gagal Meminjam Item! Ulangi? (Y/N): ").upper()
        if q == 'Y':
                borrow_gadget()
        else:
            return

# ======= F09 -  RETURN GADGET =========

def check_user(nama,Gadget_borrow):
    borrowed_item = []
    for i in range(len(Gadget_borrow)):
        if ((Gadget_borrow[i][1] == nama) and (int(Gadget_borrow[i][5]) < 2)):
            borrowed_item.append(Gadget_borrow[i])
    return borrowed_item

def balik(selected,nama,tgl_balik,jumlah,Gadget_borrow,Gadget_return,Gadget):
    success = False
    username = nama
    returnHistory(selected[0],username, selected[2], tgl_balik, jumlah, Gadget_return)
    borrowedUpdate(selected,jumlah,Gadget_borrow)
    gadgetUpdate(selected,jumlah,Gadget)
    return success

def borrowedUpdate(selected,jumlah,Gadget_borrow):
    for i in range (len(Gadget_borrow)):
        if (selected[0] == Gadget_borrow[i][0]):
            Gadget_borrow[i][6] = int(Gadget_borrow[i][6]) - int(jumlah)
            if (int(Gadget_borrow[i][6]) == 0) :
                Gadget_borrow[i][5] = 2
            else:
                Gadget_borrow[i][5] = 1

def gadgetUpdate(selected,jumlah,Gadget):
    for i in range (len(Gadget)):
        if(Gadget[i][1]==selected[2]):
            Gadget[i][3] = int(Gadget[i][3]) + int(jumlah)

def returnHistory(id_borrow, username, nama_gadget,tgl_balik,jumlah,Gadget_return):
    id_return = 1
    if len(Gadget_return) > 1:
        id_return = len(Gadget_return)
    newReturn = [str(id_return), id_borrow, username, nama_gadget,tgl_balik,jumlah]
    Gadget_return.append(newReturn)

def return_gadget():
    borrowed_item = check_user(nama,Gadget_borrow)
    jml_dipinjam = len(borrowed_item)
    if jml_dipinjam > 0:
        print("Nomor Peminjaman - Nama Item - Jumlah Dipinjam")
        for i in range(jml_dipinjam):
            print(borrowed_item[i][0] , ' - ', borrowed_item[i][2], ' - ', borrowed_item[i][6])
        input_no = input("Masukkan nomor peminjaman : ")
        tgl_balik = input("Tanggal Pengembalian : ")
        jumlah = input("Jumlah Pengembalian : ")
        selected = []
        for i in range(jml_dipinjam):
            if (input_no == borrowed_item[i][0]):
                selected = borrowed_item[i]
                if (int(selected[6]) >= int(jumlah)):
                    balik(selected,nama,tgl_balik,jumlah,Gadget_borrow,Gadget_return,Gadget)
                else:
                    q = input("Input Salah! Ulangi? (Y/N): ").upper()
                    while q != 'Y' and q != 'N':
                        q = input("Input Salah! Ulangi? (Y/N): ").upper()
                    if q == 'Y':
                        return_gadget()
                    else:
                        return
    else:
        print("Kamu tidak meminjam Gadget apapun!")

#======= F10 - ASK FOR CONSUMABLE ==========

def check_id_consumable(input_id):
    checking_id = True
    first_char = input_id[0]
    if (first_char != 'C'):
        checking_id = False
    return checking_id


def pinjamConsum(input_id, Consumable, Consum_hist, jmlh_pinjam, tgl_pinjam, nama):
    success = ""
    username = nama
    for i in range(len(Consumable)):
        if (input_id == Consumable[i][0]):
            pick_consumable = Consumable[i]
            if (int(pick_consumable[3]) >= jmlh_pinjam):
                jumlah = int(pick_consumable[3]) - jmlh_pinjam
                pick_consumable[3] = str(jumlah)
                Consumable[i] = pick_consumable
                success = pick_consumable[1]
                borrowHistoryConsum(username, pick_consumable[1], tgl_pinjam, jmlh_pinjam, Consum_hist)

    return success


def borrowHistoryConsum(username, nama_consumable, tgl_pinjam, jumlah, Consum_hist):
    idBorrow = 1
    if len(Consum_hist) > 1:
        idBorrow = len(Consum_hist)
    newBorrow = [str(idBorrow), username, nama_consumable, tgl_pinjam, jumlah]
    Consum_hist.append(newBorrow)

def ask_consumable():
    input_id = input("Masukkan ID Item   : ")
    tgl_pinjam = input("Tanggal Permintaan : ")
    jmlh_pinjam = input("Jumlah Permintaan  : ")

    try: # User tidak bisa diharapkan memasukkan angka
        jmlh_pinjam = int(jmlh_pinjam)
    except:
        print("Jumlah permintaan harus angka!")
        return
    
    pinjam_consumable = pinjamConsum(input_id, Consumable, Consum_hist, jmlh_pinjam, tgl_pinjam, nama)

    if (check_id_consumable(input_id) == True) and (pinjam_consumable != ""):
        print(pinjam_consumable,"(",jmlh_pinjam,") - Item berhasil diambil!" )
    else:
        q = input("Data yang dimasukkan salah! Ulangi? (Y/N): ").upper()
        while q != 'Y' and q != 'N':
            q = input("Data yang dimasukkan salah! Ulangi? (Y/N): ").upper()
        if q == 'Y':
                ask_consumable()
        else:
            return
        
# ======= F11 - GADGET BORROW HISTORY =======

def olderthan(date1, date2):
    # Apakah date1 lebih tua dari date2
    date1 = parser(date1, '/')
    date2 = parser(date2, '/')
    for i in range(3): # Hari, Bulan Tahun
        date1[i] = int(date1[i])
        date2[i] = int(date2[i]) 
    if date1[2] == date2[2]:
        if date1[1] == date2[1]:
            return date1[0] < date2[0]
        else:
            return date1[1] < date2[1]
    else:
        return date1[2] < date2[2]

def datesort(datelist):
    for i in range(len(datelist) - 1,0,-1):
        for k in range(i):
            if olderthan(datelist[k][3], datelist[k+1][3]):
                tmp           = datelist[k]
                datelist[k]   = datelist[k+1]
                datelist[k+1] = tmp
    return datelist

if loaded:
    gadget_borrow_list = datesort(Gadget_borrow[1:])


def gadget_borrow_history():
    global gadget_borrow_list
    jml_dipinjam = len(gadget_borrow_list)
    if jml_dipinjam > 0:
        if (int(jml_dipinjam <= 5)):
            for i in range(jml_dipinjam):
                print("ID Peminjaman        : ", gadget_borrow_list[i][0])
                print("Nama Pengambil       : ", gadget_borrow_list[i][1])
                print("Nama Gadget          : ", gadget_borrow_list[i][2])
                print("Tanggal Peminjaman   : ", gadget_borrow_list[i][3])
                print("Jumlah               : ", gadget_borrow_list[i][4])
                print()
        elif (int(jml_dipinjam > 5)):
            x = 0
            y = 5
            for i in range(x,y):
                print("ID Peminjaman        : ", gadget_borrow_list[i][0])
                print("Nama Pengambil       : ", gadget_borrow_list[i][1])
                print("Nama Gadget          : ", gadget_borrow_list[i][2])
                print("Tanggal Peminjaman   : ", gadget_borrow_list[i][3])
                print("Jumlah               : ", gadget_borrow_list[i][4])
                print()
            more = input("Apakah Anda ingin melihat 5 entry selanjutnya? Y/N : ")
            while ((more == "Y") or (more == "y")):
                x += 5
                y += 5
                if (int(jml_dipinjam > y)):
                    for i in range(x, y):
                        print("ID Peminjaman        : ", gadget_borrow_list[i][0])
                        print("Nama Pengambil       : ", gadget_borrow_list[i][1])
                        print("Nama Gadget          : ", gadget_borrow_list[i][2])
                        print("Tanggal Peminjaman   : ", gadget_borrow_list[i][3])
                        print("Jumlah               : ", gadget_borrow_list[i][4])
                        print()
                    more = input("Apakah Anda ingin melihat 5 entry selanjutnya? Y/N : ")
                else:
                    for i in range(x, jml_dipinjam):
                        print("ID Peminjaman        : ", gadget_borrow_list[i][0])
                        print("Nama Pengambil       : ", gadget_borrow_list[i][1])
                        print("Nama Gadget          : ", gadget_borrow_list[i][2])
                        print("Tanggal Peminjaman   : ", gadget_borrow_list[i][3])
                        print("Jumlah               : ", gadget_borrow_list[i][4])
                        print()
                    break
    else:
        print("\nRiwayat Kosong!\n")

# ======= F12 - GADGET RETURN HISTORY =======

def datesortreturn(datelist):
    for i in range(len(datelist) - 1,0,-1):
        for k in range(i):
            if olderthan(datelist[k][4], datelist[k+1][4]):
                tmp           = datelist[k]
                datelist[k]   = datelist[k+1]
                datelist[k+1] = tmp
    return datelist

if loaded:
    gadget_return_list = datesortreturn(Gadget_return[1:])


def gadget_return_history():
    global gadget_return_list
    jml_kembali = len(gadget_return_list)
    if jml_kembali > 0:
        if (int(jml_kembali <= 5)):
            for i in range(jml_kembali):
                print("ID Pengembalian          : ", gadget_return_list[i][0])
                print("Nama Pengembali          : ", gadget_return_list[i][2])
                print("Nama Gadget              : ", gadget_return_list[i][3])
                print("Tanggal Pengembalian     : ", gadget_return_list[i][4])
                print("Jumlah                   : ", gadget_return_list[i][5])
                print()
        elif (int(jml_kembali > 5)):
            x = 0
            y = 5
            for i in range(x,y):
                print("ID Pengembalian          : ", gadget_return_list[i][0])
                print("Nama Pengembali          : ", gadget_return_list[i][2])
                print("Nama Gadget              : ", gadget_return_list[i][3])
                print("Tanggal Pengembalian     : ", gadget_return_list[i][4])
                print("Jumlah                   : ", gadget_return_list[i][5])
                print()
            more = input("Apakah Anda ingin melihat 5 entry selanjutnya? Y/N : ")
            while ((more == "Y") or (more == "y")):
                x += 5
                y += 5
                if (int(jml_kembali > y)):
                    for i in range(x, y):
                        print("ID Pengembalian          : ", gadget_return_list[i][0])
                        print("Nama Pengembali          : ", gadget_return_list[i][2])
                        print("Nama Gadget              : ", gadget_return_list[i][3])
                        print("Tanggal Pengembalian     : ", gadget_return_list[i][4])
                        print("Jumlah                   : ", gadget_return_list[i][5])
                        print()
                    more = input("Apakah Anda ingin melihat 5 entry selanjutnya? Y/N : ")
                else:
                    for i in range(x, jml_kembali):
                        print("ID Pengembalian          : ", gadget_return_list[i][0])
                        print("Nama Pengembali          : ", gadget_return_list[i][2])
                        print("Nama Gadget              : ", gadget_return_list[i][3])
                        print("Tanggal Pengembalian     : ", gadget_return_list[i][4])
                        print("Jumlah                   : ", gadget_return_list[i][5])
                        print()
                    break
    else:
        print("\nRiwayat Kosong!\n")

# ======= F13 - ASK CONSUMABLE HISTORY =======

def datesortconsum(datelist):
    for i in range(len(datelist) - 1,0,-1):
        for k in range(i):
            if olderthan(datelist[k][3], datelist[k+1][3]):
                tmp           = datelist[k]
                datelist[k]   = datelist[k+1]
                datelist[k+1] = tmp
    return datelist

if loaded:
    consum_list = datesortconsum(Consum_hist[1:])

def consumable_history(): 
    global consum_list   
    jml_pemintaan = len(consum_list)
    if jml_pemintaan > 0:
        if (int(jml_pemintaan <= 5)):
            for i in range(jml_pemintaan):
                print("ID Pengambilan           : ", consum_list[i][0])
                print("Nama Pengambilan         : ", consum_list[i][1])
                print("Nama Consumable          : ", consum_list[i][2])
                print("Tanggal Pengambilan      : ", consum_list[i][3])
                print("Jumlah                   : ", consum_list[i][4])
                print()
        elif (int(jml_pemintaan > 5)):
            x = 0
            y = 5
            for i in range(x,y):
                print("ID Pengambilan           : ", consum_list[i][0])
                print("Nama Pengambilan         : ", consum_list[i][1])
                print("Nama Consumable          : ", consum_list[i][2])
                print("Tanggal Pengambilan      : ", consum_list[i][3])
                print("Jumlah                   : ", consum_list[i][4])
                print()
            more = input("Apakah Anda ingin melihat 5 entry selanjutnya? Y/N : ")
            while ((more == "Y") or (more == "y")):
                x += 5
                y += 5
                if (int(jml_pemintaan > y)):
                    for i in range(x, y):
                        print("ID Pengambilan           : ", consum_list[i][0])
                        print("Nama Pengambilan         : ", consum_list[i][1])
                        print("Nama Consumable          : ", consum_list[i][2])
                        print("Tanggal Pengambilan      : ", consum_list[i][3])
                        print("Jumlah                   : ", consum_list[i][4])
                        print()
                    more = input("Apakah Anda ingin melihat 5 entry selanjutnya? Y/N : ")
                else:
                    for i in range(x, jml_pemintaan):
                        print("ID Pengambilan           : ", consum_list[i][0])
                        print("Nama Pengambilan         : ", consum_list[i][1])
                        print("Nama Consumable          : ", consum_list[i][2])
                        print("Tanggal Pengambilan      : ", consum_list[i][3])
                        print("Jumlah                   : ", consum_list[i][4])
                        print()
                    break
    else:
        print("\nRiwayat Kosong!\n")

# ======= F15 -  SAVE =========

def save_data(nama_file,array_data):    # menyimpan file dan array data
    string_data = []
    for arr_data in array_data: # 
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += [";".join(arr_data_all_string)]

    string_data = "\n".join(string_data)

    f = open(nama_file, mode='w')
    f.write(string_data)
    f.close()

def save():
    nama_folder = input("Masukkan nama folder penyimpanan : ")
    if os.path.exists(nama_folder) == False:
        print("Membuat folder")
        os.makedirs(nama_folder)
    else:
        print("Folder sudah ada")
    save_data(nama_folder + '/' + "user.csv", User)
    save_data(nama_folder + '/' + "gadget.csv", Gadget)
    save_data(nama_folder + '/' + "consumable.csv", Consumable)
    save_data(nama_folder + '/' + "gadget_borrow_history.csv", Gadget_borrow)
    save_data(nama_folder + '/' + "gadget_return_history.csv", Gadget_return)
    save_data(nama_folder + '/' + "consumable_history.csv", Consum_hist)
    print("Saving...")
    print("Data telah disimpan pada folder", nama_folder)

# ======= F16 -  HELP ======

def help():
    # Penjelasan mengenai fungsi-fungsi

    # Kamus Lokal
    # message : array of char

    # Algoritma
    # Nama fungsinya masih perlu disesuaikan
    message = \
    """
    ===============================[ HELP ]===============================

    register                      [A] -  Mendaftarkan akun baru
    login                             -  Masuk ke akun yang ada
    cari rarity gadget            [*] -  Pencarian Gadget berdasarkan Rarity
    cari tahun gadget             [*] -  Pencarian gadget berdasarkan Tahun
    menambah item                 [A] -  Menambahkan Gadget atau Consumable baru
    menghapus item                [A] -  Menghapus Gadget atau Consumable
    mengubah jumlah item          [A] -  Mengubah jumlah Gadget atau Consumable
    meminjam gadget               [U] -  Meminjam Gadget
    mengembalikan gadget          [U] -  Mengembalikan Gadget
    minta consumable              [U] -  Meminta Consumable
    riwayat peminjaman gadget     [A] -  Melihat riwayat peminjaman Gadget
    riwayat pengembalian gadget   [A] -  Melihat riwayat pengembalian Gadget
    riwayat permintaan consumable [A] -  Melihat riwayat pengambilan Consumable
    save                          [*] -  Save data
    help                              -  Penjelasan fungsi-fungsi
    exit                              -  Keluar program

    Keterangan Akses:
        [A] : Admin
        [U] : User
        [*] : Admin, User
    """
    print(message)

# ======= F17 - EXIT ========

def exitprogram():
    global terminate
    x = False
    while x == False:
        simpan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N): ")
        if simpan == 'Y' or simpan == 'y':
            save()
            x = True
        elif simpan == 'N' or simpan == 'n':
            x = True
        else:
            print("Input tidak sesuai")
    terminate = True

## MAIN PROGRAM ## 

terminate = False
logged    = False

while not terminate and loaded:
    program = input("Apa yang ingin Anda lakukan: ").strip().lower()

    # Tidak perlu login dulu
    if program == "help":
        help()
    elif program == "login":
        login()
    elif program == "exit":
        exitprogram()
    
    elif logged: # Hanya bisa diakses setelah login
        # Bisa diakses Admin maupun User
        if program == "save":
            save()
        elif program == "cari rarity gadget":
            searchrarity(Gadget)
        elif program == "cari tahun gadget":
            searchyear(Gadget)
        
        elif role == 'admin': # Fungsi yang hanya bisa diakses Admin
            if program == "register":
                register()
            elif program == "menambah item":
                tambahItem()
            elif program == "menghapus item":
                hapusItem()
            elif program == "mengubah jumlah item":
                ubahJumlah()
            elif program == "riwayat peminjaman gadget":
                gadget_borrow_history()
            elif program == "riwayat pengembalian gadget":
                gadget_return_history()
            elif program == "riwayat permintaan consumable":
                consumable_history()
            else:
                print("\nProgram tidak tersedia.\n")
        
        elif role != 'admin': # Fungsi yang hanya bisa diakses User
            if program == "meminjam gadget":
                borrow_gadget()
            elif program == "mengembalikan gadget":
                return_gadget()
            elif program == "meminta consumable":
                ask_consumable()
            else:
                print("\nProgram tidak tersedia.\n")
        else:
            print("\nProgram tidak tersedia.\n")
    else:
        print("\nProgram tidak tersedia.\n")