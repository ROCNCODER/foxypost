from scrapers_modules.fb_core import FacebookAggregator
from scrapers_modules.inst_core import InstagramAggregator
class PostStatAggregator():
    def __init__(self, collection_links:list , parameter:str):
        self._collection_links = collection_links
        self._parameter = parameter

    def get_data(self):
        if self._parameter == "facebook":
            data = FacebookAggregator(collection_links=self._collection_links).get_data()
        elif self._parameter == "instagram":
            data = InstagramAggregator(collection_links=self._collection_links).get_data()
        return data


if __name__ == "__main__":
    coll = ["https://www.facebook.com/photo/?fbid=602932055321115&set=a.106491591631833", "https://www.facebook.com/photo/?fbid=754509810013139&set=a.515626203901502"]
    parameter = "facebook"
    print(PostStatAggregator(collection_links=coll,parameter=parameter).get_data())

    coll = ["https://www.instagram.com/reels/CvFRM5ArfXn/","https://www.instagram.com/p/Cumux1xqv1L","https://www.instagram.com/p/CvLOk51t-jF/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=="]
    parameter = "instagram"
    print(PostStatAggregator(collection_links=coll, parameter=parameter).get_data())