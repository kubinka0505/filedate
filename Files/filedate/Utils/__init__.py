from filedate import File

class Keep:
	"""Utility for "holding" and "dropping" file dates."""
	def __init__(self, Files: list):
		self.files = list(Files)

	def pick(self) -> dict:
		"""Pick the files dates."""
		self.__dates = {}
		for Path in self.files:
			self.__dates.update({Path: File(Path).get()})

	def drop(self):
		"""Drop the files dates."""
		for Key, Value in self.__dates.items():
			File(Key).set(
				created = Value["created"],
				modified = Value["modified"],
				accessed = Value["accessed"]
			)
	
	hold = pick
	release = drop

#---#

def copy(input: str, output: str):
	"""Copy one file date to another."""
	input = File(input).get()

	File(output).set(
		created = input["created"],
		modified = input["modified"],
		accessed = input["accessed"]
	)

def swap(input: str, output: str):
	"""Swaps file dates to another."""
	input = File(input).get()
	output = File(output).get()
	
	File(input).set(
		created = output["created"],
		modified = output["modified"],
		accessed = output["accessed"]
	)

#---#

move = transfer = copy