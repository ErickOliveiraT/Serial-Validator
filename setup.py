import sys
from cx_Freeze import setup, Executable

setup(
    name = "Default Installer",
    version = "1.0",
    description = "Bargrall's Cripto Pro Validation App",
    executables = [Executable("installer.py", base = None)])