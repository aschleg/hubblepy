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


@vcr.use_cassette('tests/cassettes/test_video_collections.yml')
def test_video_collections():
    p1 = hubblepy.video_collections(collection_name='science')
    p2 = hubblepy.video_collections(collection_name='science', page=2)
    p3 = hubblepy.video_collections(collection_name='science', page='all')
    p4 = hubblepy.video_collections(collection_name='science', return_type='content')
    p5 = hubblepy.video_collections(collection_name='science', return_type='text')

    assert isinstance(p1[0], dict)
    assert isinstance(p1, list)
    assert isinstance(p2[0], dict)
    assert isinstance(p2, list)
    assert isinstance(p3[0], dict)
    assert isinstance(p3, list)
    assert isinstance(p4, bytes)
    assert isinstance(p5, str)


@vcr.use_cassette('tests/cassettes/test_videos.yml')
def test_videos():
    p1 = hubblepy.videos(video_id='55')
    p2 = hubblepy.videos(video_id=55)
    p3 = hubblepy.videos(video_id='55', return_type='content')
    p4 = hubblepy.videos('55', return_type='text')
    p5 = hubblepy.videos(video_id=[55, 58])

    assert isinstance(p1, dict)
    assert isinstance(p2, dict)
    assert isinstance(p3, bytes)
    assert isinstance(p4, str)
    assert isinstance(p5, list)
    assert isinstance(p5[0], dict)


@vcr.use_cassette('tests/cassettes/test_glossary.yml')
def test_glossary():
    p1 = hubblepy.glossary()
    p2 = hubblepy.glossary(page=2)
    p3 = hubblepy.glossary(page='all')
    p4 = hubblepy.glossary(page=2, return_type='content')
    p5 = hubblepy.glossary(page=2, return_type='text')
    p6 = hubblepy.glossary(page=[1, 2])

    assert isinstance(p1[0], dict)
    assert isinstance(p1, list)
    assert isinstance(p2[0], dict)
    assert isinstance(p2, list)
    assert isinstance(p3[0], dict)
    assert isinstance(p3, list)
    assert isinstance(p4, bytes)
    assert isinstance(p5, str)
    assert isinstance(p6, list)
    assert isinstance(p6[0], list)
    assert isinstance(p6[0][0], dict)


@vcr.use_cassette('tests/cassettes/test_glossary_term.yml')
def test_glossary_term():
    p1 = hubblepy.glossary_term(term='asteroid')
    p2 = hubblepy.glossary_term(term=['asteroid', 'planet'])
    p3 = hubblepy.glossary_term(term='asteroid', return_type='content')
    p4 = hubblepy.glossary_term(term='asteroid', return_type='text')

    assert isinstance(p1, dict)
    assert isinstance(p2, list)
    assert isinstance(p2[0], dict)
    assert isinstance(p3, bytes)
    assert isinstance(p4, str)


@vcr.use_cassette('tests/cassettes/test_rss.yml')
def test_rss():
    p1 = hubblepy.rss(feed_name='esa_feed')
    p2 = hubblepy.rss(feed_name='esa_feed', sort='asc', page=1)
    p3 = hubblepy.rss(feed_name='esa_feed', sort='asc', page=[1, 2])
    p4 = hubblepy.rss(feed_name='esa_feed', sort='asc', page='all')
    p5 = hubblepy.rss(feed_name='esa_feed', return_type='content')
    p6 = hubblepy.rss(feed_name='esa_feed', return_type='text')

    assert isinstance(p1, list)
    assert isinstance(p1[0], dict)
    assert isinstance(p2, list)
    assert isinstance(p2[0], dict)
    assert isinstance(p2[1], dict)
    assert isinstance(p3, list)
    assert isinstance(p3[0], dict)
    assert isinstance(p4, list)
    assert isinstance(p4[0], dict)
    assert isinstance(p5, bytes)
    assert isinstance(p6, str)


@vcr.use_cassette('tests/cassettes/test_rss_posts.yml')
def test_rss_posts():
    p1 = hubblepy.rss_posts(feed_name='esa_feed', pub_date='2017-03-23T13:00:00.000-04:00')
    p2 = hubblepy.rss_posts(feed_name='esa_feed', pub_date=['2017-03-23T13:00:00.000-04:00',
                                                            '2018-09-13T11:00:00.000-04:00'])
    p3 = hubblepy.rss_posts(feed_name='esa_feed', pub_date='2017-03-23T13:00:00.000-04:00', return_type='content')
    p4 = hubblepy.rss_posts(feed_name='esa_feed', pub_date='2017-03-23T13:00:00.000-04:00', return_type='text')

    assert isinstance(p1, dict)
    assert isinstance(p2, list)
    assert isinstance(p2[0], dict)
    assert isinstance(p2[1], dict)
    assert isinstance(p3, bytes)
    assert isinstance(p4, str)
