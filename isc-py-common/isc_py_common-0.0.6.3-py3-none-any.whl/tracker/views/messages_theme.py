from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from tracker.models.messages_theme import Messages_theme, Messages_theme_Manager


@JsonResponseWithException(printing=False, printing_res=False)
def Messages_theme_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Messages_theme.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Messages_theme_Manager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Messages_theme_Add(request):
    return JsonResponse(DSResponseAdd(data=Messages_theme.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Messages_theme_Update(request):
    return JsonResponse(DSResponseUpdate(data=Messages_theme.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Messages_theme_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Messages_theme.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Messages_theme_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Messages_theme.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Messages_theme_Info(request):
    return JsonResponse(DSResponse(request=request, data=Messages_theme.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)
