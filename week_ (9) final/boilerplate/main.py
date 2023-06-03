# Install PyGithub via: $ pip install PyGithub
from github import Github
import csv
import sys

# First create a Github instance:

# using an access token
with open('token.txt', 'r') as f:
	token = f.readline()
g = Github(token)

print("Token get!")

# You can get the access token by going to github.com:
# Click on your avatar -> Settings -> Developer settings -> Personal access tokens 
# -> Tokens (classic) -> Generate new token

# Specify the repository details
# repo_owner = 'gungui98'
# repo_name = 'python-datascience-course'
# repo_owner = 'pytorch'
# repo_name = 'pytorch'
repo_owner = 'freeCodeCamp'
repo_name = 'freeCodeCamp'

# Get the repository object
repo = g.get_repo(f"{repo_owner}/{repo_name}")

# Get all open pull requests
open_prs = repo.get_commits()
print("Get Open!")

# Get all closed pull requests
# closed_prs = repo.get_pulls(state='closed')
# print("Get Close!")

# Print the open pull requests
# print(open_prs[0].commit.committer.email)
# print(open_prs[0].commit.author.name)
# print(open_prs[0].author.login)
# print(open_prs[0].commit.author.date)
# print(open_prs[0].html_url)
# print(open_prs[0].commit.message)
# print(open_prs[0].files[0].filename)
# print(open_prs[0].stats.additions)
# print(open_prs[0].get_combined_status().repository)

# repo = g.get_repo("PyGithub/PyGithub")

listFiles = {}
listFilesPull = {}
# i = 0
# contents = repo.get_contents("")
# while contents:
# 	file_content = contents.pop(0)
# 	if file_content.type == "dir":
# 		contents = repo.get_contents(file_content.path) + contents
# 	else:
# 		listFiles[file_content.path] = i
# 		i += 1

# with open('list_files.csv', 'w', newline='', encoding="utf-8") as file:
# 	writer = csv.writer(file)
# 	field = ["ID", "File Path"]
	
# 	writer.writerow(field)
# 	for info in listFiles.items():
# 		writer.writerow(list(info[::-1]))

# with open('list_files.txt', 'w', encoding="utf-8") as file:
# 	for info in listFiles.items():
# 		file.write(f'{info[1]},{info[0]}\n')

with open('list_files.txt', 'r', encoding="utf-8") as f:
	for info in f:
		l = info.strip().split(',')
		listFiles[l[1]] = l[0]
print(len(listFiles))

with open('list_files_pull_request.txt', 'r', encoding="utf-8") as f2:
	text = f2.readline()
	while text:
		l = text.strip().split('#?#$')
		if (l[1] in listFilesPull.keys()):
			print(l[1])
			raise SystemExit(1)
		listFilesPull[l[1]] = l[0]
		text = f2.readline()
print(len(listFilesPull))

# # for pr in open_prs:
# # 	print(f"#{pr.number}: {pr.title}")
# # 	print(f"Created at: {pr.created_at}") # Print the time when the pull request was open
# # 	print(f"Updated at: {pr.updated_at}") # Print the time when the pull request was last updated
# # 	print(f"Additions: {pr.additions}") # Print the number of additions in the pull requests 
# # 	print(f"Commits: {pr.commits}") # Print the number of commits in the pull request

# # For more reference, check out the PyGithub documentation: https://pygithub.readthedocs.io/en/latest/introduction.html
# # Or simply ask ChatGPT for help =)))


# # field = ["ID", "Message", "Author name", "Author email", "Date of Commit", "List of ID of Changed file"]

# # writer.writerow(field)

with open('a.txt', 'r') as f:
	hib = list(f)
	h = int(hib[0].strip())
	i = int(hib[1].strip())
	bug = int(hib[2].strip())
k = h
j = 1000*i
listKey = listFiles.keys()
while True:
	with open(f'data{i}.csv', 'w', newline='', encoding="utf-8") as file:
		writer = csv.writer(file)
		for cmt in open_prs[h:]:
			t = []
			k += 1
			for x in cmt.files:
				if x.filename in listKey:
					t.append(str(listFiles[x.filename]))
				else:
					if x.filename not in listFilesPull.keys():
						new = len(listFilesPull)
						print(bug, new)
						if bug != new:
							raise SystemExit(1)

						with open(f'list_files_pull_request.csv', 'a', newline='', encoding="utf-8") as file2:
							writer2 = csv.writer(file2)
							writer2.writerow([f'{new}P', x.filename])

						with open('list_files_pull_request.txt', 'a', encoding="utf-8") as file:
							file.write(f'{new}P#?#${x.filename}\n')

						l = bug
						listFilesPull[x.filename] = f'{l}P'

						bug += 1

					t.append(listFilesPull[x.filename])

			info = [j, cmt.commit.message, cmt.commit.author.name, cmt.commit.committer.email, cmt.commit.author.date, ' '.join(t)]
			writer.writerow(info)
			j += 1
			if j % 1000 == 0:
				break

	i += 1
	h = k
	with open('a.txt', 'w') as f:
		f.write(str(h))
		f.write('\n')
		f.write(str(i))
		f.write('\n')
		f.write(str(bug))
# # import csv
# # with open(f'a.csv', 'a', newline='') as file:
# # 	writer = csv.writer(file)
# # 	field = ["ID", "Message", "Author name", "Author email", "D", "List of ID of Changed file"]
	
# # 	j = 0
# # 	writer.writerow(field)