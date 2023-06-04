# Install PyGithub via: $ pip install PyGithub
from github import Github
import csv
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
# print("Open Pull Requests:")
# for pr in open_prs:
#     print(f"#{pr.number}: {pr.title}")
#     print(f"Created at: {pr.created_at}") # Print the time when the pull request was open
#     print(f"Updated at: {pr.updated_at}") # Print the time when the pull request was last updated
#     print(f"Additions: {pr.additions}") # Print the number of additions in the pull requests 
#     print(f"Commits: {pr.commits}") # Print the number of commits in the pull request
with open("GitHub/week_ (9) final/boilerplate/example.csv","w",newline="",encoding="utf-8-sig") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Number", "Title", "Create_at", "Update_at", "Additions", "Commits", "Number of Files Changed", "Commit ID", "Commit Message", "Author Name", "Author Email", "Commit Date", "Files Changed"])
    for pr in open_prs:
        commits = pr.get_commits()
        commit_id = [commit.sha for commit in commits]
        commit_msg = [commit.commit.message for commit in commits]
        author_name = [commit.commit.author.name for commit in commits]
        author_email = [commit.commit.author.email for commit in commits]
        commit_date = [commit.commit.author.date.strftime("%U-%Y") for commit in commits]
        files_changed = [[file.filename for file in commit.files] for commit in commits]
        number_of_files_changed = sum([len(i) for i in files_changed])
        writer.writerow([pr.number, pr.title, pr.created_at, pr.updated_at, pr.additions, pr.commits, number_of_files_changed, commit_id, commit_msg, author_name, author_email, commit_date, files_changed])
# For more reference, check out the PyGithub documentation: https://pygithub.readthedocs.io/en/latest/introduction.html
# Or simply ask ChatGPT for help =)))