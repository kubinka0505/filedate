import os
from platform import system
from datetime import datetime
from dateutil.parser import parse

#---#

class File:
	def __init__(self, File: str):
		self.file = os.path.abspath(os.path.expanduser(os.path.expandvars(File)))

	def _modify(parameter: str):
		"""Convert `set` parameter to Epoch time."""
		if isinstance(parameter, str):
			parameter = parse(parameter).timestamp()
		try:
			parameter = parameter // 1
		except TypeError:
			parameter = parameter.timestamp()
		return parameter
		

	def get(self) -> dict:
		"""Returns a dictionary containing `datetime.fromtimestamp`
		objects - when file was created, modified and accessed."""
		info = os.stat(self.file)
		dict = {
			"created": info.st_ctime,
			"modified": info.st_mtime,
			"accessed": info.st_atime
		}
		
		for Key, Value in dict.items():
			dict[Key] = datetime.fromtimestamp(Value)

		return dict

	#-----#

	def set(self, modified: str, created: str = None, accessed: str = None):
		"""Sets new file dates.

		All parameters except `self.File` support:
		- String datetime representations parsable by `dateutil.parser.parse`
		- Epoch times

		`created` parameter is Windows only."""

		Dates = File(self.file).get()
		os.chmod(self.file, 511)

		#---#

		created = (File._modify(created) if created else Dates["created"].timestamp()) // 1
		modified = (File._modify(modified) if modified else Dates["modified"].timestamp()) // 1
		accessed = (File._modify(accessed) if accessed else Dates["accessed"].timestamp()) // 1

		#---#

		if created:
			if system() == "Windows":
				from ctypes import windll, wintypes, byref

				timestamp = int((created * 1E7) + 116444736E9)
				ctime = wintypes.FILETIME(timestamp & 0xFFFFFFFF, timestamp >> 32)
				handle = windll.kernel32.CreateFileW(self.file, 256, 0, None, 3, 128, None)

				# Setting Creation Time
				windll.kernel32.SetFileTime(handle, byref(ctime), None, None)
				windll.kernel32.CloseHandle(handle)

		#---#

		# Setting Accessed & Modified Time
		os.utime(self.file, (accessed, modified))

		return None if File.SET_SILENT else File(self.file).get()
	
	#-----#
	
	SET_SILENT = False