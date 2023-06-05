from github import Github, RateLimitExceededException, BadCredentialsException, BadAttributeException, \
    GithubException, UnknownObjectException, BadUserAgentException
import pandas as pd
import requests
import time

def extract_project_PRs(repo, g):
    df_pr = pd.DataFrame()
    while True:
        try:
            pull_requests = repo.get_pulls(state='open', sort='created', base='master')

            for pr in pull_requests:
                try:
                    print(g.rate_limiting)
                    print(f'Extracting data from PR # {pr.number}')
                    # Review Comments on the Pull requests
                    review_comments = []
                    if pr.get_comments().totalCount>0:
                        for comment in pr.get_comments():
                            cmt = {
                                'comment_id': comment.id,
                                'comment_body': comment.body,
                                'comment_created': comment.created_at,
                                'commenter': comment.user.login,
                                'type': comment.user.type
                            }
                            review_comments.append(cmt)

                    new_rows = pd.DataFrame([{
                        'pr_id': pr.id, # PRs features
                        'pr_title': pr.title,
                        'pr_body': pr.body,
                        'pr_number': pr.number,
                        'pr_url': pr.url,
                        'pr_html_url': pr.html_url,
                        'pr_state': pr.state,
                        'additions': pr.additions,
                        'deletions': pr.deletions,
                        'pr_changed_files': pr.changed_files,
                        'pr_commits_count': pr.commits,
                        'pr_comments_count': pr.comments,
                        'pr_review_comments_count': pr.review_comments,
                        'pr_labels_count': len([l.name for l in pr.labels]),
                        'pr_assignees_count': len(pr.assignees),
                        'pr_labels': [l.name for l in pr.labels],
                        'pr_created_at': pr.created_at,
                        'pr_closed_at': pr.closed_at,
                        'pr_review_comments': review_comments,
                        'contributor': pr.user.login,  # Contributor's information
                        'contributor_id': pr.user.id,
                        'contributor_email': pr.user.email,
                        'contributor_type': pr.user.type,
                        'contributor_public_repos': pr.user.public_repos,
                        'contributor_private_repos': pr.user.owned_private_repos,
                        'contributor_followings': pr.user.following,
                        'contributor_followers': pr.user.followers,
                    }])
                    print("here: ", new_rows.shape)
                    df_pr = pd.concat([df_pr, new_rows], ignore_index=True)

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
    df_pr.to_csv('boilerplate/data/pr_data.csv', sep=',', encoding='utf-8', index=True)


