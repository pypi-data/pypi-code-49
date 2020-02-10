from django.conf import settings

from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.planing.models.operations import Operations
from kaf_pas.planing.models.operations_view import Operations_viewManager
from kaf_pas.planing.models.write_off_items import Write_off_items


@JsonResponseWithException()
def Write_off_items_Fetch(request):
    opers_types = [
        settings.OPERS_TYPES_STACK.WRITE_OFF_TASK.id,
        settings.OPERS_TYPES_STACK.WRITE_DETAIL_OFF_TASK.id
    ]

    return JsonResponse(
        DSResponse(
            request=request,
            data=Write_off_items.objects.
                filter(opertype__in=opers_types).
                select_related().
                get_range_rows1(
                request=request,
                function=Operations_viewManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Write_off_items_Add(request):
    return JsonResponse(DSResponseAdd(data=Write_off_items.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Write_off_items_Update(request):
    return JsonResponse(DSResponseUpdate(data=Operations.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Write_off_items_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Operations.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Write_off_items_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Write_off_items.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Write_off_items_Info(request):
    return JsonResponse(DSResponse(request=request, data=Write_off_items.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Write_off_items_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Write_off_items.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
