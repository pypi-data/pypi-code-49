from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.planing.models.operation_refs import Operation_refs, Operation_refsManager


@JsonResponseWithException()
def Operation_refs_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Operation_refs.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Operation_refsManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_refs_Add(request):
    return JsonResponse(DSResponseAdd(data=Operation_refs.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_refs_Update(request):
    return JsonResponse(DSResponseUpdate(data=Operation_refs.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_refs_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Operation_refs.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_refs_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Operation_refs.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_refs_Info(request):
    return JsonResponse(DSResponse(request=request, data=Operation_refs.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_refs_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Operation_refs.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
