# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals
from .models import DailyLog, Stat
from django.contrib.contenttypes.models import ContentType


def do_daily_stat(the_date, party):
    d = {}
    for l in party.dailylog_dailylogs.filter(the_date=the_date):
        for k, v in l.context.iteritems():
            ps = k.split('.')
            am = (ps[0], ps[1])
            mt = "%s.%s" % (ps[3], ps[4])
            r = d.setdefault(am, {}).setdefault(ps[2], {}).setdefault(mt, {'v': 0, 'u': 0})
            r['u'] += 1
            r['v'] += v
    for am, dam in d.iteritems():
        ct = ContentType.objects.get_by_natural_key(am[0], am[1])
        for oid, doid in dam.iteritems():
            for mt, dmt in doid.iteritems():
                party.dailylog_stats.update_or_create(the_date=the_date, owner_type=ct, owner_id=oid, metics=mt,
                                                      defaults=dict(value=dmt['v'], user_count=dmt['u']))
    return d
