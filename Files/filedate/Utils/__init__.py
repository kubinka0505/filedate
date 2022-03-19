import re
from filedate import File
from dateutil.parser import parse

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
	output = File(output).get()
	
	File(input).set(
		created = output["created"],
		modified = output["modified"],
		accessed = output["accessed"]
	)

def name(input: str, type: int = "created"):
	"""Sets date(s) of a file based on its name.
	
	Types (accordingly):
	1 / "created"
	2 / "modified"
	3 / "accessed"
	0 / "all\""""
	input__ = ".".join(input.split(".")[:-1])
	input__ = re.sub(r"\D", " ", input__).strip()
	try:
		date = parse(input__).timestamp()
	except ValueError:
		raise ValueError("Parsed string does not contain a date")

	#---#

	File_ = File(input)
	input_ = File_.get()
	type = str(type).lower()

	File_.set(
		created = date if type in ("0", "all", "1", "created") else input_["created"],
		modified = date if type in ("0", "all", "2", "modified") else input_["modified"],
		accessed = date if type in ("0", "all", "3", "accessed") else input_["accessed"]
	)

#---#

move = transfer = copy
fromfile = fromname = fromfn = name