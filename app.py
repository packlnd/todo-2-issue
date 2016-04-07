from flask import Flask, render_template, redirect
from util import user_logged_in, get_repos
from flask.ext.github import GitHub


app = Flask(__name__)
app.config['GITHUB_CLIENT_ID'] = 'XXX'
app.config['GITHUB_CLIENT_SECRET'] = 'YYY'

github = GitHub(app)
global token
token = None

@app.route('/')
def index():
    if user_logged_in():
        return redirect('/repositories')
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
