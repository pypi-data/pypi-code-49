from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.production.models.ready_2_launch import Ready_2_launch, Ready_2_launchManager


@JsonResponseWithException()
def Ready_2_launch_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Ready_2_launch.objects.
                filter().
                get_range_rows1(
                request=request,
                function=Ready_2_launchManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Ready_2_launch_Add(request):
    return JsonResponse(DSResponseAdd(data=Ready_2_launch.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Ready_2_launch_Update(request):
    return JsonResponse(DSResponseUpdate(data=Ready_2_launch.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Ready_2_launch_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Ready_2_launch.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Ready_2_launch_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Ready_2_launch.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Ready_2_launch_Info(request):
    return JsonResponse(DSResponse(request=request, data=Ready_2_launch.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Ready_2_launch_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Ready_2_launch.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
