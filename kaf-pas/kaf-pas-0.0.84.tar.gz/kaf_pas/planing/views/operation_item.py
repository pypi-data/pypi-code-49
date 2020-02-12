from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.planing.models.operation_item import Operation_item, Operation_itemManager


@JsonResponseWithException()
def Operation_item_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Operation_item.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Operation_itemManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_item_Add(request):
    return JsonResponse(DSResponseAdd(data=Operation_item.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_item_Update(request):
    return JsonResponse(DSResponseUpdate(data=Operation_item.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_item_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Operation_item.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_item_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Operation_item.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_item_Info(request):
    return JsonResponse(DSResponse(request=request, data=Operation_item.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_item_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Operation_item.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
