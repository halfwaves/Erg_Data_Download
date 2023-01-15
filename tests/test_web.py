# -*- coding: utf-8 -*-
import unittest

from context import importscript
from importscript.htmlParse import HTMLParseDammit as pd
import importscript.webHandling as wh
import csv

class htmlParse(unittest.TestCase):
    """Basic test cases."""
    def setUp(self):
        pass
    def generate_parser(self):
        p = pd()
        self.assertTrue(p is not None)
    
    def handle_start(self):
        p = pd()
        tag = 'p'
        at = 'attr'
        p.handle_starttag_list(tag, at)
        self.assertEqual(p.startTags[0], tag)
        self.assertEqual(p.tagAttrs[0], at)
    
    def handle_endtag_list(self):
        p = pd()
        tag = 'e'
        p.handle_endtag(tag)
        self.assertEqual(p.startTags[0], tag)

    def handle_data_list(self):
        p = pd()
        data = 'data'
        self.assertEwual(p.data[0], data)
    
    def feed_only_data(self):
        p = pd()
        p.feed('<h2>Nate Shoemaker</h2>')
        self.assertEqual(p.startTags[0], 'h2')
        self.assertFalse(p.tagAttrs[0])
        self.assertEqual(p.endTags[0], 'h2')
        self.assertEqual(p.data[0], 'Nate Shoemaker', 'incorrect data parse')
    
    def feed_tag_w_attrs(self):
        s = '<input name= "_token" type="hidden" value="test_case"> data </input>'
        attrs = {'name' : "_token", 'type' : 'hidden', 'value' : 'test_case'}
        p = pd()
        p.feed(s)
        self.assertEqual(p.startTags[0], 'input')
        self.assertEqual(p.endTags[0], 'input')
        self.assertDictEqual(p.tagAttrs[0], attrs)

class accessWeb(unittest.TestCase):
    
    def session_generator(self):
        self.assertIsNotNone(wh.startSession())
        
    def internet_connect(self):
        s = wh.startSession()
        r = wh.getReq(s, 'https://www.google.com/')
        self.assertEqual(r.status_code, 200)
     


if __name__ == '__main__':
    unittest.main()