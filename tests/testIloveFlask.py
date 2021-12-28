import sys

from iloveflask.main import *

generate_requirements()
generate_dockerfile(5000,"0.0.0.0")
generate_report("App.py")