daftar_buku = [
    {"id_buku": "001", "judul_buku": "Spy X Family", "penulis": "Tatsuya Endo", 'genre': 'manga', 'stok_buku': 8},
    {"id_buku": "002", "judul_buku": "Yuru Camp", "penulis": "Afro", 'genre': 'manga', 'stok_buku': 3},
    {"id_buku": "003", "judul_buku": "Aljabar Matriks", "penulis": "Dra. Rini Asnawati, M.Pd., Agung Putra Wijaya, S.Pd., M.Pd", 'genre': 'Non Fiksi', 'stok_buku': 2},
    {"id_buku": "004", "judul_buku": "Teori Bilangan", "penulis": "Eka Susilowati, S.Si. M.Sc", 'genre': 'Non Fiksi', 'stok_buku': 8},
]

cart = []
daftar_peminjam = []
no_pinjaman = 0

from tabulate import tabulate

def database(list_data0):
    table_header = ["No. Pinjaman", "Nama Peminjam", "id_buku", "judul_buku", "Jumlah Buku"]
    table_data = [[data['No. Pinjaman'], data['Nama Peminjam'], data['id_buku'], data['judul_buku'], data['Jumlah Buku']] for data in list_data0]

    print('\t ******************* Daftar Peminjam ******************* ')
    print(tabulate(table_data, headers=table_header, tablefmt="grid"))

def show_list(list_data1):
    table_header = ["id_buku", "judul_buku", "penulis", "genre", "stok_buku"]
    table_data = [[data['id_buku'], data['judul_buku'], data['penulis'], data['genre'], data['stok_buku']] for data in list_data1]

    print('\t ******************* Daftar Buku ******************* ')
    print(tabulate(table_data, headers=table_header, tablefmt="grid"))



def update_show_list(list_data1, x, data_baru):
    table_header = ["id_buku", "judul_buku", "penulis", "genre", "stok_buku"]
    table_data = []

    for i in range(len(list_data1)):
        new_data = list_data1[i].copy()
        if x == 1:
            new_data['id_buku'] = data_baru
        elif x == 2:
            new_data['judul_buku'] = data_baru
        elif x == 3:
            new_data['penulis'] = data_baru
        elif x == 4:
            new_data['genre'] = data_baru
        elif x == 5:
            new_data['stok_buku'] = data_baru
        table_data.append([new_data['id_buku'], new_data['judul_buku'], new_data['penulis'], new_data['genre'], new_data['stok_buku']])

    print('\t ******************* Daftar Buku ******************* ')
    print(tabulate(table_data, headers=table_header, tablefmt="grid"))

def cari_buku(input):
    cari_buku = (list(filter(lambda data: data['id_buku'] == str(input), daftar_buku)))
    return cari_buku

def read():
    try:
        input_read = int(input('''
            Menu Menampilkan Daftar Buku:
                1. Menampilkan Buku
                2. Mencari Buku
                3. Kembali ke Menu Utama
            Masukkan pilihan Anda: '''))
    except ValueError:
        print("Masukkan angka yang valid.")
        read()
        return

    if input_read == 1 and len(daftar_buku):
        show_list(daftar_buku)
    elif input_read == 2 and len(daftar_buku):
        book_id = str(input('Masukkan kode buku yang ingin Anda cari: '))
        cari_buku(book_id)
        if len(cari_buku(book_id)):
            show_list(cari_buku(book_id))
        else:
            print('\n\t Tidak ada data')
    elif input_read == 3:
        menu()
    else:
        print('\n\t Tidak ada data')

    read()

def add():
    input_add = (int(input('''
        Menu Menambah Daftar Buku:
            1. Menambah Daftar Buku
            2. Kembali ke Menu Utama
        Masukkan pilihan Anda: ''')))
    if input_add == 1:
        add_book_id = (str(input('\n\tMasukkan id_buku Baru: ')))
        list_value = [value for data_buku in daftar_buku for value in data_buku.values()]
        if add_book_id in list_value:
            print('\n\tData sudah ada!')
        else:
            judul_baru = (input('\tSilahkan masukkan judul_buku: '))
            penulis_baru = (input('\tSilahkan masukkan nama penulis: '))
            genre_baru = (input('\tSilahkan masukkan genre: '))
            stok_baru = (int(input('\tSilahkan masukkan stok_buku: ')))
            daftar_buku_baru = [{
                'id_buku': add_book_id,
                'judul_buku': judul_baru,
                'penulis': penulis_baru,
                'genre': genre_baru,
                'stok_buku': stok_baru
            }]
            show_list(daftar_buku_baru)
            save = (input('\n\t Apakah Anda ingin menyimpan data?(I/T)')).capitalize()
            if save == 'I':
                daftar_buku.extend(daftar_buku_baru)
                show_list(daftar_buku)
                print('\n\tData buku baru tersimpan!')
            else:
                print('\n\t Data tidak tersimpan!')
    elif input_add == 2:
        menu()
    add()

