# I Love Flask

iloveflask is a Python library to collect functions that help a flask developer generate reports, config files and repeat code.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Iloveflask.

```bash
pip install iloveflask
```

## Usage

```python
from iloveflask import main

# create requirements.txt
main.generate_requirements()

# create Dockerfile
main.generate_dockerfile(port, host)

# create docx report for API
main.generate_report(pathfile)
```

To use this lib run one or more of the following functions in the root of your flask project:
 
- **generate_requirements() :**
This is a simple function that allows you to create the requirements.txt file based on the libs installed in your development environment.

      main.generate_requirements()
- **generate_dockerfile(port, host) :**
It allows you to create a Docker file to deploy your API. It takes two parameters as input which are the port and the host. 

     **port**: it's an integer that indicates the port of the API.

     **host**: it's a string that indicates the IP of the Host.

      main.generate_dockerfile(5000, "0.0.0.0")

- **genrate_report(pathtofile.py) :**
This function allows you to generate a .docx report for your API based on comments in your API. 

      main.generate_report("path/to/file.py")

   So it is necessary to respect a certain type of comments here is an example of file APP.py which contains the code of the API plus the necessary comments : 
 
   ```python


     # flask_web/app.py

     # madeby:: The creators of the API separate by virgule
     '''
      desc:: This is the description of API:
       * L1 
       * L2
       * L3
      '''
     from flask import Flask
     app = Flask(__name__)

     @app.route('/hello')
     def hello_world():
       '''
        :fn: This is description of function
        :param p1: this is description of p1
        :param p2: this is description of p2
        :return: this is description of return
        '''
        return 'Hey!'

     @app.route('/hello/oldd')
     def hello_world():
       '''
       :fn: This is description of function
       :param p1: this is description of p1
       :return: this is description of return
       '''
        return 'Hey, we have  oldd!'
    if __name == '__main__':
       app.run()

   ```

## TODO 

- Add CRUD generation code
- Add generation of other config files
- Add generation of Auth jwt code
- ... your ideas 
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

Please update the readme also when you add or modify a function.

## License
[MIT](https://choosealicense.com/licenses/mit/)

Made with love by Sidi Mohamed Hicham :heart: :heart: :heart: 