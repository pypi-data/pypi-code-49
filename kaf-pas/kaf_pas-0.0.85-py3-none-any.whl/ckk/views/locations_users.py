from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.ckk.models.locations_users import Locations_users, Locations_usersManager


@JsonResponseWithException()
def Locations_users_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Locations_users.objects.
                select_related('user', 'location').
                get_range_rows1(
                request=request,
                function=Locations_usersManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Locations_users_Add(request):
    return JsonResponse(DSResponseAdd(data=Locations_users.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Locations_users_Update(request):
    return JsonResponse(DSResponseUpdate(data=Locations_users.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Locations_users_CopyUsers(request):
    return JsonResponse(DSResponseUpdate(data=Locations_users.objects.copyUsersFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Locations_users_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Locations_users.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Locations_users_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Locations_users.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Locations_users_Info(request):
    return JsonResponse(DSResponse(request=request, data=Locations_users.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Locations_users_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Locations_users.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
