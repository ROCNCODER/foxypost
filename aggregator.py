from scrapers_modules.fb_core import FacebookAggregator
from scrapers_modules.inst_core import InstagramAggregator

options = {"instagram": {"usеrname": 'shapranov.work@gmail.com', "password": "15426378ShapDi"}}

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
    # coll = ["https://www.facebook.com/photo/?fbid=602932055321115&set=a.106491591631833", "https://www.facebook.com/photo/?fbid=754509810013139&set=a.515626203901502"]
    # parameter = "facebook"
    # print(PostStatAggregator(collection_links=coll,parameter=parameter).get_data())

    coll = "https://www.instagram.com/rocknrolla2025/saved/indac/18047862079466252/"

    PostStatAggregator(social_network="instagram",collection_link=coll, options=options).get_data()
