<p align=center><img src=https://raw.githubusercontent.com/kubinka0505/filedate/master/Documents/Pictures/filedate.svg width=50%></p>
　
<p align=center><href=http://github.com/kubinka0505/filedate/releases/><img src=https://img.shields.io/github/v/release/kubinka0505/filedate?style=for-the-badge></a>　<a href=http://github.com/kubinka0505/filedate/commit><img src=https://img.shields.io/github/last-commit/kubinka0505/filedate?style=for-the-badge></a>　<a href=http://github.com/kubinka0505/filedate/blob/master/License.txt><img src=https://img.shields.io/github/license/kubinka0505/filedate?logo=readthedocs&color=red&logoColor=white&style=for-the-badge></a></p>

<p align=center><img src=https://img.shields.io/tokei/lines/github/kubinka0505/filedate?style=for-the-badge>　<img src=https://img.shields.io/github/languages/code-size/kubinka0505/filedate?style=for-the-badge>　<img src=https://img.shields.io/codeclimate/maintainability/kubinka0505/filedate?logo=code-climate&style=for-the-badge>　<img src=https://img.shields.io/codacy/grade/c8aeb5f42a38414da83d4156b546a4d1?logo=codacy&style=for-the-badge></p>

## Description 📝
Simple, convenient and cross-platform file date changing library.

## Requirements 📥
Programs:
- [`Python >= 3.6`](http://www.python.org/downloads) 🐍

Modules:
- [`dateutil`](https://github.com/dateutil/dateutil) - String date times conversion to [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime) objects 📅

## Installation 🖥️

1. [`git`](https://git-scm.com) (recommended)
```bash
git clone https://github.com/kubinka0505/filedate
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
File_Date = filedate.File("~/Documents/File.txt")

# Get file date
File_Date.get()

# Set file date
File_Date.set(
	created = "01.01.2000 12:00",
	modified = "3:30PM 2001/02/02",
	accessed = "3rd March 2002 20:00:30"
)
```

### **Keeping files dates** ⌛
```python
import filedate
from pathlib import Path

# Get all files in directory (recursive!)
Files = [str(File.resolve()) for File in Path(".").glob("**/*")]

#---#

# Initialize `Keep` object
Dates = filedate.Utils.Keep(Files)

#---#

Dates.hold()

# ... Do your stuff ...
#
# from os import system
# [system(f'optimize -i "{File}"') for File in Files]

Dates.drop()
```