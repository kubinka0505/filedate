"""Simple, convenient and cross-platform file date changing library."""

__author__  = "kubinka0505"
__credits__ = __author__
__version__ = "3.1"
__date__    = "10th February 2024"

#-=-=-=-#

from .config import *
from .core import *
from .utils import *

#-=-=-=-#

if is_win:
	del byref, windll

del is_win, is_mac, platform