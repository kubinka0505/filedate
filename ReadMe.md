
<p align=center>
	<img src="https://raw.githubusercontent.com/kubinka0505/filedate/master/Documents/Pictures/filedate.svg" width=50%>
</p>

<p align=center>
	<a href="https://github.com/kubinka0505/filedate/commit"><img src="https://custom-icon-badges.demolab.com/github/last-commit/kubinka0505/filedate?logo=commit&style=for-the-badge"></a>　<a href="https://github.com/kubinka0505/filedate/blob/master/License.txt"><img src="https://custom-icon-badges.demolab.com/github/license/kubinka0505/filedate?logo=law&color=red&style=for-the-badge"></a>
</p>

<p align=center>
	<a href="https://codeclimate.com/github/kubinka0505/filedate"><img src="https://img.shields.io/codeclimate/maintainability/kubinka0505/filedate?logo=code-climate&style=for-the-badge"></a>　<a href="https://app.codacy.com/gh/kubinka0505/filedate/issues"><img src="https://img.shields.io/codacy/grade/2922b11937274ecd95fd853daeb800b2?logo=codacy&style=for-the-badge"></a>　<a href="https://app.codacy.com/gh/kubinka0505/filedate/coverage/dashboard"><img src="https://img.shields.io/codacy/coverage/2922b11937274ecd95fd853daeb800b2?logo=code-climate&style=for-the-badge"></a>
</p>

## Description 📝
Simple, convenient and cross-platform file date changing library. 📅

## Installation 🖥️
1. [`git`](https://git-scm.com) (recommended)
```bash
git clone git://github.com/kubinka0505/filedate
cd filedate/Files
python setup.py install
```

> [!TIP]
> You can alse use this ugly one-liner for most recent commits:
> ```python
> python -m pip install "git+https://github.com/kubinka0505/filedate#egg=filedate&subdirectory=Files" -U --use-deprecated=legacy-resolver
> ```

2. [`pip`](https://pypi.org/project/pip)
```bash
python -m pip install filedate -U
```
 
## Usage 📝
```python
import filedate

# Create filedate object
File = filedate.File("~/Desktop/File.txt")

# Get file date
File.get_dates()

# Alternatives
dir(File)
File.created, File.modified, File.accessed

# Set file date
File.created  = "01.01.2000 12:00"
File.modified = "3:30PM 2001/02/02"
File.accessed = "3rd March 2002 20:00:30"

# Legacy
File.set(
    created  = "01.01.2000 12:00",
    modified = "3:30PM 2001/02/02",
    accessed = "3rd March 2002 20:00:30"
)
```

<details open>
	<summary><b>Copy file dates from one to another</b> 🔃</summary>

```python
import filedate

filedate.copy(
    "~/Desktop/Input.mp4", "~/Desktop/Output.mp4",
    created = True,
    modified = True,
    accessed = True
)
```
</details>

<details open>
	<summary><b>Keeping files dates</b> ⌛</summary>

```python
import filedate
from pathlib import Path

# Get all files in subdirectories (recursive!)
Files = []
for File in Path(".").glob("**/*"):
    File = str(File.resolve())
    Files.append(File)

#-=-=-=-#

# Initialize `Keep` object
dates = filedate.utils.Keep(Files)

# Pick dates
dates.pick()

# ... Do your stuff ...
# 
# from os import system
# for File in Files:
#     system(f'optimize -i "{File}"')

# Drop dates
dates.drop()
```
</details>

<details open>
	<summary><b>Set file dates based on its name</b> (beta) 📝</summary>

```python
from filedate import utils

utils.set_from.file_name(
    "~/Downloads/20200919_134705.wav",
    created = True,
    modified = False,
    accessed = True,
)
```
</details>
