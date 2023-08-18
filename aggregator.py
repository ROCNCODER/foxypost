from scrapers_modules.fb_core import FacebookAggregator
from scrapers_modules.inst_core import InstagramAggregator
from scrapers_modules.youtube_core import YouTubeAggregator

options = {"instagram": {"usеrname": '', "password": ""},"youtube":{"data"}}

class PostStatAggregator():
    def __init__(self, social_network, collection_link: str | list, options: dict):
        self._collection_link = collection_link
        self._social_network = social_network
        self._options = options

    def get_data(self):
        global data
        if self._social_network == "facebook":
            data = FacebookAggregator(collection_links=self._collection_link).get_data()
        elif self._social_network == "instagram":
            data = InstagramAggregator(username=self._options["instagram"].get('usеrname'),password=self._options["instagram"].get('password'),link_coll=self._collection_link).get_data()
        return data


if __name__ == "__main__":
    coll = "https://www.instagram.com/rocknrolla2025/saved/indac/18047862079466252/"

    # p = PostStatAggregator(social_network="instagram",collection_link=coll, options=options).get_data()
    d = PostStatAggregator(social_network="instagram", collection_link=coll, options=options).get_data()
    YouTubeAggregator(links=["https://www.youtube.com/shorts/AMrMAylEwFg" for i in range(1,200)]).get_data()
