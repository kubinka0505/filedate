import os
import warnings
from platform import system
from datetime import datetime
from dateutil.parser import parse

#---#

__Path = lambda File: os.path.abspath(os.path.expanduser(os.path.expandvars(File)))
SET_SILENT = True

#---#

def get(File: str) -> dict:
	"""Returns a dictionary containing datetime.fromtimestamp
	objects - when file was created, modified and accessed."""
	info = os.stat(__Path(File))
	dict = {
		"created": info.st_ctime,
		"modified": info.st_mtime,
		"accessed": info.st_atime
	}
	
	for Key, Value in dict.items():
		dict[Key] = datetime.fromtimestamp(Value)

	return dict

#-----#

def set(File: str, modified: str, created: str = None, accessed: str = None):
	"""Sets new file dates.

	All parameters except `File` support:
	- String datetime representations parsable by `dateutil.parser.parse`
	- Epoch times

	"created" is Windows only."""
	File = __Path(File)
	Dates = get(File)
	os.chmod(File, 511)
	#---#

	if modified:
		if isinstance(modified, str):
			modified = parse(modified).timestamp()
		try:
			modified = modified // 1
		except:
			modified = modified.timestamp()
		modified = modified // 1

	if accessed:
		if isinstance(accessed, str):
			accessed = parse(accessed).timestamp()
		try:
			accessed = accessed // 1
		except:
			accessed = accessed.timestamp()
		accessed = accessed // 1

	#---#

	if system() == "Windows":
		if created:
			if isinstance(created, str):
				created = parse(created).timestamp()
			try:
				created = created // 1
			except:
				created = created.timestamp()
			created = created // 1

			from ctypes import windll, wintypes, byref

			timestamp = int((created * 1E7) + 116444736E9)
			ctime = wintypes.FILETIME(timestamp & 0xFFFFFFFF, timestamp >> 32)
			handle = windll.kernel32.CreateFileW(File, 256, 0, None, 3, 128, None)

			# Setting Creation Time
			windll.kernel32.SetFileTime(handle, byref(ctime), None, None)
			windll.kernel32.CloseHandle(handle)
	elif created:
		warnings.warn('"created" argument used not on Windows', Warning, stacklevel = 2)

	# Setting Accessed & Modified Time
	os.utime(File, (accessed, modified))
	#---#
	return None if SET_SILENT else get(File)