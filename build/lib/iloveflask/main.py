from __future__ import absolute_import 

try:
    from pip._internal.operations import freeze
except ImportError:  # pip < 10.0
    from pip.operations import freeze

from report.API import API

def generate_requirements ():
    x = freeze.freeze()
    f = open("requirements.txt", "a")
    for p in x:
        if ("@" not in p): 
          f.write(p + "\n")
    f.close()

def generate_dockerfile(port, host): 
    f = open("Dockerfile", "a")
    f.write("FROM python:3.8-slim-buster" + "\n")
    f.write("WORKDIR /python-docker" + "\n")
    f.write("COPY requirements.txt requirements.txt" + "\n")
    f.write("RUN pip3 install -r requirements.txt" + "\n")
    f.write("COPY . ." + "\n")
    f.write("CMD [ \"python3\", \"-m\" , \"flask\", \"run\", \"--port="+ str(port) +" \" ,\"--host= '"+ host + "' \"]" + "\n")

    
def generate_report(name): 
    api = API.create(name)
    api.get_report()

