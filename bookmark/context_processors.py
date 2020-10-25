from .bookmark import Bookmark

def bookmark(request):
    return {'bookmark': Bookmark(request)}