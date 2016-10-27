import requests
import datetime


def get_trending_repositories(top_size):
    today = datetime.date.today()
    one_week = datetime.timedelta(days=7)
    week_ago = str(today - one_week)
    git_request = requests.get('https://api.github.com/search/repositories?q=created:>={}&sort=string'.format(week_ago))
    repos_list = git_request.json()['items'][:top_size]
    return repos_list, week_ago


def get_open_issues_amount(repo_owner, repo_name):
    git_request = requests.get('https://api.github.com/repos/{}/{}/issues'.format(repo_owner,repo_name))
    repo_issues_list = git_request.json()
    return [repo_issue['url'] for repo_issue in repo_issues_list if 'pull_request' not in repo_issue]


if __name__ == '__main__':
    top_size = 20
    repos_list, week_ago = get_trending_repositories(top_size)
    print('Most popular github repositories created since {} and after\n'.format(week_ago))
    for repo_obj in repos_list:
        repo_owner, repo_name, stars_amount = repo_obj['owner']['login'], repo_obj['name'], repo_obj['stargazers_count']
        issues_list = get_open_issues_amount(repo_owner, repo_name)
        print('Repo name: {}, stars: {}\nIssues:'.format(repo_name, stars_amount))
        if not issues_list:
            print('No issues')
        for issue in issues_list:
            print(issue)
