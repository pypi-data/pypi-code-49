import requests
from django.conf import settings
from django.http import HttpResponseRedirect

from isc_common.http.DSRequest import DSRequest
from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from isc_common.management.commands.refresh_mat_views import refresh_mat_view
from kaf_pas.kd.models.lotsman_documents_hierarcy import Lotsman_documents_hierarcy
from kaf_pas.kd.models.lotsman_documents_hierarcy_view import Lotsman_documents_hierarcy_view, Lotsman_documents_hierarcy_viewManager


@JsonResponseWithException()
def Lotsman_documents_hierarcy_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Lotsman_documents_hierarcy_view.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Lotsman_documents_hierarcy_viewManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)

@JsonResponseWithException()
def Lotsman_documents_hierarcy_Fetch1(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Lotsman_documents_hierarcy_view.objects.
                distinct('id').
                get_range_rows1(
                request=request,
                function=Lotsman_documents_hierarcy_viewManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_doc_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Lotsman_documents_hierarcy_view.objects.
                select_related().
                get_range_rows4(
                request=request,
                function=Lotsman_documents_hierarcy_viewManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_Add(request):
    return JsonResponse(DSResponseAdd(data=Lotsman_documents_hierarcy.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_Update(request):
    return JsonResponse(DSResponseUpdate(data=Lotsman_documents_hierarcy.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Lotsman_documents_hierarcy.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Lotsman_documents_hierarcy.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_Info(request):
    return JsonResponse(DSResponse(request=request, data=Lotsman_documents_hierarcy.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Lotsman_documents_hierarcy.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_MakeItem(request):
    return JsonResponse(DSResponse(request=request, data=Lotsman_documents_hierarcy.objects.makeItemFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_ReloadDoc(request):
    ws_channel = request.session.get('ws_channel')
    ws_port = settings.WS_PORT
    host = settings.WS_HOST

    _request = DSRequest(request=request)
    ids = _request.json.get('data')
    ids = ids.get('ids')

    r = requests.get(f'{settings.KOMPAS_INFORMICA}/logic/Lotsman_documents_hierarcy/ReloadDoc', params=dict(ids=ids, port=ws_port, ws_channel=ws_channel, host=host, user_id=_request.user_id))
    HttpResponseRedirect(r.url)
    return JsonResponse(DSResponse(request=request, status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcys_RefreshMView(request):
    refresh_mat_view('kd_lotsman_documents_hierarcy_mview')
    return JsonResponse(DSResponse(request=request, status=RPCResponseConstant.statusSuccess).response)
