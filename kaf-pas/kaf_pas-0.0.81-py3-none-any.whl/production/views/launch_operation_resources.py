from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.production.models.launch_operation_resources import Launch_operation_resources, Launch_operation_resourcesManager


@JsonResponseWithException()
def Launch_operation_resources_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Launch_operation_resources.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Launch_operation_resourcesManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_operation_resources_Add(request):
    return JsonResponse(DSResponseAdd(data=Launch_operation_resources.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_operation_resources_Update(request):
    return JsonResponse(DSResponseUpdate(data=Launch_operation_resources.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_operation_resources_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Launch_operation_resources.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_operation_resources_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Launch_operation_resources.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_operation_resources_Info(request):
    return JsonResponse(DSResponse(request=request, data=Launch_operation_resources.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_operation_resources_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Launch_operation_resources.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
