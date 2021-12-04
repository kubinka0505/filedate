import filedate

class Keep:
	"""Utility for "holding" and "releasing" file dates."""
	def __init__(self, Files: list):
		self.Files = Files

	def hold(self) -> dict:
		"""Hold file date."""
		return {File: filedate.get(File) for File in self.Files}

	def release(File_Dates: dict):
		"""Release file date."""
		for Key, Value in File_Dates.items():
			filedate.set(Key,
				created = Value["created"],
				modified = Value["modified"],
				accessed = Value["accessed"]
			)