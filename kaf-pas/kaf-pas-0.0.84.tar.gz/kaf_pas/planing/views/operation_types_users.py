from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.planing.models.operation_types_users import Operation_types_users, Operation_types_usersManager


@JsonResponseWithException()
def Operation_types_users_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Operation_types_users.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Operation_types_usersManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_types_users_Add(request):
    return JsonResponse(DSResponseAdd(data=Operation_types_users.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_types_users_Update(request):
    return JsonResponse(DSResponseUpdate(data=Operation_types_users.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_types_users_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Operation_types_users.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_types_users_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Operation_types_users.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_types_users_Info(request):
    return JsonResponse(DSResponse(request=request, data=Operation_types_users.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operation_types_users_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Operation_types_users.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
