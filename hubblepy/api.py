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

    if not isinstance(page, (list, tuple)):
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


def video_collections(page=None, collection_name=None, return_type='json'):
    endpoint = urljoin(api_url, 'videos/')

    if not isinstance(page, (list, tuple)):
        r = requests.get(urljoin(endpoint, collection_name))
        res = _return_types(r, return_type)

    else:
        res = []

        for i in page:
            r = requests.get(urljoin(endpoint, collection_name), params={'page': i})
            r = _return_types(r, return_type)

            res.append(r)

    return res


def videos(video_id, return_type='json'):
    endpoint = urljoin(api_url, 'video/')

    if not isinstance(video_id, (list, tuple)):
        r = requests.get(urljoin(endpoint, str(video_id)))
        res = _return_types(r, return_type)

    else:
        res = []

        for i in video_id:
            r = requests.get(urljoin(endpoint, str(i)))
            r = _return_types(r, return_type)

            res.append(r)

    return res


def glossary(page=None, return_type='json'):
    endpoint = urljoin(api_url, 'glossary')

    if not isinstance(page, (list, tuple)):
        r = requests.get(endpoint, params={'page': page})
        res = _return_types(r, return_type)

    else:
        res = []

        for i in page:
            r = requests.get(endpoint, params={'page': i})
            r = _return_types(r, return_type)

            res.append(r)

    return res


def glossary_term(term, return_type='json'):
    endpoint = urljoin(api_url, 'glossary/')

    if not isinstance(term, (list, tuple)):
        r = requests.get(urljoin(endpoint, term))
        res = _return_types(r, return_type)

    else:
        res = []

        for i in term:
            r = requests.get(urljoin(endpoint, i))
            r = _return_types(r, return_type)

            res.append(r)

    return res


def rss(feed_name, page=None, sort='desc', return_type='json'):
    endpoint = urljoin(api_url, 'external_feed/')

    if sort == 'desc':
        sort = '-pub_date'
    else:
        sort = 'pub_date'

    if not isinstance(page, (list, tuple)):
        r = requests.get(urljoin(endpoint, feed_name), params={'page': page,
                                                               'sort': sort})

        res = _return_types(r, return_type)

    else:
        res = []

        for i in page:
            r = requests.get(urljoin(endpoint, feed_name), params={'page': i,
                                                                   'sort': sort})

            res = _return_types(r, return_type)

            res.append(r)

    return res


def rss_posts(feed_name, pub_date, return_type='json'):
    endpoint = urljoin(api_url, 'external_feed/')

    if not isinstance(pub_date, (list, tuple)):
        r = requests.get(urljoin(endpoint, feed_name) + '/' + pub_date)
        res = _return_types(r, return_type)

    else:
        res = []

        for i in pub_date:
            r = requests.get(urljoin(endpoint, feed_name) + '/' + i)
            r = _return_types(r, return_type)

            res.append(r)

    return res


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
