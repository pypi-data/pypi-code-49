from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.planing.models.operation_launches import Operation_launches, Operation_launchesManager


@JsonResponseWithException()
def Operation_launches_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Operation_launches.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Operation_launchesManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_launches_Add(request):
    return JsonResponse(DSResponseAdd(data=Operation_launches.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_launches_Update(request):
    return JsonResponse(DSResponseUpdate(data=Operation_launches.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_launches_ReCalcRoutes(request):
    return JsonResponse(DSResponseUpdate(data=Operation_launches.objects.reCalcRoutesFromRequest(request), status=RPCResponseConstant.statusSuccess).response)\

@JsonResponseWithException()
def Operation_launches_CleanRoutes(request):
    return JsonResponse(DSResponseUpdate(data=Operation_launches.objects.cleanRoutesFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_launches_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Operation_launches.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_launches_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Operation_launches.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_launches_Info(request):
    return JsonResponse(DSResponse(request=request, data=Operation_launches.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_launches_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Operation_launches.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
