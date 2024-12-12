import os
from shutil import rmtree
from setuptools import setup, find_packages

# Remove directories after installing
cleanup = True

#-=-=-=-#

__title__ = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#-=-=-=-#

# Cleanup
if cleanup:
	if "install" in os.sys.argv:

		# Built directories
		dirs = [
			"build", "dist", "name",
			f"{__title__}.egg-info"
		]

		for directory in dirs:
			rmtree(directory, True)

directory = "src"
if os.path.exists(directory):
	os.rename(directory, __title__)

#-=-=-=-#

tags = [__title__, "file", "date", "change", "changing", "changer"]

setup(
	name = __title__,
	version = "3.1",
	author = "kubinka0505",
	url = f"https://github.com/kubinka0505/{__title__}",
	keywords = tags,
	classifiers = [
		"Development Status :: 6 - Mature",
		"Environment :: Console",
		"Intended Audience :: Developers",
		"Intended Audience :: End Users/Desktop",
		"Intended Audience :: System Administrators",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Natural Language :: English",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3 :: Only",
		"Topic :: Desktop Environment :: File Managers",
	],
	python_requires = ">=3.4",
	install_requires = [
		"python-dateutil",
	],
	entry_points={
		"console_scripts": [
			"filedate = filedate.cli_core:main",
		]
	},
	packages = find_packages()
)

#-=-=-=-#

if os.path.exists(__title__):
	os.rename(__title__, directory)