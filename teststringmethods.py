#!/usr/bin/python

import unittest

import codingchallenge as cc

"""codingchallenge.py: All functional code for the Grio Coding Challenge."""

__author__      = "Celia Honigberg"

class TestStringMethods(unittest.TestCase):

  def test_regular_word(self):
    # Test even word
    self.assertEqual(cc.regular_word('word', '[a-zA-Z\-]'
                                 , tuple(['.',',',':','?']))
                                 , 'word')
    # Test odd word
    self.assertEqual(cc.regular_word('words', '[a-zA-Z\-]'
                                 , tuple(['.',',',':','?']))
                                 , 'sdrow')
    # Test odd word with punctionation
    self.assertEqual(cc.regular_word('words!', '[a-zA-Z\-]'
                                 , tuple(['.',',',':','?','!']))
                                 , 'sdrow!')

  def test_is_url(self):
    # general domain http
    self.assertTrue(cc.is_url('http://grio.com'),1)
    # general domain https
    self.assertTrue(cc.is_url('https://grio.com'),1)
    # domain + path 
    self.assertTrue(cc.is_url('http://hammerfishslap.tumblr.com'),1)
    # has a path after the .com
    self.assertTrue(cc.is_url('http://grio.com/portfolio'),1)
    # not well formed, no dot anything
    self.assertFalse(cc.is_url('http://grio/portfolio'),1)

  def test_shorten_url(self):
    # general domain http
    self.assertTrue(cc.shorten_url('http://grio.com'),'grio.com')
    # general domain https
    self.assertTrue(cc.shorten_url('https://grio.com'),'grio.com')
    # domain + path 
    self.assertTrue(cc.shorten_url('http://hammerfishslap.tumblr.com'),'hammerfishslap.tumblr.com')
    # has a path after the .com
    self.assertTrue(cc.shorten_url('http://grio.com/portfolio'),'grio.com/portfolio')
    # has a path after the .com
    self.assertTrue(cc.shorten_url('http://grio.com//portfolio'),'grio.com//portfolio')
    # not well formed, no dot anything
    self.assertFalse(cc.is_url('http://grio/portfolio'),1)
    # not a real url 
    #self.assertFalse(cc.is_url('http://portfoliogrio.com/'),1)'

  def test_is_lat_long(self):
    # general false test
    self.assertFalse(cc.is_lat_long('32987.89373'),1)
    # general true test
    self.assertTrue(cc.is_lat_long('[45.4379,32.487932]'),1)
    # general false test 
    self.assertFalse(cc.is_lat_long('[ 45.4379, 32. ]'),1)
    # general true test
    self.assertTrue(cc.is_lat_long('[ 45.4, 32.4 ]'),1)

if __name__ == '__main__':
  unittest.main()
