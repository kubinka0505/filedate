"""File date manager core."""

from .config import exceptions, is_NT

import os
from pathlib import Path
from datetime import datetime
from dateutil.parser import parse

if is_NT:
	from ctypes import windll, wintypes, byref

#-=-=-=-#

class File:
	def __init__(self, path: str):
		"""
		Initialize self. See help(type(self)) for accurate signature.

		Args:
			path:   Existing file path.
		"""
		path = os.path.abspath(path)
		path = str(Path(path).resolve())

		if not os.path.exists(path):
			raise exceptions.path.NOT_FOUND

		self.path = path

	def _modify(self, parameter: str):
		if isinstance(parameter, str):
			parameter = parse(parameter).timestamp()
		try:
			parameter = parameter // 1
		except TypeError:
			parameter = parameter.timestamp()

		return parameter

	#-=-=-=-#
	# Properties

	@property
	def file(self):
		return self.path

	## Created

	@property
	def created(self):
		return self.get()["created"]

	@created.setter
	def created(self, date) -> datetime:
		return self.set(created = date)

	#if not is_NT:
	#	del created

	## Modified

	@property
	def modified(self):
		return self.get()["modified"]

	@modified.setter
	def modified(self, date) -> datetime:
		return self.set(modified = date)

	## Accessed

	@property
	def accessed(self):
		return self.get()["accessed"]

	@accessed.setter
	def accessed(self, date) -> datetime:
		return self.set(accessed = date)

	#-=-=-=-#

	def get(self) -> dict:
		"""
		Returns:
			dict: `datetime` objects - when file was created, modified and accessed.
		"""
		info = os.stat(self.path)
		dates = {
			"created":  info.st_ctime,
			"modified": info.st_mtime,
			"accessed": info.st_atime
		}
		
		for key, value in dates.items():
			dates[key] = datetime.fromtimestamp(value).replace(microsecond = 0)

		return dates

	def set(self, modified: str = None, created: str = None, accessed: str = None):
		"""
		Modifies file's dates.

		Arguments can be string date representation parsable by `dateutil.parser.parse` or time from epoch.

		Args:
			created:  Date of file creation. Windows only - sets `modified` time on other systems.
			modified: Date of file last modification.
			accessed: Date of file last access.
		"""
		dates = File(self.path).get()

		created  = int((self._modify(created)  if created  else dates["created"].timestamp()))
		modified = int((self._modify(modified) if modified else dates["modified"].timestamp()))
		accessed = int((self._modify(accessed) if accessed else dates["accessed"].timestamp())) 
	
		err = 0
		try:
			if created:
				if is_NT:
					timestamp = int((created * 1E7) + 116444736E9)
					ctime  = wintypes.FILETIME(timestamp & 0xFFFFFFFF, timestamp >> 32)
					handle = windll.kernel32.CreateFileW(self.path, 256, 0, None, 3, 33554560, None)

					windll.kernel32.SetFileTime(handle, byref(ctime), None, None)
					windll.kernel32.CloseHandle(handle)

			os.utime(self.path, (accessed, modified))
		except OSError:
			err = exceptions.date.WRONG

		if err:
			raise err

	#-=-=-=-=-=-#

	# Special methods

	def __dir__(self):
		return self.get().values()

	#-=-=-=-=-=-#

	# Aliases

	get_dates     = get
	date_created  = created
	date_modified = modified
	date_accessed = accessed

file = File