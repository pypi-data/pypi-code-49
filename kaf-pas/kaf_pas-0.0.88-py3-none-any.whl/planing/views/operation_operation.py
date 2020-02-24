from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.planing.models.operation_operation import Operation_operation, Operation_operationManager


@JsonResponseWithException()
def Operation_operation_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Operation_operation.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Operation_operationManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_operation_Add(request):
    return JsonResponse(DSResponseAdd(data=Operation_operation.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_operation_Update(request):
    return JsonResponse(DSResponseUpdate(data=Operation_operation.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_operation_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Operation_operation.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_operation_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Operation_operation.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_operation_Info(request):
    return JsonResponse(DSResponse(request=request, data=Operation_operation.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_operation_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Operation_operation.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
