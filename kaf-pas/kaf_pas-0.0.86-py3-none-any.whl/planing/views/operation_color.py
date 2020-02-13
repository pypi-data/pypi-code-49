from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.planing.models.operation_color import Operation_color, Operation_colorManager


@JsonResponseWithException()
def Operation_color_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Operation_color.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Operation_colorManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_color_Add(request):
    return JsonResponse(DSResponseAdd(data=Operation_color.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_color_Update(request):
    return JsonResponse(DSResponseUpdate(data=Operation_color.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_color_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Operation_color.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_color_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Operation_color.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_color_Info(request):
    return JsonResponse(DSResponse(request=request, data=Operation_color.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_color_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Operation_color.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
