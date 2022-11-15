from instagrapi import Client
import config
import time
import random

cl = Client()
cl.login(config.username, config.password)


class LikePost:
    def __init__(self, client):
        self.cl = client
        self.tags = ['hashtag', 'hashtag']
        self.liked_medias = []

    def get_post_id(self):
        medias = cl.hashtag_medias_recent(random.choice(self.tags), amount=1)
        media_dict = medias[0].dict()
        return str(media_dict['id'])

    def get_current_time (self):
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
        return current_time

    def like_post(self):
        while True:
            current_time = self.get_current_time()
            time.list = ['20:56:78', '22:00:02', '22:06:32', '22:11:43', '22:14:13']
            if current_time in time.list:
                random_post = self.get_post_id()
                if random_post in self.liked_medias:
                    pass
                else:
                    self.cl.media_like(media_id=random_post)
                    self.liked_medias.append(random_post)
                    print(f"liked {len(self.liked_medias)} post")
                    continue
            else:
                time.sleep(1)


start = LikePost(cl)
start.like_post()
