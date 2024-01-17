from flask import Flask, render_template, request
from static.temp import initaite_query

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

    position = request.form.get('position')
    query = request.form.get('query')

    print(position, query)
    resp = initaite_query(position, query)

    return render_template('index2.html', messages =resp, pos = position)

