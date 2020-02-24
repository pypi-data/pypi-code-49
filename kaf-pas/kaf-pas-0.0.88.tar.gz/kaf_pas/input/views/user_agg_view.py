from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.input.models.user_agg_view import User_agg_view, User_agg_viewManager


@JsonResponseWithException()
def User_agg_view_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=User_agg_view.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=User_agg_viewManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def User_agg_view_Add(request):
    return JsonResponse(DSResponseAdd(data=User_agg_view.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def User_agg_view_Update(request):
    return JsonResponse(DSResponseUpdate(data=User_agg_view.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def User_agg_view_Remove(request):
    return JsonResponse(DSResponse(request=request, data=User_agg_view.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def User_agg_view_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=User_agg_view.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def User_agg_view_Info(request):
    return JsonResponse(DSResponse(request=request, data=User_agg_view.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def User_agg_view_Copy(request):
    return JsonResponse(DSResponse(request=request, data=User_agg_view.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
