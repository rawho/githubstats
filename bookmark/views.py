from django.shortcuts import render, redirect
from .bookmark import Bookmark
import requests

# Create your views here.

def bookmark_add(request, repo_id):
    bookmark = Bookmark(request)
    repo = requests.get(f"https://api.github.com/repositories/{repo_id}")
    bookmark.add(repo=repo.json(), repo_id=repo_id)
    return redirect('bookmark_detail')
    

def bookmark_remove(request, repo_id):
    bookmark = Bookmark(request)
    repo = requests.get(f"https://api.github.com/repositories/{repo_id}")
    bookmark.remove(repo=repo.json(), repo_id=repo_id)
    return redirect("bookmark_detail")

def bookmark_detail(request):
    bookmark = Bookmark(request)
    return render(request, 'bookmark/bookmarks.html', {
        "bookmarks": bookmark
    })

