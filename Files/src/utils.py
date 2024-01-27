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
			files: List of files that dates should be kept.
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
		self.__dates = {}

		for file in self.files:
			self.__dates.update({file: File(file).get()})

	def drop(self):
		"""
		Drops the files dates.
		"""
		for key, value in self.__dates.items():
			File(key).set(
				created  = value["created"],
				modified = value["modified"],
				accessed = value["accessed"]
			)
	
	hold = pick
	release = drop

#-=-=-=-#

class set_from:
	def file_name(path: str, created: bool = True, modified: bool = True, accessed: bool = True):
		"""Utility for setting file date based on its name."""
		file_obj  = File(path)

		err = 0
		try:
			file_name = os.path.basename(file_obj.path)
			file_name = os.path.splitext(file_name)[0]

			regex = re.sub(r"\D", " ", file_name).strip()

			date = parse(regex).timestamp()
		except ValueError:
			err = 1
		
		if err:
			raise exceptions.path.NODATE

		if created:  file_obj.created  = date
		if modified: file_obj.modified = date
		if accessed: file_obj.accessed = date

	name = from_name = file_name

#-=-=-=-#

def copy(input_file: str, output_file: str, created: bool = True, modified: bool = True, accessed: bool = True):
	"""
	Copies file dates.

	Args:
		input_file:  Existing file path which dates will be copied from.
		output_file: Existing file path which dates will be copied to.

		created:  If True, input file's creation date will be copied.
		modified: If True, input file's last modification date will be copied.
		accessed: If True, input file's last access date will be copied.
	"""
	input_obj  = File(input_file)
	output_obj = File(output_file)

	if created:  output_obj.created  = input_obj.created
	if modified: output_obj.modified = input_obj.modified
	if accessed: output_obj.accessed = input_obj.accessed

keep = Keep