import os
from platform import system
from datetime import datetime
from dateutil.parser import parse

#---#

class FileDate:
	def __init__(self, File: str):
		self.file = os.path.abspath(os.path.expanduser(os.path.expandvars(File)))

	def get(self) -> dict:
		"""Returns a dictionary containing datetime.fromtimestamp
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

		All parameters except `File` support:
		- String datetime representations parsable by `dateutil.parser.parse`
		- Epoch times

		"created" is Windows only."""

		Dates = FileDate(self.file).get()
		os.chmod(self.file, 511)

		#---#

		if modified:
			if isinstance(modified, str):
				modified = parse(modified).timestamp()
			try:
				modified = modified // 1
			except:
				modified = modified.timestamp()
		else:
			modified = Dates["modified"].timestamp()
		modified = modified // 1

		if accessed:
			if isinstance(accessed, str):
				accessed = parse(accessed).timestamp()
			try:
				accessed = accessed // 1
			except:
				accessed = accessed.timestamp()
		else:
			accessed = Dates["accessed"].timestamp()
		accessed = accessed // 1

		#---#

		if created:
			if system() == "Windows":
				from ctypes import windll, wintypes, byref

				#---#

				if isinstance(created, str):
					created = parse(created).timestamp()
				try:
					created = created // 1
				except:
					created = created.timestamp()
				created = created // 1

				#---#

				timestamp = int((created * 1E7) + 116444736E9)
				ctime = wintypes.FILETIME(timestamp & 0xFFFFFFFF, timestamp >> 32)
				handle = windll.kernel32.CreateFileW(self.file, 256, 0, None, 3, 128, None)

				# Setting Creation Time
				windll.kernel32.SetFileTime(handle, byref(ctime), None, None)
				windll.kernel32.CloseHandle(handle)

		# Setting Accessed & Modified Time
		os.utime(self.file, (accessed, modified))
		#---#
		return None if FileDate.SET_SILENT else FileDate(self.file).get()
	
	#-----#
	
	SET_SILENT = False