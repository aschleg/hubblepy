import requests
from urllib.parse import urljoin


base_url = 'http://hubblesite.org/api/'
api_version = 'v3/'

api_url = urljoin(base_url, api_version)


def news(page=None, return_type='json'):
    r"""
    Returns metadata including the id, name and url of published releases produced by the Office of Public Outreach
    of the Space Telescope Science Institute. Each result set (page) contains 25 items (if available).

    Parameters
    ----------
    page : list, tuple, str, int, or None
        The page number of the published releases to return. Can be a list or tuple of ints, a str or int, or None.
        'all' returns all pages.
    return_type : str, {'json', 'content', 'text'}
        Specifies the return type of the results. Defaults to JSON.

    Returns
    -------
    list
        List of results.

    Examples
    --------
    >>> p1 = hubblepy.news()
    [{'name': 'Hubble Uncovers Never Before Seen Features Around a Neutron Star',
      'news_id': '2018-43',
      'url': 'http://hubblesite.org/news_release/news/2018-43'},
     {'name': 'Hubble Goes Wide to Seek Out Far-Flung Galaxies',
      'news_id': '2018-39',
      'url': 'http://hubblesite.org/news_release/news/2018-39'},
     {'name': "Success in Critical Communications Tests for NASA's James Webb Space Telescope",
      'news_id': '2018-31',
      'url': 'http://webbtelescope.org/articles/2018-31'},
     {'name': 'Retiring Hubble Visualization Expert Blended the Best of Science and Art',
      'news_id': '2018-41',
      ...
    >>> p2 = hubblepy.news(4)
    [{'name': "Space Telescope Science Institute to Host Data from World's Largest Digital Sky Survey",
      'news_id': '2016-41',
      'url': 'http://hubblesite.org/news_release/news/2016-41'},
     {'name': 'STScI Astronomers Nancy Levenson and David Soderblom Elected AAAS Fellows',
      'news_id': '2016-46',
      'url': 'http://hubblesite.org/news_release/news/2016-46'},
     {'name': 'Dr. Laurent Pueyo Receives 2016 Outstanding Young Scientist Award',
      'news_id': '2016-40',
      'url': 'http://hubblesite.org/news_release/news/2016-40'},
     {'name': "A Death Star's Ghostly Glow",
      'news_id': '2016-37',
      ...]

    Notes
    -----
    The news releases are sorted by publication date and time. All the returned results can also be found on the
    HubbleSite's news center, http://hubblesite.org/news.

    """
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


