from filedate import FileDate

class Keep:
	"""Utility for "holding" and "releasing" file dates."""
	def __init__(self, Files: list):
		self.files = Files

	def hold(self) -> dict:
		"""Hold the file date."""
		self.__dates = {File: FileDate(File).get() for File in self.files}

	def release(self):
		"""Release the file date."""
		for Key, Value in self.__dates.items():
			FileDate(Key).set(
				created = Value["created"],
				modified = Value["modified"],
				accessed = Value["accessed"]
			)