from github import Github

g = Github("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")

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

    commits = pr.get_commits()
    for commit in commits:
        print(commit.sha, commit.commit.message, commit.commit.author.name, commit.commit.author.email, commit.commit.author.date)

commits = repo.get_commits()
for commit in commits:
    print(commit.sha, commit.commit.message, commit.commit.author.name, commit.commit.author.email, commit.commit.author.date)