import os
from pathlib import Path
from datetime import datetime
from dateutil.parser import parse

#-=-=-=-#

if os.sys.platform.startswith("win"):
	from ctypes import windll, wintypes, byref

#-=-=-=-#

class File:
	def __init__(self, File: str):
		File = os.path.expandvars(File)    # Windows
		File = os.path.expanduser(File)    # Linux
		File = os.path.abspath(File)       # Full
		File = str(Path(File).resolve())   # Normalize

		self.file = File

	def _modify(parameter: str):
		"""Convert `filedate.File.set` parameter to Epoch time."""
		if isinstance(parameter, str):
			parameter = parse(parameter).timestamp()
		try:
			parameter = parameter // 1
		except TypeError:
			parameter = parameter.timestamp()
		return parameter
		

	def get(self) -> dict:
		"""Returns a dictionary containing `datetime.fromtimestamp`
		objects - when file was created, modified and accessed.
		"""
		info = os.stat(self.file)
		dict = {
			"created": info.st_ctime,
			"modified": info.st_mtime,
			"accessed": info.st_atime
		}
		
		for Key, Value in dict.items():
			dict[Key] = datetime.fromtimestamp(Value)

		return dict

	#-=-=-=-#

	def set(self, modified: str = None, created: str = None, accessed: str = None):
		"""Sets new file dates.

		All parameters except `self.File` support:
		- String datetime representations parsable by `dateutil.parser.parse`
		- Epoch times

		`created` parameter is Windows only.
		"""

		Dates = File(self.file).get()
		os.chmod(self.file, 511)

		#---#

		created = int((File._modify(created) if created else Dates["created"].timestamp()))
		modified = int((File._modify(modified) if modified else Dates["modified"].timestamp()))
		accessed = int((File._modify(accessed) if accessed else Dates["accessed"].timestamp())) 

		#---#

		if created:
			if os.sys.platform.startswith("win"):
				timestamp = int((created * 1E7) + 116444736E9)
				ctime = wintypes.FILETIME(timestamp & 0xFFFFFFFF, timestamp >> 32)
				handle = windll.kernel32.CreateFileW(self.file, 256, 0, None, 3, 128, None)

				# Setting Created Time
				windll.kernel32.SetFileTime(handle, byref(ctime), None, None)
				windll.kernel32.CloseHandle(handle)

		#---#

		# Setting Accessed & Modified Time
		os.utime(self.file, (accessed, modified))

		#---#

		return None if File.SET_SILENT else File(self.file).get()
	
	#-=-=-=-#
	
	SET_SILENT = False