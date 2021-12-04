<h1 align=center><code><b>Filedate</b></code> 📝📅</h1>
<p align=center><a href=http://github.com/kubinka0505/filedate/releases/><img src=https://img.shields.io/github/v/release/kubinka0505/filedate?style=for-the-badge></a>　<a href=http://github.com/kubinka0505/filedate/commit><img src=https://img.shields.io/github/last-commit/kubinka0505/filedate?style=for-the-badge></a>　<a href=http://github.com/kubinka0505/filedate/blob/master/License.txt><img src=https://img.shields.io/github/license/kubinka0505/filedate?logo=readthedocs&color=red&logoColor=white&style=for-the-badge></a></p>

<p align=center><img src=https://img.shields.io/tokei/lines/github/kubinka0505/filedate?style=for-the-badge>　<img src=https://img.shields.io/github/languages/code-size/kubinka0505/filedate?style=for-the-badge>　<img src=https://img.shields.io/codeclimate/maintainability/kubinka0505/filedate?logo=code-climate&style=for-the-badge>　<img src=https://img.shields.io/codacy/grade/c8aeb5f42a38414da83d4156b546a4d1?logo=codacy&style=for-the-badge></p>

## Description 📝
Simple file date changing library. *<sub>~~with complicated code~~</sub>*

## Requirements 📥
Programs:
- [`Python >= 3.5`](http://www.python.org/downloads) 🐍

Modules:
- [`dateutil`](http://github.com/python-pillow/Pillow) - String date times conversion to [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime) objects 📅

## Installation 🖥️

1. [`git`](https://git-scm.com) (recommended)
```bash
git clone git://github.com/kubinka0505/filedate
cd filedate/Files
python setup.py install
```

2. [`pip`](https://pypi.org/project/pip)
```bash
python -m pip install filedate
```
 
## Usage 📝

```python
import filedate
File_Path = "~/Documents/File.txt"

# Get file date
filedate.get(File_Path)

# Set file date
filedate.set(File_Path,
	created = "01.01.2000 12:00",
	modified = "3:30PM 2001/02/02",
	accessed = "3rd March 2002 20:00:30"
)
```

### **Keeping file dates** ⌛
```python
from pathlib import Path
from filedate.Utils import Keep

#---#

Files = []
Directory = "~/Documents/Directory"

#---#

# Recursive!
Files = [str(File.resolve()) for File in Path(Directory).glob("**/*")]

# = Hold =
Dates = Keep(Files).hold()

# ... Do your stuff ...
#
# import os
# [os.rename(File, File.replace("_.", ".")) for File in Files]

# = Release =
Keep.release(Dates)
```