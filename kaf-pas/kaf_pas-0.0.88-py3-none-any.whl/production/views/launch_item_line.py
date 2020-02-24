from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.production.models.launch_item_line import Launch_item_line, Launch_item_lineManager


@JsonResponseWithException()
def Launch_item_line_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Launch_item_line.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Launch_item_lineManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_item_line_Add(request):
    return JsonResponse(DSResponseAdd(data=Launch_item_line.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_item_line_Update(request):
    return JsonResponse(DSResponseUpdate(data=Launch_item_line.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_item_line_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Launch_item_line.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_item_line_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Launch_item_line.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_item_line_Info(request):
    return JsonResponse(DSResponse(request=request, data=Launch_item_line.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_item_line_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Launch_item_line.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
