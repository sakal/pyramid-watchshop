from os import listdir
from os.path import (
    isdir,
    realpath,
)

modules_path = realpath(__file__)

for module_name in listdir(modules_path):
    if isdir(module_name):
        pass


