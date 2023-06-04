from github import Github
import csv

g = Github("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")

repo_owner = 'kunjgit'
repo_name = 'GameZone'

repo = g.get_repo(f"{repo_owner}/{repo_name}")

pulls = repo.get_pulls(state='all')

commits = []
for pull in pulls:
    for commit in pull.get_commits():
        commits.append(commit)
        
commit_data = []
for commit in commits:
    commit_id=commit.sha
    author_name=commit.commit.author.name
    author_email=commit.commit.author.email
    message=commit.commit.message
    date_of_commit=commit.commit.author.date
    num_files_changed=len(commit.files)
    files_changed=[]
    for file in commit.files:
        files_changed.append([file.filename])
    commit_data.append([commit_id,
                        author_name,
                        author_email,
                        message,
                        date_of_commit,num_files_changed,
                       files_changed])
df = pd.DataFrame(commit_data, columns=['commit_id',
                                        'author_name',
                                        'author_email',
                                        'message',
                                        'date_of_commit',
                                        'num_files_changed','files_changed'
                                        ])
df=df.set_index('commit_id')
df.to_csv('commit_data.csv')