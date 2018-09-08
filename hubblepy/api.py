import requests
from urllib.parse import urljoin


base_url = 'http://hubblesite.org/api/'
api_version = 'v3/'

api_url = urljoin(base_url, api_version)


def news(page=None, return_type='json'):

    endpoint = urljoin(api_url, 'news')

    if page is None or not isinstance(page, (tuple, list)):
        r = requests.get(endpoint, params={'page': page})
        res = _return_types(r, return_type)

    else:
        res = []

        for i in page:
            r = requests.get(endpoint, params={'page': i})
            r = _return_types(r, return_type)

            res.append(r)

    return res


def news_release(which=None, return_type='json'):
    endpoint = urljoin(api_url, 'news_release/')

    if which is None or not isinstance(which, (tuple, list)):
        r = requests.get(urljoin(endpoint, which))
        res = _return_types(r, return_type)

    else:
        res = []

        for i in which:
            r = requests.get(urljoin(endpoint, i))
            r = _return_types(r, return_type)

            res.append(r)

    return res


def image_collections(page=None, collection_name=None, return_type='json'):
    endpoint = urljoin(api_url, 'images/')

    if page is None or not isinstance(page, (list, tuple)):
        r = requests.get(urljoin(endpoint, collection_name))
        res = _return_types(r, return_type)

    else:
        if page == 'all':
            r = requests.get(urljoin(endpoint, collection_name), params={'page': page})
            res = _return_types(r, return_type)
        else:
            res = []

            for i in page:
                r = requests.get(urljoin(endpoint, collection_name), params={'page': i})
                r = _return_types(r, return_type)

                res.append(r)

    return res


def images(image_id, return_type='json'):
    endpoint = urljoin(api_url, 'image/')

    if not isinstance(image_id, (list, tuple)):
        r = requests.get(urljoin(endpoint, str(image_id)))
        res = _return_types(r, return_type)

    else:
        res = []

        for i in image_id:
            r = requests.get(urljoin(endpoint, str(i)))
            r = _return_types(r, return_type)

            res.append(r)

    return res


def videos():
    pass


def glossary():
    pass


def rss():
    pass


def rss_posts():
    pass


def _return_types(r, return_type):
    if return_type == 'json':
        r = r.json()
    elif return_type == 'text':
        r = r.text
    elif return_type == 'content':
        r = r.content
    else:
        raise ValueError("'return_type' must be one of 'json', 'text', 'content'.")

    return r
