from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.accounting.models.buffers import Buffers, BuffersManager


@JsonResponseWithException()
def Buffers_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Buffers.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=BuffersManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Buffers_Add(request):
    return JsonResponse(DSResponseAdd(data=Buffers.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Buffers_Update(request):
    return JsonResponse(DSResponseUpdate(data=Buffers.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Buffers_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Buffers.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Buffers_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Buffers.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Buffers_Info(request):
    return JsonResponse(DSResponse(request=request, data=Buffers.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Buffers_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Buffers.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
