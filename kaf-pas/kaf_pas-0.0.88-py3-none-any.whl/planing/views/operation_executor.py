from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.planing.models.operation_executor import Operation_executor, Operation_executorManager


@JsonResponseWithException()
def Operation_executor_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Operation_executor.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Operation_executorManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_executor_Add(request):
    return JsonResponse(DSResponseAdd(data=Operation_executor.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_executor_Update(request):
    return JsonResponse(DSResponseUpdate(data=Operation_executor.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_executor_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Operation_executor.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_executor_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Operation_executor.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_executor_Info(request):
    return JsonResponse(DSResponse(request=request, data=Operation_executor.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_executor_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Operation_executor.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
