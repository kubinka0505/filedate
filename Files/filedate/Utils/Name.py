import re
from pathlib import Path
from filedate import File
from dateutil.parser import parse

#-=-=-=-#

class Name:
	"""Utility for setting file date based on its name."""
	def __init__(self, input: str):
		self.input = input
		try:
			regex = re.sub(
				r"\D",
				" ",
				Path(self.input).stem
			).strip()
			self.__date = parse(regex).timestamp()
		except ValueError:
			raise ValueError("Parsed string does not contain a date")

	def created(self):
		"""Sets the created date based on `self.input` file name."""
		File(self.input).set(created = self.__date)

	def modified(self):
		"""Sets the modified date based on `self.input` file name."""
		File(self.input).set(modified = self.__date)

	def accessed(self):
		"""Sets the accessed date based on `self.input` file name."""
		File(self.input).set(accessed = self.__date)

	def all(self):
		"""Sets all dates based on `self.input` file name."""
		File(self.input).set(
			created = self.__date,
			modified = self.__date,
			accessed = self.__date
		)

#-=-=-=-#

FromFile = FromName = Name