from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/issues', methods=['POST'])
def issues():
    raise NotImplementedError

@app.route('/results')
def results():
    raise NotImplementedError

if __name__ == '__main__':
    app.run(debug=True)
