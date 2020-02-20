#! /usr/bin/env python3

from mdstat_influx.mdstat_influx import MdData

if __name__ == '__main__':
    md = MdData()
    print(md.get_messages())
