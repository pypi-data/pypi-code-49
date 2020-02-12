from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.production.models.resource_users import Resource_users, Resource_usersManager


@JsonResponseWithException()
def Resource_users_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Resource_users.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Resource_usersManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Resource_users_Add(request):
    return JsonResponse(DSResponseAdd(data=Resource_users.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Resource_users_Update(request):
    return JsonResponse(DSResponseUpdate(data=Resource_users.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Resource_users_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Resource_users.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Resource_users_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Resource_users.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Resource_users_Info(request):
    return JsonResponse(DSResponse(request=request, data=Resource_users.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Resource_users_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Resource_users.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
