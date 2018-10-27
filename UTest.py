import unittest
import Solution

cyr_alph="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
cyr_res="{'а': (1, '3.0%'), 'б': (1, '3.0%'), 'в': (1, '3.0%'), 'г': (1, '3.0%'), 'д': (1, '3.0%'), 'е': (1, '3.0%'), 'ж': (1, '3.0%'), 'з': (1, '3.0%'),"
cyr_res+="'и': (1, '3.0%'), 'й': (1, '3.0%'), 'к': (1, '3.0%'), 'л': (1, '3.0%'), 'м': (1, '3.0%'), 'н': (1, '3.0%'), 'о': (1, '3.0%'), 'п': (1, '3.0%'),"
cyr_res+="'р': (1, '3.0%'), 'с': (1, '3.0%'), 'т': (1, '3.0%'), 'у': (1, '3.0%'), 'ф': (1, '3.0%'), 'х': (1, '3.0%'), 'ц': (1, '3.0%'), 'ч': (1, '3.0%'),"
cyr_res+="'ш': (1, '3.0%'), 'щ': (1, '3.0%'), 'ъ': (1, '3.0%'), 'ы': (1, '3.0%'), 'ь': (1, '3.0%'), 'э': (1, '3.0%'), 'ю': (1, '3.0%'), 'я': (1, '3.0%'), 'ё': (1, '3.0%')}"

lat_alp="qwertyuiopasdfghjklmnbvcxz"
lat_res="ile or string is empty or do not contain cyrillic symbols."

badfile="Wrong encoding."
nofile="Error. File not exist."

 
class SolTest(unittest.TestCase):
    def test_cyrillic_alph(self):
        self.assertEqual(sol(cyr_alph),cyr_res)
        
    def test_lat_alph(self):
       self.assertEqual(sol(lat_alp),lat_res)

    def test_empty_array():
       self.assertEqual("",lat_res)

    def test_cyrillic_file(self):
        self.assertEqual(sol("cytest"),cyr_res)
        
    def test_lat_file(self):
       self.assertEqual(sol("latest"),lat_res)

    def test_cyrillic_file2(self):
        assertIsNot(codecs("cytest"),badfile)
        
    def test_lat_file2(self):
       assertIsNot(codecs("stupid"),nofile) 

   
if __name__ == '__main__':
    unittest.main()
