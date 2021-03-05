from flask import Flask
app = Flask(__name__)

@app.route('/')
def default():
    return 'To check catalogue file format, enter "/evaluate/" followed by url'

@app.route('/evaluate/<name>')
def evaluate(name):
    #end_of_url = name[-3:-1]
    #return 'end of url: ' + end_of_url
    return 'url: ' + name

if __name__ == '__main__':
    app.run()
