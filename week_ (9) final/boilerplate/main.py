from github import Github
from dotenv import load_dotenv
import csv
import os

load_dotenv()
#get access token from environment variable
access_token = os.getenv('ACCESS_TOKEN')

g = Github(access_token)

repo_owner = 'pytorch'
repo_name = 'audio'

repo = g.get_repo(f"{repo_owner}/{repo_name}")

with open('pytorch_audio_raw_data.csv', 'w', newline='', encoding='utf-8-sig') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Commit ID', 'Commit Message', 'Author Name', 'Author Email', 'Date of Commit', 'Changed Files', 'Pass all checks'])

    commits = repo.get_commits()
    for commit in commits:
        commit_id = commit.sha
        commit_data = commit.commit
        commit_message = commit_data.message
        author_name = commit_data.author.name
        author_email = commit_data.author.email
        date_of_commit = commit_data.author.date.strftime("%Y-%m-%d %H:%M:%S")

        files = commit.files
        changed_file = [file.filename for file in files]

        check_passed = commit.get_check_runs()
        passed = all(check.conclusion == 'success' for check in check_passed)
        
        csv_writer.writerow([commit_id, commit_message, author_name, author_email, date_of_commit, changed_file, passed])


# # Install PyGithub via: $ pip install PyGithub
# from github import Github

# # First create a Github instance:

# # using an access token
# g = Github("your access token here")

# # You can get the access token by going to github.com:
# # Click on your avatar -> Settings -> Developer settings -> Personal access tokens 
# # -> Tokens (classic) -> Generate new token

# # Specify the repository details
# repo_owner = 'gungui98'
# repo_name = 'python-datascience-course'

# # Get the repository object
# repo = g.get_repo(f"{repo_owner}/{repo_name}")

# # Get all open pull requests
# open_prs = repo.get_pulls(state='open')

# # Get all closed pull requests
# closed_prs = repo.get_pulls(state='closed')

# # Print the open pull requests
# print("Open Pull Requests:")
# for pr in open_prs:
#     print(f"#{pr.number}: {pr.title}")
#     print(f"Created at: {pr.created_at}") # Print the time when the pull request was open
#     print(f"Updated at: {pr.updated_at}") # Print the time when the pull request was last updated
#     print(f"Additions: {pr.additions}") # Print the number of additions in the pull requests 
#     print(f"Commits: {pr.commits}") # Print the number of commits in the pull request

# # For more reference, check out the PyGithub documentation: https://pygithub.readthedocs.io/en/latest/introduction.html
# # Or simply ask ChatGPT for help =)))