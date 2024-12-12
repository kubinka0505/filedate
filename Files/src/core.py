"""Module core."""

from .config import exceptions, is_win, is_mac

import os
from pathlib import Path
from datetime import datetime
from dateutil.parser import parse

if is_win:
	from ctypes import windll, wintypes, byref

#-=-=-=-#

class File:
	def __init__(self, path: str):
		"""
		Initialize self. See help(type(self)) for accurate signature.

		Args:
			path (string): Existing file path.
		"""
		path = os.path.abspath(path)
		path = str(Path(path).resolve())

		if not os.path.exists(path):
			raise exceptions.path.NOT_FOUND.__class__(
				exceptions.path.NOT_FOUND.args[0].format(file_path = path)
			)

		self.path = path

	def __modify(self, parameter):
		error = 0
		reset = 0

		# `dateutil.parser.parse` string
		if isinstance(parameter, str):
			if parameter.lower() == "now":
				reset = 1
			else:
				try:
					parameter = parse(parameter).timestamp()
				except OSError:
					error = exceptions.date.RANGE_DATETIME_SET

		# EPOCH timestamp number
		if isinstance(parameter, (int, float)):
			if parameter < 0:
				reset = 1

		# Iterable collection
		if isinstance(parameter, (list, tuple)):
			if parameter:
				parameter = datetime(*map(int, parameter)).timestamp()

		# Datetime object
		if isinstance(parameter, datetime):
			try:
				parameter = parameter.timestamp()
			except OSError:
				error = exceptions.date.RANGE_TIMESTAMP_SET

		#-=-=-=-#

		# Set to `datetime.datetime.now()`
		if reset:
			parameter = datetime.now().timestamp()

		if error:
			raise error

		return parameter

	#-=-=-=-#
	# Properties

	@property
	def file(self):
		return self.path

	## Created

	@property
	def created(self) -> datetime:
		return self.get()["created"]

	@created.setter
	def created(self, date):
		return self.set(created = date)

	@created.deleter
	def created(self):
		return self.set(created = "now")

	## Modified

	@property
	def modified(self) -> datetime:
		return self.get()["modified"]

	@modified.setter
	def modified(self, date):
		return self.set(modified = date)

	@modified.deleter
	def modified(self):
		return self.set(modified = "now")

	## Accessed

	@property
	def accessed(self) -> datetime:
		return self.get()["accessed"]

	@accessed.setter
	def accessed(self, date):
		return self.set(accessed = date)

	@accessed.deleter
	def accessed(self):
		return self.set(accessed = "now")

	#-=-=-=-#

	def get(self) -> dict:
		"""
		Returns:
			dict: `datetime` objects - when file was created, modified and accessed.
		"""
		error = 0

		info = os.stat(self.path)
		dates = {
			"created":  info.st_ctime,
			"modified": info.st_mtime,
			"accessed": info.st_atime
		}

		for key, value in dates.items():
			dates[key] = datetime.fromtimestamp(value)

		if error:
			raise error

		return dates

	def set(self, modified: str = None, accessed: str = None, created: str = None):
		"""
		Modifies file's dates.

		Arguments can be:
			- String parsable by `dateutil.parser.parse`
			- supported epoch time number
			- Iterable collection in to `datetime.datetime` format
			- `datetime.datetime` object
			- "now": equivalent to `datetime.datetime.now`
			- None: not modifying

		Args:
			created:  Date of file creation. Does nothing on non-Windows operating systems.
			modified: Date of file modification.
			accessed: Date of file access.
		"""
		# Created
		if created:
			created = int((self.__modify(created)))
		else:
			created = File(self.path).get()["created"].timestamp()

		# Modified
		if modified:
			modified = float((self.__modify(modified)))
		else:
			modified = File(self.path).get()["modified"].timestamp()

		# Accessed
		if accessed:
			accessed = float((self.__modify(accessed)))
		else:
			accessed = File(self.path).get()["accessed"].timestamp()

		#-=-=-=-#

		error = 0
		try:
			if created:
				if is_win:
					timestamp = int((created * 1E7) + 116444736E9)
					ctime  = wintypes.FILETIME(timestamp & 0xFFFFFFFF, timestamp >> 32)
					handle = windll.kernel32.CreateFileW(self.path, 256, 0, None, 3, 33554560, None)

					windll.kernel32.SetFileTime(handle, byref(ctime), None, None)
					windll.kernel32.CloseHandle(handle)
				elif is_mac:
					_util = (
						"/Developer/Tools/SetFile",
						"/usr/bin/SetFile",
						"/Developer/usr/bin/SetFile"
					)

					for file in _util:
						if os.path.exists(file):
							_util = file
							break

					if isinstance(_util, str):
						command = '{0} -d "{1}" "{2}"'.format(
							_util,
							datetime.fromtimestamp(created).strftime("%m/%d/%Y %H:%M:%S"),
							self.path
						)

						process = subprocess.Popen(
							command, shell = True,
							stdout = subprocess.PIPE,
							stderr = subprocess.PIPE
						)

			os.utime(self.path, (accessed, modified))
		except OSError:
			error = exceptions.date.WRONG

		if error:
			raise error

	#-=-=-=-=-=-#

	# "Dunder" methods

	def __dir__(self):
		return self.get().values()

	#-=-=-=-=-=-#

	# Aliases

	date_created  = creation_date     = created
	date_modified = modification_date = modified
	date_accessed = accesed_date      = accessed

file = File