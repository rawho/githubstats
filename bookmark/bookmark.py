from django.conf import settings
import requests

class Bookmark(object):

    def __init__(self, request):
        """
        Initialize the bookmark
        """
        self.session = request.session
        bookmark = self.session.get(settings.BOOKMARK_SESSION_ID)
        if not bookmark:
            # save an empty bookmark in the session 
            bookmark = self.session[settings.BOOKMARK_SESSION_ID] = {}
        self.bookmark = bookmark

    
    def add(self, repo, repo_id):
        """
        Add a repo to the bookmark
        """

        
        if repo_id not in self.bookmark:
            self.bookmark[repo_id] = {
                                        'name': repo["full_name"],
                                        'id' : repo_id,  
                                        'url' : repo["html_url"],
                                        'likes' : repo["stargazers_count"],
                                        'description' : repo["description"],
                                        'language': repo["language"],
                                        'forks': repo["forks_count"]
                                    }
        self.save()
    
    def save(self):
        #  Update the bookmark session
        self.session[settings.BOOKMARK_SESSION_ID] = self.bookmark

        # mark the session as modified to make sure it is saved
        self.session.modified = True

    def remove(self, repo, repo_id):
        """
        Remove a repo from bookmark
        """
        if repo_id in self.bookmark:
            del self.bookmark[repo_id]
            self.save()

    def check(self,repos):
        """
        Check whether the repo is in bookmarks
        """
        if repo_id in self.bookmark:
            return True
        else:
            return False

    def __iter__(self):
        repo_ids = self.bookmark.keys()
        repos_list = []
        for repo_id in repo_ids:
            res = requests.get(f"https://api.github.com/repositories/{repo_id}")
            repo_details = res.json()
            repos_list.append(repo_details)

        
        for item in self.bookmark.values():
            yield item

    def __len__(self):
        """
        count all repos in bookmark
        """
        return len(self.bookmark.values())
    
    def clear(self):
        # remove from bookmark
        del self.session[settings.BOOKMARK_SESSION_ID]
        self.session.modified = True
