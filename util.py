def user_logged_in():
    return False

def get_repos(user, repo):
    github.get('repos/%s/' % user)

def get_issues(user, repo):
    github.get('repos/%s/%s/issues' % (user, repo))

def read_config():
    return {}
