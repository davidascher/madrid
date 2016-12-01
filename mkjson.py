# this will make the JSON file off of the Google Drive file structure (synced to a local filesystem)
import os, pprint, json, sys

PLACESDIR = "/Users/da/Google Drive/Places"

bigdata = {}

def escapeSpaces(words):
  return [word.replace(' ', '+') for word in words]

def filter_junk(alist):
  return [thing for thing in alist if (
    not os.path.basename(thing).startswith('.')
    and not os.path.basename(thing).startswith('Icon')) ]

def process_photos(placename, timestamp):
  thedir = os.path.join(PLACESDIR, placename, timestamp, 'PHOTOS') 
  files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(thedir) for f in filenames]
  photonames = [f[len(PLACESDIR)+1:] for f in filter_junk(files)]
  photonames = escapeSpaces(photonames)
  bigdata[placename]['photos']['urls'].extend(photonames)
  bigdata[placename]['photos']['size'] = len(photonames)


def process_audios(placename, timestamp):
  thedir = os.path.join(PLACESDIR, placename, timestamp, 'AUDIO') 
  languages = filter_junk(os.listdir(thedir))
  for language in languages:
    languagedir = os.path.normpath(os.path.join(PLACESDIR, placename, timestamp, 'AUDIO', language))
    if os.path.isdir(languagedir):
      audios = [os.path.normpath(os.path.join(languagedir, f)) for f in filter_junk(os.listdir(languagedir))]
      audios = [f[len(PLACESDIR)+1:] for f in audios]
      bigdata[placename]['audios'][language].extend(audios)
      bigdata[placename]['audios']['size'] += len(audios)
    
def process_videos(placename, timestamp):
  thedir = os.path.join(PLACESDIR, placename, timestamp, 'VIDEO') 
  photonames = filter_junk(os.listdir(thedir))
  bigdata[placename]['videos']['urls'].extend(photonames)
  bigdata[placename]['videos']['size'] = len(photonames)


def exploretimestamp(placename, timestamp):
  for filetype in filter_junk(os.listdir(os.path.join(PLACESDIR, placename, timestamp))):
    print >> sys.stderr, filetype
    if filetype == "AUDIO":
      process_audios(placename, timestamp)
    elif filetype == "VIDEO":
      process_videos(placename, timestamp)
    elif filetype == "PHOTOS":
      process_photos(placename, timestamp)
  

def mkplace(placename):
  bigdata[placename] = {
    'name': placename,
    'photos': {'name': 'photos', 'size': 0, 'urls': []},
    'videos': {'name': 'videos', 'size': 0, 'urls': []},
    'audios': {'name': 'audios', 'size': 0, 'ENGLISH': [], 'SPANISH': []}
  }
  print >> sys.stderr, placename
  for timestamp in filter_junk(os.listdir(os.path.join(PLACESDIR, placename))):
    if timestamp.startswith('photos to print'): continue
    if not os.path.isdir(os.path.join(PLACESDIR, placename, timestamp)): continue
    exploretimestamp(placename, timestamp)
    return {'name': placename.split(' - ')[0],
      'children': [
        bigdata[placename]['photos'],
        bigdata[placename]['audios'],
        bigdata[placename]['videos']
      ]
    }
    # return bigdata[placename]
  # # photos = find_photos(os.path.join(PLACESDIR, '') 
  # place = {
  #   name: placename,
  #   photos: photos,
  #   audios: audios,
  #   videos: videos
  # }

stuff = []
places = os.listdir(os.path.abspath(PLACESDIR))
for place in places:
  if place.startswith('.'): continue
  if place.startswith("EXAMPLE"): continue
  if place.startswith("Icon"): continue
  stuff.append(mkplace(place))

jsonblob = {
    "name": "Madrid",
    "children": stuff
}


print json.dumps(jsonblob, sort_keys=True, indent=4, separators=(',', ': '))
