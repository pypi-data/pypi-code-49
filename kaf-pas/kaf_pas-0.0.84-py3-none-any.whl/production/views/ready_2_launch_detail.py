from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.production.models.ready_2_launch_detail import Ready_2_launch_detail, Ready_2_launch_detailManager


@JsonResponseWithException()
def Ready_2_launch_detail_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Ready_2_launch_detail.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Ready_2_launch_detailManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Ready_2_launch_detail_Add(request):
    return JsonResponse(DSResponseAdd(data=Ready_2_launch_detail.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Ready_2_launch_detail_Update(request):
    return JsonResponse(DSResponseUpdate(data=Ready_2_launch_detail.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Ready_2_launch_detail_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Ready_2_launch_detail.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Ready_2_launch_detail_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Ready_2_launch_detail.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Ready_2_launch_detail_Info(request):
    return JsonResponse(DSResponse(request=request, data=Ready_2_launch_detail.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Ready_2_launch_detail_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Ready_2_launch_detail.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
