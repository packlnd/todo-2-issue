from flask import Flask, render_template, redirect
from util import get_repos, read_config
from flask.ext.github import GitHub


app = Flask(__name__)
config = read_config()
app.config['GITHUB_CLIENT_ID'] = config['id']
app.config['GITHUB_CLIENT_SECRET'] = config['secret']

github = GitHub(app)
global token
token = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/issues', methods=['POST'])
def issues():
    raise NotImplementedError

@app.route('/repositories')
def results():
    repos = get_repos()
    return render_template('repositories.html',data=repos)

@app.route('/github')
def github():
    return github.authorize()

@app.route('/callback')
def callback(api_token):
    global token
    token = api_token
    return redirect('/repositories')

if __name__ == '__main__':
    app.run(debug=True)
