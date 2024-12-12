import os
import filedate
import unittest
from datetime import datetime

files = ("!_01_file.test", "!_02_file.test")

for file in files:
	open(file, "w").close()

file_obj_01 = filedate.File(files[0])
file_obj_02 = filedate.File(files[1])

#-=-=-=-#

class Test(unittest.TestCase):
	def test_check_path(self):
		assert file_obj_01.path == os.path.abspath(files[0])

	def test_created(self):
		file_obj_01.created = "01st September 2016"
		assert file_obj_01.created == datetime(day = 1, month = 9, year = 2016)

	def test_modified(self):
		file_obj_01.modified = "28th April 2018"
		assert file_obj_01.modified == datetime(day = 28, month = 4, year = 2018)

	def test_accessed(self):
		file_obj_01.accessed = "23rd June 2019"
		assert file_obj_01.accessed == datetime(day = 23, month = 6, year = 2019)

	def test_copy(self):
		# Not created, as differences with microseconds occur
		filedate.copy(files[0], files[1])
		assert file_obj_01.modified == file_obj_02.modified

	#-=-=-=-#

	def test_keep(self):
		file_obj_01_orig = file_obj_01.get()
		file_obj_02_orig = file_obj_02.get()

		#-=-=-=-#

		file_keep_obj = filedate.utils.Keep(files)

		file_keep_obj.pick()

		for file in files:
			date_temp_obj = filedate.File(file)

			date_temp_obj.modified = "01st January 2024"
			date_temp_obj.accessed = "28th December 2023"

			assert date_temp_obj.modified == datetime(day = 1, month = 1, year = 2024)
			assert date_temp_obj.accessed == datetime(day = 28, month = 12, year = 2023)

		file_keep_obj.drop()

		assert file_obj_01_orig == file_obj_01.get()
		assert file_obj_02_orig == file_obj_02.get()

#-=-=-=-#

if __name__ == "__main__":
	unittest.main()