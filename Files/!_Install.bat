@echo off
color 0e

for %%I in (..) do set Name=%%~nxI

pip uninstall %Name% -y
py setup.py install

rd build dist %Name%.egg-info /S /Q