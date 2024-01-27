"""Module configuration classes and variables."""

class exceptions:

	class path:
		NOT_FOUND = FileNotFoundError("File was not found")
		NO_DATE   = ValueError("Parsed string does not contain a date")

#-=-=-=-=-=-#

# Setup

import os

is_NT = os.sys.platform.lower().startswith("win")