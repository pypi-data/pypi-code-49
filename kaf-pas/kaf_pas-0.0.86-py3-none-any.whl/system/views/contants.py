from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.system.models.contants import ContantsManager, Contants


@JsonResponseWithException()
def Contants_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Contants.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=ContantsManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Contants_Add(request):
    return JsonResponse(DSResponseAdd(data=Contants.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Contants_Update(request):
    return JsonResponse(DSResponseUpdate(data=Contants.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)

@JsonResponseWithException()
def Contants_RefreshMatView(request):
    return JsonResponse(DSResponseUpdate(data=Contants.objects.refreshMatViewFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Contants_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Contants.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)\

@JsonResponseWithException()
def Contants_fixed_num_in_operations(request):
    return JsonResponse(DSResponse(request=request, data=Contants.objects.fixed_num_in_operationsFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Contants_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Contants.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Contants_Info(request):
    return JsonResponse(DSResponse(request=request, data=Contants.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Contants_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Contants.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
