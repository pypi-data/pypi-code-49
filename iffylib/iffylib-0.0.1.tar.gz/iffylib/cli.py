#! /usr/bin/python

import argparse
from iffylib import client
import prettytable
from collections.abc import MutableMapping
import re


class dispatch(object):

    @classmethod
    def search(cls, args):
        g = client.Giphy(args.apikey)
        r = g.api.search(
            args.query, limit=args.limit, offset=args.offset,
            rating=args.rating, lang=args.lang, random_id=args.random_id)
        data = r.json()
        if data.get('meta') and args.debug:
            print(cls._make_table(data['meta']))
        if data.get('pagination'):
            print(cls._make_table(data['pagination']))
        if data.get('data'):
            new_data = []
            for d in data['data']:
                new_data.append(
                    dict(
                        bitly_url=d['bitly_url'],
                        id=d['id'],
                        rating=d['rating'],
                        title=d['title'],
                        type=d['type']
                    ))
            data['data'] = new_data
            print(cls._make_table(data['data']))

    @classmethod
    def get(cls, args):
        g = client.Giphy(args.apikey)
        r = g.api.get(args.id, random_id=args.random_id)
        data = r.json()
        if data.get('meta') and args.debug:
            print(cls._make_table(data['meta']))
        if data.get('data'):
            d=data['data']
            new_data = dict(
                bitly_url=d['bitly_url'],
                id=d['id'],
                rating=d['rating'],
                title=d['title'],
                type=d['type']
            )
            image_data = None
            if args.image_type:
                itype = data['data']['images'][args.image_type]
                image_data = dict(images={args.image_type:itype})
            print(cls._make_table(new_data))
            if image_data:
                print(cls._make_table(image_data))


    @classmethod
    def _parse_datastructure(cls, datastruct):
        # assumes a dict or a list, as returned by json.loads()
        headers = []
        if isinstance(datastruct, list):
            flat_jobj_list = list()
            for item in datastruct:
                flat_jobj = cls._holograph(item)
                flat_jobj_list.append(flat_jobj)
                headers.extend(list(flat_jobj.keys()))
            datastruct = flat_jobj_list
            headers = list(set(headers))
        elif isinstance(datastruct, dict):
            datastruct = cls._holograph(datastruct)
            headers = list(datastruct.keys())
        else:
            raise Exception(
                "Unparseable datastructure, "
                "cannot derive table: {}".format(str(datastruct)))

        return headers, datastruct

    @classmethod
    def _make_table(cls, datastruct):
        # assumes a dict or a list, as returned by json.loads()
        table = prettytable.PrettyTable()
        headers, datastruct = cls._parse_datastructure(datastruct)

        # Alphabetical header sort
        headers = list(set(headers))
        headers.sort()

        # If there's a single `id` field, put that first
        priority_header = [s for s in headers if re.search(r"^\w+\.id$", s)]
        if len(priority_header) == 1:
            priority_header = priority_header[0]
            headers.remove(priority_header)
            headers.insert(0, priority_header)

        table.field_names = headers
        if isinstance(datastruct, list):
            for item in datastruct:
                r = []
                for h in headers:
                    r.append(str(item.get(h)))
                table.add_row(r)
        else:
            r = []
            for h in headers:
                r.append(str(datastruct.get(h)))
            table.add_row(r)

        if len(table._rows) == 0:
            return None

        return table

    @classmethod
    def _holograph(cls, d, parent_key='', sep='.'):
        '''
        recurses through d to create a single flat dictionary where the keys
        are a composite of all the sub-keys the parent dict, separated by 'sep',
        thus representing the multi-dimensional dict as a flat dict.
        '''
        composite_keys = []
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, MutableMapping):
                composite_keys.extend(
                    cls._holograph(v, new_key, sep=sep).items())
            else:
                composite_keys.append((new_key, v))
        return dict(composite_keys)

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('apikey')
    subparsers = parser.add_subparsers()

    search_parser = subparsers.add_parser("search")
    search_parser.set_defaults(func=dispatch.search)
    search_parser.add_argument('query')
    search_parser.add_argument('--limit')
    search_parser.add_argument('--offset')
    search_parser.add_argument('--rating')
    search_parser.add_argument('--lang')
    search_parser.add_argument('--random-id')
    search_parser.add_argument('--debug', action='store_true')

    get_parser = subparsers.add_parser("get")
    get_parser.set_defaults(func=dispatch.get)
    get_parser.add_argument('id')
    get_parser.add_argument('--random-id')
    get_parser.add_argument(
        '--image-type',
        choices=[
        'fixed_height',
        'fixed_height_still',
        'fixed_height_downsampled',
        'fixed_width',
        'fixed_width_still',
        'fixed_width_downsampled',
        'fixed_height_small',
        'fixed_height_small_still',
        'fixed_width_small',
        'fixed_width_small_still',
        'downsized',
        'downsized_still',
        'downsized_large',
        'downsized_medium',
        'downsized_small',
        'original',
        'original_still',
        'looping',
        'preview',
        'preview_gif'])
    get_parser.add_argument('--debug', action='store_true')

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)

if __name__ == "__main__":
    cli()
