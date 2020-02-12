from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.planing.models.status_operation_types import Status_operation_types, Status_operation_typesManager


@JsonResponseWithException()
def Status_operation_types_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Status_operation_types.objects.
                filter().
                get_range_rows1(
                request=request,
                function=Status_operation_typesManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Status_operation_types_Add(request):
    return JsonResponse(DSResponseAdd(data=Status_operation_types.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Status_operation_types_Update(request):
    return JsonResponse(DSResponseUpdate(data=Status_operation_types.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Status_operation_types_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Status_operation_types.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Status_operation_types_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Status_operation_types.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Status_operation_types_Info(request):
    return JsonResponse(DSResponse(request=request, data=Status_operation_types.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Status_operation_types_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Status_operation_types.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
