import unittest

from  machinetranslation.translator import englishToFrench, frenchToEnglish

class TestTranslation(unittest.TestCase):
    def test_eng2fr_equal(self):
        print('check englishToFrench assertEqual response... ')
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

    def test_eng2fr_notEqual(self):
        print('check englishToFrench assertNotEqual response... ')
        self.assertNotEqual(englishToFrench('Bonjour'),'Goodbye')

    def test_fr2eng_equal(self):
        print('check frenchToEnglish assertEqual response...')
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')

    def test_fr2eng_notEqual(self):
        print('check frenchToEnglish assertNotEqual response..')
        self.assertNotEqual(frenchToEnglish('Bonjour'),'Go home')


if __name__ == '__main__':
    unittest.main()
