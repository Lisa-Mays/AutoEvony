from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize([
        "autoJointRally.py",
        "guilde.py",
        "menuJoinRalies.py",
        "menuMarket.py",
        "menuRelic.py",
        "menustart.py",
        "resfreshPort.py",
        "savefile.py",
        "screeenshot.py"
        
    ], output_dir='filec/')
)
