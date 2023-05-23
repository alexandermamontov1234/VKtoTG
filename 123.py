import requests
import json
from config import VK_TOKEN


api_version = '5.89'
res_wall = requests.get(f'https://api.vk.com/method/wall.get?domain=dota2_facts&count=10&access_token={VK_TOKEN}&v={api_version}')

res = res_wall.json()


# for items in d.items():
#     print(items)


# for photo in res['response']['items']:
#     for img in photo["attachments"][0]["photo"]["sizes"]:
#         if img['type'] == 'w':
#             print(img)
    # print(photo["attachments"][0]["photo"]["sizes"])


with open("post.txt", 'w') as f:
    json.dump(res, f, indent=4)
