from flask import Flask

app = Flask(__name__)
html_template = """
<body>
    <p>the todo list is </p>
    <ul>
        <li>{0}</li>
        <li>{1}</li>
</body>
"""


@app.route('/')
def todolist():
    return html_template.format('asdf', 'bdfg')
