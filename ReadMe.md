<p align=center><img src=https://raw.githubusercontent.com/kubinka0505/filedate/master/Documents/Pictures/filedate.svg width=50%></p>

<p align=center><a href=http://github.com/kubinka0505/filedate/releases><img src=https://img.shields.io/github/v/release/kubinka0505/filedate?style=for-the-badge></a>　<a href=http://github.com/kubinka0505/filedate/commit><img src=https://img.shields.io/github/last-commit/kubinka0505/filedate?style=for-the-badge></a>　<a href=http://github.com/kubinka0505/filedate/blob/master/License.txt><img src=https://img.shields.io/github/license/kubinka0505/filedate?logo=readthedocs&color=red&logoColor=white&style=for-the-badge></a></p>

<p align=center><img src=https://img.shields.io/tokei/lines/github/kubinka0505/filedate?style=for-the-badge>　<img src=https://img.shields.io/github/languages/code-size/kubinka0505/filedate?style=for-the-badge>　<img src=https://img.shields.io/codeclimate/maintainability/kubinka0505/filedate?logo=code-climate&style=for-the-badge>　<img src=https://img.shields.io/codacy/grade/c8aeb5f42a38414da83d4156b546a4d1?logo=codacy&style=for-the-badge></p>

## Description 📝
Simple, convenient and cross-platform file date changing library.

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
File_Date = filedate.File("~/Desktop/File.txt")

# Get file date
File_Date.get()

# Set file date
File_Date.set(
	created = "01.01.2000 12:00",
	modified = "3:30PM 2001/02/02",
	accessed = "3rd March 2002 20:00:30"
)
```

### Copy file date from one to another 🔃
```python
import filedate

filedate.Utils.copy(
	"~/Desktop/Input.mp4",
	"~/Desktop/Output.mp4"
)
```

### **Keeping files dates** ⌛
```python
import filedate
from pathlib import Path

# Get all files in directory (recursive!)
Files = []
for File in Path(".").glob("**/*"):
	Files.append(File)

#---#

# Initialize `Keep` object
Dates = filedate.Utils.Keep(Files)

#---#

Dates.hold()

# ... Do your stuff ...
#
# from os import system
# for File in Files:
# 	system(f'optimize -i "{File}"')

Dates.drop()
```

### **Set file date based on its name** 📝
```python
import filedate

# Sets creation date
File_Date = filedate.Utils.fromfile(
	"~/Downloads/20200919_134705.wav",
	"created"
)

# Sets all file dates
File_Date = filedate.Utils.fromfile(
	"20010204_103503.mp3",
	0
)