def update():
    input_update = (int(input('''
        Menu Memperbaharui Daftar Buku:
            1. Memperbaharui Daftar Buku
            2. Kembali ke Menu Utama
        Masukkan pilihan Anda: ''')))
    if input_update == 1:
        show_list(daftar_buku)
        update_book = (input('\n\tMasukkan id_buku yang ingin diperbaharui: '))
        list_value = [value for data_buku in daftar_buku for value in data_buku.values()]
        if update_book not in list_value:
            print('\n\t Data yang ingin diubah tidak tersedia!')
            update()
        else:
            cari_buku(update_book)
            show_list(cari_buku(update_book))
            input_update = (input('\tApakah Anda yakin ingin perbaharui data berikut(I/T?): ')).capitalize()
            if input_update == 'I':
                input_kategori = (int(input('''
                        \tKategori Data Buku:
                        1. id_buku
                        2. judul_buku
                        3. penulis
                        4. genre
                        5. stok_buku
                    Masukkan kategori buku yang ingin Anda perbaharui: ''')))
                if input_kategori == 1:
                    masukkan_data = (input('\tMasukkan data baru: '))
                    update_show_list(cari_buku(update_book),1,masukkan_data)
                    update_book(cari_buku(update_book),'id_buku',masukkan_data)
                elif input_kategori == 2:
                    masukkan_data = (input('\tMasukkan data baru: '))
                    update_show_list(cari_buku(update_book),2,masukkan_data)
                    update_book(cari_buku(update_book),'judul_buku',masukkan_data)
                elif input_kategori == 3:
                    masukkan_data = (input('\tMasukkan data baru: '))
                    update_show_list(cari_buku(update_book),3,masukkan_data)
                    update_book(cari_buku(update_book),'penulis',masukkan_data)
                elif input_kategori == 4:
                    masukkan_data = (input('\tMasukkan data baru: '))
                    update_show_list(cari_buku(update_book),4,masukkan_data)
                    update_book(cari_buku(update_book),'genre',masukkan_data)
                elif input_kategori == 5:
                    masukkan_data = (input('\tMasukkan data baru: '))
                    update_show_list(cari_buku(update_book),1,masukkan_data)
                    update_book(cari_buku(update_book),'stok_buku',masukkan_data)   
                else:
                    print('\tKategori tidak ada!')
    elif input_update == 2:
        menu()

def keluar():
    print("Program telah keluar.")
       
def delete():
    input_del = (int(input('''
        Menu Menghapus Daftar Buku:
            1. Menghapus Daftar Buku
            2. Kembali ke Menu Utama
        Masukkan pilihan Anda: ''')))
    if input_del == 1:
        show_list(daftar_buku)
        del_book_id = (input('\n\tMasukkan id_buku yang ingin Anda hapus: '))
        list_value_2 = [value_2 for databuku in daftar_buku for value_2 in databuku.values()]
        if del_book_id not in list_value_2:
            print('\n\t Data yang ingin Anda hapus tidak ada!')
        else:
            cari_buku(del_book_id)
            show_list(cari_buku(del_book_id))
            hapus = (input('\n\tApakah Anda yakin ingin menghapus data? (I/T)')).capitalize()
            if hapus == 'I':
                for e in cari_buku(del_book_id):
                    daftar_buku.remove(e)
                print('\n\t Data berhasil dihapus!')
            else:
                print('\n\t Data tidak berhasil dihapus!')
    elif input_del == 2:
        menu()
    delete()  

def cart_fung(list_data2):
    table_header = ["id_buku", "judul_buku", "Jumlah Buku"]
    table_data = [[data['id_buku'], data['judul_buku'], data['Jumlah']] for data in list_data2]

    print('\t ******************* Daftar Keranjang ******************* ')
    print(tabulate(table_data, headers=table_header, tablefmt="grid"))
      
