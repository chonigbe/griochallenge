#!/usr/bin/python
import re
import sys
import time
import httplib

import requests

"""codingchallenge.py: All functional code for the Grio Coding Challenge."""

__author__      = "Celia Honigberg"


def regular_word(word,charregex,punctation):
  """Takes in a string
  and a regular expression of what characters matter
  and a tuple of ending punctuation marks
  returns a string that is reversed when string has an odd
  number of characters.
  """
  length = len(re.findall(charregex, word))
  if length % 2 != 0:
    if word.endswith(punctation):
      word = (word[length-1::-1] 
      	      + word[length:])
    else:
      word = word[::-1] 
  return word

def is_url(url):
  """Takes in a string
  returns true if the string is a properly formatted url
  """
  return re.match('(^http|https)://([a-z0-9][a-z0-9\-]*\.)+[a-z0-9][a-z0-9\-]*', url)

def is_lat_long(latlong):
  """Takes in a string
  returns true if the string has properly formatted 
  longitude and latitude coordinates
  """
  return re.match('\[ ?\-?[1-9]{1,3}\.[1-9]+\, ?\-?[1-9]{1,3}\.[1-9]+ ?\]?\.'
                  , latlong)

def is_half_lat_long(latlong):
  """Takes in a string
  returns true if the string has properly formatted 
  the first part of the lat long coordinates
  """
  return re.match('\[\-?[1-9]{1,3}\.[1-9]+\,'
                  , latlong)

def is_back_half(latlong):
  """Takes in a string
  returns true if the string has properly formatted 
  the second part of the lat long coordinates
  """
  return re.match('\-?[1-9]{1,3}\.[1-9]+\]?\.'
                  , latlong)

def shorten_url(url):
  """Takes in a url 
  returns the url without https:// or http://
  """
  return url.split('//', 1)[-1]

def get_address(latlong):
  """Takes in longitude and latitude coordinates 
  returns the street address from google maps api. 
  Handles punctuation at the end of words poorly. 
  """
  url = 'http://maps.googleapis.com/maps/api/geocode/json'
  l = latlong.replace(']', '')
  l = l.replace('[', '')
  l = l.replace(' ', '')
  if latlong.endswith(tuple(['.',',',':','?','!'])):
    punc = latlong[-1:]
    l = l[:-1]
    latlong = latlong[:-1]
  else: 
    punc = ''
  mysensor = 'true'
  payload = {'latlng':l, 'sensor':mysensor}
  r = requests.get(url, params=payload)

  json = r.json()
  print json['results'][0]["formatted_address"]
  address = '{} {}, {}, {}'.format(json['results'][0]['address_components'][0]['long_name']
                            , json['results'][0]['address_components'][1]['long_name']
                            , json['results'][0]['address_components'][3]['long_name']
                            , json['results'][0]['address_components'][5]['short_name'])
  return '{}({}){}'.format(latlong,address,punc)

def translate_content(line):
  """Takes in a file
  and prints out each line in the file with some alterrations. 
  """
  current = ''
  l = line.split()
  # only used for avoiding extra spaces
  length = len(l)
  for i, word in enumerate(l):
    if (is_url(word)):
      word = shorten_url(word)
    elif (is_half_lat_long(word)):
      latlong = '{} {}'.format(word,l[i+1])
      if (is_lat_long(latlong)):
        word = get_address(latlong)
    elif (is_back_half(word)):
      word = ''
    else: 
      word = regular_word(word
    	                    , '[a-zA-Z\-]'
    	                    , tuple(['.',',',':','?','!']))
    if (i == length or word == ""):
      current += word
    else: 
      current += word + ' '
  return current

def print_content(file):
  """Takes in a file
  and prints each processed line in the given file.
  """
  with open(file) as f:
    # processes and prints line by line
    for line in f:
      print translate_content(line)

def main():
  print_content('giventest.txt')

if __name__ == "__main__": main()