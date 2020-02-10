from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.sales.models.precent_types import Precent_types, Precent_typesManager


@JsonResponseWithException()
def Precent_types_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Precent_types.objects.
                select_related('precent_item_type').
                get_range_rows1(
                request=request,
                function=Precent_typesManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Precent_types_Add(request):
    return JsonResponse(DSResponseAdd(data=Precent_types.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Precent_types_Update(request):
    return JsonResponse(DSResponseUpdate(data=Precent_types.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Precent_types_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Precent_types.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Precent_types_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Precent_types.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Precent_types_Info(request):
    return JsonResponse(DSResponse(request=request, data=Precent_types.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Precent_types_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Precent_types.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
