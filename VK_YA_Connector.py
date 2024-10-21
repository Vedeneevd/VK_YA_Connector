import os.path
from itertools import count

import requests
from dotenv import load_dotenv
from pprint import pprint

dotenv_path = "config.env"
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

vk_token = os.getenv("VK_TOKEN")

class VKconnector:
    def __init__(self,access_token,version="5.199"):
        self.access_token = access_token
        self.version = version
        self.base_url = "https://api.vk.com/method/"
        self.params = {
            "access_token":self.access_token,
            "v": self.version
        }
    def user_info(self,user_id):
        url = f"{self.base_url}users.get"
        params = {
            **self.params,
            'user_ids': user_id
        }

        response = requests.get(url,params=params)

    def photo_info(self, user_id,count=1):
        url = f"{self.base_url}photos.get"
        params = {
            **self.params,
            'owner_id': user_id,
            'album_id': 'profile',
            'count':count
        }

        response = requests.get(url, params=params)
        return response.json()



connector = VKconnector(vk_token)
