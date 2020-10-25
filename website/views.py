from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse

# Create your views here.
import requests




def user_details(request, username):
    res = requests.get(f"https://api.github.com/users/{username}")
    profile_data = res.json()

    repos_res = requests.get(f"https://api.github.com/users/{username}/repos")
    repos = repos_res.json()
    # print(repos[0]["stargazers_count"])
    print(len(repos))

    repos_list = []

    
    if res.status_code == 200:
        for repo in repos:
            if repo["fork"] == False:
                repos_list.append(repo)
        repos_list_short = sorted(repos_list, key=lambda  i: i['stargazers_count'], reverse=True)[:4]


        dp_url = profile_data["avatar_url"]
        name = profile_data["name"]
        username = profile_data['login']
        bio = profile_data["bio"]
        github_link = profile_data["html_url"]
        if profile_data["blog"].startswith("http"):
            website_url = profile_data["blog"]
        elif(profile_data["blog"] == None):
            website_url = "Coming Soon"
        else:
            website_url = f"http://{profile_data['blog']}"

        if profile_data["location"] == None:
            location = "Earth"
        else:
            location = profile_data["location"]

        followers_count = profile_data["followers"]
        following_count = profile_data["following"]
        public_repos_count = len(repos_list)
        public_gists_count = profile_data["public_gists"]

        return render(request, 'website/user_details.html', {
        'dp_url': dp_url,
        'name': name,
        'username': username,
        'bio': bio,
        "github_link": github_link,
        "website_url" : website_url,
        "location": location,
        "followers_count": followers_count,
        "following_count": following_count,
        "public_repos_count": public_repos_count,
        "public_gists_count" : public_gists_count,
        "repos_list_short" : repos_list_short,
        "repos_list": repos_list,
        

    })
    elif res.status_code == 403:
        return render(request, 'website/limit-exceeded.html', {
            
        })

    elif res.status_code == 404:
        return render(request, 'website/404.html', {

        })

    return render(request, 'website/404.html')
    

def search(request):
    username = request.GET.get("username")
    return HttpResponseRedirect(reverse('user_details', args=(username,)))


def index(request):
    return render(request, 'website/index.html', {
        
    })