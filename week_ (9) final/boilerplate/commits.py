from github import Github, RateLimitExceededException, BadCredentialsException, BadAttributeException, \
    GithubException, UnknownObjectException, BadUserAgentException
import pandas as pd
import requests
import time
from datetime import datetime

def extract_project_commits(repo_owner, access_token, cnt):
    g = Github(access_token)
    repo_name = 'python-datascience-course'
    repo = g.get_repo(f"{repo_owner}/{repo_name}")

    df_commits = pd.DataFrame()
    while True:
        try:
            #start_time = datetime.strptime("2010-01-01 00:00:00", '%Y-%m-%d %H:%M:%S')
            #end_time = datetime.strptime("2012-3-31 00:00:00", '%Y-%m-%d %H:%M:%S')
            all_commits = repo.get_commits()
            counter = 0
            print(all_commits.totalCount)
            for commit in all_commits:
                while True:
                    try:
                        counter += 1
                        print(f"Loop counter {counter}")
                        print(g.rate_limiting)
                        
                        files_changed = []
                        files = commit.files
                    
                        for file in files:
                            if file.changes > 0:
                                files_changed.append(file.filename)
                        #print(*files_changed)

                        new_rows = pd.DataFrame([{
                            'commit_sha': commit.sha,
                            'committer_username': commit.author.login if commit.author is not None else '',
                            'committer_name': commit.author.name if commit.author is not None else '',
                            'committer_email': commit.author.email if commit.author is not None else '',
                            'commit_date': commit.commit.author.date if commit.author is not None else '',
                            'commit_message' : commit.commit.message if commit.author is not None else '',
                            'commit_files_changed' : files_changed if commit.author is not None else ' '
                        }])
                        df_commits = pd.concat([df_commits, new_rows], ignore_index=True)

                    except RateLimitExceededException as e:
                        print(e.status)
                        print('Rate limit exceeded')
                        time.sleep(300)
                        continue
                    except BadCredentialsException as e:
                        print(e.status)
                        print('Bad credentials exception')
                        break
                    except UnknownObjectException as e:
                        print(e.status)
                        print('Unknown object exception')
                        break
                    except GithubException as e:
                        print(e.status)
                        print('General exception')
                        break
                    except requests.exceptions.ConnectionError as e:
                        print('Retries limit exceeded')
                        print(str(e))
                        time.sleep(10)
                        continue
                    except requests.exceptions.Timeout as e:
                        print(str(e))
                        print('Time out exception')
                        time.sleep(10)
                        continue
                    break
        except RateLimitExceededException as e:
            print(e.status)
            print('Rate limit exceeded')
            time.sleep(300)
            continue
        except BadCredentialsException as e:
            print(e.status)
            print('Bad credentials exception')
            break
        except UnknownObjectException as e:
            print(e.status)
            print('Unknown object exception')
            break
        except GithubException as e:
            print(e.status)
            print('General exception')
            break
        except requests.exceptions.ConnectionError as e:
            print('Retries limit exceeded')
            print(str(e))
            time.sleep(10)
            continue
        except requests.exceptions.Timeout as e:
            print(str(e))
            print('Time out exception')
            time.sleep(10)
            continue
        break
    if cnt == 1:
        df_commits.to_csv('boilerplate/data/commits_data.csv', sep=',', mode='a+', encoding='utf-8', index=True)
    else:
        df_commits.to_csv('boilerplate/data/commits_data.csv', sep=',', mode='a+', encoding='utf-8', index=True, header = False)