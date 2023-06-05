from github import Github
import csv
import datetime
import time

# Create a Github instance
g = Github("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")

# Specify the repository details
repo_owner = 'AtsushiSakai'
repo_name = 'PythonRobotics'

# Get the repository object
repo = g.get_repo(f"{repo_owner}/{repo_name}")

# Specify the file path
csv_file = 'commits.csv'

# Open the file in write mode
with open(csv_file, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Commit ID', 'Commit Message', 'Author Name', 'Author Email', 'Created at', 'Updated at', 'Files Changed', 'Branch', 'Contributor', 'All Checks Passed'])

    since_date = datetime.datetime(2010, 1, 1)  # Start date
    until_date = datetime.datetime(2024, 1, 1)  # End date
    # Get all commits
    commits = repo.get_commits(since=since_date, until=until_date)

    # Write the data rows for commits
    for commit in commits:
        commit_id = commit.sha
        commit_message = commit.commit.message
        author_name = commit.commit.author.name
        author_email = commit.commit.author.email
        commit_date = commit.commit.author.date.strftime("%Y-%m-%d %H:%M:%S")

        files_changed = commit.files
        changed_files = [file.filename for file in files_changed]

        # Get the branch information
        branches = commit.commit.parents
        branch = branches[0].url.split('/')[-1] if branches else 'N/A'

        # Get the contributor information
        contributor = commit.author.login if commit.author else 'N/A'

        # Get the status of checks for the commit
        check_runs = commit.get_check_runs()
        all_checks_passed = all(check_run.conclusion == 'success' for check_run in check_runs)

        writer.writerow([commit_id, commit_message, author_name, author_email, commit_date, commit_date, changed_files, branch, contributor, all_checks_passed])

        # Introduce a delay of 1 second between each iteration
        time.sleep(1)

print("Commit details saved to the CSV file.")