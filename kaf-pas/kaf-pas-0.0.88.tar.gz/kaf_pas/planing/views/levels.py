from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.planing.models.levels import Levels, LevelsManager


@JsonResponseWithException()
def Levels_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Levels.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=LevelsManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Levels_Add(request):
    return JsonResponse(DSResponseAdd(data=Levels.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Levels_Update(request):
    return JsonResponse(DSResponseUpdate(data=Levels.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Levels_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Levels.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Levels_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Levels.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Levels_Info(request):
    return JsonResponse(DSResponse(request=request, data=Levels.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Levels_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Levels.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
