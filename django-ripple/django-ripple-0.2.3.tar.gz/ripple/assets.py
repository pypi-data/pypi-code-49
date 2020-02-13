
from .models import ImageAsset, Article, ArticleCollection, ArticleOrder
from .models import ArticleCollectionOrder, RichTextAsset, TextAsset
from .serializers import RichTextAssetSerializerB, ImageAssetSerializerB, TextAssetSerializerB
from .serializers import ArticleSerializerB, ArticleCollectionSerializerB
from django.db.models import Max, F, OuterRef, Subquery, Q

import datetime
from django.utils import timezone


def get_assets(module, version=None, user=None, update=False):

    if not version:
        version=timezone.now().strftime("%Y-%m-%dT%H:%M:%S%fZ")

    version_dt = datetime.datetime.strptime(version, "%Y-%m-%dT%H:%M:%S%fZ")
    version_dt = timezone.make_aware(version_dt)

    filter = []

    filter.append(Q(module=module))

    if user and (user.is_superuser or user.is_staff) :
        filter.append(Q(owner=user.id) | Q(published=True))
    else:
        filter.append(Q(published=True))

    assets = {'version': version, 'module': module,
              'is_admin': user and user.is_superuser,
              'userid': (user and user.id) or -1}

    #images

    latest = ImageAsset.objects.filter(*filter).filter(assetid=OuterRef('assetid')).order_by('-updated_at')
    os = ImageAsset.objects.filter(*filter).filter(id=Subquery(latest.values('id')[:1]))
    s = ImageAssetSerializerB(os, many=True)
    assets['images'] = s.data

    # #text

    latest = TextAsset.objects.filter(*filter).filter(assetid=OuterRef('assetid')).order_by('-updated_at')
    os = TextAsset.objects.filter(*filter).filter(id=Subquery(latest.values('id')[:1]))
    s = TextAssetSerializerB(os, many=True)
    assets['text'] = s.data

    #richtext

    latest = RichTextAsset.objects.filter(*filter).filter(assetid=OuterRef('assetid')).order_by('-updated_at')
    os = RichTextAsset.objects.filter(*filter).filter(id=Subquery(latest.values('id')[:1]))
    s = RichTextAssetSerializerB(os, many=True)
    assets['richtext'] = s.data

    #articles

    os = Article.objects.filter(*filter)
    s = ArticleSerializerB(os, many=True)
    assets['articles'] = s.data

    #article collections
    # this will need to be in order

    article_collections = []

    os = ArticleCollection.objects.filter(*filter)
    for a in os:
        s = ArticleCollectionSerializerB(a)
        ac = s.data

        items = []

        a_orders = {}
        ac_orders = {}

        for ao in a.articles.filter(*filter):
            orders = ArticleOrder.objects.filter(article=ao.id, article_collection=a.id)
            order = orders[0].order
            key = "%d:%d" % (ao.id, a.id)
            if len(orders) > 0:
                if key not in a_orders:
                    a_orders[key] = 0
                order = orders[a_orders[key]].order
                a_orders[key] += 1

            items.append({'order': order, 'type': 'article', 'assetid': ao.assetid, 'id': ao.id})

        for aci in a.article_collections.filter(*filter):
            orders = ArticleCollectionOrder.objects.filter(container_article_collection=a.id, article_collection=aci.id)
            order = orders[0].order
            key = "%d:%d" % (a.id, aci.id)
            if len(orders) > 0:
                if key not in ac_orders:
                    ac_orders[key] = 0
                order = orders[ac_orders[key]].order
                ac_orders[key] += 1

            items.append({'order': order, 'type': 'article_collection', 'assetid': aci.assetid, 'id': aci.id})

        items.sort(key=lambda a: a['order'])
        ac['items'] = items
        article_collections.append(ac)

    assets['article_collections'] = article_collections

    return assets

