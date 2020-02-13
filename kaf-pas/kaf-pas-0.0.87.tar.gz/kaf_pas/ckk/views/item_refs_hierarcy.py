from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.ckk.models.item_refs_hierarcy import Item_refs_hierarcyManager, Item_refs_hierarcy


@JsonResponseWithException()
def Item_refs_hierarcy_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Item_refs_hierarcy.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Item_refs_hierarcyManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Item_refs_hierarcy_Add(request):
    return JsonResponse(DSResponseAdd(data=Item_refs_hierarcy.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Item_refs_hierarcy_Update(request):
    return JsonResponse(DSResponseUpdate(data=Item_refs_hierarcy.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Item_refs_hierarcy_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Item_refs_hierarcy.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Item_refs_hierarcy_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Item_refs_hierarcy.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Item_refs_hierarcy_Info(request):
    return JsonResponse(DSResponse(request=request, data=Item_refs_hierarcy.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Item_refs_hierarcy_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Item_refs_hierarcy.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
