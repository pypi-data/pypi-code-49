from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.production.models.launch_item_refs import Launch_item_refs, Launch_item_refsManager


@JsonResponseWithException()
def Launch_item_refs_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Launch_item_refs.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Launch_item_refsManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_item_refs_Add(request):
    return JsonResponse(DSResponseAdd(data=Launch_item_refs.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_item_refs_Update(request):
    return JsonResponse(DSResponseUpdate(data=Launch_item_refs.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_item_refs_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Launch_item_refs.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_item_refs_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Launch_item_refs.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_item_refs_Info(request):
    return JsonResponse(DSResponse(request=request, data=Launch_item_refs.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_item_refs_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Launch_item_refs.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
