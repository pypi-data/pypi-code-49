from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.planing.models.operation_locations import Operation_locations, Operation_locationsManager


@JsonResponseWithException()
def Operation_locations_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Operation_locations.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Operation_locationsManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_locations_Add(request):
    return JsonResponse(DSResponseAdd(data=Operation_locations.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_locations_Update(request):
    return JsonResponse(DSResponseUpdate(data=Operation_locations.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_locations_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Operation_locations.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_locations_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Operation_locations.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_locations_Info(request):
    return JsonResponse(DSResponse(request=request, data=Operation_locations.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_locations_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Operation_locations.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
