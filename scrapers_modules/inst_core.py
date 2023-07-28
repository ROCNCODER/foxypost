
from instagrapi import Client

class InstagramAggregator():
    USERNAME = "Kamillycastro41t"
    PASSWORD = "xx0022"
    def __init__(self, collection_links:list):
        self._collection_links = collection_links
    def get_data(self):
        cl = Client()
        cl.login(self.USERNAME, self.PASSWORD)
        col = {}
        for link in self._collection_links:
            print(link)
            data = cl.media_pk_from_url(link)
            data = cl.media_info(data).dict()
            print(data)
            col[link] = f"likes:{data['like_count']} comments:{data['comment_count']} play_count:{data['play_count']}"
        return col
