import logging

from django.forms import model_to_dict

from isc_common.http.DSRequest import DSRequest
from kaf_pas.ckk.models.locations import Locations
from kaf_pas.planing.models.operations_view import Operations_view, Operations_viewManager, Operations_viewQuerySet

logger = logging.getLogger(__name__)


class RoutingQuerySet(Operations_viewQuerySet):
    def raw(self, raw_query=None, params=None, translations=None, using=None, function=None):
        if raw_query == None:
            raw_query = '''select *
                                    from (with r as (select distinct pr."id",
                                                         pr."child_id",
                                                         null::bigint "parent_id",
                                                         pr."date",
                                                         pr."deleted_at",
                                                         pr."editing",
                                                         pr."deliting",
                                                         pr."lastmodified",
                                                         pr."opertype_id",
                                                         pr."status_id",
                                                         pr."description",
                                                         pr."value_id",
                                                         pr."item_id",
                                                         pr."item_full_name",
                                                         pr."launch_id",
                                                         pr."color_id",
                                                         pr."creator_id",
                                                         pr."operation_level_id",
                                                         pr."operation_level_code",
                                                         pr."operation_level_name",
                                                         pr."resource_id",
                                                         pr."resource_location_id",
                                                         pr."resource_name",
                                                         0 as "props",
                                                         pr."production_operation_id",
                                                         pr."production_operation_num",
                                                         pr."production_operation_qty",
                                                         pr."production_operation_edizm_id",
                                                         pr."mark",
                                                         pr."isFolder"
                                         from planing_operations_view pr
                                                  join planing_operation_resources por on pr.id = por.operation_id
                                                  join production_resource pr1 on por.resource_id = pr1.id
                                         where pr.item_id = %s
                                           and por.resource_id = %s)
                                    
                                          select distinct poi."id",
                                               pr."child_id",
                                               null::bigint as "parent_id",
                                               poi."date",
                                               poi."deleted_at",
                                               poi."editing",
                                               poi."deliting",
                                               poi."lastmodified",
                                               poi."opertype_id",
                                               poi."status_id",
                                               poi."description",
                                               poi."value_id",
                                               poi."item_id",
                                               poi."item_full_name",
                                               poi."launch_id",
                                               poi."color_id",
                                               poi."creator_id",
                                               poi."operation_level_id",
                                               poi."operation_level_code",
                                               poi."operation_level_name",
                                               poi."resource_id",
                                               poi."resource_location_id",
                                               poi."resource_name",
                                               poi."props",
                                               poi."production_operation_id",
                                               poi."production_operation_num",
                                               poi."production_operation_qty",
                                               poi."production_operation_edizm_id",
                                               poi."isFolder",
                                               'income'       as mark
                                        from planing_operations_view pr
                                        left join planing_operations_view poi on pr.parent_id = poi.id
                                        where pr.child_id = (select distinct poi.id
                                                          from planing_operations_view poi
                                                          where poi.item_id = %s
                                                            and poi.opertype_id = %s
                                                            and poi.production_operation_num = (select min(production_operation_num)
                                                                           from planing_operations_view poi
                                                                           where poi.item_id = %s
                                                                             and poi.resource_id = %s
                                                                             and poi.opertype_id = %s
                                                          ))
                                          and pr.props = 2
                                          union
                                          select pr."id",
                                                 pr."child_id",
                                                 pr."parent_id",
                                                 pr."date",
                                                 pr."deleted_at",
                                                 pr."editing",
                                                 pr."deliting",
                                                 pr."lastmodified",
                                                 pr."opertype_id",
                                                 pr."status_id",
                                                 pr."description",
                                                 pr."value_id",
                                                 pr."item_id",
                                                 pr."item_full_name",
                                                 pr."launch_id",
                                                 pr."color_id",
                                                 pr."creator_id",
                                                 pr."operation_level_id",
                                                 pr."operation_level_code",
                                                 pr."operation_level_name",
                                                 pr."resource_id",
                                                 pr."resource_location_id",
                                                 pr."resource_name",
                                                 pr."props",
                                                 pr."production_operation_id",
                                                 pr."production_operation_num",
                                                 pr."production_operation_qty",
                                                 pr."production_operation_edizm_id",
                                                 pr."isFolder",
                                                 'local' as mark
                                          from r pr
                                          union
                                          select pr."id",
                                                 pr."child_id",
                                                 null  as "parent_id",
                                                 pr."date",
                                                 pr."deleted_at",
                                                 pr."editing",
                                                 pr."deliting",
                                                 pr."lastmodified",
                                                 pr."opertype_id",
                                                 pr."status_id",
                                                 pr."description",
                                                 pr."value_id",
                                                 pr."item_id",
                                                 pr."item_full_name",
                                                 pr."launch_id",
                                                 pr."color_id",
                                                 pr."creator_id",
                                                 pr."operation_level_id",
                                                 pr."operation_level_code",
                                                 pr."operation_level_name",
                                                 pr."resource_id",
                                                 pr."resource_location_id",
                                                 pr."resource_name",
                                                 pr."props",
                                                 pr."production_operation_id",
                                                 pr."production_operation_num",
                                                 pr."production_operation_qty",
                                                 pr."production_operation_edizm_id",
                                                 pr."isFolder",
                                                 'outcome'      as mark
                                          from planing_operations_view pr
                                          where parent_id = (select distinct poo.operation_id
                                                             from planing_operation_item poi
                                                                      join planing_operation_operation poo on poi.operation_id = poo.operation_id
                                                                      join planing_operations_view op on poi.operation_id = op.id
                                                             where poi.item_id = %s
                                                               and op.opertype_id = %s
                                                               and poo.num = (select max(production_operation_num)
                                                                              from planing_operations_view poi
                                                                              where poi.item_id = %s
                                                                                and poi.resource_id = %s
                                                                                and poi.opertype_id = %s
                                                             ))
                                            and pr.props = 2) as a
                                    '''

        queryResult = super().raw(raw_query=raw_query, params=params, translations=translations, using=using)
        if function:
            res = [function(record) for record in queryResult]
        else:
            res = [model_to_dict(record) for record in queryResult]
        return res


