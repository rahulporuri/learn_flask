from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def todolist(items=[]):
    return render_template('todolist.html', items=['asdf', 'bdfg'])
