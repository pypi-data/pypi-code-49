from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.planing.models.operation_level import Operation_level, Operation_levelManager


@JsonResponseWithException()
def Operation_level_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Operation_level.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Operation_levelManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_level_Add(request):
    return JsonResponse(DSResponseAdd(data=Operation_level.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_level_Update(request):
    return JsonResponse(DSResponseUpdate(data=Operation_level.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_level_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Operation_level.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_level_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Operation_level.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_level_Info(request):
    return JsonResponse(DSResponse(request=request, data=Operation_level.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_level_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Operation_level.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
