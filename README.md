# Tugas Mandiri 1b - Penerapan Struktur Data Linear

**Nama:** SM. YUDILFAN INRAWINATA  
**NIM:** 12450111492  
**Program Studi:** Teknik Informatika  
**Universitas:** UIN Sultan Syarif Kasim Riau

## Deskripsi
Program ini merupakan penerapan struktur data linear menggunakan Python.

Struktur data yang digunakan:
- **Queue** untuk antrean pelayanan mahasiswa dengan konsep FIFO (First In First Out).
- **Stack** untuk fitur Undo dengan konsep LIFO (Last In First Out).

## Fitur Queue
1. Penambahan data (Enqueue)
2. Penghapusan data (Dequeue)
3. Melihat data terdepan (Peek)
4. Memeriksa kondisi kosong (IsEmpty)

## Fitur Undo
1. Penambahan data (Push)
2. Penghapusan data (Pop)
3. Melihat aktivitas terakhir (Peek)
4. Memeriksa kondisi kosong (IsEmpty)

## File
- `tugas_1b.py` - Program utama Queue dan Undo
- `test_antrean.py` - Unit Testing Queue
- `test_undo.py` - Unit Testing Undo

## Cara Menjalankan

Jalankan program utama:

```bash
python tugas_1b.py
```

Unit Testing Queue:

```bash
python -m unittest test_antrean.py
```

Unit Testing Undo:

```bash
python -m unittest test_undo.py
```

## Kompleksitas
Operasi Queue menggunakan `deque` memiliki kompleksitas utama O(1).

Operasi Stack menggunakan `list` memiliki kompleksitas utama O(1) untuk append, pop, akses elemen terakhir, dan pengecekan kosong.
