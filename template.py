import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]:%(message)s')

packagename= "deepclassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{packagename}/__init__.py",
    f"src/{packagename}/components/__init__.py",
    f"src/{packagename}/utils/__init__.py",
    f"src/{packagename}/config/__init__.py",
    f"src/{packagename}/pipeline/__init__.py",
    f"src/{packagename}/entity/__init__.py",
    f"src/{packagename}/constant/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipyb"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath , "w") as f:
            pass #create an empty file
            logging.info(f"Creating file directory {filedir}")

    else:
        logging.info(f"{filepath} already exists")