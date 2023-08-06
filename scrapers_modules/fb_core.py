from facebook_scraper import get_posts

class FacebookAggregator():
    def __init__(self, collection_links:list):
        self._collection_links = collection_links

    def get_data(self):
        col = {}
        print(self._collection_links)
        for link in self._collection_links:
            post = next(get_posts(post_urls=[link],timeout=400))
            print(post)
            text = f"likes:{post['likes']} comments:{post['comments']} shares:{post['shares']}"
            col[link] = text
        return col

