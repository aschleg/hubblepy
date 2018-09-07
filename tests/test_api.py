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
