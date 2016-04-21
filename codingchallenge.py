#!/usr/bin/python

##################################################
# Author: Celia Honigberg
# Date: 04/20/16
# Description: Grio Code Challenge
##################################################

# standard library imports
# related third party imports
# local application/library specific imports
import re
import sys
import time
import httplib

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


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
  MORE WORK NEEDED HERE. 
  """
  return re.match('(^http|https)://', url)

def is_lat_long(latlong):
  """Takes in a string
  returns true if the string has properly formatted 
  longitude and latitude coordinates
  """
  return re.match('\[ *[1-9]{2}\.[1-9]+ *\, *[1-9]{2}\.[1-9]+ *\]', latlong)

def shorten_url(url):
  """Takes in a url 
  returns the url without https:// or http://
  """
  return url.split('//', 1)[-1]

def get_address(latlong):
  """Takes in longitude and latitude coordinates 
  returns the street address from google maps api. 
  """
  return 'FML T_____T OTL'

def translate_content(line):
  """Takes in a file
  and prints out each line in the file with some alterrations. 
  """
  current = ''
  for word in line.split():
    if (is_url(word)):
      word = shorten_url(word)
    elif (is_lat_long(word)):
      word = word + ' ' + get_address(word)
    else: 
      word = regular_word(word
    	                    , '[a-zA-Z\-]'
    	                    , tuple(['.',',',':','?','!']))
    # if (at end of line):
    #   current += word
    # else: 
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


# For(all the lines in the file) {
# 	read one line of input file
# 	for (all the words in the line) {
# 		take each word, check if it is a 
# 		1. url (verfication, ignore lat longs in a url regex: http:// or https:// + domain (white list characters?) + . + small number of address characters + and infinite number of /text/text/text) (before you start writing you have to figure out what this is going to involve)
# 		2. lat long (do verification to make sure) regex that handles [+lat+,+long+] and then verify that it's actually a place and then print out its place then print out it. 
# 		3. Check and see if it has an odd number of characters, if it does, reverse it. 
# 		4. If it has an even number of characters, just print it out. 
# 	}
# }

def main():
  start = time.clock()
  print_content('giventest.txt')
  # translate_content('If you want to visit Grio, you can go to \
  #       http://grio.com or visit us at [37.78667, -122.39782]. Thank you.')
  end = time.clock()
  print end - start
  # start = time.clock()
  # translate_content('testlargestring.txt')
  # end = time.clock()
  # print end - start
  # display some lines

if __name__ == "__main__": main()