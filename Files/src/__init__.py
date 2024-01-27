"""Simple, convenient and cross-platform file date changing library."""

__author__  = "kubinka0505"
__credits__ = __author__
__version__ = "3.0"
__date__    = "28th December 2023"

#-=-=-=-#

from .config import *
from .core import *
from .utils import *

#-=-=-=-#

if is_NT:
	del byref, windll

del is_NT