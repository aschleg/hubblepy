import vcr
import pytest

import hubblepy


tape = vcr.VCR(
    cassette_library_dir='tests/cassettes',
    serializer='json',
    record_mode='once'
)


@vcr.use_cassette('tests/cassettes/test_news.yml')
def test_news():
    p1 = hubblepy.news(1)
    p2 = hubblepy.news('1')
    p3 = hubblepy.news([1, 2, 3])
    p4 = hubblepy.news(1, 'text')
    p5 = hubblepy.news(1, 'content')

    assert isinstance(p1, list)
    assert isinstance(p1[0], dict)
    assert isinstance(p2[0], dict)
    assert isinstance(p3, list)
    assert isinstance(p4, str)
    assert isinstance(p5, bytes)


@vcr.use_cassette('tests/cassettes/test_news_releases.yml')
def test_news_release():
    p1 = hubblepy.news_release('first')
    p2 = hubblepy.news_release('2016-24')

    assert isinstance(p1, dict)
    assert isinstance(p2, dict)


@vcr.use_cassette('tests/cassettes/test_image_collections.yml')
def test_image_collections():
    p1 = hubblepy.image_collections(collection_name='news')
    p2 = hubblepy.image_collections(collection_name='news', page=[1, 2])
    p3 = hubblepy.image_collections(collection_name='news', page=1)
    p4 = hubblepy.image_collections(collection_name='news', page='1')
    p5 = hubblepy.image_collections(collection_name='news', page=1, return_type='text')
    p6 = hubblepy.image_collections(collection_name='news', page=1, return_type='content')

    assert isinstance(p1, list)
    assert isinstance(p1[0], dict)
    assert isinstance(p2, list)
    assert isinstance(p3, list)
    assert isinstance(p3[0], dict)
    assert isinstance(p4, list)
    assert isinstance(p4[0], dict)
    assert isinstance(p5, str)
    assert isinstance(p6, bytes)


@vcr.use_cassette('tests/cassettes/test_images.yml')
def test_images():
    p1 = hubblepy.images(image_id=4229)
    p2 = hubblepy.images(image_id=[4229, 4230])
    p3 = hubblepy.images(image_id=4229, return_type='content')
    p4 = hubblepy.images(image_id=4229, return_type='text')
    p5 = hubblepy.images(image_id=[4229, 4230], return_type='text')

    assert isinstance(p1, dict)
    assert isinstance(p2, list)
    assert isinstance(p3, bytes)
    assert isinstance(p4, str)
    assert isinstance(p5, list)
    assert isinstance(p5[0], str)
