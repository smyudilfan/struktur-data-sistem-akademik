from collections import deque

data = [
    {"nim": "001", "nama": "Andi"},
    {"nim": "002", "nama": "Budi"},
    {"nim": "003", "nama": "Citra"}
]

undo = []
antrian = deque()


def tampil():
    print("\nData Mahasiswa")
    for x in data:
        print(x["nim"], "-", x["nama"])


def tambah():
    nim = input("NIM: ")
    nama = input("Nama: ")

    mahasiswa = {"nim": nim, "nama": nama}

    data.append(mahasiswa)
    undo.append(mahasiswa)

    print("Data berhasil ditambahkan")


def hapus():
    nim = input("NIM yang ingin dihapus: ")

    for x in data:
        if x["nim"] == nim:
            data.remove(x)
            print("Data berhasil dihapus")
            return

    print("Data tidak ditemukan")


def cari():
    nim = input("Masukkan NIM: ")

    for x in data:
        if x["nim"] == nim:
            print("NIM :", x["nim"])
            print("Nama:", x["nama"])
            return

    print("Data tidak ditemukan")


def undo_data():
    if len(undo) > 0:
        mahasiswa = undo.pop()

        if mahasiswa in data:
            data.remove(mahasiswa)
            print("Undo:", mahasiswa["nama"])
    else:
        print("Tidak ada data")


def masuk_antrian():
    nama = input("Nama mahasiswa: ")
    antrian.append(nama)
    print(nama, "masuk antrean")


def proses():
    if len(antrian) > 0:
        nama = antrian.popleft()
        print(nama, "sedang diproses")
    else:
        print("Antrean kosong")


while True:
    print("\n1. Tampilkan")
    print("2. Tambah")
    print("3. Hapus")
    print("4. Cari")
    print("5. Undo")
    print("6. Masuk Antrean")
    print("7. Proses Antrean")
    print("8. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        tampil()

    elif pilih == "2":
        tambah()

    elif pilih == "3":
        hapus()

    elif pilih == "4":
        cari()

    elif pilih == "5":
        undo_data()

    elif pilih == "6":
        masuk_antrian()

    elif pilih == "7":
        proses()

    elif pilih == "8":
        break

    else:
        print("Pilihan salah")
