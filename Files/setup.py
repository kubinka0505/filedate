from setuptools import *

setup(
	name = "filedate",
	description = "Simple, convenient and cross-platform file date changing library.",
	version = "1.3",
	author = "kubinka0505",
	license = "GPL v3",
	keywords = "filedate file date change changing changer",
	url = "https://github.com/kubinka0505/filedate",
	packages = find_packages(),
	install_requires = ["python-dateutil"],
	classifiers = [
		"Development Status :: 6 - Mature",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Programming Language :: Python :: 3 :: Only",
		"Operating System :: OS Independent",
		"Environment :: Console",
		"Intended Audience :: End Users/Desktop",
		"Topic :: Desktop Environment :: File Managers",
		"Natural Language :: English"
	],
)