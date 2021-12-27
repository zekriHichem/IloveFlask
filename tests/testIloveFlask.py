import sys
sys.path.append('./..')

from iloveflask.main import *

generate_requariements()
genrate_dockerfile(5000,"0.0.0.0")
genrate_raport("App.py")