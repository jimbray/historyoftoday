from flask import Flask

from GetHistory import gethistory
from GetHistory import DatabaseManager
import json

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/')
def index():
    json_str = gethistory.start()
    return 'This is the index page.And the history is Ready'

@app.route('/user/<user_name>')
def show_name(user_name):
    return 'your name is %s ' %  user_name

@app.route('/json/<file_name>')
def readFile(file_name):
    json_line = []

    try:
        file =  open(file_name, 'r')
        while 1:
            lines = file.readlines(100000)
            if not lines:
                break
            for line in lines:
                json_line.append(line)

        file.close()
    except IOError:
        return 'Failed to read file.'

    return ''.join(json_line)

@app.route("/today")
def getToday():
    history_list = DatabaseManager.getAllHistory()
    return json.dumps(history_list,ensure_ascii=False)

if __name__ == '__main__':
    app.debug = True
    app.run()
