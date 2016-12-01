import json, urllib, urlparse, os, urllib2, datetime, pprint
from bs4 import BeautifulSoup
import random
import sys
orgs = []
methods = []
cases = []

for thing in json.loads(open('./organizations.json').read()):
  thing = {
    'name': thing.get('title_en', ''),
    'children': [],
    'size': random.randint(10,50)
  }
  orgs.append(thing)

for thing in json.loads(open('./methods.json').read()):
  thing = {
    'name': thing.get('title_en', ''),
    'children': [],
    'size': random.randint(10,50)
  }
  methods.append(thing)

for thing in json.loads(open('./cases.json').read()):
  thing = {
    'name': thing.get('title_en', ''),
    'children': [],
    'size': random.randint(10,50)
  }
  cases.append(thing)

pp = {
  'name': 'Participedia',
  'children': [
    {
      'name': 'Organizations',
      'children': orgs
    },
    {
      'name': 'Methods',
      'children': methods
    },
    {
      'name': 'Cases',
      'children': cases
    },
  ]
}

print json.dumps(pp, sort_keys=True, indent=4, separators=(',', ': '))
# pprint.pprint(orgs)
