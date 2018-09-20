# Hubblepy - Python wrapper for the Hubblesite.org API

[![Build Status](https://travis-ci.org/aschleg/hubblepy.svg?branch=master)](https://travis-ci.org/aschleg/hubblepy)
[![Build status](https://ci.appveyor.com/api/projects/status/h4arxow3ord4njd7?svg=true)](https://ci.appveyor.com/project/aschleg/hubblepy)
[![Coverage Status](https://coveralls.io/repos/github/aschleg/hubblepy/badge.svg?branch=master)](https://coveralls.io/github/aschleg/hubblepy?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/586d9f157a2248bf951a5d392f5ebbef)](https://www.codacy.com/app/aschleg/hubblepy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=aschleg/hubblepy&amp;utm_campaign=Badge_Grade)
![Python versions](https://img.shields.io/badge/python-3.4%2C%203.5%2C%203.6-blue.svg)

`hubblepy` is a straightforward and easy-to-use API wrapper for the [Hubblesite](http://hubblesite.org/) API.

## Requirements

* Python 3.4+
* `requests >= 2.18`

## Installation

## Documentation

* [Hubblesite.org API Documentation](http://hubblesite.org/api/documentation)

## Examples

The following are some short examples outlining the capabilities and functionality of `hubblepy`.

### Getting most recent news articles

~~~ python
hubblepy.news()[0:3]

[{'name': 'Hubble Uncovers Never Before Seen Features Around a Neutron Star',
  'news_id': '2018-43',
  'url': 'http://hubblesite.org/news_release/news/2018-43'},
 {'name': 'Hubble Goes Wide to Seek Out Far-Flung Galaxies',
  'news_id': '2018-39',
  'url': 'http://hubblesite.org/news_release/news/2018-39'},
 {'name': "Success in Critical Communications Tests for NASA's James Webb Space Telescope",
  'news_id': '2018-31',
  'url': 'http://webbtelescope.org/articles/2018-31'}]
~~~

### Finding more specific details of a published news article

Return the abstract and more information on the most recent published article.

~~~ python
hubblepy.news_release('last')

{'abstract': 'Imagine crushing more than 50,000 aircraft carriers into the size of a baseball. This describes neutron 
  stars. They are among the strangest objects in the universe. Neutron stars are a case of extreme physics produced by 
  the unforgiving force of gravity. The entire core of an exploded star has been squeezed into a solid ball of neutrons 
  with the density of an atom’s nucleus. Neutron stars spin as fast as a blender on puree. Some spit out death-star 
  beams of intense radiation — like interstellar lighthouses. These are called pulsars.\r\n\r\nThese beams are normally 
  seen in X-rays, gamma-rays, and radio waves. But astronomers used Hubble\'s near-infrared (IR) vision to look at a 
  nearby neutron star cataloged RX J0806.4-4123. They were surprised to see a gush of IR light coming from a region 
  around the neutron star. That infrared light might come from a circumstellar disk 18 billion miles across. Another 
  idea is that a wind of subatomic particles from the pulsar’s magnetic field is slamming into interstellar gas. 
  Hubble\'s IR vision opens a new window into understanding how these "infernal machines" work.\r\n',
 'credits': '<a href="http://www.nasa.gov">NASA</a>, <a href="http://www.spacetelescope.org">ESA</a>, and B. Posselt 
 (Pennsylania State University)',
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
~~~

Or, using a `news_id` returned from the `news()` function, we can get more specific information about any other 
article published.

~~~ python
hubblepy.news_release('2018-31')

{'abstract': 'When NASA’s James Webb Space Telescope is en route to and in orbit nearly a million miles from Earth, 
  continuous communications with its Mission Operations Center (MOC) in Baltimore will be essential. Recently, at the 
  Space Telescope Science Institute—home of the MOC—Webb’s Flight Operations Team successfully completed two critical 
  communications tests. The first demonstrated that from the moment Webb launches through the first six hours of flight, 
  complex exchanges could be accomplished among the five different service providers around the world who will 
  alternately convey command and telemetry communications. The second test showed that the MOC could successfully 
  command the telescope.',
 'keystone_image_1x': 'https://media.stsci.edu/uploads/story/display_image/1239/low_STSCI-J-p1831a-k-1340x520.png',
 'keystone_image_2x': 'https://media.stsci.edu/uploads/story/display_image/1239/STSCI-J-p1831a-k-1340x520.png',
 'mission': 'james_webb',
 'name': "Success in Critical Communications Tests for NASA's James Webb Space Telescope",
 'news_id': '2018-31',
 'publication': '2018-09-05T10:00:00.000-04:00',
 'release_images': [4225],
 'thumbnail': 'https://media.stsci.edu/uploads/story/thumbnail/1239/low_STSCI-J-p1831a-t800x800.png',
 'thumbnail_1x': 'https://media.stsci.edu/uploads/story/thumbnail/1239/low_STSCI-J-p1831a-t800x800.png',
 'thumbnail_2x': 'https://media.stsci.edu/uploads/story/thumbnail/1239/STSCI-J-p1831a-t800x800.png',
 'thumbnail_retina': 'https://media.stsci.edu/uploads/story/thumbnail/1239/STSCI-J-p1831a-t800x800.png',
 'url': 'http://webbtelescope.org/articles/2018-31'}
~~~

### Returning image collections produced by the HubbleSite and other agencies

~~~ python
hubblepy.image_collections(collection_name='spacecraft')

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
~~~

### Get metadata and other information on images within collections

~~~ python
hubblepy.images([3814, 3813])

[{'collection': 'spacecraft',
  'credits': '<a href="http://www.nasa.gov">NASA</a>',
  'description': 'The Hubble Space Telescope in a picture snapped by a Servicing Mission 4 crewmember just after the 
   Space Shuttle Atlantis captured Hubble with its robotic arm on May 13, 2009, beginning the mission to upgrade and 
   repair the telescope.',
  'image_files': [{'file_size': 4987706,
    'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29291/STScI-H-spacecraft24-title.pdf',
    'height': 792,
    'width': 612},
   {'file_size': 1256136,
    'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29290/STScI-H-spacecraft24-title-2400x3000.jpg',
    'height': 3000,
    'width': 2400},
   {'file_size': 2051306,
    'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29288/STScI-H-spacecraft24-3072x2040.jpg',
    'height': 2040,
    'width': 3072},
   {'file_size': 18842624,
    'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29289/STScI-H-spacecraft24-3072x2040.tif',
    'height': 2040,
    'width': 3072}],
  'mission': 'hubble',
  'name': 'Grappling Hubble (2009)'},
 {'collection': 'spacecraft',
  'credits': '<a href="http://www.nasa.gov">NASA</a>',
  'description': 'Hubble, released by the Space Shuttle Atlantis after Servicing Mission 4 in May 2009, floats against 
   the background of space. The shuttle and telescope had been linked for the better part of a week while astronauts 
   conducted five spacewalks. The mission is expected to be the last astronaut visit to the telescope.',
  'image_files': [{'file_size': 2694334,
    'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29287/STScI-H-spacecraft25-title.pdf',
    'height': 792,
    'width': 612},
   {'file_size': 1029841,
    'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29286/STScI-H-spacecraft25-title-2400x3000.jpg',
    'height': 3000,
    'width': 2400},
   {'file_size': 5850609,
    'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29284/STScI-H-spacecraft25-3744x2952.jpg',
    'height': 2952,
    'width': 3744},
   {'file_size': 33200652,
    'file_url': 'https://media.stsci.edu/uploads/image_file/image_attachment/29285/STScI-H-spacecraft25-3744x2952.tif',
    'height': 2952,
    'width': 3744}],
  'mission': 'hubble',
  'name': 'Bidding Hubble Farewell (2009)'}]
~~~

### Returning video collections

Similar to collections of images curated by HubbleSite, video collections can also be found and explored.

~~~ python
hubblepy.video_collections('space')[0:3]

[{'collection': 'science',
  'id': 1046,
  'image': 'https://media.stsci.edu/uploads/video/image_attachment/1046/thumb_low_STScI-H-MWC_t420x236.png',
  'name': 'Milky Way Center in Multiple Wavelengths'},
 {'collection': 'news',
  'id': 1171,
  'image': 'https://media.stsci.edu/uploads/video/image_attachment/1171/thumb_low_STScI-H-v1839a-t420x236.png',
  'name': 'Video zoom into Abell 370',
  'news_name': 'a'},
 {'collection': 'science',
  'id': 1141,
  'image': 'https://media.stsci.edu/uploads/video/image_attachment/1141/thumb_low_arp273-example_frame-1920x1080.jpg',
  'name': 'A Rose of Galaxies: Interacting Galaxies Arp 273'}]
~~~

### Returning metadata of a particular video or videos

~~~ python
hubblepy.videos(1046)

{'collection': 'science',
 'credits': 'Video: <a href="http://www.nasa.gov/">NASA</a>, <a href="http://www.spacetelescope.org/">ESA</a>, and 
 G. Bacon (<a href="http://www.stsci.edu/">STScI</a>)\r\n\r\nImage Credits: <a href="http://www.nasa.gov/">NASA</a>, 
 <a href="http://www.spacetelescope.org/">ESA</a>, CXC, SSC and <a href="http://www.stsci.edu/">STScI</a>',
 'image': 'https://media.stsci.edu/uploads/video/image_attachment/1046/low_STScI-H-MWC_t420x236.png',
 'image_retina': 'https://media.stsci.edu/uploads/video/image_attachment/1046/STScI-H-MWC_t420x236.png',
 'mission': 'hubble',
 'name': 'Milky Way Center in Multiple Wavelengths',
 'short_description': 'This animation reveals the center of our Milky Way galaxy, first in near-infrared, then 
 mid-infrared, then X-ray light, and then all three in combination.',
 'video_files': [{'file_size': 16428379,
   'file_url': 'https://media.stsci.edu/uploads/video_file/video_attachment/4694/STScI-H-MWC_1x-3840x2160.mp4',
   'format': 'MPEG-4 4K-UHD',
   'frame_rate': '29.97',
   'height': 2160,
   'width': 3840},
  {'file_size': 11292487,
   'file_url': 'https://media.stsci.edu/uploads/video_file/video_attachment/4698/STScI-H-MWC_2x-3840x2160.mp4',
   'format': 'MPEG-4 4K-UHD',
   'frame_rate': '29.97',
   'height': 2160,
   'width': 3840},
  {'file_size': 18985331,
   'file_url': 'https://media.stsci.edu/uploads/video_file/video_attachment/4693/STScI-H-MWC_1x-1920x1080.mp4',
   'format': 'MPEG-4 (H.264)',
   'frame_rate': '29.97',
   'height': 1080,
   'width': 1920},
  {'file_size': 11551183,
   'file_url': 'https://media.stsci.edu/uploads/video_file/video_attachment/4697/STScI-H-MWC_2x-1920x1080.mp4',
   'format': 'MPEG-4 (H.264)',
   'frame_rate': '29.97',
   'height': 1080,
   'width': 1920},
  {'file_size': 8758378,
   'file_url': 'https://media.stsci.edu/uploads/video_file/video_attachment/4692/STScI-H-MWC_1x-1280x720.mp4',
   'format': 'MPEG-4 (H.264)',
   'frame_rate': '29.97',
   'height': 720,
   'width': 1280},
  {'file_size': 5539118,
   'file_url': 'https://media.stsci.edu/uploads/video_file/video_attachment/4696/STScI-H-MWC_2x-1280x720.mp4',
   'format': 'MPEG-4 (H.264)',
   'frame_rate': '29.97',
   'height': 720,
   'width': 1280},
  {'file_size': 2908461,
   'file_url': 'https://media.stsci.edu/uploads/video_file/video_attachment/4691/STScI-H-MWC_1x-640x360.mp4',
   'format': 'MPEG-4 (H.264)',
   'frame_rate': '29.97',
   'height': 360,
   'width': 640},
  {'file_size': 1803284,
   'file_url': 'https://media.stsci.edu/uploads/video_file/video_attachment/4695/STScI-H-MWC_2x-640x360.mp4',
   'format': 'MPEG-4 (H.264)',
   'frame_rate': '29.97',
   'height': 360,
   'width': 640}],
 'youtube_id': 'mUQ0yl0w0iQ'}
~~~


## Notes

Please note I am in no way affiliated with the HubbleSite, I simply found the content and the API interesting so I 
wanted to write an API wrapper to hopefully increase awareness and get others excited about space and astronomy! 