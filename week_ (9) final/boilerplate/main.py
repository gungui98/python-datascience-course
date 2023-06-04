# Install PyGithub via: $ pip install PyGithub
from github import Github

# First create a Github instance:

# using an access token
g = Github("your access token here")

# You can get the access token by going to github.com:
# Click on your avatar -> Settings -> Developer settings -> Personal access tokens 
# -> Tokens (classic) -> Generate new token

# Specify the repository details
repo_owner = 'gungui98'
repo_name = 'python-datascience-course'

# Get the repository object
repo = g.get_repo(f"{repo_owner}/{repo_name}")

# Get all open pull requests
open_prs = repo.get_pulls(state='open')

# Get all closed pull requests
closed_prs = repo.get_pulls(state='closed')

# Print the open pull requests
print("Open Pull Requests:")
for pr in open_prs:
    print(f"#{pr.number}: {pr.title}")
    print(f"Created at: {pr.created_at}") # Print the time when the pull request was open
    print(f"Updated at: {pr.updated_at}") # Print the time when the pull request was last updated
    print(f"Additions: {pr.additions}") # Print the number of additions in the pull requests 
    print(f"Commits: {pr.commits}") # Print the number of commits in the pull request

# For more reference, check out the PyGithub documentation: https://pygithub.readthedocs.io/en/latest/introduction.html
# Or simply ask ChatGPT for help =)))