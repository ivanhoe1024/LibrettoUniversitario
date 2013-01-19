from applicazione import __author__, __version__


import sys
from cx_Freeze import setup, Executable


includes=["shelve", "dbm.dumb"]
data_files=["application.ico"] #["..\Icons"]
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"], "includes" : includes, "include_files":data_files}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = "Win32GUI"
if sys.platform == "win32":
    base = "Win32GUI"


setup(  name = "Libretto Universitario",
        version = __version__,
        author = __author__,
        description = "Libretto Universitario aiuta a tenere traccia del tuo andamento universitario!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("applicazione.py", base=base, icon="application.ico", appendScriptToExe=True, appendScriptToLibrary=False)])