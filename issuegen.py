import requests
#POST https://api.github.com/repos/:owner/:repo/issues

def github_post(ep, params):
    raise NotImplementedError

def main():
    endpoint = 'repos/%s/%s/issues' % ('packlnd','todo-2-issue')
    github_post(endpoint, {
        'title':'[VINCENT] Issue',
        'body':'This is the body of my issue',
        'assignee':'packlnd'
    })
