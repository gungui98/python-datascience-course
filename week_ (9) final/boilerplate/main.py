# Install PyGithub via: $ pip install PyGithub
from github import Github
import pandas as pd
import pull_requests 
import commits
# First create a Github instance:

# using an access token
token = "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"
g = Github(token)

# You can get the access token by going to github.com:
# Click on your avatar -> Settings -> Developer settings -> Personal access tokens 
# -> Tokens (classic) -> Generate new token

# Specify the repository details
repo_owner = 'gungui98'
repo_name = 'python-datascience-course'
# Get the repository object
repo = g.get_repo(f"{repo_owner}/{repo_name}")

#DEBUG
CREATE_pr = False
CREATE_cm = True
#Pull request
if CREATE_pr:
    pull_requests.extract_project_PRs(repo, g)

if CREATE_cm:
    # Print the open pull requests
    print("Open Pull Requests:")

    df_pr = pd.read_csv('C:/Users/Admin/Desktop/project/python-datascience-course/week_ (9) final/boilerplate/data/pr_data.csv')
    cnt = 0
    for i in df_pr['contributor']:
        cnt += 1
        commits.extract_project_commits(i, token, cnt)

# For more reference, check out the PyGithub documentation: https://pygithub.readthedocs.io/en/latest/introduction.html
# Or simply ask ChatGPT for help =)))