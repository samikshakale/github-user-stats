#Samiksha Kale 6/1/2023
import github
from github import Github
import sys
import json

def get_stats(username, nonforked):
    # Create github object
    g = Github("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")
    try:
        user = g.get_user(username)
    except github.GithubException:
        return 0


    #Initialize counts
    total_count = 0
    total_stargazer_count = 0
    total_fork_count = 0
    rep_total_size = 0

    languages_dict = dict()

    #Aggregate stats for each repo
    for repo in user.get_repos():
        if nonforked == True and repo.fork==True:
            continue
        total_count+=1
        total_stargazer_count+=repo.stargazers_count
        total_fork_count+=repo.forks_count
        rep_total_size+=repo.size
        language = repo.language
        if language in languages_dict:
            languages_dict[language] +=1
        else:
            languages_dict[language] = 1

    if total_count > 0:
        avg_rep_size = rep_total_size/total_count
    else:
        avg_rep_size = 0

    languages_dict = dict(sorted(languages_dict.items(), key = lambda x: x[1], reverse = True))

    #Create dictionary for output
    output = {'total repository count':total_count, 'total stargazers':total_stargazer_count, 'total fork count': total_fork_count,
          'average repository size (MB)': avg_rep_size, 'languages': languages_dict}
    
    return output