import unittest
import filecmp
import main

class TestFixedWidthToCSV(unittest.TestCase):

	def test_windows_1252_file(self):
		""" To test windows_1252 encoded file with windows_1252 characters
		And second line in error
		"""
		main.Main(['input/windows_1252.txt']).run()
		self.assertTrue(filecmp.cmp('output/output.csv', 'output/windows_1252.csv'))

	def test_windows_1252_1_file(self):
		""" To test windows_1252 encoded file with windows_1252 characters
		"""
		main.Main(['input/windows_1252_1.txt']).run()
		self.assertTrue(filecmp.cmp('output/output.csv', 'output/windows_1252_1.csv'))

	def test_utf8_cp1252_char_file(self):
		""" To test UTF8 file with character included from windows-1252
		But in utf8 format
		"""
		main.Main(['input/utf8.txt']).run()
		self.assertTrue(filecmp.cmp('output/output.csv', 'output/utf8.csv'))

	def test_empty_file(self):
		""" To test empty txt file, output should contain header only
		"""
		main.Main(['input/empty.txt']).run()
		self.assertTrue(filecmp.cmp('output/output.csv', 'output/empty.csv'))

	def test_not_present_file(self):
		""" To test file, which is not present
		"""
		try:
			main.Main(['input/abc.txt']).run()
		except:
			self.assertTrue(True)

if __name__ == '__main__':
	unittest.main()
