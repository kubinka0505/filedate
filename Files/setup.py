from setuptools import *

setup(
	name = "filedate",
	description = open("ReadMe.rst").readline().rstrip(),
	version = "1.6",
	author = "kubinka0505",
	license = "GPLv3",
	keywords = "filedate file date change changing changer",
	url = "https://github.com/kubinka0505/filedate",
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
	python_requires = ">=3.3",
	install_requires = "python-dateutil",
	packages = find_packages()
)