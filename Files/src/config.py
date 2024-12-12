"""Module configuration classes and variables."""

import os

platform = os.sys.platform.lower()

is_win = platform.startswith("win")
is_mac = platform.startswith("darwin")

#-=-=-=-=-=-#

class exceptions:
	SYSTEM = OSError

	class date:
		WRONG = ValueError("One of the dates could not be converted to a date object")
		RANGE_TIMESTAMP_SET = ValueError("Cannot use this `datetime.datetime` object to set the date, as its `timestamp` bound method call fails")
		RANGE_DATETIME_SET = ValueError("Cannot set the date not being in the `datetime.datetime` values range")

	class path:
		NOT_FOUND = FileNotFoundError('File was not found ("{file_path}")')
		NO_DATE   = ValueError('No date was detected in the parsed path string ("{string}")')