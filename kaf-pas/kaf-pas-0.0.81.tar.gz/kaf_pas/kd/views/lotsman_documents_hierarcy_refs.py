from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.kd.models.lotsman_documents_hierarcy_refs import Lotsman_documents_hierarcy_refs, Lotsman_documents_hierarcy_refsManager


@JsonResponseWithException()
def Lotsman_documents_hierarcy_refs_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Lotsman_documents_hierarcy_refs.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Lotsman_documents_hierarcy_refsManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_refs_Add(request):
    return JsonResponse(DSResponseAdd(data=Lotsman_documents_hierarcy_refs.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_refs_Update(request):
    return JsonResponse(DSResponseUpdate(data=Lotsman_documents_hierarcy_refs.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_refs_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Lotsman_documents_hierarcy_refs.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_refs_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Lotsman_documents_hierarcy_refs.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_refs_Info(request):
    return JsonResponse(DSResponse(request=request, data=Lotsman_documents_hierarcy_refs.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_refs_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Lotsman_documents_hierarcy_refs.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
