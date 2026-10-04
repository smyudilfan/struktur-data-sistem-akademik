import unittest

class TestUndo(unittest.TestCase):

    def setUp(self):
        self.undo = []

    def test_penambahan_data(self):
        self.undo.append("Andi")
        self.assertEqual(self.undo[-1], "Andi")

    def test_penghapusan_data(self):
        self.undo.append("Andi")
        self.undo.append("Budi")
        aktivitas = self.undo.pop()
        self.assertEqual(aktivitas, "Budi")

    def test_melihat_data_terakhir(self):
        self.undo.append("Andi")
        self.undo.append("Budi")
        self.assertEqual(self.undo[-1], "Budi")

    def test_kondisi_kosong(self):
        self.assertTrue(len(self.undo) == 0)

if __name__ == "__main__":
    unittest.main()
