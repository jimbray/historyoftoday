from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/')
def index():
    return 'This is the index page.'

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

if __name__ == '__main__':
    app.debug = True
    app.run()
