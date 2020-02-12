from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.production.models.launch_operation_material import Launch_operations_materialManager, Launch_operations_material


@JsonResponseWithException()
def Launch_operations_material_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Launch_operations_material.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Launch_operations_materialManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_operations_material_Add(request):
    return JsonResponse(DSResponseAdd(data=Launch_operations_material.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_operations_material_Update(request):
    return JsonResponse(DSResponseUpdate(data=Launch_operations_material.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_operations_material_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Launch_operations_material.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_operations_material_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Launch_operations_material.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_operations_material_Info(request):
    return JsonResponse(DSResponse(request=request, data=Launch_operations_material.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_operations_material_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Launch_operations_material.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
