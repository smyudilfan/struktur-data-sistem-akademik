import unittest
from collections import deque

class TestAntrean(unittest.TestCase):

    def setUp(self):
        self.antrian = deque()

    def test_penambahan_data(self):
        self.antrian.append("Andi")
        self.assertEqual(self.antrian[0], "Andi")

    def test_penghapusan_data(self):
        self.antrian.append("Andi")
        self.antrian.append("Budi")
        nama = self.antrian.popleft()
        self.assertEqual(nama, "Andi")

    def test_melihat_data_terdepan(self):
        self.antrian.append("Andi")
        self.antrian.append("Budi")
        self.assertEqual(self.antrian[0], "Andi")

    def test_kondisi_kosong(self):
        self.assertTrue(len(self.antrian) == 0)

if __name__ == "__main__":
    unittest.main()
