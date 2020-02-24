from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.input.models.users_ex import Users_ex, Users_exManager


@JsonResponseWithException()
def Users_ex_Fetch(request):
    from isc_common.auth.models.user import User
    return JsonResponse(
        DSResponse(
            request=request,
            data=Users_ex.objects.
                select_related().
                exclude(props=User.props.bot).
                get_range_rows1(
                request=request,
                function=Users_exManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Users_ex_Add(request):
    return JsonResponse(DSResponseAdd(data=Users_ex.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Users_ex_Update(request):
    return JsonResponse(DSResponseUpdate(data=Users_ex.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Users_ex_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Users_ex.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Users_ex_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Users_ex.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Users_ex_Info(request):
    return JsonResponse(DSResponse(request=request, data=Users_ex.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Users_ex_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Users_ex.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
