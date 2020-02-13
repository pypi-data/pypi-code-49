from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.planing.models.operation_standard_prod import Operation_standard_prod, Operation_standard_prodManager


@JsonResponseWithException()
def Operation_standard_prod_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Operation_standard_prod.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Operation_standard_prodManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_standard_prod_Add(request):
    return JsonResponse(DSResponseAdd(data=Operation_standard_prod.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_standard_prod_Update(request):
    return JsonResponse(DSResponseUpdate(data=Operation_standard_prod.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_standard_prod_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Operation_standard_prod.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_standard_prod_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Operation_standard_prod.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_standard_prod_Info(request):
    return JsonResponse(DSResponse(request=request, data=Operation_standard_prod.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_standard_prod_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Operation_standard_prod.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
