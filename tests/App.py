# flask_web/app.py

# madeby:: ZEKRI SIDI MOhamed Hicham
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