import os
from warnings import warn
from filedate import File

#-=-=-=-#

class Copy:
	"""Utility for "copying" files dates."""
	def __init__(self, input: str, output: str):
		self.input = File(input).get()
		self.output = File(output)

	def created(self):
		"""Copies created date from `self.input` to `self.output`."""
		if not os.sys.platform.startswith("win"):
			warn('Unix system - setting creation date is obsolete')
		#-=-=-=-#
		self.output.set(created = self.input["created"])

	def modified(self):
		"""Copies created date from `self.input` to `self.output`."""
		self.output.set(modified = self.input["modified"])

	def accessed(self):
		"""Copies created date from `self.input` to `self.output`."""
		self.output.set(accessed = self.input["accessed"])
	
	def all(self):
		"""Copies all dates from `self.input` to `self.output`."""
		self.output.set(
			created = self.input["created"],
			modified = self.input["modified"],
			accessed = self.input["accessed"]
		)

#-=-=-=-#

Move = Transfer = Copy