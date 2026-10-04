from collections import deque

# Queue untuk antrean mahasiswa
antrian = deque()

# Stack untuk Undo
undo = []


# =========================
# OPERASI ANTREAN
# =========================

def tambah_antrian():
    nama = input("Nama mahasiswa: ")
    antrian.append(nama)
    print(nama, "berhasil masuk antrean")


def proses_antrian():
    if len(antrian) > 0:
        nama = antrian.popleft()
        print(nama, "sedang diproses")
    else:
        print("Antrean kosong")


def lihat_depan():
    if len(antrian) > 0:
        print("Mahasiswa terdepan:", antrian[0])
    else:
        print("Antrean kosong")


def cek_antrian():
    if len(antrian) == 0:
        print("Antrean kosong")
    else:
        print("Antrean tidak kosong")


# =========================
# OPERASI UNDO
# =========================

def tambah_undo():
    aktivitas = input("Masukkan aktivitas: ")
    undo.append(aktivitas)
    print("Aktivitas berhasil disimpan")


def proses_undo():
    if len(undo) > 0:
        aktivitas = undo.pop()
        print("Undo:", aktivitas)
    else:
        print("Tidak ada aktivitas yang dapat di-Undo")


def lihat_undo():
    if len(undo) > 0:
        print("Aktivitas terakhir:", undo[-1])
    else:
        print("Tidak ada aktivitas")


def cek_undo():
    if len(undo) == 0:
        print("Undo kosong")
    else:
        print("Undo tidak kosong")


# =========================
# MENU PROGRAM
# =========================

while True:

    print("\n===== MENU =====")
    print("1. Tambah antrean")
    print("2. Proses antrean")
    print("3. Lihat mahasiswa terdepan")
    print("4. Cek antrean")

    print("5. Tambah aktivitas Undo")
    print("6. Undo aktivitas")
    print("7. Lihat aktivitas terakhir")
    print("8. Cek Undo")

    print("9. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_antrian()

    elif pilih == "2":
        proses_antrian()

    elif pilih == "3":
        lihat_depan()

    elif pilih == "4":
        cek_antrian()

    elif pilih == "5":
        tambah_undo()

    elif pilih == "6":
        proses_undo()

    elif pilih == "7":
        lihat_undo()

    elif pilih == "8":
        cek_undo()

    elif pilih == "9":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak tersedia")