def news_release(which, return_type='json'):
    r"""
    Returns more detailed metadata including the abstract, image thumbnails, and more, of a published release.

    Parameters
    ----------
    which : list, tuple, str
        Specifies which news release content to return. Possible values include 'last' for the last news release
        published, 'first', which returns the first published release, and the release identifier in the format
        YYYY-NN.
    return_type : str, {'json', 'content', 'text'}
        Specifies the return type of the results. Defaults to JSON.

    Returns
    -------
    dict or list
        The returned results.

    Examples
    --------
    >>> hubblepy.news_release(which='last')
    {'abstract': 'Imagine crushing more than 50,000 aircraft carriers into the size of a baseball. This describes neutron stars. They are among the strangest objects in the universe. Neutron stars are a case of extreme physics produced by the unforgiving force of gravity. The entire core of an exploded star has been squeezed into a solid ball of neutrons with the density of an atom’s nucleus. Neutron stars spin as fast as a blender on puree. Some spit out death-star beams of intense radiation — like interstellar lighthouses. These are called pulsars.\r\n\r\nThese beams are normally seen in X-rays, gamma-rays, and radio waves. But astronomers used Hubble\'s near-infrared (IR) vision to look at a nearby neutron star cataloged RX J0806.4-4123. They were surprised to see a gush of IR light coming from a region around the neutron star. That infrared light might come from a circumstellar disk 18 billion miles across. Another idea is that a wind of subatomic particles from the pulsar’s magnetic field is slamming into interstellar gas. Hubble\'s IR vision opens a new window into understanding how these "infernal machines" work.\r\n',
     'credits': '<a href="http://www.nasa.gov">NASA</a>, <a href="http://www.spacetelescope.org">ESA</a>, and B. Posselt (Pennsylania State University)',
     'keystone_image_1x': 'https://media.stsci.edu/uploads/story/display_image/1243/low_STSCI-H-p1843a-k-1340x520.png',
     'keystone_image_2x': 'https://media.stsci.edu/uploads/story/display_image/1243/STSCI-H-p1843a-k-1340x520.png',
     'mission': 'hubble',
     'name': 'Hubble Uncovers Never Before Seen Features Around a Neutron Star',
     'news_id': '2018-43',
     'publication': '2018-09-17T11:00:00.000-04:00',
     'release_images': [4231, 4232, 4233],
     'thumbnail': 'https://media.stsci.edu/uploads/story/thumbnail/1243/low_STSCI-H-p1843a-t-400x400.png',
     'thumbnail_1x': 'https://media.stsci.edu/uploads/story/thumbnail/1243/low_STSCI-H-p1843a-t-400x400.png',
     'thumbnail_2x': 'https://media.stsci.edu/uploads/story/thumbnail/1243/STSCI-H-p1843a-t-400x400.png',
     'thumbnail_retina': 'https://media.stsci.edu/uploads/story/thumbnail/1243/STSCI-H-p1843a-t-400x400.png',
     'url': 'http://hubblesite.org/news_release/news/2018-43'}
    >>> hubblepy.news_release(which=['last', 'first', '2016-24'])
    [{'abstract': 'Imagine crushing more than 50,000 aircraft carriers into the size of a baseball. This describes neutron stars. They are among the strangest objects in the universe. Neutron stars are a case of extreme physics produced by the unforgiving force of gravity. The entire core of an exploded star has been squeezed into a solid ball of neutrons with the density of an atom’s nucleus. Neutron stars spin as fast as a blender on puree. Some spit out death-star beams of intense radiation — like interstellar lighthouses. These are called pulsars.\r\n\r\nThese beams are normally seen in X-rays, gamma-rays, and radio waves. But astronomers used Hubble\'s near-infrared (IR) vision to look at a nearby neutron star cataloged RX J0806.4-4123. They were surprised to see a gush of IR light coming from a region around the neutron star. That infrared light might come from a circumstellar disk 18 billion miles across. Another idea is that a wind of subatomic particles from the pulsar’s magnetic field is slamming into interstellar gas. Hubble\'s IR vision opens a new window into understanding how these "infernal machines" work.\r\n',
      'credits': '<a href="http://www.nasa.gov">NASA</a>, <a href="http://www.spacetelescope.org">ESA</a>, and B. Posselt (Pennsylania State University)',
      'keystone_image_1x': 'https://media.stsci.edu/uploads/story/display_image/1243/low_STSCI-H-p1843a-k-1340x520.png',
      'keystone_image_2x': 'https://media.stsci.edu/uploads/story/display_image/1243/STSCI-H-p1843a-k-1340x520.png',
      'mission': 'hubble',
      'name': 'Hubble Uncovers Never Before Seen Features Around a Neutron Star',
      'news_id': '2018-43',
      'publication': '2018-09-17T11:00:00.000-04:00',
      'release_images': [4231, 4232, 4233],
      'thumbnail': 'https://media.stsci.edu/uploads/story/thumbnail/1243/low_STSCI-H-p1843a-t-400x400.png',
      'thumbnail_1x': 'https://media.stsci.edu/uploads/story/thumbnail/1243/low_STSCI-H-p1843a-t-400x400.png',
      'thumbnail_2x': 'https://media.stsci.edu/uploads/story/thumbnail/1243/STSCI-H-p1843a-t-400x400.png',
      'thumbnail_retina': 'https://media.stsci.edu/uploads/story/thumbnail/1243/STSCI-H-p1843a-t-400x400.png',
      'url': 'http://hubblesite.org/news_release/news/2018-43'},
     {'abstract': "On the right is part of the first image taken with NASA's Hubble Space Telescope's (HST) Wide Field/Planetary Camera. It is shown with a ground-based picture from a Las Campanas, Chile, observatory of the same region of the sky. The Las Campanas picture was taken with a 100-inch telescope and it is typical of high-quality pictures obtained from the ground. All objects seen are stars within the Milky Way galaxy.",
      'credits': 'Credit: <a href="http://www.nasa.gov/">NASA</a>, <a href="http://www.spacetelescope.org/">ESA</a>, and <a href="http://www.stsci.edu/">STScI</a>',
      'mission': 'hubble',
      'name': 'HST WC/PC First Light Image',
      'news_id': '1990-04',
      'publication': '1990-05-20T00:00:00.000-04:00',
      'release_images': [1],
      'thumbnail': 'https://media.stsci.edu/uploads/story/thumbnail/1/low_small_web.jpg',
      'thumbnail_1x': 'https://media.stsci.edu/uploads/story/thumbnail/1/low_small_web.jpg',
      'thumbnail_2x': 'https://media.stsci.edu/uploads/story/thumbnail/1/small_web.jpg',
      'thumbnail_retina': 'https://media.stsci.edu/uploads/story/thumbnail/1/small_web.jpg',
      'url': 'http://hubblesite.org/news_release/news/1990-04'},
     {'abstract': "Astronomers are using NASA's Hubble Space Telescope to study auroras — stunning light shows in a planet's atmosphere — on the poles of the largest planet in the solar system, Jupiter. The auroras were photographed during a series of Hubble Space Telescope Imaging Spectrograph far-ultraviolet-light observations taking place as NASA's Juno spacecraft approaches and enters into orbit around Jupiter. The aim of the program is to determine how Jupiter's auroras respond to changing conditions in the solar wind, a stream of charged particles emitted from the sun. Auroras are formed when charged particles in the space surrounding the planet are accelerated to high energies along the planet's magnetic field. When the particles hit the atmosphere near the magnetic poles, they cause it to glow like gases in a fluorescent light fixture. Jupiter's magnetosphere is 20,000 times stronger than Earth's. These observations will reveal how the solar system's largest and most powerful magnetosphere behaves.\r\n\r\nThe full-color disk of Jupiter in this image was separately photographed at a different time by Hubble's Outer Planet Atmospheres Legacy (OPAL) program, a long-term Hubble project that annually captures global maps of the outer planets.",
      'credits': 'Credit: <a href="http://www.nasa.gov/">NASA</a>, <a href="http://www.spacetelescope.org/">ESA</a>, and J. Nichols (University of Leicester)\r\n\r\nAcknowledgment: A. Simon (<a href="http://www.nasa.gov/">NASA</a>/GSFC) and the OPAL team',
      'keystone_image_1x': 'https://media.stsci.edu/uploads/story/display_image/1144/low_keystone.png',
      'keystone_image_2x': 'https://media.stsci.edu/uploads/story/display_image/1144/keystone.png',
      'mission': 'hubble',
      'name': "Hubble Captures Vivid Auroras in Jupiter's Atmosphere",
      'news_id': '2016-24',
      'publication': '2016-06-30T10:00:00.000-04:00',
      'release_images': [3756, 3758, 3757],
      'release_videos': [865, 867, 866, 868],
      'thumbnail': 'https://media.stsci.edu/uploads/story/thumbnail/1144/low_web.jpg',
      'thumbnail_1x': 'https://media.stsci.edu/uploads/story/thumbnail/1144/low_web.jpg',
      'thumbnail_2x': 'https://media.stsci.edu/uploads/story/thumbnail/1144/web.jpg',
      'thumbnail_retina': 'https://media.stsci.edu/uploads/story/thumbnail/1144/web.jpg',
      'url': 'http://hubblesite.org/news_release/news/2016-24'}]

    """
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
    r"""
    Returns metadata including the id, name, name of the associated news release, collection and mission of images
    from different collections available on the HubbleSite.

    Parameters
    ----------
    page : list, tuple, str, int, or None
        The page number of the published images to return. Can be a list or tuple of ints, a str or int, or None.
        'all' returns all pages.
    collection_name : list, str, or None
        The name of the collection to return images. Collections are sets of images such as 'news', 'spacecraft',
        etc. If 'all', returns all images from all collections.
    return_type : str, {'json', 'content', 'text'}
        Specifies the return type of the results. Defaults to JSON.

    Returns
    -------
    list
        List of results

    Examples
    --------
    >>> hubblepy.image_collections(1, 'spacecraft')
    [{'id': 3814, 'name': 'Grappling Hubble (2009)'},
     {'id': 3813, 'name': 'Bidding Hubble Farewell (2009)'},
     {'id': 3812, 'name': 'Hubble From Behind (2009)'},
     {'id': 3811, 'name': 'Installing Wide Field Camera 3 (2009)'},
     {'id': 3810, 'name': 'Final Release Over Earth (2009)'},
     {'id': 3809, 'name': 'Reflecting on Work (2009)'},
     {'id': 3808, 'name': "In a Day's Work (2009)"},
     {'id': 3807, 'name': 'Going Up? (2009)'},
     {'id': 3806, 'name': 'Getting in Position (2009)'},
     {'id': 3805, 'name': 'Hanging Out With Hubble (2009)'},
     {'id': 3804, 'name': "Lifting Hubble from Atlantis' Cargo Bay (2009)"},
     {'id': 3836,
      'name': 'Hubble Control Center, Goddard Space Flight Center (1999)'},
     {'id': 3835,
      'name': 'Working at the Hubble Control Center, Space Telescope Science Institute (2005)'},
     {'id': 3834, 'name': 'Hubble in Flight (1997) '},
     {'id': 3833, 'name': "Hubble Restored: The Telescope's Latest Look (2002)"},
     {'id': 3832, 'name': 'Hubble Floating Free (2002)'},
     {'id': 3831, 'name': "Hubble Against Earth's Horizon (1997)"},
     {'id': 3830, 'name': 'Repairing Hubble (1997)'},
     {'id': 3829, 'name': 'Camera Crew: Taking Pictures of the Mission (1997)'},
     {'id': 3828, 'name': 'Hubble Docked with the Shuttle Endeavor (1993)'},
     {'id': 3827, 'name': 'Hubble Docked with Discovery (1999)'},
     {'id': 3826,
      'name': 'Giving Guidance: Replacing the Fine Guidance Sensors (1997)'},
     {'id': 3825, 'name': 'Cast-off: Releasing a Solar Array (1993)'},
     {'id': 3824,
      'name': 'Out with the Old: Replacing the High Resolution Spectrograph (1997)'},
     {'id': 3823,
      'name': 'A Second Look: Replacing the Wide Field and Planetary Camera (1993)'}]

    """
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
    r"""
    Returns more specific metadata of available images including the description, credits, the location of the image
    files and more.

    Parameters
    ----------
    image_id : list, tuple, str, int
        A list or tuple of str or int representing the image ids to return.
    return_type : str, {'json', 'content', 'text'}
        Specifies the return type of the results. Defaults to JSON.

    Returns
    -------
    dict or list
        If only one image_id is passed, a dictionary of the results is returned. Otherwise, a list of dictionaries
        containing the results is returned.

    Examples
    --------
    >>> hubblepy.images(3823)
    {'collection': 'spacecraft',
     'credits': '<a href="http://www.nasa.gov">NASA</a>',
     'description': "Astronauts remove the Wide Field and Planetary Camera to replace it with its more powerful successor, Wide Field and Planetary Camera 2, during Hubble’s first servicing mission in 1993. The camera, shaped something like a grand piano, weighs 610 pounds (277 kg) on Earth, but nothing in space. It can detect stars a billion times fainter than the ones we can see with our eyes. Most of Hubble's most popular pictures have been taken with this second camera.",
     'image_files': [{'file_size': 112455,
       'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29327/STScI-H-spacecraft15-title.pdf',
       'height': 612,
       'width': 792},
      {'file_size': 335340,
       'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29324/STScI-H-spacecraft15-3000x2016.jpg',
       'height': 2016,
       'width': 3000},
      {'file_size': 18164836,
       'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29325/STScI-H-spacecraft15-3000x2016.tif',
       'height': 2016,
       'width': 3000},
      {'file_size': 619187,
       'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29326/STScI-H-spacecraft15-title-3000x2400.jpg',
       'height': 2400,
       'width': 3000}],
     'mission': 'hubble',
     'name': 'A Second Look: Replacing the Wide Field and Planetary Camera (1993)'}
    >>> hubblepy.images([3823, 3834])
    [{'collection': 'spacecraft',
      'credits': '<a href="http://www.nasa.gov">NASA</a>',
      'description': "Astronauts remove the Wide Field and Planetary Camera to replace it with its more powerful successor, Wide Field and Planetary Camera 2, during Hubble’s first servicing mission in 1993. The camera, shaped something like a grand piano, weighs 610 pounds (277 kg) on Earth, but nothing in space. It can detect stars a billion times fainter than the ones we can see with our eyes. Most of Hubble's most popular pictures have been taken with this second camera.",
      'image_files': [{'file_size': 112455,
        'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29327/STScI-H-spacecraft15-title.pdf',
        'height': 612,
        'width': 792},
       {'file_size': 335340,
        'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29324/STScI-H-spacecraft15-3000x2016.jpg',
        'height': 2016,
        'width': 3000},
       {'file_size': 18164836,
        'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29325/STScI-H-spacecraft15-3000x2016.tif',
        'height': 2016,
        'width': 3000},
       {'file_size': 619187,
        'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29326/STScI-H-spacecraft15-title-3000x2400.jpg',
        'height': 2400,
        'width': 3000}],
      'mission': 'hubble',
      'name': 'A Second Look: Replacing the Wide Field and Planetary Camera (1993)'},
     {'collection': 'spacecraft',
      'credits': '<a href="http://www.nasa.gov">NASA</a>',
      'description': "The Hubble Space Telescope drifts through space in this picture, taken by Space Shuttle Discovery during Hubble's second servicing mission in 1997. The 10-foot aperture door, open to admit light, closes to block out space debris. The observatory's solar panels and foil-like thermal blankets are clearly visible. The solar panels provide power, while the thermal blankets protect Hubble from the extreme temperatures of space.",
      'image_files': [{'file_size': 80695,
        'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29371/STScI-H-spacecraft03-title.pdf',
        'height': 612,
        'width': 792},
       {'file_size': 1186774,
        'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29368/STScI-H-spacecraft03-1500x1500.jpg',
        'height': 1500,
        'width': 1500},
       {'file_size': 6771696,
        'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29369/STScI-H-spacecraft03-1500x1500.tif',
        'height': 1500,
        'width': 1500},
       {'file_size': 649084,
        'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29370/STScI-H-spacecraft03-title-3000x2400.jpg',
        'height': 2400,
        'width': 3000}],
      'mission': 'hubble',
      'name': 'Hubble in Flight (1997) '}]

    """
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
    r"""
    Returns metadata of published videos available on the HubbleSite including the video id, name, image,
    and the associated collection and mission.

    Parameters
    ----------
    page : list, tuple, str, int, or None
        The page number of the published videos to return. Can be a list or tuple of ints, a str or int, or None.
        'all' returns all pages.
    collection_name : list, str, or None
        The name of the collection to return. Collections are sets of videos such as 'news', 'spacecraft',
        etc. If 'all', returns all images from all collections.
    return_type : str, {'json', 'content', 'text'}
        Specifies the return type of the results. Defaults to JSON.

    Returns
    -------
    list
        List of results.

    Examples
    --------
    >>> hubblepy.video_collections(1, 'space')
    [{'id': 1046,
      'image': 'https://media.stsci.edu/uploads/video/image_attachment/1046/thumb_low_STScI-H-MWC_t420x236.png',
      'name': 'Milky Way Center in Multiple Wavelengths'},
     {'id': 1141,
      'image': 'https://media.stsci.edu/uploads/video/image_attachment/1141/thumb_low_arp273-example_frame-1920x1080.jpg',
      'name': 'A Rose of Galaxies: Interacting Galaxies Arp 273'},
     {'id': 1155,
      'image': 'https://media.stsci.edu/uploads/video/image_attachment/1155/thumb_low_orion_vis_dome-example_frame-1920x1080.png',
      'name': 'Flight Through the Orion Nebula in Visible Light - Dome Version'},
      ...]
    """
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
    r"""

    Parameters
    ----------

    Returns
    -------

    Examples
    --------

    """
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
    r"""

    Parameters
    ----------

    Returns
    -------

    Examples
    --------

    """
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
    r"""

    Parameters
    ----------

    Returns
    -------

    Examples
    --------

    """
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
    r"""

    Parameters
    ----------

    Returns
    -------

    Examples
    --------
    """
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
    r"""

    Parameters
    ----------

    Returns
    -------

    Examples
    --------

    """
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
    r"""

    Parameters
    ----------

    Returns
    -------

    """
    if return_type == 'json':
        r = r.json()
    elif return_type == 'text':
        r = r.text
    elif return_type == 'content':
        r = r.content
    else:
        raise ValueError("'return_type' must be one of 'json', 'text', 'content'.")

    return r
