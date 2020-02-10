from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.planing.models.operation_value import Operation_value, Operation_valueManager


@JsonResponseWithException()
def Operation_value_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Operation_value.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Operation_valueManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_value_Add(request):
    return JsonResponse(DSResponseAdd(data=Operation_value.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_value_Update(request):
    return JsonResponse(DSResponseUpdate(data=Operation_value.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_value_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Operation_value.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_value_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Operation_value.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_value_Info(request):
    return JsonResponse(DSResponse(request=request, data=Operation_value.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_value_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Operation_value.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
