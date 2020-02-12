from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.production.models.launch_item_line_view import Launch_item_line_view, Launch_item_line_viewManager


@JsonResponseWithException()
def Launch_item_line_view_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Launch_item_line_view.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Launch_item_line_viewManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_item_line_view_Add(request):
    return JsonResponse(DSResponseAdd(data=Launch_item_line_view.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_item_line_view_Update(request):
    return JsonResponse(DSResponseUpdate(data=Launch_item_line_view.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_item_line_view_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Launch_item_line_view.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_item_line_view_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Launch_item_line_view.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_item_line_view_Info(request):
    return JsonResponse(DSResponse(request=request, data=Launch_item_line_view.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Launch_item_line_view_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Launch_item_line_view.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
