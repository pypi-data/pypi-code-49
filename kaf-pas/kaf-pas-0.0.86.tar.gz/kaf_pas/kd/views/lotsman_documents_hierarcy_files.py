from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.kd.models.lotsman_documents_hierarcy_files import Lotsman_documents_hierarcy_files, Lotsman_documents_hierarcy_filesManager


@JsonResponseWithException()
def Lotsman_documents_hierarcy_files_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Lotsman_documents_hierarcy_files.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=Lotsman_documents_hierarcy_filesManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_files_Add(request):
    return JsonResponse(DSResponseAdd(data=Lotsman_documents_hierarcy_files.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_files_Update(request):
    return JsonResponse(DSResponseUpdate(data=Lotsman_documents_hierarcy_files.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_files_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Lotsman_documents_hierarcy_files.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_files_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Lotsman_documents_hierarcy_files.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_files_Info(request):
    return JsonResponse(DSResponse(request=request, data=Lotsman_documents_hierarcy_files.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Lotsman_documents_hierarcy_files_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Lotsman_documents_hierarcy_files.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
