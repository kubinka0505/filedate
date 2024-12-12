from .config import exceptions

import os
import re
from filedate import File
from dateutil.parser import parse

#-=-=-=-#

class Keep:
	def __init__(self, files: list):
		"""
		Initialize self. See help(type(self)) for accurate signature.

		Args:
			files (list): List of files that dates should be kept.
		"""
		if isinstance(files, (list, tuple)):
			files = list(files)
		else:
			files = [files]

		self.files = files

	def pick(self):
		"""
		Picks the files dates.
		"""
		self.dates = {}

		for path in self.files:
			self.dates.update({path: File(path).get()})

	def drop(self):
		"""
		Drops the files dates.
		"""
		for path, dates in self.dates.items():
			File(path).set(
				created  = dates["created"],
				modified = dates["modified"],
				accessed = dates["accessed"]
			)
	
	hold = pick
	release = drop

#-=-=-=-#

class set_from:
	def file_name(path: str, created: bool = True, modified: bool = True, accessed: bool = True):
		"""
		Utility for setting file date based on its name.

		Args:
			path (string): Existing file path.

			created  (boolean):  Determines whether the file creation date should be set. Windows only.
			modified (boolean):  Determines whether the file modification date should be set.
			accessed (boolean):  Determines whether the file last access date should be set.
		"""
		file_obj  = File(path)
		file_name = os.path.basename(file_obj.path)
		file_name = os.path.splitext(file_name)[0]

		error = 0
		try:
			regex = re.sub(r"\D", " ", file_name).strip()

			date = parse(regex).timestamp()
		except ValueError:
			error = 1
		
		if error:
			raise exceptions.path.NO_DATE.__class__(
				exceptions.path.NO_DATE.args[0].format(string = file_name)
			)

		if created:  file_obj.created  = date
		if modified: file_obj.modified = date
		if accessed: file_obj.accessed = date

	name = from_name = file_name

#-=-=-=-#

def copy(input_file: str, output_file: str, created: bool = True, modified: bool = True, accessed: bool = True):
	"""
	Copies file dates from one file to another.

	Args:
		input_file  (string): Existing file path which dates will be copied from.
		output_file (string): Existing file path which dates will be copied to.

		created  (boolean): Determines whether the input file's creation date should be copied. Windows only.
		modified (boolean): Determines whether the input file's modification date should be copied.
		accessed (boolean): Determines whether the input file's last access date should be copied.
	"""
	input_obj  = File(input_file)
	output_obj = File(output_file)

	if created:  output_obj.created  = input_obj.created
	if modified: output_obj.modified = input_obj.modified
	if accessed: output_obj.accessed = input_obj.accessed

keep = Keep