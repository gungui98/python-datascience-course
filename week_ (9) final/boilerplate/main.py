# Install PyGithub via: $ pip install PyGithub
from github import Github
import csv

# First create a Github instance:

# using an access token
g = Github("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")

# You can get the access token by going to github.com:
# Click on your avatar -> Settings -> Developer settings -> Personal access tokens 
# -> Tokens (classic) -> Generate new token

# Specify the repository details
repo_owner = 'gungui98'
repo_name = 'python-datascience-course'

# Get the repository object
repo = g.get_repo(f"{repo_owner}/{repo_name}")

# Specify the file path
csv_file = 'test.csv'

# # Open the file in write mode
with open(csv_file, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)

#     # Write the header row
    writer.writerow(['Pull Request', 'Name', 'Created at', 'Updated at', 'Additions', 'Commits', 'Status', 'File Changed'])

   # Get all pull requests
    open_prs = repo.get_pulls(state='open')

    for pr in open_prs:
        commits = repo.get_pull(pr.number).get_commits()
        status = "unknown"  # Trạng thái mặc định
        if pr.commits == 0 | pr.additions == 0: 
            writer.writerow([pr.number, pr.title, ' ', pr.created_at, pr.updated_at, pr.additions, pr.commits, status])
        else:
            for commit in commits:
                author = commit.author
                commit_message = commit.commit.message
                committed_at = commit.commit.committer.date
                
                # Lấy trạng thái từ trạng thái "checks" của commit
                check_runs = repo.get_commit(commit.sha).get_check_runs()
                status = "unknown" # Trạng thái mặc định
                
                for check_run in check_runs:
                    if check_run.head_sha == commit.sha:
                        status = check_run.conclusion
                        break
                
                changed_files = commit.files
                changed_file_names = [file.filename for file in changed_files]
                writer.writerow([pr.number, author, commit_message, pr.created_at, committed_at, pr.additions, pr.commits, status, changed_file_names])


    close_prs = repo.get_pulls(state='close')

    for pr in close_prs:
        commits = repo.get_pull(pr.number).get_commits()
        status = "unknown"  # Trạng thái mặc định
        if pr.commits == 0 | pr.additions == 0: 
            writer.writerow([pr.number, pr.title, commit_message, pr.created_at, pr.updated_at, pr.additions, pr.commits, status])
        else:
            for commit in commits:
                author = commit.author
                commit_message = commit.commit.message
                committed_at = commit.commit.committer.date
                
                # Lấy trạng thái từ trạng thái "checks" của commit
                check_runs = repo.get_commit(commit.sha).get_check_runs()
                status = "unknown" # Trạng thái mặc định
                
                for check_run in check_runs:
                    if check_run.head_sha == commit.sha:
                        status = check_run.conclusion
                        break
                
                changed_files = commit.files
                changed_file_names = [file.filename for file in changed_files]
                writer.writerow([pr.number, author, commit_message, pr.created_at, committed_at, pr.additions, pr.commits, status, changed_file_names])

print("Pull requests saved to the CSV file.")

# # Print the open pull requests
# print("Open Pull Requests:")


# # For more reference, check out the PyGithub documentation: https://pygithub.readthedocs.io/en/latest/introduction.html
# # Or simply ask ChatGPT for help =)))