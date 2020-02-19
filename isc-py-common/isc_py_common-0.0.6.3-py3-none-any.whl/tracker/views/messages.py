from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from tracker.models.messages import Messages, MessagesManager


@JsonResponseWithException(printing=False)
def Messages_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Messages.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=MessagesManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Messages_Add(request):
    return JsonResponse(DSResponseAdd(data=Messages.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Messages_Add_Auto_Error(request):
    return JsonResponse(DSResponseAdd(data=Messages.objects.createAutoErrorFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Messages_Update(request):
    return JsonResponse(DSResponseUpdate(data=Messages.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Messages_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Messages.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Messages_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Messages.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException(printing=False)
def Messages_Info(request):
    return JsonResponse(DSResponse(request=request, data=Messages.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)