class RoutingManager(Operations_viewManager):

    @staticmethod
    def getRecord(record):
        return Operations_viewManager.getRecord(record)

    def get_queryset(self):
        return RoutingQuerySet(self.model, using=self._db)

    def fetchLevelsFromRequest(self, request):
        request = DSRequest(request=request)

        launch_id = request.get_data().get('launch_id')
        levels = RoutingManager.make_levels(launch_id=launch_id)
        return levels

    @staticmethod
    def make_levels(launch_id):
        res = [
            dict(
                id=operation.get('operation_level_id'),
                title=operation.get('operation_level__name'),
                prompt=f'''ID: {operation.get('operation_level_id')}, {operation.get('operation_level__code')} : {operation.get('operation_level__name')}'''
            )
            for operation in Operations_view.objects.
                filter(launch_id=launch_id).
                order_by('operation_level__code').
                values('operation_level_id', 'operation_level__name', 'operation_level__code').
                distinct()
        ]
        return res

    def fetchLocationsLevelFromRequest(self, request):
        request = DSRequest(request=request)

        launch_id = request.get_data().get('launch_id')
        level_id = request.get_data().get('level_id')
        levels = RoutingManager.make_locationsLevel(launch_id=launch_id, level_id=level_id)
        return levels

    @staticmethod
    def make_locationsLevel(launch_id, level_id):
        res = sorted([
            dict(
                id=operation.get('resource__location_id'),
                title=Locations.objects.get(id=operation.get('resource__location_id')).full_name,
                # prompt=Locations.objects.get(id=operation.get('resource__location_id')).full_name,
                prompt=f'''ID: {operation.get('resource__location_id')}''',
            )
            for operation in Operations_view.objects.
                filter(launch_id=launch_id, operation_level_id=level_id).
                values('resource__location_id', 'resource__location__name').
                distinct()
        ],
            key=lambda x: x['title'])

        return res

    def fetchResourcesLevelFromRequest(self, request):
        request = DSRequest(request=request)

        launch_id = request.get_data().get('launch_id')
        level_id = request.get_data().get('level_id')
        location_id = request.get_data().get('location_id')
        levels = RoutingManager.make_resourcesLevel(launch_id=launch_id, level_id=level_id, location_id=location_id)
        return levels

    @staticmethod
    def make_resourcesLevel(launch_id, level_id, location_id):
        res = sorted([
            dict(
                id=operation.get('resource_id'),
                title=operation.get('resource__name'),
                prompt=f'''ID: {operation.get('resource_id')}, {operation.get('resource__description')}''',
            )
            for operation in Operations_view.objects.
                filter(launch_id=launch_id, operation_level_id=level_id, resource__location_id=location_id).
                values('resource_id', 'resource__name', 'resource__description').
                distinct()
        ],
            key=lambda x: x['title'])

        return res


class Routing(Operations_view):
    objects = RoutingManager()

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Маршрутизация'
        proxy = True