def borrow_book():
    global cart
    global no_pinjaman

    input_borrow = int(input('''
        Menu Meminjam Buku:
            1. Meminjam Buku
            2. Kembali ke Menu Utama
        Masukkan pilihan Anda: '''))

    if input_borrow == 1:
        show_list(daftar_buku)
        while True:
            inputBor = str(input('\n\tMasukkan id_buku yang ingin Anda pinjam: '))
            list_value_3 = [value_3 for databuku in daftar_buku for value_3 in databuku.values()]
            if inputBor not in list_value_3:
                print('\n\tBuku yang ingin Anda pinjam tidak tersedia!')
                borrow_book()
            else:
                print('\tData buku yang ingin Anda pinjam: ')
                var = cari_buku(inputBor)
                show_list(var)
                tambahan = str(input('\n\tTambahkan daftar buku ke dalam keranjang? (I/T)')).capitalize()
                if tambahan == 'I':
                    jumlah = int(input('Berapa buku yang ingin Anda pinjam: '))
                    if jumlah > var[0]['stok_buku']:
                        print('\n\t Mohon maaf stok_buku tidak mencukupi.')
                    else:
                        cart.append(
                            {
                                'judul_buku': var[0]['judul_buku'],
                                'Jumlah': jumlah,
                                'id_buku': var[0]['id_buku']
                            })
                else:
                    print('\n\t Keranjang tidak berubah!')
                    cart.clear()
                    borrow_book()
            cart_fung(cart)
            checker = str(input('\tApakah Anda ingin meminjam buku yang lain? (I/T)')).capitalize()
            if checker != 'I':
                break

        cart_fung(cart)
        check_out = str(input('\t Lanjutkan untuk selesai meminjam? (I/T)')).capitalize()
        if check_out == "T":
            print('Peminjaman dibatalkan!')
            borrow_book()
        elif check_out == 'Y':
            nama_peminjam = str(input('Masukkan nama Anda: '))
            no_pinjaman += 1
            print(f'''\t\n ====== No. Pinjaman Anda adalah: {no_pinjaman} ======''')
            penampungan_sementara = {'No. Pinjaman': no_pinjaman, 'Nama Peminjam': nama_peminjam}
            for item in range(len(cart)):
                cart[item].update(penampungan_sementara)
            daftar_peminjam.extend(cart)
            print('\n\n\t ~~~~ Pengembalian buku 7 hari dari sekarang ~~~~ \n\t\t ~~~~~ Selamat Membaca! ~~~~~')
            for item in cart:
                (cari_buku(item['id_buku']))[0]['stok_buku'] -= item['Jumlah']
            print('\n\t Info: stok_buku Terupdate!')
        else:
            cart.clear()

        cart.clear()
        show_list(daftar_buku)
        print('\n')
        database(daftar_peminjam)
    elif input_borrow == 2:
        menu()
    borrow_book()

def return_book():
    input_return = int(input('''
        Menu Mengembalikan Buku:
            1. Mengembalikan Buku
            2. Kembali ke Menu Utama
        Masukkan pilihan Anda: '''))
    if input_return == 1:
        database(daftar_peminjam)
        while True:
            inputRet = (input('\n\tMasukkan No. Pinjaman untuk mengembalikan buku: '))
            list_value_4 = [value_4 for datapeminjam in daftar_peminjam for value_4 in datapeminjam.values()]
            if inputRet not in list_value_4:
                print('\n\tNo. Pinjaman tidak tersedia!')
                return_book()
            else:
                print('\tData buku yang ingin Anda kembalikan: ')
                cari_buku_4 = (list(filter(lambda data: data['No. Pinjaman'] == (inputRet), daftar_peminjam)))
                database(cari_buku_4)
                hapus_1 = str(input('\n\tApakah Anda ingin mengembalikan semua buku? (I/T)')).capitalize()
                if hapus_1 == 'I':
                    for item in cari_buku_4:
                        (cari_buku(item['id_buku']))[0]['stok_buku'] += item['Jumlah']
                        daftar_peminjam.remove(item)
                        print('\n\t ~~~~ Buku Sudah Dikembalikan! ~~~~')
                        print('\n\t Info: stok_buku Terupdate!')
                    else:
                        print('\n\t Buku belum dikembalikan!')
                        return_book()
            checker = str(input('\tApakah Anda ingin mengembalikan buku yang lain? (I/T)')).capitalize()
            if checker != 'I':
                print('~~~Terima Kasih! Selamat Datang Kembali ~~~')
                break
    elif input_return == 2:
        menu()
    return_book()
                
def menu():
    while True:
        daftar_menu = input('''
          Selamat Datang di Perpustakaan Teluk Mata Ikan
          Daftar Menu:
          1. Menampilkan Daftar Buku
          2. Menambah Daftar Buku
          3. Memperbaharui Daftar Buku
          4. Menghapus Daftar Buku
          5. Meminjam Buku
          6. Mengembalikan Buku
          7. Keluar Program

          Masukkan pilihan Anda yang ingin dijalankan: 
          ''')
        
        try:
            daftar_menu = int(daftar_menu)
        except ValueError:
            print("Masukkan angka yang valid.")
            continue
        
        if(daftar_menu == 1):
            read()
        elif(daftar_menu == 2):
            add()
        elif(daftar_menu == 3):
            update()
        elif(daftar_menu == 4):
            delete()
        elif(daftar_menu == 5):
            borrow_book()
        elif(daftar_menu == 6):
            return_book()
        elif(daftar_menu == 7):
            keluar()
            break
        else:
            print('Pilihan tidak valid. Silakan coba lagi.')
            
menu()
