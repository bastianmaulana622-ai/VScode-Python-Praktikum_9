# Percobaan 11.1: Implementasi Dasar Nesting Dictionary
import datetime

mahasiswa1 = {
    'nama': 'Ucup Surucup',
    'nim': '19022001',
    'sks_lulus': 130,
    'beasiswa': False,
    'lahir': datetime.datetime(2001, 4, 10)  # tahun, bulan, tanggal
}

mahasiswa2 = {
    'nama': 'Azan Magrib',
    'nim': '19022002',
    'sks_lulus': 140,
    'beasiswa': True,
    'lahir': datetime.datetime(2002, 10, 10)
}

mahasiswa3 = {
    'nama': 'Slamet Dunia Akhirat',
    'nim': '19022003',
    'sks_lulus': 100,
    'beasiswa': True,
    'lahir': datetime.datetime(1977, 5, 10)
}

data_mahasiswa = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3,
}

print(f"{'KEY':<6} {'Nama':<20} {'SKS':<5} {'Beasiswa':<9} {'Lahir':<10}")
print("-" * 55)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<20} {SKS:<5} {str(BEASISWA):<9} {LAHIR:<10}")

# Percobaan 11.2: Input Data Dinamis dengan dict.fromkeys()
import datetime

mahasiswa_template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}

data_mahasiswa = {}

print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("-" * 20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
mahasiswa['nama'] = input("Nama Mahasiswa: ")
mahasiswa['nim'] = input("NIM Mahasiswa: ")
mahasiswa['sks_lulus'] = int(input("SKS lulus: "))


TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

print(mahasiswa)

# Percobaan 11.3: Multi-Input & Generate Key Otomatis
import datetime
import os
import string
import random

mahasiswa_template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}

data_mahasiswa = {}

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-" * 20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
    TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY: mahasiswa})

    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<10} {'SKS Lulus':<10} {'Tanggal Lahir':<12}")
    print('-' * 60)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA:<17} {NIM:<10} {SKS:^10} {LAHIR:^12}")

    print("\n")
    is_done = input("Mau tambah lagi bro (y/n)? ")
    if is_done.lower() == "n":
        break

print("\nAkhir dari program, terima kasih")

# Latihan: Sistem Manajemen Perpustakaan Sederhana
import datetime
import os
import string
import random

# Template dictionary buku
buku_template = {
    'judul': 'judul',
    'penulis': 'penulis',
    'tahun_terbit': 0000,
    'tanggal_pinjam': datetime.datetime(1111, 1, 11),
    'status': 'TERSEDIA'
}

data_perpustakaan = {}

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{'SISTEM MANAJEMEN PERPUSTAKAAN':^75}")
    print(f"{'INPUT DATA BUKU BARU':^75}")
    print("=" * 75)

    buku = dict.fromkeys(buku_template.keys())
    buku['judul'] = input("Judul Buku             : ")
    buku['penulis'] = input("Penulis                : ")
    buku['tahun_terbit'] = int(input("Tahun Terbit (YYYY)    : "))
    
    print("\n--- Tanggal Terakhir Pinjam ---")
    tahun = int(input("Tahun (YYYY)           : "))
    bulan = int(input("Bulan (1-12)           : "))
    tanggal = int(input("Tanggal (1-31)         : "))
    buku['tanggal_pinjam'] = datetime.datetime(tahun, bulan, tanggal)
    
    status_input = input("Status (TERSEDIA/TIDAK): ").upper()
    buku['status'] = status_input if status_input in ['TERSEDIA', 'TIDAK'] else 'TIDAK'

    # Generate key unik 6 karakter (kombinasi huruf kapital dan angka)
    KEY = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    data_perpustakaan.update({KEY: buku})

    # Menampilkan tabel data perpustakaan
    print("\n" + "=" * 95)
    print(f"{'KEYS':<8} {'JUDUL BUKU':<25} {'PENULIS':<20} {'TAHUN':<7} {'TERAKHIR PINJAM':<17} {'STATUS':<10}")
    print("-" * 95)

    for key in data_perpustakaan:
        JUDUL = data_perpustakaan[key]['judul']
        PENULIS = data_perpustakaan[key]['penulis']
        TAHUN = data_perpustakaan[key]['tahun_terbit']
        PINJAM = data_perpustakaan[key]['tanggal_pinjam'].strftime("%d/%m/%Y")
        STATUS = data_perpustakaan[key]['status']

        print(f"{key:<8} {JUDUL:<25} {PENULIS:<20} {TAHUN:<7} {PINJAM:<17} {STATUS:<10}")

    print("=" * 95)
    lanjut = input("\nApakah ingin menambahkan buku lagi? (y/n): ")
    if lanjut.lower() == 'n':
        break

print("\nProgram selesai. Terima kasih telah menggunakan sistem perpustakaan.")