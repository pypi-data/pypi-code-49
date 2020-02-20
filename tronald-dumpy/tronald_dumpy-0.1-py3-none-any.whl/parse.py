import argparse
import json
import datetime
from .api import TronaldDumpAPI
from .api import TronaldDumpResponse


class Parser(TronaldDumpAPI):
    '''Parser class. Provides functionality for retrieving data from JSON objects'''

    def __init__(self, resp):
        self.resp = resp
        self.data = resp.data
        self.url = resp.url

    def printout(self):
        '''Print formatted contents of the JSON file-object'''
        print(json.dumps(self.data, indent=4, sort_keys=True))

    # TAGS

    def tag_value(self):
        '''Retrieve tag(s) value from the given JSON. '''
        value = self.data.get('value')
        if value == "":
            tags = []
            for tag in self.data.get('_embedded').get('tag'):
                tags.append(tag.get('value'))
            return tags
        return value

    # QUOTES

    def value(self):
        '''Retrive quote's value'''
        return self.data.get('value')

    def author(self):
        '''Retrieve quote's author value'''
        author = self.data.get('author')
        if author == "":
            embedded = self.data.get('_embedded')
            return embedded.get('author')
        return author

    def date_appeared(self):
        '''Retrieve the date when quote first appeared at as a datetime object'''
        date_value = self.data.get('appeared_at')
        return datetime.date.fromisoformat(date_value[:10]) 

    def tags(self):
        '''Retrieve all tags for the given quote'''
        return self.data.get('tags')

    def quote_id(self):
        '''Retrieve quote ID'''
        return self.data.get('quote-id')

    def source(self):
        '''Retrieve source of a quote'''
        source = self.data.get('source')
        if source == "":
            embedded = self.data.get('_embedded')
            return embedded.get('source')
        return source

# TODO:
# Search-by-query parsing and pageable output
