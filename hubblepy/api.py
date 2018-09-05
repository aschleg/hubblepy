import requests
from urllib.parse import urljoin


base_url = 'http://hubblesite.org/api/'
api_version = 'v3'

api_url = urljoin(base_url, api_version)


def get_news(page=None):
    endpoint = urljoin(api_url, 'news')

    r = requests.get(endpoint, params={'page': page})

    return r
