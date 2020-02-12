"""
Main interface for appmesh service type definitions.

Usage::

    from mypy_boto3.appmesh.type_defs import ClientCreateMeshResponsemeshmetadataTypeDef

    data: ClientCreateMeshResponsemeshmetadataTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientCreateMeshResponsemeshmetadataTypeDef",
    "ClientCreateMeshResponsemeshspecegressFilterTypeDef",
    "ClientCreateMeshResponsemeshspecTypeDef",
    "ClientCreateMeshResponsemeshstatusTypeDef",
    "ClientCreateMeshResponsemeshTypeDef",
    "ClientCreateMeshResponseTypeDef",
    "ClientCreateMeshSpecegressFilterTypeDef",
    "ClientCreateMeshSpecTypeDef",
    "ClientCreateMeshTagsTypeDef",
    "ClientCreateRouteResponseroutemetadataTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRouteactionTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRoutematchTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    "ClientCreateRouteResponseroutespecgrpcRouteTypeDef",
    "ClientCreateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    "ClientCreateRouteResponseroutespechttp2RouteactionTypeDef",
    "ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    "ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    "ClientCreateRouteResponseroutespechttp2RoutematchheadersTypeDef",
    "ClientCreateRouteResponseroutespechttp2RoutematchTypeDef",
    "ClientCreateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    "ClientCreateRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    "ClientCreateRouteResponseroutespechttp2RouteTypeDef",
    "ClientCreateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    "ClientCreateRouteResponseroutespechttpRouteactionTypeDef",
    "ClientCreateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    "ClientCreateRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    "ClientCreateRouteResponseroutespechttpRoutematchheadersTypeDef",
    "ClientCreateRouteResponseroutespechttpRoutematchTypeDef",
    "ClientCreateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientCreateRouteResponseroutespechttpRouteretryPolicyTypeDef",
    "ClientCreateRouteResponseroutespechttpRouteTypeDef",
    "ClientCreateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    "ClientCreateRouteResponseroutespectcpRouteactionTypeDef",
    "ClientCreateRouteResponseroutespectcpRouteTypeDef",
    "ClientCreateRouteResponseroutespecTypeDef",
    "ClientCreateRouteResponseroutestatusTypeDef",
    "ClientCreateRouteResponserouteTypeDef",
    "ClientCreateRouteResponseTypeDef",
    "ClientCreateRouteSpecgrpcRouteactionweightedTargetsTypeDef",
    "ClientCreateRouteSpecgrpcRouteactionTypeDef",
    "ClientCreateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef",
    "ClientCreateRouteSpecgrpcRoutematchmetadatamatchTypeDef",
    "ClientCreateRouteSpecgrpcRoutematchmetadataTypeDef",
    "ClientCreateRouteSpecgrpcRoutematchTypeDef",
    "ClientCreateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientCreateRouteSpecgrpcRouteretryPolicyTypeDef",
    "ClientCreateRouteSpecgrpcRouteTypeDef",
    "ClientCreateRouteSpechttp2RouteactionweightedTargetsTypeDef",
    "ClientCreateRouteSpechttp2RouteactionTypeDef",
    "ClientCreateRouteSpechttp2RoutematchheadersmatchrangeTypeDef",
    "ClientCreateRouteSpechttp2RoutematchheadersmatchTypeDef",
    "ClientCreateRouteSpechttp2RoutematchheadersTypeDef",
    "ClientCreateRouteSpechttp2RoutematchTypeDef",
    "ClientCreateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    "ClientCreateRouteSpechttp2RouteretryPolicyTypeDef",
    "ClientCreateRouteSpechttp2RouteTypeDef",
    "ClientCreateRouteSpechttpRouteactionweightedTargetsTypeDef",
    "ClientCreateRouteSpechttpRouteactionTypeDef",
    "ClientCreateRouteSpechttpRoutematchheadersmatchrangeTypeDef",
    "ClientCreateRouteSpechttpRoutematchheadersmatchTypeDef",
    "ClientCreateRouteSpechttpRoutematchheadersTypeDef",
    "ClientCreateRouteSpechttpRoutematchTypeDef",
    "ClientCreateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientCreateRouteSpechttpRouteretryPolicyTypeDef",
    "ClientCreateRouteSpechttpRouteTypeDef",
    "ClientCreateRouteSpectcpRouteactionweightedTargetsTypeDef",
    "ClientCreateRouteSpectcpRouteactionTypeDef",
    "ClientCreateRouteSpectcpRouteTypeDef",
    "ClientCreateRouteSpecTypeDef",
    "ClientCreateRouteTagsTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodemetadataTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecloggingTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodespecTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodestatusTypeDef",
    "ClientCreateVirtualNodeResponsevirtualNodeTypeDef",
    "ClientCreateVirtualNodeResponseTypeDef",
    "ClientCreateVirtualNodeSpecbackendsvirtualServiceTypeDef",
    "ClientCreateVirtualNodeSpecbackendsTypeDef",
    "ClientCreateVirtualNodeSpeclistenershealthCheckTypeDef",
    "ClientCreateVirtualNodeSpeclistenersportMappingTypeDef",
    "ClientCreateVirtualNodeSpeclistenersTypeDef",
    "ClientCreateVirtualNodeSpecloggingaccessLogfileTypeDef",
    "ClientCreateVirtualNodeSpecloggingaccessLogTypeDef",
    "ClientCreateVirtualNodeSpecloggingTypeDef",
    "ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef",
    "ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef",
    "ClientCreateVirtualNodeSpecserviceDiscoverydnsTypeDef",
    "ClientCreateVirtualNodeSpecserviceDiscoveryTypeDef",
    "ClientCreateVirtualNodeSpecTypeDef",
    "ClientCreateVirtualNodeTagsTypeDef",
    "ClientCreateVirtualRouterResponsevirtualRoutermetadataTypeDef",
    "ClientCreateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    "ClientCreateVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    "ClientCreateVirtualRouterResponsevirtualRouterspecTypeDef",
    "ClientCreateVirtualRouterResponsevirtualRouterstatusTypeDef",
    "ClientCreateVirtualRouterResponsevirtualRouterTypeDef",
    "ClientCreateVirtualRouterResponseTypeDef",
    "ClientCreateVirtualRouterSpeclistenersportMappingTypeDef",
    "ClientCreateVirtualRouterSpeclistenersTypeDef",
    "ClientCreateVirtualRouterSpecTypeDef",
    "ClientCreateVirtualRouterTagsTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServicemetadataTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServicespecproviderTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServicespecTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServicestatusTypeDef",
    "ClientCreateVirtualServiceResponsevirtualServiceTypeDef",
    "ClientCreateVirtualServiceResponseTypeDef",
    "ClientCreateVirtualServiceSpecprovidervirtualNodeTypeDef",
    "ClientCreateVirtualServiceSpecprovidervirtualRouterTypeDef",
    "ClientCreateVirtualServiceSpecproviderTypeDef",
    "ClientCreateVirtualServiceSpecTypeDef",
    "ClientCreateVirtualServiceTagsTypeDef",
    "ClientDeleteMeshResponsemeshmetadataTypeDef",
    "ClientDeleteMeshResponsemeshspecegressFilterTypeDef",
    "ClientDeleteMeshResponsemeshspecTypeDef",
    "ClientDeleteMeshResponsemeshstatusTypeDef",
    "ClientDeleteMeshResponsemeshTypeDef",
    "ClientDeleteMeshResponseTypeDef",
    "ClientDeleteRouteResponseroutemetadataTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRouteactionTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRoutematchTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    "ClientDeleteRouteResponseroutespecgrpcRouteTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RouteactionTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RoutematchheadersTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RoutematchTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    "ClientDeleteRouteResponseroutespechttp2RouteTypeDef",
    "ClientDeleteRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    "ClientDeleteRouteResponseroutespechttpRouteactionTypeDef",
    "ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    "ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    "ClientDeleteRouteResponseroutespechttpRoutematchheadersTypeDef",
    "ClientDeleteRouteResponseroutespechttpRoutematchTypeDef",
    "ClientDeleteRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientDeleteRouteResponseroutespechttpRouteretryPolicyTypeDef",
    "ClientDeleteRouteResponseroutespechttpRouteTypeDef",
    "ClientDeleteRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    "ClientDeleteRouteResponseroutespectcpRouteactionTypeDef",
    "ClientDeleteRouteResponseroutespectcpRouteTypeDef",
    "ClientDeleteRouteResponseroutespecTypeDef",
    "ClientDeleteRouteResponseroutestatusTypeDef",
    "ClientDeleteRouteResponserouteTypeDef",
    "ClientDeleteRouteResponseTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodemetadataTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecloggingTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodespecTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodestatusTypeDef",
    "ClientDeleteVirtualNodeResponsevirtualNodeTypeDef",
    "ClientDeleteVirtualNodeResponseTypeDef",
    "ClientDeleteVirtualRouterResponsevirtualRoutermetadataTypeDef",
    "ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    "ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    "ClientDeleteVirtualRouterResponsevirtualRouterspecTypeDef",
    "ClientDeleteVirtualRouterResponsevirtualRouterstatusTypeDef",
    "ClientDeleteVirtualRouterResponsevirtualRouterTypeDef",
    "ClientDeleteVirtualRouterResponseTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServicemetadataTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServicespecproviderTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServicespecTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServicestatusTypeDef",
    "ClientDeleteVirtualServiceResponsevirtualServiceTypeDef",
    "ClientDeleteVirtualServiceResponseTypeDef",
    "ClientDescribeMeshResponsemeshmetadataTypeDef",
    "ClientDescribeMeshResponsemeshspecegressFilterTypeDef",
    "ClientDescribeMeshResponsemeshspecTypeDef",
    "ClientDescribeMeshResponsemeshstatusTypeDef",
    "ClientDescribeMeshResponsemeshTypeDef",
    "ClientDescribeMeshResponseTypeDef",
    "ClientDescribeRouteResponseroutemetadataTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRouteactionTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRoutematchTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    "ClientDescribeRouteResponseroutespecgrpcRouteTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RouteactionTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RoutematchheadersTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RoutematchTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    "ClientDescribeRouteResponseroutespechttp2RouteTypeDef",
    "ClientDescribeRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    "ClientDescribeRouteResponseroutespechttpRouteactionTypeDef",
    "ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    "ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    "ClientDescribeRouteResponseroutespechttpRoutematchheadersTypeDef",
    "ClientDescribeRouteResponseroutespechttpRoutematchTypeDef",
    "ClientDescribeRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientDescribeRouteResponseroutespechttpRouteretryPolicyTypeDef",
    "ClientDescribeRouteResponseroutespechttpRouteTypeDef",
    "ClientDescribeRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    "ClientDescribeRouteResponseroutespectcpRouteactionTypeDef",
    "ClientDescribeRouteResponseroutespectcpRouteTypeDef",
    "ClientDescribeRouteResponseroutespecTypeDef",
    "ClientDescribeRouteResponseroutestatusTypeDef",
    "ClientDescribeRouteResponserouteTypeDef",
    "ClientDescribeRouteResponseTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodemetadataTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecloggingTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodespecTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodestatusTypeDef",
    "ClientDescribeVirtualNodeResponsevirtualNodeTypeDef",
    "ClientDescribeVirtualNodeResponseTypeDef",
    "ClientDescribeVirtualRouterResponsevirtualRoutermetadataTypeDef",
    "ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    "ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    "ClientDescribeVirtualRouterResponsevirtualRouterspecTypeDef",
    "ClientDescribeVirtualRouterResponsevirtualRouterstatusTypeDef",
    "ClientDescribeVirtualRouterResponsevirtualRouterTypeDef",
    "ClientDescribeVirtualRouterResponseTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServicemetadataTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServicespecproviderTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServicespecTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServicestatusTypeDef",
    "ClientDescribeVirtualServiceResponsevirtualServiceTypeDef",
    "ClientDescribeVirtualServiceResponseTypeDef",
    "ClientListMeshesResponsemeshesTypeDef",
    "ClientListMeshesResponseTypeDef",
    "ClientListRoutesResponseroutesTypeDef",
    "ClientListRoutesResponseTypeDef",
    "ClientListTagsForResourceResponsetagsTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientListVirtualNodesResponsevirtualNodesTypeDef",
    "ClientListVirtualNodesResponseTypeDef",
    "ClientListVirtualRoutersResponsevirtualRoutersTypeDef",
    "ClientListVirtualRoutersResponseTypeDef",
    "ClientListVirtualServicesResponsevirtualServicesTypeDef",
    "ClientListVirtualServicesResponseTypeDef",
    "ClientTagResourceTagsTypeDef",
    "ClientUpdateMeshResponsemeshmetadataTypeDef",
    "ClientUpdateMeshResponsemeshspecegressFilterTypeDef",
    "ClientUpdateMeshResponsemeshspecTypeDef",
    "ClientUpdateMeshResponsemeshstatusTypeDef",
    "ClientUpdateMeshResponsemeshTypeDef",
    "ClientUpdateMeshResponseTypeDef",
    "ClientUpdateMeshSpecegressFilterTypeDef",
    "ClientUpdateMeshSpecTypeDef",
    "ClientUpdateRouteResponseroutemetadataTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRouteactionTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRoutematchTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    "ClientUpdateRouteResponseroutespecgrpcRouteTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RouteactionTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RoutematchheadersTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RoutematchTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    "ClientUpdateRouteResponseroutespechttp2RouteTypeDef",
    "ClientUpdateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteResponseroutespechttpRouteactionTypeDef",
    "ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    "ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    "ClientUpdateRouteResponseroutespechttpRoutematchheadersTypeDef",
    "ClientUpdateRouteResponseroutespechttpRoutematchTypeDef",
    "ClientUpdateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientUpdateRouteResponseroutespechttpRouteretryPolicyTypeDef",
    "ClientUpdateRouteResponseroutespechttpRouteTypeDef",
    "ClientUpdateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteResponseroutespectcpRouteactionTypeDef",
    "ClientUpdateRouteResponseroutespectcpRouteTypeDef",
    "ClientUpdateRouteResponseroutespecTypeDef",
    "ClientUpdateRouteResponseroutestatusTypeDef",
    "ClientUpdateRouteResponserouteTypeDef",
    "ClientUpdateRouteResponseTypeDef",
    "ClientUpdateRouteSpecgrpcRouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteSpecgrpcRouteactionTypeDef",
    "ClientUpdateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef",
    "ClientUpdateRouteSpecgrpcRoutematchmetadatamatchTypeDef",
    "ClientUpdateRouteSpecgrpcRoutematchmetadataTypeDef",
    "ClientUpdateRouteSpecgrpcRoutematchTypeDef",
    "ClientUpdateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientUpdateRouteSpecgrpcRouteretryPolicyTypeDef",
    "ClientUpdateRouteSpecgrpcRouteTypeDef",
    "ClientUpdateRouteSpechttp2RouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteSpechttp2RouteactionTypeDef",
    "ClientUpdateRouteSpechttp2RoutematchheadersmatchrangeTypeDef",
    "ClientUpdateRouteSpechttp2RoutematchheadersmatchTypeDef",
    "ClientUpdateRouteSpechttp2RoutematchheadersTypeDef",
    "ClientUpdateRouteSpechttp2RoutematchTypeDef",
    "ClientUpdateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    "ClientUpdateRouteSpechttp2RouteretryPolicyTypeDef",
    "ClientUpdateRouteSpechttp2RouteTypeDef",
    "ClientUpdateRouteSpechttpRouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteSpechttpRouteactionTypeDef",
    "ClientUpdateRouteSpechttpRoutematchheadersmatchrangeTypeDef",
    "ClientUpdateRouteSpechttpRoutematchheadersmatchTypeDef",
    "ClientUpdateRouteSpechttpRoutematchheadersTypeDef",
    "ClientUpdateRouteSpechttpRoutematchTypeDef",
    "ClientUpdateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef",
    "ClientUpdateRouteSpechttpRouteretryPolicyTypeDef",
    "ClientUpdateRouteSpechttpRouteTypeDef",
    "ClientUpdateRouteSpectcpRouteactionweightedTargetsTypeDef",
    "ClientUpdateRouteSpectcpRouteactionTypeDef",
    "ClientUpdateRouteSpectcpRouteTypeDef",
    "ClientUpdateRouteSpecTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodemetadataTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecloggingTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodespecTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodestatusTypeDef",
    "ClientUpdateVirtualNodeResponsevirtualNodeTypeDef",
    "ClientUpdateVirtualNodeResponseTypeDef",
    "ClientUpdateVirtualNodeSpecbackendsvirtualServiceTypeDef",
    "ClientUpdateVirtualNodeSpecbackendsTypeDef",
    "ClientUpdateVirtualNodeSpeclistenershealthCheckTypeDef",
    "ClientUpdateVirtualNodeSpeclistenersportMappingTypeDef",
    "ClientUpdateVirtualNodeSpeclistenersTypeDef",
    "ClientUpdateVirtualNodeSpecloggingaccessLogfileTypeDef",
    "ClientUpdateVirtualNodeSpecloggingaccessLogTypeDef",
    "ClientUpdateVirtualNodeSpecloggingTypeDef",
    "ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef",
    "ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef",
    "ClientUpdateVirtualNodeSpecserviceDiscoverydnsTypeDef",
    "ClientUpdateVirtualNodeSpecserviceDiscoveryTypeDef",
    "ClientUpdateVirtualNodeSpecTypeDef",
    "ClientUpdateVirtualRouterResponsevirtualRoutermetadataTypeDef",
    "ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    "ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    "ClientUpdateVirtualRouterResponsevirtualRouterspecTypeDef",
    "ClientUpdateVirtualRouterResponsevirtualRouterstatusTypeDef",
    "ClientUpdateVirtualRouterResponsevirtualRouterTypeDef",
    "ClientUpdateVirtualRouterResponseTypeDef",
    "ClientUpdateVirtualRouterSpeclistenersportMappingTypeDef",
    "ClientUpdateVirtualRouterSpeclistenersTypeDef",
    "ClientUpdateVirtualRouterSpecTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServicemetadataTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServicespecproviderTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServicespecTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServicestatusTypeDef",
    "ClientUpdateVirtualServiceResponsevirtualServiceTypeDef",
    "ClientUpdateVirtualServiceResponseTypeDef",
    "ClientUpdateVirtualServiceSpecprovidervirtualNodeTypeDef",
    "ClientUpdateVirtualServiceSpecprovidervirtualRouterTypeDef",
    "ClientUpdateVirtualServiceSpecproviderTypeDef",
    "ClientUpdateVirtualServiceSpecTypeDef",
    "MeshRefTypeDef",
    "ListMeshesOutputTypeDef",
    "RouteRefTypeDef",
    "ListRoutesOutputTypeDef",
    "TagRefTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "VirtualNodeRefTypeDef",
    "ListVirtualNodesOutputTypeDef",
    "VirtualRouterRefTypeDef",
    "ListVirtualRoutersOutputTypeDef",
    "VirtualServiceRefTypeDef",
    "ListVirtualServicesOutputTypeDef",
    "PaginatorConfigTypeDef",
)

ClientCreateMeshResponsemeshmetadataTypeDef = TypedDict(
    "ClientCreateMeshResponsemeshmetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientCreateMeshResponsemeshspecegressFilterTypeDef = TypedDict(
    "ClientCreateMeshResponsemeshspecegressFilterTypeDef",
    {"type": Literal["ALLOW_ALL", "DROP_ALL"]},
    total=False,
)

ClientCreateMeshResponsemeshspecTypeDef = TypedDict(
    "ClientCreateMeshResponsemeshspecTypeDef",
    {"egressFilter": ClientCreateMeshResponsemeshspecegressFilterTypeDef},
    total=False,
)

ClientCreateMeshResponsemeshstatusTypeDef = TypedDict(
    "ClientCreateMeshResponsemeshstatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientCreateMeshResponsemeshTypeDef = TypedDict(
    "ClientCreateMeshResponsemeshTypeDef",
    {
        "meshName": str,
        "metadata": ClientCreateMeshResponsemeshmetadataTypeDef,
        "spec": ClientCreateMeshResponsemeshspecTypeDef,
        "status": ClientCreateMeshResponsemeshstatusTypeDef,
    },
    total=False,
)

ClientCreateMeshResponseTypeDef = TypedDict(
    "ClientCreateMeshResponseTypeDef", {"mesh": ClientCreateMeshResponsemeshTypeDef}, total=False
)

ClientCreateMeshSpecegressFilterTypeDef = TypedDict(
    "ClientCreateMeshSpecegressFilterTypeDef", {"type": Literal["ALLOW_ALL", "DROP_ALL"]}
)

ClientCreateMeshSpecTypeDef = TypedDict(
    "ClientCreateMeshSpecTypeDef",
    {"egressFilter": ClientCreateMeshSpecegressFilterTypeDef},
    total=False,
)

_RequiredClientCreateMeshTagsTypeDef = TypedDict(
    "_RequiredClientCreateMeshTagsTypeDef", {"key": str}
)
_OptionalClientCreateMeshTagsTypeDef = TypedDict(
    "_OptionalClientCreateMeshTagsTypeDef", {"value": str}, total=False
)


class ClientCreateMeshTagsTypeDef(
    _RequiredClientCreateMeshTagsTypeDef, _OptionalClientCreateMeshTagsTypeDef
):
    pass


ClientCreateRouteResponseroutemetadataTypeDef = TypedDict(
    "ClientCreateRouteResponseroutemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientCreateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientCreateRouteResponseroutespecgrpcRouteactionTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespecgrpcRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientCreateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)

ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)

ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

ClientCreateRouteResponseroutespecgrpcRoutematchmetadataTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    {
        "invert": bool,
        "match": ClientCreateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef,
        "name": str,
    },
    total=False,
)

ClientCreateRouteResponseroutespecgrpcRoutematchTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespecgrpcRoutematchTypeDef",
    {
        "metadata": List[ClientCreateRouteResponseroutespecgrpcRoutematchmetadataTypeDef],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)

ClientCreateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)

ClientCreateRouteResponseroutespecgrpcRouteretryPolicyTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    {
        "grpcRetryEvents": List[
            Literal[
                "cancelled", "deadline-exceeded", "internal", "resource-exhausted", "unavailable"
            ]
        ],
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientCreateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)

ClientCreateRouteResponseroutespecgrpcRouteTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespecgrpcRouteTypeDef",
    {
        "action": ClientCreateRouteResponseroutespecgrpcRouteactionTypeDef,
        "match": ClientCreateRouteResponseroutespecgrpcRoutematchTypeDef,
        "retryPolicy": ClientCreateRouteResponseroutespecgrpcRouteretryPolicyTypeDef,
    },
    total=False,
)

ClientCreateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientCreateRouteResponseroutespechttp2RouteactionTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespechttp2RouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientCreateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)

ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)

ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

ClientCreateRouteResponseroutespechttp2RoutematchheadersTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespechttp2RoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientCreateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)

ClientCreateRouteResponseroutespechttp2RoutematchTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespechttp2RoutematchTypeDef",
    {
        "headers": List[ClientCreateRouteResponseroutespechttp2RoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)

ClientCreateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)

ClientCreateRouteResponseroutespechttp2RouteretryPolicyTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientCreateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)

ClientCreateRouteResponseroutespechttp2RouteTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespechttp2RouteTypeDef",
    {
        "action": ClientCreateRouteResponseroutespechttp2RouteactionTypeDef,
        "match": ClientCreateRouteResponseroutespechttp2RoutematchTypeDef,
        "retryPolicy": ClientCreateRouteResponseroutespechttp2RouteretryPolicyTypeDef,
    },
    total=False,
)

ClientCreateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientCreateRouteResponseroutespechttpRouteactionTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespechttpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientCreateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)

ClientCreateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)

ClientCreateRouteResponseroutespechttpRoutematchheadersmatchTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientCreateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

ClientCreateRouteResponseroutespechttpRoutematchheadersTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespechttpRoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientCreateRouteResponseroutespechttpRoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)

ClientCreateRouteResponseroutespechttpRoutematchTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespechttpRoutematchTypeDef",
    {
        "headers": List[ClientCreateRouteResponseroutespechttpRoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)

ClientCreateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)

ClientCreateRouteResponseroutespechttpRouteretryPolicyTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespechttpRouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientCreateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)

ClientCreateRouteResponseroutespechttpRouteTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespechttpRouteTypeDef",
    {
        "action": ClientCreateRouteResponseroutespechttpRouteactionTypeDef,
        "match": ClientCreateRouteResponseroutespechttpRoutematchTypeDef,
        "retryPolicy": ClientCreateRouteResponseroutespechttpRouteretryPolicyTypeDef,
    },
    total=False,
)

ClientCreateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientCreateRouteResponseroutespectcpRouteactionTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespectcpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientCreateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)

ClientCreateRouteResponseroutespectcpRouteTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespectcpRouteTypeDef",
    {"action": ClientCreateRouteResponseroutespectcpRouteactionTypeDef},
    total=False,
)

ClientCreateRouteResponseroutespecTypeDef = TypedDict(
    "ClientCreateRouteResponseroutespecTypeDef",
    {
        "grpcRoute": ClientCreateRouteResponseroutespecgrpcRouteTypeDef,
        "http2Route": ClientCreateRouteResponseroutespechttp2RouteTypeDef,
        "httpRoute": ClientCreateRouteResponseroutespechttpRouteTypeDef,
        "priority": int,
        "tcpRoute": ClientCreateRouteResponseroutespectcpRouteTypeDef,
    },
    total=False,
)

ClientCreateRouteResponseroutestatusTypeDef = TypedDict(
    "ClientCreateRouteResponseroutestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientCreateRouteResponserouteTypeDef = TypedDict(
    "ClientCreateRouteResponserouteTypeDef",
    {
        "meshName": str,
        "metadata": ClientCreateRouteResponseroutemetadataTypeDef,
        "routeName": str,
        "spec": ClientCreateRouteResponseroutespecTypeDef,
        "status": ClientCreateRouteResponseroutestatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)

ClientCreateRouteResponseTypeDef = TypedDict(
    "ClientCreateRouteResponseTypeDef",
    {"route": ClientCreateRouteResponserouteTypeDef},
    total=False,
)

_RequiredClientCreateRouteSpecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "_RequiredClientCreateRouteSpecgrpcRouteactionweightedTargetsTypeDef", {"virtualNode": str}
)
_OptionalClientCreateRouteSpecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "_OptionalClientCreateRouteSpecgrpcRouteactionweightedTargetsTypeDef",
    {"weight": int},
    total=False,
)


class ClientCreateRouteSpecgrpcRouteactionweightedTargetsTypeDef(
    _RequiredClientCreateRouteSpecgrpcRouteactionweightedTargetsTypeDef,
    _OptionalClientCreateRouteSpecgrpcRouteactionweightedTargetsTypeDef,
):
    pass


ClientCreateRouteSpecgrpcRouteactionTypeDef = TypedDict(
    "ClientCreateRouteSpecgrpcRouteactionTypeDef",
    {"weightedTargets": List[ClientCreateRouteSpecgrpcRouteactionweightedTargetsTypeDef]},
)

ClientCreateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef = TypedDict(
    "ClientCreateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)

ClientCreateRouteSpecgrpcRoutematchmetadatamatchTypeDef = TypedDict(
    "ClientCreateRouteSpecgrpcRoutematchmetadatamatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientCreateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

ClientCreateRouteSpecgrpcRoutematchmetadataTypeDef = TypedDict(
    "ClientCreateRouteSpecgrpcRoutematchmetadataTypeDef",
    {"invert": bool, "match": ClientCreateRouteSpecgrpcRoutematchmetadatamatchTypeDef, "name": str},
    total=False,
)

ClientCreateRouteSpecgrpcRoutematchTypeDef = TypedDict(
    "ClientCreateRouteSpecgrpcRoutematchTypeDef",
    {
        "metadata": List[ClientCreateRouteSpecgrpcRoutematchmetadataTypeDef],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)

ClientCreateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "ClientCreateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)

ClientCreateRouteSpecgrpcRouteretryPolicyTypeDef = TypedDict(
    "ClientCreateRouteSpecgrpcRouteretryPolicyTypeDef",
    {
        "grpcRetryEvents": List[
            Literal[
                "cancelled", "deadline-exceeded", "internal", "resource-exhausted", "unavailable"
            ]
        ],
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientCreateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)

_RequiredClientCreateRouteSpecgrpcRouteTypeDef = TypedDict(
    "_RequiredClientCreateRouteSpecgrpcRouteTypeDef",
    {"action": ClientCreateRouteSpecgrpcRouteactionTypeDef},
)
_OptionalClientCreateRouteSpecgrpcRouteTypeDef = TypedDict(
    "_OptionalClientCreateRouteSpecgrpcRouteTypeDef",
    {
        "match": ClientCreateRouteSpecgrpcRoutematchTypeDef,
        "retryPolicy": ClientCreateRouteSpecgrpcRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientCreateRouteSpecgrpcRouteTypeDef(
    _RequiredClientCreateRouteSpecgrpcRouteTypeDef, _OptionalClientCreateRouteSpecgrpcRouteTypeDef
):
    pass


ClientCreateRouteSpechttp2RouteactionweightedTargetsTypeDef = TypedDict(
    "ClientCreateRouteSpechttp2RouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientCreateRouteSpechttp2RouteactionTypeDef = TypedDict(
    "ClientCreateRouteSpechttp2RouteactionTypeDef",
    {"weightedTargets": List[ClientCreateRouteSpechttp2RouteactionweightedTargetsTypeDef]},
    total=False,
)

ClientCreateRouteSpechttp2RoutematchheadersmatchrangeTypeDef = TypedDict(
    "ClientCreateRouteSpechttp2RoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)

ClientCreateRouteSpechttp2RoutematchheadersmatchTypeDef = TypedDict(
    "ClientCreateRouteSpechttp2RoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientCreateRouteSpechttp2RoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

ClientCreateRouteSpechttp2RoutematchheadersTypeDef = TypedDict(
    "ClientCreateRouteSpechttp2RoutematchheadersTypeDef",
    {"invert": bool, "match": ClientCreateRouteSpechttp2RoutematchheadersmatchTypeDef, "name": str},
    total=False,
)

ClientCreateRouteSpechttp2RoutematchTypeDef = TypedDict(
    "ClientCreateRouteSpechttp2RoutematchTypeDef",
    {
        "headers": List[ClientCreateRouteSpechttp2RoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)

ClientCreateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "ClientCreateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)

ClientCreateRouteSpechttp2RouteretryPolicyTypeDef = TypedDict(
    "ClientCreateRouteSpechttp2RouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientCreateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)

ClientCreateRouteSpechttp2RouteTypeDef = TypedDict(
    "ClientCreateRouteSpechttp2RouteTypeDef",
    {
        "action": ClientCreateRouteSpechttp2RouteactionTypeDef,
        "match": ClientCreateRouteSpechttp2RoutematchTypeDef,
        "retryPolicy": ClientCreateRouteSpechttp2RouteretryPolicyTypeDef,
    },
    total=False,
)

ClientCreateRouteSpechttpRouteactionweightedTargetsTypeDef = TypedDict(
    "ClientCreateRouteSpechttpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientCreateRouteSpechttpRouteactionTypeDef = TypedDict(
    "ClientCreateRouteSpechttpRouteactionTypeDef",
    {"weightedTargets": List[ClientCreateRouteSpechttpRouteactionweightedTargetsTypeDef]},
    total=False,
)

ClientCreateRouteSpechttpRoutematchheadersmatchrangeTypeDef = TypedDict(
    "ClientCreateRouteSpechttpRoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)

ClientCreateRouteSpechttpRoutematchheadersmatchTypeDef = TypedDict(
    "ClientCreateRouteSpechttpRoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientCreateRouteSpechttpRoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

ClientCreateRouteSpechttpRoutematchheadersTypeDef = TypedDict(
    "ClientCreateRouteSpechttpRoutematchheadersTypeDef",
    {"invert": bool, "match": ClientCreateRouteSpechttpRoutematchheadersmatchTypeDef, "name": str},
    total=False,
)

ClientCreateRouteSpechttpRoutematchTypeDef = TypedDict(
    "ClientCreateRouteSpechttpRoutematchTypeDef",
    {
        "headers": List[ClientCreateRouteSpechttpRoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)

ClientCreateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "ClientCreateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)

ClientCreateRouteSpechttpRouteretryPolicyTypeDef = TypedDict(
    "ClientCreateRouteSpechttpRouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientCreateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)

ClientCreateRouteSpechttpRouteTypeDef = TypedDict(
    "ClientCreateRouteSpechttpRouteTypeDef",
    {
        "action": ClientCreateRouteSpechttpRouteactionTypeDef,
        "match": ClientCreateRouteSpechttpRoutematchTypeDef,
        "retryPolicy": ClientCreateRouteSpechttpRouteretryPolicyTypeDef,
    },
    total=False,
)

ClientCreateRouteSpectcpRouteactionweightedTargetsTypeDef = TypedDict(
    "ClientCreateRouteSpectcpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientCreateRouteSpectcpRouteactionTypeDef = TypedDict(
    "ClientCreateRouteSpectcpRouteactionTypeDef",
    {"weightedTargets": List[ClientCreateRouteSpectcpRouteactionweightedTargetsTypeDef]},
    total=False,
)

ClientCreateRouteSpectcpRouteTypeDef = TypedDict(
    "ClientCreateRouteSpectcpRouteTypeDef",
    {"action": ClientCreateRouteSpectcpRouteactionTypeDef},
    total=False,
)

ClientCreateRouteSpecTypeDef = TypedDict(
    "ClientCreateRouteSpecTypeDef",
    {
        "grpcRoute": ClientCreateRouteSpecgrpcRouteTypeDef,
        "http2Route": ClientCreateRouteSpechttp2RouteTypeDef,
        "httpRoute": ClientCreateRouteSpechttpRouteTypeDef,
        "priority": int,
        "tcpRoute": ClientCreateRouteSpectcpRouteTypeDef,
    },
    total=False,
)

_RequiredClientCreateRouteTagsTypeDef = TypedDict(
    "_RequiredClientCreateRouteTagsTypeDef", {"key": str}
)
_OptionalClientCreateRouteTagsTypeDef = TypedDict(
    "_OptionalClientCreateRouteTagsTypeDef", {"value": str}, total=False
)


class ClientCreateRouteTagsTypeDef(
    _RequiredClientCreateRouteTagsTypeDef, _OptionalClientCreateRouteTagsTypeDef
):
    pass


ClientCreateVirtualNodeResponsevirtualNodemetadataTypeDef = TypedDict(
    "ClientCreateVirtualNodeResponsevirtualNodemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientCreateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef = TypedDict(
    "ClientCreateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    {"virtualServiceName": str},
    total=False,
)

ClientCreateVirtualNodeResponsevirtualNodespecbackendsTypeDef = TypedDict(
    "ClientCreateVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    {"virtualService": ClientCreateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef},
    total=False,
)

ClientCreateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef = TypedDict(
    "ClientCreateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "path": str,
        "port": int,
        "protocol": Literal["grpc", "http", "http2", "tcp"],
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
    total=False,
)

ClientCreateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef = TypedDict(
    "ClientCreateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)

ClientCreateVirtualNodeResponsevirtualNodespeclistenersTypeDef = TypedDict(
    "ClientCreateVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    {
        "healthCheck": ClientCreateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef,
        "portMapping": ClientCreateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef,
    },
    total=False,
)

ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef = TypedDict(
    "ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    {"path": str},
    total=False,
)

ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef = TypedDict(
    "ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    {"file": ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef},
    total=False,
)

ClientCreateVirtualNodeResponsevirtualNodespecloggingTypeDef = TypedDict(
    "ClientCreateVirtualNodeResponsevirtualNodespecloggingTypeDef",
    {"accessLog": ClientCreateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef},
    total=False,
)

ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef = TypedDict(
    "ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    {
        "attributes": List[
            ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
        ],
        "namespaceName": str,
        "serviceName": str,
    },
    total=False,
)

ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef = TypedDict(
    "ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    {"hostname": str},
    total=False,
)

ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef = TypedDict(
    "ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    {
        "awsCloudMap": ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef,
        "dns": ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef,
    },
    total=False,
)

ClientCreateVirtualNodeResponsevirtualNodespecTypeDef = TypedDict(
    "ClientCreateVirtualNodeResponsevirtualNodespecTypeDef",
    {
        "backends": List[ClientCreateVirtualNodeResponsevirtualNodespecbackendsTypeDef],
        "listeners": List[ClientCreateVirtualNodeResponsevirtualNodespeclistenersTypeDef],
        "logging": ClientCreateVirtualNodeResponsevirtualNodespecloggingTypeDef,
        "serviceDiscovery": ClientCreateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef,
    },
    total=False,
)

ClientCreateVirtualNodeResponsevirtualNodestatusTypeDef = TypedDict(
    "ClientCreateVirtualNodeResponsevirtualNodestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientCreateVirtualNodeResponsevirtualNodeTypeDef = TypedDict(
    "ClientCreateVirtualNodeResponsevirtualNodeTypeDef",
    {
        "meshName": str,
        "metadata": ClientCreateVirtualNodeResponsevirtualNodemetadataTypeDef,
        "spec": ClientCreateVirtualNodeResponsevirtualNodespecTypeDef,
        "status": ClientCreateVirtualNodeResponsevirtualNodestatusTypeDef,
        "virtualNodeName": str,
    },
    total=False,
)

ClientCreateVirtualNodeResponseTypeDef = TypedDict(
    "ClientCreateVirtualNodeResponseTypeDef",
    {"virtualNode": ClientCreateVirtualNodeResponsevirtualNodeTypeDef},
    total=False,
)

ClientCreateVirtualNodeSpecbackendsvirtualServiceTypeDef = TypedDict(
    "ClientCreateVirtualNodeSpecbackendsvirtualServiceTypeDef", {"virtualServiceName": str}
)

ClientCreateVirtualNodeSpecbackendsTypeDef = TypedDict(
    "ClientCreateVirtualNodeSpecbackendsTypeDef",
    {"virtualService": ClientCreateVirtualNodeSpecbackendsvirtualServiceTypeDef},
    total=False,
)

ClientCreateVirtualNodeSpeclistenershealthCheckTypeDef = TypedDict(
    "ClientCreateVirtualNodeSpeclistenershealthCheckTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "path": str,
        "port": int,
        "protocol": Literal["grpc", "http", "http2", "tcp"],
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
    total=False,
)

ClientCreateVirtualNodeSpeclistenersportMappingTypeDef = TypedDict(
    "ClientCreateVirtualNodeSpeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)

ClientCreateVirtualNodeSpeclistenersTypeDef = TypedDict(
    "ClientCreateVirtualNodeSpeclistenersTypeDef",
    {
        "healthCheck": ClientCreateVirtualNodeSpeclistenershealthCheckTypeDef,
        "portMapping": ClientCreateVirtualNodeSpeclistenersportMappingTypeDef,
    },
    total=False,
)

ClientCreateVirtualNodeSpecloggingaccessLogfileTypeDef = TypedDict(
    "ClientCreateVirtualNodeSpecloggingaccessLogfileTypeDef", {"path": str}, total=False
)

ClientCreateVirtualNodeSpecloggingaccessLogTypeDef = TypedDict(
    "ClientCreateVirtualNodeSpecloggingaccessLogTypeDef",
    {"file": ClientCreateVirtualNodeSpecloggingaccessLogfileTypeDef},
    total=False,
)

ClientCreateVirtualNodeSpecloggingTypeDef = TypedDict(
    "ClientCreateVirtualNodeSpecloggingTypeDef",
    {"accessLog": ClientCreateVirtualNodeSpecloggingaccessLogTypeDef},
    total=False,
)

ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef = TypedDict(
    "ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef",
    {
        "attributes": List[ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef],
        "namespaceName": str,
        "serviceName": str,
    },
    total=False,
)

ClientCreateVirtualNodeSpecserviceDiscoverydnsTypeDef = TypedDict(
    "ClientCreateVirtualNodeSpecserviceDiscoverydnsTypeDef", {"hostname": str}, total=False
)

ClientCreateVirtualNodeSpecserviceDiscoveryTypeDef = TypedDict(
    "ClientCreateVirtualNodeSpecserviceDiscoveryTypeDef",
    {
        "awsCloudMap": ClientCreateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef,
        "dns": ClientCreateVirtualNodeSpecserviceDiscoverydnsTypeDef,
    },
    total=False,
)

ClientCreateVirtualNodeSpecTypeDef = TypedDict(
    "ClientCreateVirtualNodeSpecTypeDef",
    {
        "backends": List[ClientCreateVirtualNodeSpecbackendsTypeDef],
        "listeners": List[ClientCreateVirtualNodeSpeclistenersTypeDef],
        "logging": ClientCreateVirtualNodeSpecloggingTypeDef,
        "serviceDiscovery": ClientCreateVirtualNodeSpecserviceDiscoveryTypeDef,
    },
    total=False,
)

_RequiredClientCreateVirtualNodeTagsTypeDef = TypedDict(
    "_RequiredClientCreateVirtualNodeTagsTypeDef", {"key": str}
)
_OptionalClientCreateVirtualNodeTagsTypeDef = TypedDict(
    "_OptionalClientCreateVirtualNodeTagsTypeDef", {"value": str}, total=False
)


class ClientCreateVirtualNodeTagsTypeDef(
    _RequiredClientCreateVirtualNodeTagsTypeDef, _OptionalClientCreateVirtualNodeTagsTypeDef
):
    pass


ClientCreateVirtualRouterResponsevirtualRoutermetadataTypeDef = TypedDict(
    "ClientCreateVirtualRouterResponsevirtualRoutermetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientCreateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef = TypedDict(
    "ClientCreateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)

ClientCreateVirtualRouterResponsevirtualRouterspeclistenersTypeDef = TypedDict(
    "ClientCreateVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    {"portMapping": ClientCreateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef},
    total=False,
)

ClientCreateVirtualRouterResponsevirtualRouterspecTypeDef = TypedDict(
    "ClientCreateVirtualRouterResponsevirtualRouterspecTypeDef",
    {"listeners": List[ClientCreateVirtualRouterResponsevirtualRouterspeclistenersTypeDef]},
    total=False,
)

ClientCreateVirtualRouterResponsevirtualRouterstatusTypeDef = TypedDict(
    "ClientCreateVirtualRouterResponsevirtualRouterstatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientCreateVirtualRouterResponsevirtualRouterTypeDef = TypedDict(
    "ClientCreateVirtualRouterResponsevirtualRouterTypeDef",
    {
        "meshName": str,
        "metadata": ClientCreateVirtualRouterResponsevirtualRoutermetadataTypeDef,
        "spec": ClientCreateVirtualRouterResponsevirtualRouterspecTypeDef,
        "status": ClientCreateVirtualRouterResponsevirtualRouterstatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)

ClientCreateVirtualRouterResponseTypeDef = TypedDict(
    "ClientCreateVirtualRouterResponseTypeDef",
    {"virtualRouter": ClientCreateVirtualRouterResponsevirtualRouterTypeDef},
    total=False,
)

_RequiredClientCreateVirtualRouterSpeclistenersportMappingTypeDef = TypedDict(
    "_RequiredClientCreateVirtualRouterSpeclistenersportMappingTypeDef", {"port": int}
)
_OptionalClientCreateVirtualRouterSpeclistenersportMappingTypeDef = TypedDict(
    "_OptionalClientCreateVirtualRouterSpeclistenersportMappingTypeDef",
    {"protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)


class ClientCreateVirtualRouterSpeclistenersportMappingTypeDef(
    _RequiredClientCreateVirtualRouterSpeclistenersportMappingTypeDef,
    _OptionalClientCreateVirtualRouterSpeclistenersportMappingTypeDef,
):
    pass


ClientCreateVirtualRouterSpeclistenersTypeDef = TypedDict(
    "ClientCreateVirtualRouterSpeclistenersTypeDef",
    {"portMapping": ClientCreateVirtualRouterSpeclistenersportMappingTypeDef},
)

ClientCreateVirtualRouterSpecTypeDef = TypedDict(
    "ClientCreateVirtualRouterSpecTypeDef",
    {"listeners": List[ClientCreateVirtualRouterSpeclistenersTypeDef]},
    total=False,
)

_RequiredClientCreateVirtualRouterTagsTypeDef = TypedDict(
    "_RequiredClientCreateVirtualRouterTagsTypeDef", {"key": str}
)
_OptionalClientCreateVirtualRouterTagsTypeDef = TypedDict(
    "_OptionalClientCreateVirtualRouterTagsTypeDef", {"value": str}, total=False
)


class ClientCreateVirtualRouterTagsTypeDef(
    _RequiredClientCreateVirtualRouterTagsTypeDef, _OptionalClientCreateVirtualRouterTagsTypeDef
):
    pass


ClientCreateVirtualServiceResponsevirtualServicemetadataTypeDef = TypedDict(
    "ClientCreateVirtualServiceResponsevirtualServicemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef = TypedDict(
    "ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    {"virtualNodeName": str},
    total=False,
)

ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef = TypedDict(
    "ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    {"virtualRouterName": str},
    total=False,
)

ClientCreateVirtualServiceResponsevirtualServicespecproviderTypeDef = TypedDict(
    "ClientCreateVirtualServiceResponsevirtualServicespecproviderTypeDef",
    {
        "virtualNode": ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef,
        "virtualRouter": ClientCreateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef,
    },
    total=False,
)

ClientCreateVirtualServiceResponsevirtualServicespecTypeDef = TypedDict(
    "ClientCreateVirtualServiceResponsevirtualServicespecTypeDef",
    {"provider": ClientCreateVirtualServiceResponsevirtualServicespecproviderTypeDef},
    total=False,
)

ClientCreateVirtualServiceResponsevirtualServicestatusTypeDef = TypedDict(
    "ClientCreateVirtualServiceResponsevirtualServicestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientCreateVirtualServiceResponsevirtualServiceTypeDef = TypedDict(
    "ClientCreateVirtualServiceResponsevirtualServiceTypeDef",
    {
        "meshName": str,
        "metadata": ClientCreateVirtualServiceResponsevirtualServicemetadataTypeDef,
        "spec": ClientCreateVirtualServiceResponsevirtualServicespecTypeDef,
        "status": ClientCreateVirtualServiceResponsevirtualServicestatusTypeDef,
        "virtualServiceName": str,
    },
    total=False,
)

ClientCreateVirtualServiceResponseTypeDef = TypedDict(
    "ClientCreateVirtualServiceResponseTypeDef",
    {"virtualService": ClientCreateVirtualServiceResponsevirtualServiceTypeDef},
    total=False,
)

ClientCreateVirtualServiceSpecprovidervirtualNodeTypeDef = TypedDict(
    "ClientCreateVirtualServiceSpecprovidervirtualNodeTypeDef", {"virtualNodeName": str}
)

ClientCreateVirtualServiceSpecprovidervirtualRouterTypeDef = TypedDict(
    "ClientCreateVirtualServiceSpecprovidervirtualRouterTypeDef",
    {"virtualRouterName": str},
    total=False,
)

ClientCreateVirtualServiceSpecproviderTypeDef = TypedDict(
    "ClientCreateVirtualServiceSpecproviderTypeDef",
    {
        "virtualNode": ClientCreateVirtualServiceSpecprovidervirtualNodeTypeDef,
        "virtualRouter": ClientCreateVirtualServiceSpecprovidervirtualRouterTypeDef,
    },
    total=False,
)

ClientCreateVirtualServiceSpecTypeDef = TypedDict(
    "ClientCreateVirtualServiceSpecTypeDef",
    {"provider": ClientCreateVirtualServiceSpecproviderTypeDef},
    total=False,
)

_RequiredClientCreateVirtualServiceTagsTypeDef = TypedDict(
    "_RequiredClientCreateVirtualServiceTagsTypeDef", {"key": str}
)
_OptionalClientCreateVirtualServiceTagsTypeDef = TypedDict(
    "_OptionalClientCreateVirtualServiceTagsTypeDef", {"value": str}, total=False
)


class ClientCreateVirtualServiceTagsTypeDef(
    _RequiredClientCreateVirtualServiceTagsTypeDef, _OptionalClientCreateVirtualServiceTagsTypeDef
):
    pass


ClientDeleteMeshResponsemeshmetadataTypeDef = TypedDict(
    "ClientDeleteMeshResponsemeshmetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientDeleteMeshResponsemeshspecegressFilterTypeDef = TypedDict(
    "ClientDeleteMeshResponsemeshspecegressFilterTypeDef",
    {"type": Literal["ALLOW_ALL", "DROP_ALL"]},
    total=False,
)

ClientDeleteMeshResponsemeshspecTypeDef = TypedDict(
    "ClientDeleteMeshResponsemeshspecTypeDef",
    {"egressFilter": ClientDeleteMeshResponsemeshspecegressFilterTypeDef},
    total=False,
)

ClientDeleteMeshResponsemeshstatusTypeDef = TypedDict(
    "ClientDeleteMeshResponsemeshstatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientDeleteMeshResponsemeshTypeDef = TypedDict(
    "ClientDeleteMeshResponsemeshTypeDef",
    {
        "meshName": str,
        "metadata": ClientDeleteMeshResponsemeshmetadataTypeDef,
        "spec": ClientDeleteMeshResponsemeshspecTypeDef,
        "status": ClientDeleteMeshResponsemeshstatusTypeDef,
    },
    total=False,
)

ClientDeleteMeshResponseTypeDef = TypedDict(
    "ClientDeleteMeshResponseTypeDef", {"mesh": ClientDeleteMeshResponsemeshTypeDef}, total=False
)

ClientDeleteRouteResponseroutemetadataTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientDeleteRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientDeleteRouteResponseroutespecgrpcRouteactionTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespecgrpcRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDeleteRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)

ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)

ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

ClientDeleteRouteResponseroutespecgrpcRoutematchmetadataTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    {
        "invert": bool,
        "match": ClientDeleteRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef,
        "name": str,
    },
    total=False,
)

ClientDeleteRouteResponseroutespecgrpcRoutematchTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespecgrpcRoutematchTypeDef",
    {
        "metadata": List[ClientDeleteRouteResponseroutespecgrpcRoutematchmetadataTypeDef],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)

ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)

ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    {
        "grpcRetryEvents": List[
            Literal[
                "cancelled", "deadline-exceeded", "internal", "resource-exhausted", "unavailable"
            ]
        ],
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)

ClientDeleteRouteResponseroutespecgrpcRouteTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespecgrpcRouteTypeDef",
    {
        "action": ClientDeleteRouteResponseroutespecgrpcRouteactionTypeDef,
        "match": ClientDeleteRouteResponseroutespecgrpcRoutematchTypeDef,
        "retryPolicy": ClientDeleteRouteResponseroutespecgrpcRouteretryPolicyTypeDef,
    },
    total=False,
)

ClientDeleteRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientDeleteRouteResponseroutespechttp2RouteactionTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespechttp2RouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDeleteRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)

ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)

ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

ClientDeleteRouteResponseroutespechttp2RoutematchheadersTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespechttp2RoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientDeleteRouteResponseroutespechttp2RoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)

ClientDeleteRouteResponseroutespechttp2RoutematchTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespechttp2RoutematchTypeDef",
    {
        "headers": List[ClientDeleteRouteResponseroutespechttp2RoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)

ClientDeleteRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)

ClientDeleteRouteResponseroutespechttp2RouteretryPolicyTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientDeleteRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)

ClientDeleteRouteResponseroutespechttp2RouteTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespechttp2RouteTypeDef",
    {
        "action": ClientDeleteRouteResponseroutespechttp2RouteactionTypeDef,
        "match": ClientDeleteRouteResponseroutespechttp2RoutematchTypeDef,
        "retryPolicy": ClientDeleteRouteResponseroutespechttp2RouteretryPolicyTypeDef,
    },
    total=False,
)

ClientDeleteRouteResponseroutespechttpRouteactionweightedTargetsTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientDeleteRouteResponseroutespechttpRouteactionTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespechttpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDeleteRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)

ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)

ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

ClientDeleteRouteResponseroutespechttpRoutematchheadersTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespechttpRoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientDeleteRouteResponseroutespechttpRoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)

ClientDeleteRouteResponseroutespechttpRoutematchTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespechttpRoutematchTypeDef",
    {
        "headers": List[ClientDeleteRouteResponseroutespechttpRoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)

ClientDeleteRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)

ClientDeleteRouteResponseroutespechttpRouteretryPolicyTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespechttpRouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientDeleteRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)

ClientDeleteRouteResponseroutespechttpRouteTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespechttpRouteTypeDef",
    {
        "action": ClientDeleteRouteResponseroutespechttpRouteactionTypeDef,
        "match": ClientDeleteRouteResponseroutespechttpRoutematchTypeDef,
        "retryPolicy": ClientDeleteRouteResponseroutespechttpRouteretryPolicyTypeDef,
    },
    total=False,
)

ClientDeleteRouteResponseroutespectcpRouteactionweightedTargetsTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientDeleteRouteResponseroutespectcpRouteactionTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespectcpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDeleteRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)

ClientDeleteRouteResponseroutespectcpRouteTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespectcpRouteTypeDef",
    {"action": ClientDeleteRouteResponseroutespectcpRouteactionTypeDef},
    total=False,
)

ClientDeleteRouteResponseroutespecTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutespecTypeDef",
    {
        "grpcRoute": ClientDeleteRouteResponseroutespecgrpcRouteTypeDef,
        "http2Route": ClientDeleteRouteResponseroutespechttp2RouteTypeDef,
        "httpRoute": ClientDeleteRouteResponseroutespechttpRouteTypeDef,
        "priority": int,
        "tcpRoute": ClientDeleteRouteResponseroutespectcpRouteTypeDef,
    },
    total=False,
)

ClientDeleteRouteResponseroutestatusTypeDef = TypedDict(
    "ClientDeleteRouteResponseroutestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientDeleteRouteResponserouteTypeDef = TypedDict(
    "ClientDeleteRouteResponserouteTypeDef",
    {
        "meshName": str,
        "metadata": ClientDeleteRouteResponseroutemetadataTypeDef,
        "routeName": str,
        "spec": ClientDeleteRouteResponseroutespecTypeDef,
        "status": ClientDeleteRouteResponseroutestatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)

ClientDeleteRouteResponseTypeDef = TypedDict(
    "ClientDeleteRouteResponseTypeDef",
    {"route": ClientDeleteRouteResponserouteTypeDef},
    total=False,
)

ClientDeleteVirtualNodeResponsevirtualNodemetadataTypeDef = TypedDict(
    "ClientDeleteVirtualNodeResponsevirtualNodemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientDeleteVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef = TypedDict(
    "ClientDeleteVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    {"virtualServiceName": str},
    total=False,
)

ClientDeleteVirtualNodeResponsevirtualNodespecbackendsTypeDef = TypedDict(
    "ClientDeleteVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    {"virtualService": ClientDeleteVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef},
    total=False,
)

ClientDeleteVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef = TypedDict(
    "ClientDeleteVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "path": str,
        "port": int,
        "protocol": Literal["grpc", "http", "http2", "tcp"],
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
    total=False,
)

ClientDeleteVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef = TypedDict(
    "ClientDeleteVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)

ClientDeleteVirtualNodeResponsevirtualNodespeclistenersTypeDef = TypedDict(
    "ClientDeleteVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    {
        "healthCheck": ClientDeleteVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef,
        "portMapping": ClientDeleteVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef,
    },
    total=False,
)

ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef = TypedDict(
    "ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    {"path": str},
    total=False,
)

ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef = TypedDict(
    "ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    {"file": ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef},
    total=False,
)

ClientDeleteVirtualNodeResponsevirtualNodespecloggingTypeDef = TypedDict(
    "ClientDeleteVirtualNodeResponsevirtualNodespecloggingTypeDef",
    {"accessLog": ClientDeleteVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef},
    total=False,
)

ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef = TypedDict(
    "ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    {
        "attributes": List[
            ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
        ],
        "namespaceName": str,
        "serviceName": str,
    },
    total=False,
)

ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef = TypedDict(
    "ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    {"hostname": str},
    total=False,
)

ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef = TypedDict(
    "ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    {
        "awsCloudMap": ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef,
        "dns": ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef,
    },
    total=False,
)

ClientDeleteVirtualNodeResponsevirtualNodespecTypeDef = TypedDict(
    "ClientDeleteVirtualNodeResponsevirtualNodespecTypeDef",
    {
        "backends": List[ClientDeleteVirtualNodeResponsevirtualNodespecbackendsTypeDef],
        "listeners": List[ClientDeleteVirtualNodeResponsevirtualNodespeclistenersTypeDef],
        "logging": ClientDeleteVirtualNodeResponsevirtualNodespecloggingTypeDef,
        "serviceDiscovery": ClientDeleteVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef,
    },
    total=False,
)

ClientDeleteVirtualNodeResponsevirtualNodestatusTypeDef = TypedDict(
    "ClientDeleteVirtualNodeResponsevirtualNodestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientDeleteVirtualNodeResponsevirtualNodeTypeDef = TypedDict(
    "ClientDeleteVirtualNodeResponsevirtualNodeTypeDef",
    {
        "meshName": str,
        "metadata": ClientDeleteVirtualNodeResponsevirtualNodemetadataTypeDef,
        "spec": ClientDeleteVirtualNodeResponsevirtualNodespecTypeDef,
        "status": ClientDeleteVirtualNodeResponsevirtualNodestatusTypeDef,
        "virtualNodeName": str,
    },
    total=False,
)

ClientDeleteVirtualNodeResponseTypeDef = TypedDict(
    "ClientDeleteVirtualNodeResponseTypeDef",
    {"virtualNode": ClientDeleteVirtualNodeResponsevirtualNodeTypeDef},
    total=False,
)

ClientDeleteVirtualRouterResponsevirtualRoutermetadataTypeDef = TypedDict(
    "ClientDeleteVirtualRouterResponsevirtualRoutermetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef = TypedDict(
    "ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)

ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersTypeDef = TypedDict(
    "ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    {"portMapping": ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef},
    total=False,
)

ClientDeleteVirtualRouterResponsevirtualRouterspecTypeDef = TypedDict(
    "ClientDeleteVirtualRouterResponsevirtualRouterspecTypeDef",
    {"listeners": List[ClientDeleteVirtualRouterResponsevirtualRouterspeclistenersTypeDef]},
    total=False,
)

ClientDeleteVirtualRouterResponsevirtualRouterstatusTypeDef = TypedDict(
    "ClientDeleteVirtualRouterResponsevirtualRouterstatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientDeleteVirtualRouterResponsevirtualRouterTypeDef = TypedDict(
    "ClientDeleteVirtualRouterResponsevirtualRouterTypeDef",
    {
        "meshName": str,
        "metadata": ClientDeleteVirtualRouterResponsevirtualRoutermetadataTypeDef,
        "spec": ClientDeleteVirtualRouterResponsevirtualRouterspecTypeDef,
        "status": ClientDeleteVirtualRouterResponsevirtualRouterstatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)

ClientDeleteVirtualRouterResponseTypeDef = TypedDict(
    "ClientDeleteVirtualRouterResponseTypeDef",
    {"virtualRouter": ClientDeleteVirtualRouterResponsevirtualRouterTypeDef},
    total=False,
)

ClientDeleteVirtualServiceResponsevirtualServicemetadataTypeDef = TypedDict(
    "ClientDeleteVirtualServiceResponsevirtualServicemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef = TypedDict(
    "ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    {"virtualNodeName": str},
    total=False,
)

ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef = TypedDict(
    "ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    {"virtualRouterName": str},
    total=False,
)

ClientDeleteVirtualServiceResponsevirtualServicespecproviderTypeDef = TypedDict(
    "ClientDeleteVirtualServiceResponsevirtualServicespecproviderTypeDef",
    {
        "virtualNode": ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef,
        "virtualRouter": ClientDeleteVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef,
    },
    total=False,
)

ClientDeleteVirtualServiceResponsevirtualServicespecTypeDef = TypedDict(
    "ClientDeleteVirtualServiceResponsevirtualServicespecTypeDef",
    {"provider": ClientDeleteVirtualServiceResponsevirtualServicespecproviderTypeDef},
    total=False,
)

ClientDeleteVirtualServiceResponsevirtualServicestatusTypeDef = TypedDict(
    "ClientDeleteVirtualServiceResponsevirtualServicestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientDeleteVirtualServiceResponsevirtualServiceTypeDef = TypedDict(
    "ClientDeleteVirtualServiceResponsevirtualServiceTypeDef",
    {
        "meshName": str,
        "metadata": ClientDeleteVirtualServiceResponsevirtualServicemetadataTypeDef,
        "spec": ClientDeleteVirtualServiceResponsevirtualServicespecTypeDef,
        "status": ClientDeleteVirtualServiceResponsevirtualServicestatusTypeDef,
        "virtualServiceName": str,
    },
    total=False,
)

ClientDeleteVirtualServiceResponseTypeDef = TypedDict(
    "ClientDeleteVirtualServiceResponseTypeDef",
    {"virtualService": ClientDeleteVirtualServiceResponsevirtualServiceTypeDef},
    total=False,
)

ClientDescribeMeshResponsemeshmetadataTypeDef = TypedDict(
    "ClientDescribeMeshResponsemeshmetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientDescribeMeshResponsemeshspecegressFilterTypeDef = TypedDict(
    "ClientDescribeMeshResponsemeshspecegressFilterTypeDef",
    {"type": Literal["ALLOW_ALL", "DROP_ALL"]},
    total=False,
)

ClientDescribeMeshResponsemeshspecTypeDef = TypedDict(
    "ClientDescribeMeshResponsemeshspecTypeDef",
    {"egressFilter": ClientDescribeMeshResponsemeshspecegressFilterTypeDef},
    total=False,
)

ClientDescribeMeshResponsemeshstatusTypeDef = TypedDict(
    "ClientDescribeMeshResponsemeshstatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientDescribeMeshResponsemeshTypeDef = TypedDict(
    "ClientDescribeMeshResponsemeshTypeDef",
    {
        "meshName": str,
        "metadata": ClientDescribeMeshResponsemeshmetadataTypeDef,
        "spec": ClientDescribeMeshResponsemeshspecTypeDef,
        "status": ClientDescribeMeshResponsemeshstatusTypeDef,
    },
    total=False,
)

ClientDescribeMeshResponseTypeDef = TypedDict(
    "ClientDescribeMeshResponseTypeDef",
    {"mesh": ClientDescribeMeshResponsemeshTypeDef},
    total=False,
)

ClientDescribeRouteResponseroutemetadataTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientDescribeRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientDescribeRouteResponseroutespecgrpcRouteactionTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespecgrpcRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDescribeRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)

ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)

ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

ClientDescribeRouteResponseroutespecgrpcRoutematchmetadataTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    {
        "invert": bool,
        "match": ClientDescribeRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef,
        "name": str,
    },
    total=False,
)

ClientDescribeRouteResponseroutespecgrpcRoutematchTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespecgrpcRoutematchTypeDef",
    {
        "metadata": List[ClientDescribeRouteResponseroutespecgrpcRoutematchmetadataTypeDef],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)

ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)

ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    {
        "grpcRetryEvents": List[
            Literal[
                "cancelled", "deadline-exceeded", "internal", "resource-exhausted", "unavailable"
            ]
        ],
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)

ClientDescribeRouteResponseroutespecgrpcRouteTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespecgrpcRouteTypeDef",
    {
        "action": ClientDescribeRouteResponseroutespecgrpcRouteactionTypeDef,
        "match": ClientDescribeRouteResponseroutespecgrpcRoutematchTypeDef,
        "retryPolicy": ClientDescribeRouteResponseroutespecgrpcRouteretryPolicyTypeDef,
    },
    total=False,
)

ClientDescribeRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientDescribeRouteResponseroutespechttp2RouteactionTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespechttp2RouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDescribeRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)

ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)

ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

ClientDescribeRouteResponseroutespechttp2RoutematchheadersTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespechttp2RoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientDescribeRouteResponseroutespechttp2RoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)

ClientDescribeRouteResponseroutespechttp2RoutematchTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespechttp2RoutematchTypeDef",
    {
        "headers": List[ClientDescribeRouteResponseroutespechttp2RoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)

ClientDescribeRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)

ClientDescribeRouteResponseroutespechttp2RouteretryPolicyTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientDescribeRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)

ClientDescribeRouteResponseroutespechttp2RouteTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespechttp2RouteTypeDef",
    {
        "action": ClientDescribeRouteResponseroutespechttp2RouteactionTypeDef,
        "match": ClientDescribeRouteResponseroutespechttp2RoutematchTypeDef,
        "retryPolicy": ClientDescribeRouteResponseroutespechttp2RouteretryPolicyTypeDef,
    },
    total=False,
)

ClientDescribeRouteResponseroutespechttpRouteactionweightedTargetsTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientDescribeRouteResponseroutespechttpRouteactionTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespechttpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDescribeRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)

ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)

ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

ClientDescribeRouteResponseroutespechttpRoutematchheadersTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespechttpRoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientDescribeRouteResponseroutespechttpRoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)

ClientDescribeRouteResponseroutespechttpRoutematchTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespechttpRoutematchTypeDef",
    {
        "headers": List[ClientDescribeRouteResponseroutespechttpRoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)

ClientDescribeRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)

ClientDescribeRouteResponseroutespechttpRouteretryPolicyTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespechttpRouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientDescribeRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)

ClientDescribeRouteResponseroutespechttpRouteTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespechttpRouteTypeDef",
    {
        "action": ClientDescribeRouteResponseroutespechttpRouteactionTypeDef,
        "match": ClientDescribeRouteResponseroutespechttpRoutematchTypeDef,
        "retryPolicy": ClientDescribeRouteResponseroutespechttpRouteretryPolicyTypeDef,
    },
    total=False,
)

ClientDescribeRouteResponseroutespectcpRouteactionweightedTargetsTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientDescribeRouteResponseroutespectcpRouteactionTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespectcpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientDescribeRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)

ClientDescribeRouteResponseroutespectcpRouteTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespectcpRouteTypeDef",
    {"action": ClientDescribeRouteResponseroutespectcpRouteactionTypeDef},
    total=False,
)

ClientDescribeRouteResponseroutespecTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutespecTypeDef",
    {
        "grpcRoute": ClientDescribeRouteResponseroutespecgrpcRouteTypeDef,
        "http2Route": ClientDescribeRouteResponseroutespechttp2RouteTypeDef,
        "httpRoute": ClientDescribeRouteResponseroutespechttpRouteTypeDef,
        "priority": int,
        "tcpRoute": ClientDescribeRouteResponseroutespectcpRouteTypeDef,
    },
    total=False,
)

ClientDescribeRouteResponseroutestatusTypeDef = TypedDict(
    "ClientDescribeRouteResponseroutestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientDescribeRouteResponserouteTypeDef = TypedDict(
    "ClientDescribeRouteResponserouteTypeDef",
    {
        "meshName": str,
        "metadata": ClientDescribeRouteResponseroutemetadataTypeDef,
        "routeName": str,
        "spec": ClientDescribeRouteResponseroutespecTypeDef,
        "status": ClientDescribeRouteResponseroutestatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)

ClientDescribeRouteResponseTypeDef = TypedDict(
    "ClientDescribeRouteResponseTypeDef",
    {"route": ClientDescribeRouteResponserouteTypeDef},
    total=False,
)

ClientDescribeVirtualNodeResponsevirtualNodemetadataTypeDef = TypedDict(
    "ClientDescribeVirtualNodeResponsevirtualNodemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientDescribeVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef = TypedDict(
    "ClientDescribeVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    {"virtualServiceName": str},
    total=False,
)

ClientDescribeVirtualNodeResponsevirtualNodespecbackendsTypeDef = TypedDict(
    "ClientDescribeVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    {
        "virtualService": ClientDescribeVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef
    },
    total=False,
)

ClientDescribeVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef = TypedDict(
    "ClientDescribeVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "path": str,
        "port": int,
        "protocol": Literal["grpc", "http", "http2", "tcp"],
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
    total=False,
)

ClientDescribeVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef = TypedDict(
    "ClientDescribeVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)

ClientDescribeVirtualNodeResponsevirtualNodespeclistenersTypeDef = TypedDict(
    "ClientDescribeVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    {
        "healthCheck": ClientDescribeVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef,
        "portMapping": ClientDescribeVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef,
    },
    total=False,
)

ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef = TypedDict(
    "ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    {"path": str},
    total=False,
)

ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef = TypedDict(
    "ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    {"file": ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef},
    total=False,
)

ClientDescribeVirtualNodeResponsevirtualNodespecloggingTypeDef = TypedDict(
    "ClientDescribeVirtualNodeResponsevirtualNodespecloggingTypeDef",
    {"accessLog": ClientDescribeVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef},
    total=False,
)

ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef = TypedDict(
    "ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    {
        "attributes": List[
            ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
        ],
        "namespaceName": str,
        "serviceName": str,
    },
    total=False,
)

ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef = TypedDict(
    "ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    {"hostname": str},
    total=False,
)

ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef = TypedDict(
    "ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    {
        "awsCloudMap": ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef,
        "dns": ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef,
    },
    total=False,
)

ClientDescribeVirtualNodeResponsevirtualNodespecTypeDef = TypedDict(
    "ClientDescribeVirtualNodeResponsevirtualNodespecTypeDef",
    {
        "backends": List[ClientDescribeVirtualNodeResponsevirtualNodespecbackendsTypeDef],
        "listeners": List[ClientDescribeVirtualNodeResponsevirtualNodespeclistenersTypeDef],
        "logging": ClientDescribeVirtualNodeResponsevirtualNodespecloggingTypeDef,
        "serviceDiscovery": ClientDescribeVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef,
    },
    total=False,
)

ClientDescribeVirtualNodeResponsevirtualNodestatusTypeDef = TypedDict(
    "ClientDescribeVirtualNodeResponsevirtualNodestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientDescribeVirtualNodeResponsevirtualNodeTypeDef = TypedDict(
    "ClientDescribeVirtualNodeResponsevirtualNodeTypeDef",
    {
        "meshName": str,
        "metadata": ClientDescribeVirtualNodeResponsevirtualNodemetadataTypeDef,
        "spec": ClientDescribeVirtualNodeResponsevirtualNodespecTypeDef,
        "status": ClientDescribeVirtualNodeResponsevirtualNodestatusTypeDef,
        "virtualNodeName": str,
    },
    total=False,
)

ClientDescribeVirtualNodeResponseTypeDef = TypedDict(
    "ClientDescribeVirtualNodeResponseTypeDef",
    {"virtualNode": ClientDescribeVirtualNodeResponsevirtualNodeTypeDef},
    total=False,
)

ClientDescribeVirtualRouterResponsevirtualRoutermetadataTypeDef = TypedDict(
    "ClientDescribeVirtualRouterResponsevirtualRoutermetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef = TypedDict(
    "ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)

ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersTypeDef = TypedDict(
    "ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    {
        "portMapping": ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef
    },
    total=False,
)

ClientDescribeVirtualRouterResponsevirtualRouterspecTypeDef = TypedDict(
    "ClientDescribeVirtualRouterResponsevirtualRouterspecTypeDef",
    {"listeners": List[ClientDescribeVirtualRouterResponsevirtualRouterspeclistenersTypeDef]},
    total=False,
)

ClientDescribeVirtualRouterResponsevirtualRouterstatusTypeDef = TypedDict(
    "ClientDescribeVirtualRouterResponsevirtualRouterstatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientDescribeVirtualRouterResponsevirtualRouterTypeDef = TypedDict(
    "ClientDescribeVirtualRouterResponsevirtualRouterTypeDef",
    {
        "meshName": str,
        "metadata": ClientDescribeVirtualRouterResponsevirtualRoutermetadataTypeDef,
        "spec": ClientDescribeVirtualRouterResponsevirtualRouterspecTypeDef,
        "status": ClientDescribeVirtualRouterResponsevirtualRouterstatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)

ClientDescribeVirtualRouterResponseTypeDef = TypedDict(
    "ClientDescribeVirtualRouterResponseTypeDef",
    {"virtualRouter": ClientDescribeVirtualRouterResponsevirtualRouterTypeDef},
    total=False,
)

ClientDescribeVirtualServiceResponsevirtualServicemetadataTypeDef = TypedDict(
    "ClientDescribeVirtualServiceResponsevirtualServicemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef = TypedDict(
    "ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    {"virtualNodeName": str},
    total=False,
)

ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef = TypedDict(
    "ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    {"virtualRouterName": str},
    total=False,
)

ClientDescribeVirtualServiceResponsevirtualServicespecproviderTypeDef = TypedDict(
    "ClientDescribeVirtualServiceResponsevirtualServicespecproviderTypeDef",
    {
        "virtualNode": ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef,
        "virtualRouter": ClientDescribeVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef,
    },
    total=False,
)

ClientDescribeVirtualServiceResponsevirtualServicespecTypeDef = TypedDict(
    "ClientDescribeVirtualServiceResponsevirtualServicespecTypeDef",
    {"provider": ClientDescribeVirtualServiceResponsevirtualServicespecproviderTypeDef},
    total=False,
)

ClientDescribeVirtualServiceResponsevirtualServicestatusTypeDef = TypedDict(
    "ClientDescribeVirtualServiceResponsevirtualServicestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientDescribeVirtualServiceResponsevirtualServiceTypeDef = TypedDict(
    "ClientDescribeVirtualServiceResponsevirtualServiceTypeDef",
    {
        "meshName": str,
        "metadata": ClientDescribeVirtualServiceResponsevirtualServicemetadataTypeDef,
        "spec": ClientDescribeVirtualServiceResponsevirtualServicespecTypeDef,
        "status": ClientDescribeVirtualServiceResponsevirtualServicestatusTypeDef,
        "virtualServiceName": str,
    },
    total=False,
)

ClientDescribeVirtualServiceResponseTypeDef = TypedDict(
    "ClientDescribeVirtualServiceResponseTypeDef",
    {"virtualService": ClientDescribeVirtualServiceResponsevirtualServiceTypeDef},
    total=False,
)

ClientListMeshesResponsemeshesTypeDef = TypedDict(
    "ClientListMeshesResponsemeshesTypeDef", {"arn": str, "meshName": str}, total=False
)

ClientListMeshesResponseTypeDef = TypedDict(
    "ClientListMeshesResponseTypeDef",
    {"meshes": List[ClientListMeshesResponsemeshesTypeDef], "nextToken": str},
    total=False,
)

ClientListRoutesResponseroutesTypeDef = TypedDict(
    "ClientListRoutesResponseroutesTypeDef",
    {"arn": str, "meshName": str, "routeName": str, "virtualRouterName": str},
    total=False,
)

ClientListRoutesResponseTypeDef = TypedDict(
    "ClientListRoutesResponseTypeDef",
    {"nextToken": str, "routes": List[ClientListRoutesResponseroutesTypeDef]},
    total=False,
)

ClientListTagsForResourceResponsetagsTypeDef = TypedDict(
    "ClientListTagsForResourceResponsetagsTypeDef", {"key": str, "value": str}, total=False
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"nextToken": str, "tags": List[ClientListTagsForResourceResponsetagsTypeDef]},
    total=False,
)

ClientListVirtualNodesResponsevirtualNodesTypeDef = TypedDict(
    "ClientListVirtualNodesResponsevirtualNodesTypeDef",
    {"arn": str, "meshName": str, "virtualNodeName": str},
    total=False,
)

ClientListVirtualNodesResponseTypeDef = TypedDict(
    "ClientListVirtualNodesResponseTypeDef",
    {"nextToken": str, "virtualNodes": List[ClientListVirtualNodesResponsevirtualNodesTypeDef]},
    total=False,
)

ClientListVirtualRoutersResponsevirtualRoutersTypeDef = TypedDict(
    "ClientListVirtualRoutersResponsevirtualRoutersTypeDef",
    {"arn": str, "meshName": str, "virtualRouterName": str},
    total=False,
)

ClientListVirtualRoutersResponseTypeDef = TypedDict(
    "ClientListVirtualRoutersResponseTypeDef",
    {
        "nextToken": str,
        "virtualRouters": List[ClientListVirtualRoutersResponsevirtualRoutersTypeDef],
    },
    total=False,
)

ClientListVirtualServicesResponsevirtualServicesTypeDef = TypedDict(
    "ClientListVirtualServicesResponsevirtualServicesTypeDef",
    {"arn": str, "meshName": str, "virtualServiceName": str},
    total=False,
)

ClientListVirtualServicesResponseTypeDef = TypedDict(
    "ClientListVirtualServicesResponseTypeDef",
    {
        "nextToken": str,
        "virtualServices": List[ClientListVirtualServicesResponsevirtualServicesTypeDef],
    },
    total=False,
)

_RequiredClientTagResourceTagsTypeDef = TypedDict(
    "_RequiredClientTagResourceTagsTypeDef", {"key": str}
)
_OptionalClientTagResourceTagsTypeDef = TypedDict(
    "_OptionalClientTagResourceTagsTypeDef", {"value": str}, total=False
)


class ClientTagResourceTagsTypeDef(
    _RequiredClientTagResourceTagsTypeDef, _OptionalClientTagResourceTagsTypeDef
):
    pass


ClientUpdateMeshResponsemeshmetadataTypeDef = TypedDict(
    "ClientUpdateMeshResponsemeshmetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientUpdateMeshResponsemeshspecegressFilterTypeDef = TypedDict(
    "ClientUpdateMeshResponsemeshspecegressFilterTypeDef",
    {"type": Literal["ALLOW_ALL", "DROP_ALL"]},
    total=False,
)

ClientUpdateMeshResponsemeshspecTypeDef = TypedDict(
    "ClientUpdateMeshResponsemeshspecTypeDef",
    {"egressFilter": ClientUpdateMeshResponsemeshspecegressFilterTypeDef},
    total=False,
)

ClientUpdateMeshResponsemeshstatusTypeDef = TypedDict(
    "ClientUpdateMeshResponsemeshstatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientUpdateMeshResponsemeshTypeDef = TypedDict(
    "ClientUpdateMeshResponsemeshTypeDef",
    {
        "meshName": str,
        "metadata": ClientUpdateMeshResponsemeshmetadataTypeDef,
        "spec": ClientUpdateMeshResponsemeshspecTypeDef,
        "status": ClientUpdateMeshResponsemeshstatusTypeDef,
    },
    total=False,
)

ClientUpdateMeshResponseTypeDef = TypedDict(
    "ClientUpdateMeshResponseTypeDef", {"mesh": ClientUpdateMeshResponsemeshTypeDef}, total=False
)

ClientUpdateMeshSpecegressFilterTypeDef = TypedDict(
    "ClientUpdateMeshSpecegressFilterTypeDef", {"type": Literal["ALLOW_ALL", "DROP_ALL"]}
)

ClientUpdateMeshSpecTypeDef = TypedDict(
    "ClientUpdateMeshSpecTypeDef",
    {"egressFilter": ClientUpdateMeshSpecegressFilterTypeDef},
    total=False,
)

ClientUpdateRouteResponseroutemetadataTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientUpdateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientUpdateRouteResponseroutespecgrpcRouteactionTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespecgrpcRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientUpdateRouteResponseroutespecgrpcRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)

ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)

ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

ClientUpdateRouteResponseroutespecgrpcRoutematchmetadataTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespecgrpcRoutematchmetadataTypeDef",
    {
        "invert": bool,
        "match": ClientUpdateRouteResponseroutespecgrpcRoutematchmetadatamatchTypeDef,
        "name": str,
    },
    total=False,
)

ClientUpdateRouteResponseroutespecgrpcRoutematchTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespecgrpcRoutematchTypeDef",
    {
        "metadata": List[ClientUpdateRouteResponseroutespecgrpcRoutematchmetadataTypeDef],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)

ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)

ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyTypeDef",
    {
        "grpcRetryEvents": List[
            Literal[
                "cancelled", "deadline-exceeded", "internal", "resource-exhausted", "unavailable"
            ]
        ],
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)

ClientUpdateRouteResponseroutespecgrpcRouteTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespecgrpcRouteTypeDef",
    {
        "action": ClientUpdateRouteResponseroutespecgrpcRouteactionTypeDef,
        "match": ClientUpdateRouteResponseroutespecgrpcRoutematchTypeDef,
        "retryPolicy": ClientUpdateRouteResponseroutespecgrpcRouteretryPolicyTypeDef,
    },
    total=False,
)

ClientUpdateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientUpdateRouteResponseroutespechttp2RouteactionTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespechttp2RouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientUpdateRouteResponseroutespechttp2RouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)

ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)

ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

ClientUpdateRouteResponseroutespechttp2RoutematchheadersTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespechttp2RoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientUpdateRouteResponseroutespechttp2RoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)

ClientUpdateRouteResponseroutespechttp2RoutematchTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespechttp2RoutematchTypeDef",
    {
        "headers": List[ClientUpdateRouteResponseroutespechttp2RoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)

ClientUpdateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)

ClientUpdateRouteResponseroutespechttp2RouteretryPolicyTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespechttp2RouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientUpdateRouteResponseroutespechttp2RouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)

ClientUpdateRouteResponseroutespechttp2RouteTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespechttp2RouteTypeDef",
    {
        "action": ClientUpdateRouteResponseroutespechttp2RouteactionTypeDef,
        "match": ClientUpdateRouteResponseroutespechttp2RoutematchTypeDef,
        "retryPolicy": ClientUpdateRouteResponseroutespechttp2RouteretryPolicyTypeDef,
    },
    total=False,
)

ClientUpdateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientUpdateRouteResponseroutespechttpRouteactionTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespechttpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientUpdateRouteResponseroutespechttpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)

ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)

ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

ClientUpdateRouteResponseroutespechttpRoutematchheadersTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespechttpRoutematchheadersTypeDef",
    {
        "invert": bool,
        "match": ClientUpdateRouteResponseroutespechttpRoutematchheadersmatchTypeDef,
        "name": str,
    },
    total=False,
)

ClientUpdateRouteResponseroutespechttpRoutematchTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespechttpRoutematchTypeDef",
    {
        "headers": List[ClientUpdateRouteResponseroutespechttpRoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)

ClientUpdateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)

ClientUpdateRouteResponseroutespechttpRouteretryPolicyTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespechttpRouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientUpdateRouteResponseroutespechttpRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)

ClientUpdateRouteResponseroutespechttpRouteTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespechttpRouteTypeDef",
    {
        "action": ClientUpdateRouteResponseroutespechttpRouteactionTypeDef,
        "match": ClientUpdateRouteResponseroutespechttpRoutematchTypeDef,
        "retryPolicy": ClientUpdateRouteResponseroutespechttpRouteretryPolicyTypeDef,
    },
    total=False,
)

ClientUpdateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientUpdateRouteResponseroutespectcpRouteactionTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespectcpRouteactionTypeDef",
    {
        "weightedTargets": List[
            ClientUpdateRouteResponseroutespectcpRouteactionweightedTargetsTypeDef
        ]
    },
    total=False,
)

ClientUpdateRouteResponseroutespectcpRouteTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespectcpRouteTypeDef",
    {"action": ClientUpdateRouteResponseroutespectcpRouteactionTypeDef},
    total=False,
)

ClientUpdateRouteResponseroutespecTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutespecTypeDef",
    {
        "grpcRoute": ClientUpdateRouteResponseroutespecgrpcRouteTypeDef,
        "http2Route": ClientUpdateRouteResponseroutespechttp2RouteTypeDef,
        "httpRoute": ClientUpdateRouteResponseroutespechttpRouteTypeDef,
        "priority": int,
        "tcpRoute": ClientUpdateRouteResponseroutespectcpRouteTypeDef,
    },
    total=False,
)

ClientUpdateRouteResponseroutestatusTypeDef = TypedDict(
    "ClientUpdateRouteResponseroutestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientUpdateRouteResponserouteTypeDef = TypedDict(
    "ClientUpdateRouteResponserouteTypeDef",
    {
        "meshName": str,
        "metadata": ClientUpdateRouteResponseroutemetadataTypeDef,
        "routeName": str,
        "spec": ClientUpdateRouteResponseroutespecTypeDef,
        "status": ClientUpdateRouteResponseroutestatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)

ClientUpdateRouteResponseTypeDef = TypedDict(
    "ClientUpdateRouteResponseTypeDef",
    {"route": ClientUpdateRouteResponserouteTypeDef},
    total=False,
)

_RequiredClientUpdateRouteSpecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "_RequiredClientUpdateRouteSpecgrpcRouteactionweightedTargetsTypeDef", {"virtualNode": str}
)
_OptionalClientUpdateRouteSpecgrpcRouteactionweightedTargetsTypeDef = TypedDict(
    "_OptionalClientUpdateRouteSpecgrpcRouteactionweightedTargetsTypeDef",
    {"weight": int},
    total=False,
)


class ClientUpdateRouteSpecgrpcRouteactionweightedTargetsTypeDef(
    _RequiredClientUpdateRouteSpecgrpcRouteactionweightedTargetsTypeDef,
    _OptionalClientUpdateRouteSpecgrpcRouteactionweightedTargetsTypeDef,
):
    pass


ClientUpdateRouteSpecgrpcRouteactionTypeDef = TypedDict(
    "ClientUpdateRouteSpecgrpcRouteactionTypeDef",
    {"weightedTargets": List[ClientUpdateRouteSpecgrpcRouteactionweightedTargetsTypeDef]},
)

ClientUpdateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef = TypedDict(
    "ClientUpdateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)

ClientUpdateRouteSpecgrpcRoutematchmetadatamatchTypeDef = TypedDict(
    "ClientUpdateRouteSpecgrpcRoutematchmetadatamatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientUpdateRouteSpecgrpcRoutematchmetadatamatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

ClientUpdateRouteSpecgrpcRoutematchmetadataTypeDef = TypedDict(
    "ClientUpdateRouteSpecgrpcRoutematchmetadataTypeDef",
    {"invert": bool, "match": ClientUpdateRouteSpecgrpcRoutematchmetadatamatchTypeDef, "name": str},
    total=False,
)

ClientUpdateRouteSpecgrpcRoutematchTypeDef = TypedDict(
    "ClientUpdateRouteSpecgrpcRoutematchTypeDef",
    {
        "metadata": List[ClientUpdateRouteSpecgrpcRoutematchmetadataTypeDef],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)

ClientUpdateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "ClientUpdateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)

ClientUpdateRouteSpecgrpcRouteretryPolicyTypeDef = TypedDict(
    "ClientUpdateRouteSpecgrpcRouteretryPolicyTypeDef",
    {
        "grpcRetryEvents": List[
            Literal[
                "cancelled", "deadline-exceeded", "internal", "resource-exhausted", "unavailable"
            ]
        ],
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientUpdateRouteSpecgrpcRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)

_RequiredClientUpdateRouteSpecgrpcRouteTypeDef = TypedDict(
    "_RequiredClientUpdateRouteSpecgrpcRouteTypeDef",
    {"action": ClientUpdateRouteSpecgrpcRouteactionTypeDef},
)
_OptionalClientUpdateRouteSpecgrpcRouteTypeDef = TypedDict(
    "_OptionalClientUpdateRouteSpecgrpcRouteTypeDef",
    {
        "match": ClientUpdateRouteSpecgrpcRoutematchTypeDef,
        "retryPolicy": ClientUpdateRouteSpecgrpcRouteretryPolicyTypeDef,
    },
    total=False,
)


class ClientUpdateRouteSpecgrpcRouteTypeDef(
    _RequiredClientUpdateRouteSpecgrpcRouteTypeDef, _OptionalClientUpdateRouteSpecgrpcRouteTypeDef
):
    pass


ClientUpdateRouteSpechttp2RouteactionweightedTargetsTypeDef = TypedDict(
    "ClientUpdateRouteSpechttp2RouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientUpdateRouteSpechttp2RouteactionTypeDef = TypedDict(
    "ClientUpdateRouteSpechttp2RouteactionTypeDef",
    {"weightedTargets": List[ClientUpdateRouteSpechttp2RouteactionweightedTargetsTypeDef]},
    total=False,
)

ClientUpdateRouteSpechttp2RoutematchheadersmatchrangeTypeDef = TypedDict(
    "ClientUpdateRouteSpechttp2RoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)

ClientUpdateRouteSpechttp2RoutematchheadersmatchTypeDef = TypedDict(
    "ClientUpdateRouteSpechttp2RoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientUpdateRouteSpechttp2RoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

ClientUpdateRouteSpechttp2RoutematchheadersTypeDef = TypedDict(
    "ClientUpdateRouteSpechttp2RoutematchheadersTypeDef",
    {"invert": bool, "match": ClientUpdateRouteSpechttp2RoutematchheadersmatchTypeDef, "name": str},
    total=False,
)

ClientUpdateRouteSpechttp2RoutematchTypeDef = TypedDict(
    "ClientUpdateRouteSpechttp2RoutematchTypeDef",
    {
        "headers": List[ClientUpdateRouteSpechttp2RoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)

ClientUpdateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "ClientUpdateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)

ClientUpdateRouteSpechttp2RouteretryPolicyTypeDef = TypedDict(
    "ClientUpdateRouteSpechttp2RouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientUpdateRouteSpechttp2RouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)

ClientUpdateRouteSpechttp2RouteTypeDef = TypedDict(
    "ClientUpdateRouteSpechttp2RouteTypeDef",
    {
        "action": ClientUpdateRouteSpechttp2RouteactionTypeDef,
        "match": ClientUpdateRouteSpechttp2RoutematchTypeDef,
        "retryPolicy": ClientUpdateRouteSpechttp2RouteretryPolicyTypeDef,
    },
    total=False,
)

ClientUpdateRouteSpechttpRouteactionweightedTargetsTypeDef = TypedDict(
    "ClientUpdateRouteSpechttpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientUpdateRouteSpechttpRouteactionTypeDef = TypedDict(
    "ClientUpdateRouteSpechttpRouteactionTypeDef",
    {"weightedTargets": List[ClientUpdateRouteSpechttpRouteactionweightedTargetsTypeDef]},
    total=False,
)

ClientUpdateRouteSpechttpRoutematchheadersmatchrangeTypeDef = TypedDict(
    "ClientUpdateRouteSpechttpRoutematchheadersmatchrangeTypeDef",
    {"end": int, "start": int},
    total=False,
)

ClientUpdateRouteSpechttpRoutematchheadersmatchTypeDef = TypedDict(
    "ClientUpdateRouteSpechttpRoutematchheadersmatchTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": ClientUpdateRouteSpechttpRoutematchheadersmatchrangeTypeDef,
        "regex": str,
        "suffix": str,
    },
    total=False,
)

ClientUpdateRouteSpechttpRoutematchheadersTypeDef = TypedDict(
    "ClientUpdateRouteSpechttpRoutematchheadersTypeDef",
    {"invert": bool, "match": ClientUpdateRouteSpechttpRoutematchheadersmatchTypeDef, "name": str},
    total=False,
)

ClientUpdateRouteSpechttpRoutematchTypeDef = TypedDict(
    "ClientUpdateRouteSpechttpRoutematchTypeDef",
    {
        "headers": List[ClientUpdateRouteSpechttpRoutematchheadersTypeDef],
        "method": Literal[
            "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"
        ],
        "prefix": str,
        "scheme": Literal["http", "https"],
    },
    total=False,
)

ClientUpdateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef = TypedDict(
    "ClientUpdateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef",
    {"unit": Literal["ms", "s"], "value": int},
    total=False,
)

ClientUpdateRouteSpechttpRouteretryPolicyTypeDef = TypedDict(
    "ClientUpdateRouteSpechttpRouteretryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "maxRetries": int,
        "perRetryTimeout": ClientUpdateRouteSpechttpRouteretryPolicyperRetryTimeoutTypeDef,
        "tcpRetryEvents": List[str],
    },
    total=False,
)

ClientUpdateRouteSpechttpRouteTypeDef = TypedDict(
    "ClientUpdateRouteSpechttpRouteTypeDef",
    {
        "action": ClientUpdateRouteSpechttpRouteactionTypeDef,
        "match": ClientUpdateRouteSpechttpRoutematchTypeDef,
        "retryPolicy": ClientUpdateRouteSpechttpRouteretryPolicyTypeDef,
    },
    total=False,
)

ClientUpdateRouteSpectcpRouteactionweightedTargetsTypeDef = TypedDict(
    "ClientUpdateRouteSpectcpRouteactionweightedTargetsTypeDef",
    {"virtualNode": str, "weight": int},
    total=False,
)

ClientUpdateRouteSpectcpRouteactionTypeDef = TypedDict(
    "ClientUpdateRouteSpectcpRouteactionTypeDef",
    {"weightedTargets": List[ClientUpdateRouteSpectcpRouteactionweightedTargetsTypeDef]},
    total=False,
)

ClientUpdateRouteSpectcpRouteTypeDef = TypedDict(
    "ClientUpdateRouteSpectcpRouteTypeDef",
    {"action": ClientUpdateRouteSpectcpRouteactionTypeDef},
    total=False,
)

ClientUpdateRouteSpecTypeDef = TypedDict(
    "ClientUpdateRouteSpecTypeDef",
    {
        "grpcRoute": ClientUpdateRouteSpecgrpcRouteTypeDef,
        "http2Route": ClientUpdateRouteSpechttp2RouteTypeDef,
        "httpRoute": ClientUpdateRouteSpechttpRouteTypeDef,
        "priority": int,
        "tcpRoute": ClientUpdateRouteSpectcpRouteTypeDef,
    },
    total=False,
)

ClientUpdateVirtualNodeResponsevirtualNodemetadataTypeDef = TypedDict(
    "ClientUpdateVirtualNodeResponsevirtualNodemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientUpdateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef = TypedDict(
    "ClientUpdateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef",
    {"virtualServiceName": str},
    total=False,
)

ClientUpdateVirtualNodeResponsevirtualNodespecbackendsTypeDef = TypedDict(
    "ClientUpdateVirtualNodeResponsevirtualNodespecbackendsTypeDef",
    {"virtualService": ClientUpdateVirtualNodeResponsevirtualNodespecbackendsvirtualServiceTypeDef},
    total=False,
)

ClientUpdateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef = TypedDict(
    "ClientUpdateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "path": str,
        "port": int,
        "protocol": Literal["grpc", "http", "http2", "tcp"],
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
    total=False,
)

ClientUpdateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef = TypedDict(
    "ClientUpdateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)

ClientUpdateVirtualNodeResponsevirtualNodespeclistenersTypeDef = TypedDict(
    "ClientUpdateVirtualNodeResponsevirtualNodespeclistenersTypeDef",
    {
        "healthCheck": ClientUpdateVirtualNodeResponsevirtualNodespeclistenershealthCheckTypeDef,
        "portMapping": ClientUpdateVirtualNodeResponsevirtualNodespeclistenersportMappingTypeDef,
    },
    total=False,
)

ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef = TypedDict(
    "ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef",
    {"path": str},
    total=False,
)

ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef = TypedDict(
    "ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef",
    {"file": ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogfileTypeDef},
    total=False,
)

ClientUpdateVirtualNodeResponsevirtualNodespecloggingTypeDef = TypedDict(
    "ClientUpdateVirtualNodeResponsevirtualNodespecloggingTypeDef",
    {"accessLog": ClientUpdateVirtualNodeResponsevirtualNodespecloggingaccessLogTypeDef},
    total=False,
)

ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef = TypedDict(
    "ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef",
    {
        "attributes": List[
            ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapattributesTypeDef
        ],
        "namespaceName": str,
        "serviceName": str,
    },
    total=False,
)

ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef = TypedDict(
    "ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef",
    {"hostname": str},
    total=False,
)

ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef = TypedDict(
    "ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef",
    {
        "awsCloudMap": ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryawsCloudMapTypeDef,
        "dns": ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoverydnsTypeDef,
    },
    total=False,
)

ClientUpdateVirtualNodeResponsevirtualNodespecTypeDef = TypedDict(
    "ClientUpdateVirtualNodeResponsevirtualNodespecTypeDef",
    {
        "backends": List[ClientUpdateVirtualNodeResponsevirtualNodespecbackendsTypeDef],
        "listeners": List[ClientUpdateVirtualNodeResponsevirtualNodespeclistenersTypeDef],
        "logging": ClientUpdateVirtualNodeResponsevirtualNodespecloggingTypeDef,
        "serviceDiscovery": ClientUpdateVirtualNodeResponsevirtualNodespecserviceDiscoveryTypeDef,
    },
    total=False,
)

ClientUpdateVirtualNodeResponsevirtualNodestatusTypeDef = TypedDict(
    "ClientUpdateVirtualNodeResponsevirtualNodestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientUpdateVirtualNodeResponsevirtualNodeTypeDef = TypedDict(
    "ClientUpdateVirtualNodeResponsevirtualNodeTypeDef",
    {
        "meshName": str,
        "metadata": ClientUpdateVirtualNodeResponsevirtualNodemetadataTypeDef,
        "spec": ClientUpdateVirtualNodeResponsevirtualNodespecTypeDef,
        "status": ClientUpdateVirtualNodeResponsevirtualNodestatusTypeDef,
        "virtualNodeName": str,
    },
    total=False,
)

ClientUpdateVirtualNodeResponseTypeDef = TypedDict(
    "ClientUpdateVirtualNodeResponseTypeDef",
    {"virtualNode": ClientUpdateVirtualNodeResponsevirtualNodeTypeDef},
    total=False,
)

ClientUpdateVirtualNodeSpecbackendsvirtualServiceTypeDef = TypedDict(
    "ClientUpdateVirtualNodeSpecbackendsvirtualServiceTypeDef", {"virtualServiceName": str}
)

ClientUpdateVirtualNodeSpecbackendsTypeDef = TypedDict(
    "ClientUpdateVirtualNodeSpecbackendsTypeDef",
    {"virtualService": ClientUpdateVirtualNodeSpecbackendsvirtualServiceTypeDef},
    total=False,
)

ClientUpdateVirtualNodeSpeclistenershealthCheckTypeDef = TypedDict(
    "ClientUpdateVirtualNodeSpeclistenershealthCheckTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "path": str,
        "port": int,
        "protocol": Literal["grpc", "http", "http2", "tcp"],
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
    total=False,
)

ClientUpdateVirtualNodeSpeclistenersportMappingTypeDef = TypedDict(
    "ClientUpdateVirtualNodeSpeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)

ClientUpdateVirtualNodeSpeclistenersTypeDef = TypedDict(
    "ClientUpdateVirtualNodeSpeclistenersTypeDef",
    {
        "healthCheck": ClientUpdateVirtualNodeSpeclistenershealthCheckTypeDef,
        "portMapping": ClientUpdateVirtualNodeSpeclistenersportMappingTypeDef,
    },
    total=False,
)

ClientUpdateVirtualNodeSpecloggingaccessLogfileTypeDef = TypedDict(
    "ClientUpdateVirtualNodeSpecloggingaccessLogfileTypeDef", {"path": str}, total=False
)

ClientUpdateVirtualNodeSpecloggingaccessLogTypeDef = TypedDict(
    "ClientUpdateVirtualNodeSpecloggingaccessLogTypeDef",
    {"file": ClientUpdateVirtualNodeSpecloggingaccessLogfileTypeDef},
    total=False,
)

ClientUpdateVirtualNodeSpecloggingTypeDef = TypedDict(
    "ClientUpdateVirtualNodeSpecloggingTypeDef",
    {"accessLog": ClientUpdateVirtualNodeSpecloggingaccessLogTypeDef},
    total=False,
)

ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef = TypedDict(
    "ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef",
    {"key": str, "value": str},
    total=False,
)

ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef = TypedDict(
    "ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef",
    {
        "attributes": List[ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapattributesTypeDef],
        "namespaceName": str,
        "serviceName": str,
    },
    total=False,
)

ClientUpdateVirtualNodeSpecserviceDiscoverydnsTypeDef = TypedDict(
    "ClientUpdateVirtualNodeSpecserviceDiscoverydnsTypeDef", {"hostname": str}, total=False
)

ClientUpdateVirtualNodeSpecserviceDiscoveryTypeDef = TypedDict(
    "ClientUpdateVirtualNodeSpecserviceDiscoveryTypeDef",
    {
        "awsCloudMap": ClientUpdateVirtualNodeSpecserviceDiscoveryawsCloudMapTypeDef,
        "dns": ClientUpdateVirtualNodeSpecserviceDiscoverydnsTypeDef,
    },
    total=False,
)

ClientUpdateVirtualNodeSpecTypeDef = TypedDict(
    "ClientUpdateVirtualNodeSpecTypeDef",
    {
        "backends": List[ClientUpdateVirtualNodeSpecbackendsTypeDef],
        "listeners": List[ClientUpdateVirtualNodeSpeclistenersTypeDef],
        "logging": ClientUpdateVirtualNodeSpecloggingTypeDef,
        "serviceDiscovery": ClientUpdateVirtualNodeSpecserviceDiscoveryTypeDef,
    },
    total=False,
)

ClientUpdateVirtualRouterResponsevirtualRoutermetadataTypeDef = TypedDict(
    "ClientUpdateVirtualRouterResponsevirtualRoutermetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef = TypedDict(
    "ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef",
    {"port": int, "protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)

ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersTypeDef = TypedDict(
    "ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersTypeDef",
    {"portMapping": ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersportMappingTypeDef},
    total=False,
)

ClientUpdateVirtualRouterResponsevirtualRouterspecTypeDef = TypedDict(
    "ClientUpdateVirtualRouterResponsevirtualRouterspecTypeDef",
    {"listeners": List[ClientUpdateVirtualRouterResponsevirtualRouterspeclistenersTypeDef]},
    total=False,
)

ClientUpdateVirtualRouterResponsevirtualRouterstatusTypeDef = TypedDict(
    "ClientUpdateVirtualRouterResponsevirtualRouterstatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientUpdateVirtualRouterResponsevirtualRouterTypeDef = TypedDict(
    "ClientUpdateVirtualRouterResponsevirtualRouterTypeDef",
    {
        "meshName": str,
        "metadata": ClientUpdateVirtualRouterResponsevirtualRoutermetadataTypeDef,
        "spec": ClientUpdateVirtualRouterResponsevirtualRouterspecTypeDef,
        "status": ClientUpdateVirtualRouterResponsevirtualRouterstatusTypeDef,
        "virtualRouterName": str,
    },
    total=False,
)

ClientUpdateVirtualRouterResponseTypeDef = TypedDict(
    "ClientUpdateVirtualRouterResponseTypeDef",
    {"virtualRouter": ClientUpdateVirtualRouterResponsevirtualRouterTypeDef},
    total=False,
)

_RequiredClientUpdateVirtualRouterSpeclistenersportMappingTypeDef = TypedDict(
    "_RequiredClientUpdateVirtualRouterSpeclistenersportMappingTypeDef", {"port": int}
)
_OptionalClientUpdateVirtualRouterSpeclistenersportMappingTypeDef = TypedDict(
    "_OptionalClientUpdateVirtualRouterSpeclistenersportMappingTypeDef",
    {"protocol": Literal["grpc", "http", "http2", "tcp"]},
    total=False,
)


class ClientUpdateVirtualRouterSpeclistenersportMappingTypeDef(
    _RequiredClientUpdateVirtualRouterSpeclistenersportMappingTypeDef,
    _OptionalClientUpdateVirtualRouterSpeclistenersportMappingTypeDef,
):
    pass


ClientUpdateVirtualRouterSpeclistenersTypeDef = TypedDict(
    "ClientUpdateVirtualRouterSpeclistenersTypeDef",
    {"portMapping": ClientUpdateVirtualRouterSpeclistenersportMappingTypeDef},
)

ClientUpdateVirtualRouterSpecTypeDef = TypedDict(
    "ClientUpdateVirtualRouterSpecTypeDef",
    {"listeners": List[ClientUpdateVirtualRouterSpeclistenersTypeDef]},
    total=False,
)

ClientUpdateVirtualServiceResponsevirtualServicemetadataTypeDef = TypedDict(
    "ClientUpdateVirtualServiceResponsevirtualServicemetadataTypeDef",
    {"arn": str, "createdAt": datetime, "lastUpdatedAt": datetime, "uid": str, "version": int},
    total=False,
)

ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef = TypedDict(
    "ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef",
    {"virtualNodeName": str},
    total=False,
)

ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef = TypedDict(
    "ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef",
    {"virtualRouterName": str},
    total=False,
)

ClientUpdateVirtualServiceResponsevirtualServicespecproviderTypeDef = TypedDict(
    "ClientUpdateVirtualServiceResponsevirtualServicespecproviderTypeDef",
    {
        "virtualNode": ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualNodeTypeDef,
        "virtualRouter": ClientUpdateVirtualServiceResponsevirtualServicespecprovidervirtualRouterTypeDef,
    },
    total=False,
)

ClientUpdateVirtualServiceResponsevirtualServicespecTypeDef = TypedDict(
    "ClientUpdateVirtualServiceResponsevirtualServicespecTypeDef",
    {"provider": ClientUpdateVirtualServiceResponsevirtualServicespecproviderTypeDef},
    total=False,
)

ClientUpdateVirtualServiceResponsevirtualServicestatusTypeDef = TypedDict(
    "ClientUpdateVirtualServiceResponsevirtualServicestatusTypeDef",
    {"status": Literal["ACTIVE", "DELETED", "INACTIVE"]},
    total=False,
)

ClientUpdateVirtualServiceResponsevirtualServiceTypeDef = TypedDict(
    "ClientUpdateVirtualServiceResponsevirtualServiceTypeDef",
    {
        "meshName": str,
        "metadata": ClientUpdateVirtualServiceResponsevirtualServicemetadataTypeDef,
        "spec": ClientUpdateVirtualServiceResponsevirtualServicespecTypeDef,
        "status": ClientUpdateVirtualServiceResponsevirtualServicestatusTypeDef,
        "virtualServiceName": str,
    },
    total=False,
)

ClientUpdateVirtualServiceResponseTypeDef = TypedDict(
    "ClientUpdateVirtualServiceResponseTypeDef",
    {"virtualService": ClientUpdateVirtualServiceResponsevirtualServiceTypeDef},
    total=False,
)

ClientUpdateVirtualServiceSpecprovidervirtualNodeTypeDef = TypedDict(
    "ClientUpdateVirtualServiceSpecprovidervirtualNodeTypeDef", {"virtualNodeName": str}
)

ClientUpdateVirtualServiceSpecprovidervirtualRouterTypeDef = TypedDict(
    "ClientUpdateVirtualServiceSpecprovidervirtualRouterTypeDef",
    {"virtualRouterName": str},
    total=False,
)

ClientUpdateVirtualServiceSpecproviderTypeDef = TypedDict(
    "ClientUpdateVirtualServiceSpecproviderTypeDef",
    {
        "virtualNode": ClientUpdateVirtualServiceSpecprovidervirtualNodeTypeDef,
        "virtualRouter": ClientUpdateVirtualServiceSpecprovidervirtualRouterTypeDef,
    },
    total=False,
)

ClientUpdateVirtualServiceSpecTypeDef = TypedDict(
    "ClientUpdateVirtualServiceSpecTypeDef",
    {"provider": ClientUpdateVirtualServiceSpecproviderTypeDef},
    total=False,
)

MeshRefTypeDef = TypedDict("MeshRefTypeDef", {"arn": str, "meshName": str})

_RequiredListMeshesOutputTypeDef = TypedDict(
    "_RequiredListMeshesOutputTypeDef", {"meshes": List[MeshRefTypeDef]}
)
_OptionalListMeshesOutputTypeDef = TypedDict(
    "_OptionalListMeshesOutputTypeDef", {"nextToken": str}, total=False
)


class ListMeshesOutputTypeDef(_RequiredListMeshesOutputTypeDef, _OptionalListMeshesOutputTypeDef):
    pass


RouteRefTypeDef = TypedDict(
    "RouteRefTypeDef", {"arn": str, "meshName": str, "routeName": str, "virtualRouterName": str}
)

_RequiredListRoutesOutputTypeDef = TypedDict(
    "_RequiredListRoutesOutputTypeDef", {"routes": List[RouteRefTypeDef]}
)
_OptionalListRoutesOutputTypeDef = TypedDict(
    "_OptionalListRoutesOutputTypeDef", {"nextToken": str}, total=False
)


class ListRoutesOutputTypeDef(_RequiredListRoutesOutputTypeDef, _OptionalListRoutesOutputTypeDef):
    pass


_RequiredTagRefTypeDef = TypedDict("_RequiredTagRefTypeDef", {"key": str})
_OptionalTagRefTypeDef = TypedDict("_OptionalTagRefTypeDef", {"value": str}, total=False)


class TagRefTypeDef(_RequiredTagRefTypeDef, _OptionalTagRefTypeDef):
    pass


_RequiredListTagsForResourceOutputTypeDef = TypedDict(
    "_RequiredListTagsForResourceOutputTypeDef", {"tags": List[TagRefTypeDef]}
)
_OptionalListTagsForResourceOutputTypeDef = TypedDict(
    "_OptionalListTagsForResourceOutputTypeDef", {"nextToken": str}, total=False
)


class ListTagsForResourceOutputTypeDef(
    _RequiredListTagsForResourceOutputTypeDef, _OptionalListTagsForResourceOutputTypeDef
):
    pass


VirtualNodeRefTypeDef = TypedDict(
    "VirtualNodeRefTypeDef", {"arn": str, "meshName": str, "virtualNodeName": str}
)

_RequiredListVirtualNodesOutputTypeDef = TypedDict(
    "_RequiredListVirtualNodesOutputTypeDef", {"virtualNodes": List[VirtualNodeRefTypeDef]}
)
_OptionalListVirtualNodesOutputTypeDef = TypedDict(
    "_OptionalListVirtualNodesOutputTypeDef", {"nextToken": str}, total=False
)


class ListVirtualNodesOutputTypeDef(
    _RequiredListVirtualNodesOutputTypeDef, _OptionalListVirtualNodesOutputTypeDef
):
    pass


VirtualRouterRefTypeDef = TypedDict(
    "VirtualRouterRefTypeDef", {"arn": str, "meshName": str, "virtualRouterName": str}
)

_RequiredListVirtualRoutersOutputTypeDef = TypedDict(
    "_RequiredListVirtualRoutersOutputTypeDef", {"virtualRouters": List[VirtualRouterRefTypeDef]}
)
_OptionalListVirtualRoutersOutputTypeDef = TypedDict(
    "_OptionalListVirtualRoutersOutputTypeDef", {"nextToken": str}, total=False
)


class ListVirtualRoutersOutputTypeDef(
    _RequiredListVirtualRoutersOutputTypeDef, _OptionalListVirtualRoutersOutputTypeDef
):
    pass


VirtualServiceRefTypeDef = TypedDict(
    "VirtualServiceRefTypeDef", {"arn": str, "meshName": str, "virtualServiceName": str}
)

_RequiredListVirtualServicesOutputTypeDef = TypedDict(
    "_RequiredListVirtualServicesOutputTypeDef", {"virtualServices": List[VirtualServiceRefTypeDef]}
)
_OptionalListVirtualServicesOutputTypeDef = TypedDict(
    "_OptionalListVirtualServicesOutputTypeDef", {"nextToken": str}, total=False
)


class ListVirtualServicesOutputTypeDef(
    _RequiredListVirtualServicesOutputTypeDef, _OptionalListVirtualServicesOutputTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
