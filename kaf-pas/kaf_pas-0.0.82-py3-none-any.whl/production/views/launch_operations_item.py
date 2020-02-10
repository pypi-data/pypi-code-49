from django.db import transaction

from isc_common.http.DSRequest import DSRequest
from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.ckk.models.item import Item
from kaf_pas.production.models.launch_operation_material import Launch_operations_material
from kaf_pas.production.models.launch_operations_item import Launch_operations_item, Launch_operations_itemManager


@JsonResponseWithException()
def Launch_operations_item_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Launch_operations_item.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Launch_operations_itemManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_operations_item_Add(request):
    return JsonResponse(DSResponseAdd(data=Launch_operations_item.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_operations_item_Update(request):
    return JsonResponse(DSResponseUpdate(data=Launch_operations_item.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_operations_item_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Launch_operations_item.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_operations_item_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Launch_operations_item.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_operations_item_Info(request):
    return JsonResponse(DSResponse(request=request, data=Launch_operations_item.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_operations_item_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Launch_operations_item.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)

@JsonResponseWithException()
def Launch_operations_item_CopyOpers(request):
    _request = DSRequest(request=request)
    source = _request.json.get('source')
    destination = _request.json.get('destination')
    res = False

    if source and destination:
        srecords = source.get('records')
        drecord = destination.get('record')
        item = Item.objects.get(id=drecord.get('id'))

        if isinstance(srecords, list) and isinstance(drecord, dict):
            with transaction.atomic():
                for srecord in srecords:
                    old_launch_operations_item = Launch_operations_item.objects.get(id=srecord.get('id'))
                    launch_operations_item, created = Launch_operations_item.objects.get_or_create(
                        item=item,
                        operation=old_launch_operations_item.operation,
                        defaults=dict(
                            ed_izm=old_launch_operations_item.ed_izm,
                            operationitem=old_launch_operations_item.operationitem,
                            qty=old_launch_operations_item.qty,
                            num=old_launch_operations_item.num,
                            description=old_launch_operations_item.description,
                        ))

                    if created:
                        for launch_operation_resources in launch_operation_resources.objects.filter(launch_operationitem=old_launch_operations_item):
                            launch_operation_resources.objects.get_or_create(
                                launch_operationitem=launch_operations_item,
                                operation_resources=launch_operation_resources.operation_resources,
                                resource=launch_operation_resources.resource,
                                location=launch_operation_resources.location
                            )

                        for launch_operation_material in Launch_operations_material.objects.filter(launch_operationitem=old_launch_operations_item):
                            Launch_operations_material.objects.get_or_create(
                                launch_operationitem=launch_operations_item,
                                operation_material=launch_operations_item.operation_material,
                                material=launch_operation_material.material,
                                material_askon=launch_operation_material.material_askon,
                                ed_izm=launch_operation_material.ed_izm,
                                qty=launch_operation_material.qty,
                            )

        return JsonResponse(DSResponse(request=request, status=RPCResponseConstant.statusSuccess).response)
    else:
        raise Exception(f'Копирование не выполнено.')
