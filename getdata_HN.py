import requests
import json
import os.path
from urllib.parse import urljoin

URL = 'https://hacker-news.firebaseio.com/v0/'
KEYWORDS = ['python', 'django']
story = {}


def get_json(param):
    url = urljoin(URL, param)
    req = requests.get(url)
    return req.json()


def get_stories():
    parameter = 'topstories.json?print=pretty'
    return get_json(parameter)


def check_item():
    for item in get_stories():
        parameter = 'item/{}.json?print=pretty'.format(item)
        item = get_json(parameter)
        for kwd in KEYWORDS:
            if kwd in item['title']:
                return item


def get_item(item):
    parameter = 'item/{}.json?print=pretty'.format(item)
    item = get_json(parameter)
    story[item['id']] = {'title': item['title']}
    return


def save_items(items, filename='tmp-data.json'):
    with open(filename, 'w') as outfile:
        json.dump(items, outfile, indent=4)
    return


if os.path.isfile('tmp-data.json'):
    with open('tmp-data.json') as json_data:
        stories = json.load(json_data)
    if check_item():
        parameter = 'item/{}.json?print=pretty'.format(check_item())
        new_item = get_json(parameter)
        stories[check_item()] = {
            'title': new_item['title']
        }
    save_items(stories)
else:
    if check_item(check_item()):
        get_item(check_item())
    save_items(story)
