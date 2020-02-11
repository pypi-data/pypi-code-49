from isc_common.http.DSRequest import DSRequest
from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.accounting.models.tmp_buffer import Tmp_buffer, Tmp_bufferManager


@JsonResponseWithException()
def Tmp_buffer_off_Fetch(request):
    from kaf_pas.accounting.models.buffers import Buffers

    req = DSRequest(request=request)
    Tmp_buffer.objects.filter(user=req.user).delete()
    for buffers in Buffers.objects.all():
        Tmp_buffer.objects.create(
            item=buffers.item,
            location=buffers.location,
            color=buffers.color,
            edizm=buffers.edizm,
            value=buffers.value,
            user=req.user,
        )

    return JsonResponse(
        DSResponse(
            request=request,
            data=Tmp_buffer.objects.
                filter(user=req.user).
                select_related().
                get_range_rows1(
                request=request,
                function=Tmp_bufferManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Tmp_buffer_off_Add(request):
    return JsonResponse(DSResponseAdd(data=Tmp_buffer.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Tmp_buffer_off_Update(request):
    return JsonResponse(DSResponseUpdate(data=Tmp_buffer.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Tmp_buffer_off_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Tmp_buffer.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Tmp_buffer_off_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Tmp_buffer.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Tmp_buffer_off_Info(request):
    return JsonResponse(DSResponse(request=request, data=Tmp_buffer.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Tmp_buffer_off_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Tmp_buffer.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
