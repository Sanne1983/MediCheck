import unittest
from utils.dosage_utils import get_dosage_text

class TestGetDosageText(unittest.TestCase):
    def test_valid_dosage(self):
        dosage = "0:0 mg Einnahme nicht empfohlen, 20:200 mg (1/2 Tabl.) max. 3 x täglich, 30:400 mg (1 Tabl.) max. 3 x tägl., 40:600 mg (1 1/2 Tabl.) max. 3 x täglich"
        weight = 25
        expected = "200 mg (1/2 Tabl.) max. 3 x täglich"
        self.assertEqual(get_dosage_text(dosage, weight), expected)

    def test_exact_weight_match(self):
        dosage = "0:0 mg Einnahme nicht empfohlen, 20:200 mg (1/2 Tabl.) max. 3 x täglich, 30:400 mg (1 Tabl.) max. 3 x tägl., 40:600 mg (1 1/2 Tabl.) max. 3 x täglich"
        weight = 20
        expected = "200 mg (1/2 Tabl.) max. 3 x täglich"
        self.assertEqual(get_dosage_text(dosage, weight), expected)
    
    def test_weight_0(self):
        dosage = "0:0 mg Einnahme nicht empfohlen, 20:200 mg (1/2 Tabl.) max. 3 x täglich, 30:400 mg (1 Tabl.) max. 3 x tägl., 40:600 mg (1 1/2 Tabl.) max. 3 x täglich"
        weight = 0
        expected = "0 mg Einnahme nicht empfohlen"
        self.assertEqual(get_dosage_text(dosage, weight), expected)

if __name__ == "__main__":
    unittest.main()