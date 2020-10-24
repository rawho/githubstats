import requests


res = requests.get("https://api.github.com/users/rawhofdsafasdfasdfasdfasdf")
profile_data = res.json()
print(res.status_code)

repos_res = requests.get("https://api.github.com/users/rawho/repos")
repos = repos_res.json()
# print(repos[0]["stargazers_count"])

repos_list = []



if res.status_code == 200:
    for repo in repos:
        if repo["fork"] == False:
            repos_list.append(repo)
elif res.status_code == 403:
    print("limit exceeded")
repos_list_short = sorted(repos_list, key=lambda  i: i['stargazers_count'], reverse=True)[:4]
