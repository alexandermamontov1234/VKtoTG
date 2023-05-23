import os
import requests
from dotenv import load_dotenv


load_dotenv()
DOMAIN = str(os.getenv('DOMAIN'))
api_version = str(os.getenv('api_version'))
VK_TOKEN = str(os.getenv('VK_TOKEN'))


res_wall = requests.get(f'https://api.vk.com/method/wall.get?domain={DOMAIN}&count=10&access_token={VK_TOKEN}&v={api_version}')
res = res_wall.json()


def get_data():
    d = {}
    for item in res['response']['items'][1:]:
        with open('last_known_id.txt', 'r') as f:
            lst_id = f.read()

        if item['id'] <= int(lst_id):
            break
        else:
            if item['text']:
                text = item['text']
            else:
                text = ""
            if item["attachments"]:
                max_size = 0
                for size in item["attachments"][0]["photo"]["sizes"]:
                    if max_size < size['width']:
                        max_size = size['width']
                for size in item["attachments"][0]["photo"]["sizes"]:
                    if max_size == size['width']:
                        img = size['url']
            else:
                img = None
            with open('last_known_id.txt', 'w') as f:
                f.write(f"{item['id']}")
            d[text] = img
    print(d)
    return d
