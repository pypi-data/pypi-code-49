"""
Main interface for codecommit service type definitions.

Usage::

    from mypy_boto3.codecommit.type_defs import ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseerrorsTypeDef

    data: ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseerrorsTypeDef = {...}
"""
from datetime import datetime
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseerrorsTypeDef",
    "ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileModesTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileSizesTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataisBinaryFileTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatamergeOperationsTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataobjectTypesTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksbaseTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksdestinationTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsmergeHunkssourceTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksTypeDef",
    "ClientBatchDescribeMergeConflictsResponseconflictsTypeDef",
    "ClientBatchDescribeMergeConflictsResponseerrorsTypeDef",
    "ClientBatchDescribeMergeConflictsResponseTypeDef",
    "ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseerrorsTypeDef",
    "ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseTypeDef",
    "ClientBatchGetCommitsResponsecommitsauthorTypeDef",
    "ClientBatchGetCommitsResponsecommitscommitterTypeDef",
    "ClientBatchGetCommitsResponsecommitsTypeDef",
    "ClientBatchGetCommitsResponseerrorsTypeDef",
    "ClientBatchGetCommitsResponseTypeDef",
    "ClientBatchGetRepositoriesResponserepositoriesTypeDef",
    "ClientBatchGetRepositoriesResponseTypeDef",
    "ClientCreateApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef",
    "ClientCreateApprovalRuleTemplateResponseTypeDef",
    "ClientCreateCommitDeleteFilesTypeDef",
    "ClientCreateCommitPutFilessourceFileTypeDef",
    "ClientCreateCommitPutFilesTypeDef",
    "ClientCreateCommitResponsefilesAddedTypeDef",
    "ClientCreateCommitResponsefilesDeletedTypeDef",
    "ClientCreateCommitResponsefilesUpdatedTypeDef",
    "ClientCreateCommitResponseTypeDef",
    "ClientCreateCommitSetFileModesTypeDef",
    "ClientCreatePullRequestApprovalRuleResponseapprovalRuleoriginApprovalRuleTemplateTypeDef",
    "ClientCreatePullRequestApprovalRuleResponseapprovalRuleTypeDef",
    "ClientCreatePullRequestApprovalRuleResponseTypeDef",
    "ClientCreatePullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    "ClientCreatePullRequestResponsepullRequestapprovalRulesTypeDef",
    "ClientCreatePullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientCreatePullRequestResponsepullRequestpullRequestTargetsTypeDef",
    "ClientCreatePullRequestResponsepullRequestTypeDef",
    "ClientCreatePullRequestResponseTypeDef",
    "ClientCreatePullRequestTargetsTypeDef",
    "ClientCreateRepositoryResponserepositoryMetadataTypeDef",
    "ClientCreateRepositoryResponseTypeDef",
    "ClientCreateUnreferencedMergeCommitConflictResolutiondeleteFilesTypeDef",
    "ClientCreateUnreferencedMergeCommitConflictResolutionreplaceContentsTypeDef",
    "ClientCreateUnreferencedMergeCommitConflictResolutionsetFileModesTypeDef",
    "ClientCreateUnreferencedMergeCommitConflictResolutionTypeDef",
    "ClientCreateUnreferencedMergeCommitResponseTypeDef",
    "ClientDeleteApprovalRuleTemplateResponseTypeDef",
    "ClientDeleteBranchResponsedeletedBranchTypeDef",
    "ClientDeleteBranchResponseTypeDef",
    "ClientDeleteCommentContentResponsecommentTypeDef",
    "ClientDeleteCommentContentResponseTypeDef",
    "ClientDeleteFileResponseTypeDef",
    "ClientDeletePullRequestApprovalRuleResponseTypeDef",
    "ClientDeleteRepositoryResponseTypeDef",
    "ClientDescribeMergeConflictsResponseconflictMetadatafileModesTypeDef",
    "ClientDescribeMergeConflictsResponseconflictMetadatafileSizesTypeDef",
    "ClientDescribeMergeConflictsResponseconflictMetadataisBinaryFileTypeDef",
    "ClientDescribeMergeConflictsResponseconflictMetadatamergeOperationsTypeDef",
    "ClientDescribeMergeConflictsResponseconflictMetadataobjectTypesTypeDef",
    "ClientDescribeMergeConflictsResponseconflictMetadataTypeDef",
    "ClientDescribeMergeConflictsResponsemergeHunksbaseTypeDef",
    "ClientDescribeMergeConflictsResponsemergeHunksdestinationTypeDef",
    "ClientDescribeMergeConflictsResponsemergeHunkssourceTypeDef",
    "ClientDescribeMergeConflictsResponsemergeHunksTypeDef",
    "ClientDescribeMergeConflictsResponseTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleEventMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleOverriddenEventMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventsapprovalStateChangedEventMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef",
    "ClientDescribePullRequestEventsResponsepullRequestEventsTypeDef",
    "ClientDescribePullRequestEventsResponseTypeDef",
    "ClientEvaluatePullRequestApprovalRulesResponseevaluationTypeDef",
    "ClientEvaluatePullRequestApprovalRulesResponseTypeDef",
    "ClientGetApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef",
    "ClientGetApprovalRuleTemplateResponseTypeDef",
    "ClientGetBlobResponseTypeDef",
    "ClientGetBranchResponsebranchTypeDef",
    "ClientGetBranchResponseTypeDef",
    "ClientGetCommentResponsecommentTypeDef",
    "ClientGetCommentResponseTypeDef",
    "ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatacommentsTypeDef",
    "ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatalocationTypeDef",
    "ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDataTypeDef",
    "ClientGetCommentsForComparedCommitResponseTypeDef",
    "ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatacommentsTypeDef",
    "ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatalocationTypeDef",
    "ClientGetCommentsForPullRequestResponsecommentsForPullRequestDataTypeDef",
    "ClientGetCommentsForPullRequestResponseTypeDef",
    "ClientGetCommitResponsecommitauthorTypeDef",
    "ClientGetCommitResponsecommitcommitterTypeDef",
    "ClientGetCommitResponsecommitTypeDef",
    "ClientGetCommitResponseTypeDef",
    "ClientGetDifferencesResponsedifferencesafterBlobTypeDef",
    "ClientGetDifferencesResponsedifferencesbeforeBlobTypeDef",
    "ClientGetDifferencesResponsedifferencesTypeDef",
    "ClientGetDifferencesResponseTypeDef",
    "ClientGetFileResponseTypeDef",
    "ClientGetFolderResponsefilesTypeDef",
    "ClientGetFolderResponsesubFoldersTypeDef",
    "ClientGetFolderResponsesubModulesTypeDef",
    "ClientGetFolderResponsesymbolicLinksTypeDef",
    "ClientGetFolderResponseTypeDef",
    "ClientGetMergeCommitResponseTypeDef",
    "ClientGetMergeConflictsResponseconflictMetadataListfileModesTypeDef",
    "ClientGetMergeConflictsResponseconflictMetadataListfileSizesTypeDef",
    "ClientGetMergeConflictsResponseconflictMetadataListisBinaryFileTypeDef",
    "ClientGetMergeConflictsResponseconflictMetadataListmergeOperationsTypeDef",
    "ClientGetMergeConflictsResponseconflictMetadataListobjectTypesTypeDef",
    "ClientGetMergeConflictsResponseconflictMetadataListTypeDef",
    "ClientGetMergeConflictsResponseTypeDef",
    "ClientGetMergeOptionsResponseTypeDef",
    "ClientGetPullRequestApprovalStatesResponseapprovalsTypeDef",
    "ClientGetPullRequestApprovalStatesResponseTypeDef",
    "ClientGetPullRequestOverrideStateResponseTypeDef",
    "ClientGetPullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    "ClientGetPullRequestResponsepullRequestapprovalRulesTypeDef",
    "ClientGetPullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientGetPullRequestResponsepullRequestpullRequestTargetsTypeDef",
    "ClientGetPullRequestResponsepullRequestTypeDef",
    "ClientGetPullRequestResponseTypeDef",
    "ClientGetRepositoryResponserepositoryMetadataTypeDef",
    "ClientGetRepositoryResponseTypeDef",
    "ClientGetRepositoryTriggersResponsetriggersTypeDef",
    "ClientGetRepositoryTriggersResponseTypeDef",
    "ClientListApprovalRuleTemplatesResponseTypeDef",
    "ClientListAssociatedApprovalRuleTemplatesForRepositoryResponseTypeDef",
    "ClientListBranchesResponseTypeDef",
    "ClientListPullRequestsResponseTypeDef",
    "ClientListRepositoriesForApprovalRuleTemplateResponseTypeDef",
    "ClientListRepositoriesResponserepositoriesTypeDef",
    "ClientListRepositoriesResponseTypeDef",
    "ClientListTagsForResourceResponseTypeDef",
    "ClientMergeBranchesByFastForwardResponseTypeDef",
    "ClientMergeBranchesBySquashConflictResolutiondeleteFilesTypeDef",
    "ClientMergeBranchesBySquashConflictResolutionreplaceContentsTypeDef",
    "ClientMergeBranchesBySquashConflictResolutionsetFileModesTypeDef",
    "ClientMergeBranchesBySquashConflictResolutionTypeDef",
    "ClientMergeBranchesBySquashResponseTypeDef",
    "ClientMergeBranchesByThreeWayConflictResolutiondeleteFilesTypeDef",
    "ClientMergeBranchesByThreeWayConflictResolutionreplaceContentsTypeDef",
    "ClientMergeBranchesByThreeWayConflictResolutionsetFileModesTypeDef",
    "ClientMergeBranchesByThreeWayConflictResolutionTypeDef",
    "ClientMergeBranchesByThreeWayResponseTypeDef",
    "ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    "ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesTypeDef",
    "ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsTypeDef",
    "ClientMergePullRequestByFastForwardResponsepullRequestTypeDef",
    "ClientMergePullRequestByFastForwardResponseTypeDef",
    "ClientMergePullRequestBySquashConflictResolutiondeleteFilesTypeDef",
    "ClientMergePullRequestBySquashConflictResolutionreplaceContentsTypeDef",
    "ClientMergePullRequestBySquashConflictResolutionsetFileModesTypeDef",
    "ClientMergePullRequestBySquashConflictResolutionTypeDef",
    "ClientMergePullRequestBySquashResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    "ClientMergePullRequestBySquashResponsepullRequestapprovalRulesTypeDef",
    "ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsTypeDef",
    "ClientMergePullRequestBySquashResponsepullRequestTypeDef",
    "ClientMergePullRequestBySquashResponseTypeDef",
    "ClientMergePullRequestByThreeWayConflictResolutiondeleteFilesTypeDef",
    "ClientMergePullRequestByThreeWayConflictResolutionreplaceContentsTypeDef",
    "ClientMergePullRequestByThreeWayConflictResolutionsetFileModesTypeDef",
    "ClientMergePullRequestByThreeWayConflictResolutionTypeDef",
    "ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    "ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesTypeDef",
    "ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsTypeDef",
    "ClientMergePullRequestByThreeWayResponsepullRequestTypeDef",
    "ClientMergePullRequestByThreeWayResponseTypeDef",
    "ClientPostCommentForComparedCommitLocationTypeDef",
    "ClientPostCommentForComparedCommitResponsecommentTypeDef",
    "ClientPostCommentForComparedCommitResponselocationTypeDef",
    "ClientPostCommentForComparedCommitResponseTypeDef",
    "ClientPostCommentForPullRequestLocationTypeDef",
    "ClientPostCommentForPullRequestResponsecommentTypeDef",
    "ClientPostCommentForPullRequestResponselocationTypeDef",
    "ClientPostCommentForPullRequestResponseTypeDef",
    "ClientPostCommentReplyResponsecommentTypeDef",
    "ClientPostCommentReplyResponseTypeDef",
    "ClientPutFileResponseTypeDef",
    "ClientPutRepositoryTriggersResponseTypeDef",
    "ClientPutRepositoryTriggersTriggersTypeDef",
    "ClientTestRepositoryTriggersResponsefailedExecutionsTypeDef",
    "ClientTestRepositoryTriggersResponseTypeDef",
    "ClientTestRepositoryTriggersTriggersTypeDef",
    "ClientUpdateApprovalRuleTemplateContentResponseapprovalRuleTemplateTypeDef",
    "ClientUpdateApprovalRuleTemplateContentResponseTypeDef",
    "ClientUpdateApprovalRuleTemplateDescriptionResponseapprovalRuleTemplateTypeDef",
    "ClientUpdateApprovalRuleTemplateDescriptionResponseTypeDef",
    "ClientUpdateApprovalRuleTemplateNameResponseapprovalRuleTemplateTypeDef",
    "ClientUpdateApprovalRuleTemplateNameResponseTypeDef",
    "ClientUpdateCommentResponsecommentTypeDef",
    "ClientUpdateCommentResponseTypeDef",
    "ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleoriginApprovalRuleTemplateTypeDef",
    "ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleTypeDef",
    "ClientUpdatePullRequestApprovalRuleContentResponseTypeDef",
    "ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    "ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesTypeDef",
    "ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsTypeDef",
    "ClientUpdatePullRequestDescriptionResponsepullRequestTypeDef",
    "ClientUpdatePullRequestDescriptionResponseTypeDef",
    "ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    "ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesTypeDef",
    "ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsTypeDef",
    "ClientUpdatePullRequestStatusResponsepullRequestTypeDef",
    "ClientUpdatePullRequestStatusResponseTypeDef",
    "ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    "ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesTypeDef",
    "ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    "ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsTypeDef",
    "ClientUpdatePullRequestTitleResponsepullRequestTypeDef",
    "ClientUpdatePullRequestTitleResponseTypeDef",
    "ApprovalRuleEventMetadataTypeDef",
    "ApprovalRuleOverriddenEventMetadataTypeDef",
    "ApprovalStateChangedEventMetadataTypeDef",
    "PullRequestCreatedEventMetadataTypeDef",
    "MergeMetadataTypeDef",
    "PullRequestMergedStateChangedEventMetadataTypeDef",
    "PullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    "PullRequestStatusChangedEventMetadataTypeDef",
    "PullRequestEventTypeDef",
    "DescribePullRequestEventsOutputTypeDef",
    "CommentTypeDef",
    "LocationTypeDef",
    "CommentsForComparedCommitTypeDef",
    "GetCommentsForComparedCommitOutputTypeDef",
    "CommentsForPullRequestTypeDef",
    "GetCommentsForPullRequestOutputTypeDef",
    "BlobMetadataTypeDef",
    "DifferenceTypeDef",
    "GetDifferencesOutputTypeDef",
    "ListBranchesOutputTypeDef",
    "ListPullRequestsOutputTypeDef",
    "RepositoryNameIdPairTypeDef",
    "ListRepositoriesOutputTypeDef",
    "PaginatorConfigTypeDef",
)

ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseerrorsTypeDef = TypedDict(
    "ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseerrorsTypeDef",
    {"repositoryName": str, "errorCode": str, "errorMessage": str},
    total=False,
)

ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseTypeDef = TypedDict(
    "ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseTypeDef",
    {
        "associatedRepositoryNames": List[str],
        "errors": List[
            ClientBatchAssociateApprovalRuleTemplateWithRepositoriesResponseerrorsTypeDef
        ],
    },
    total=False,
)

ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileModesTypeDef = TypedDict(
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileModesTypeDef",
    {
        "source": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "destination": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "base": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)

ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileSizesTypeDef = TypedDict(
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileSizesTypeDef",
    {"source": int, "destination": int, "base": int},
    total=False,
)

ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataisBinaryFileTypeDef = TypedDict(
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataisBinaryFileTypeDef",
    {"source": bool, "destination": bool, "base": bool},
    total=False,
)

ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatamergeOperationsTypeDef = TypedDict(
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatamergeOperationsTypeDef",
    {"source": Literal["A", "M", "D"], "destination": Literal["A", "M", "D"]},
    total=False,
)

ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataobjectTypesTypeDef = TypedDict(
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataobjectTypesTypeDef",
    {
        "source": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
        "destination": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
        "base": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
    },
    total=False,
)

ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataTypeDef = TypedDict(
    "ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataTypeDef",
    {
        "filePath": str,
        "fileSizes": ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileSizesTypeDef,
        "fileModes": ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatafileModesTypeDef,
        "objectTypes": ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataobjectTypesTypeDef,
        "numberOfConflicts": int,
        "isBinaryFile": ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataisBinaryFileTypeDef,
        "contentConflict": bool,
        "fileModeConflict": bool,
        "objectTypeConflict": bool,
        "mergeOperations": ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadatamergeOperationsTypeDef,
    },
    total=False,
)

ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksbaseTypeDef = TypedDict(
    "ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksbaseTypeDef",
    {"startLine": int, "endLine": int, "hunkContent": str},
    total=False,
)

ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksdestinationTypeDef = TypedDict(
    "ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksdestinationTypeDef",
    {"startLine": int, "endLine": int, "hunkContent": str},
    total=False,
)

ClientBatchDescribeMergeConflictsResponseconflictsmergeHunkssourceTypeDef = TypedDict(
    "ClientBatchDescribeMergeConflictsResponseconflictsmergeHunkssourceTypeDef",
    {"startLine": int, "endLine": int, "hunkContent": str},
    total=False,
)

ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksTypeDef = TypedDict(
    "ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksTypeDef",
    {
        "isConflict": bool,
        "source": ClientBatchDescribeMergeConflictsResponseconflictsmergeHunkssourceTypeDef,
        "destination": ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksdestinationTypeDef,
        "base": ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksbaseTypeDef,
    },
    total=False,
)

ClientBatchDescribeMergeConflictsResponseconflictsTypeDef = TypedDict(
    "ClientBatchDescribeMergeConflictsResponseconflictsTypeDef",
    {
        "conflictMetadata": ClientBatchDescribeMergeConflictsResponseconflictsconflictMetadataTypeDef,
        "mergeHunks": List[ClientBatchDescribeMergeConflictsResponseconflictsmergeHunksTypeDef],
    },
    total=False,
)

ClientBatchDescribeMergeConflictsResponseerrorsTypeDef = TypedDict(
    "ClientBatchDescribeMergeConflictsResponseerrorsTypeDef",
    {"filePath": str, "exceptionName": str, "message": str},
    total=False,
)

ClientBatchDescribeMergeConflictsResponseTypeDef = TypedDict(
    "ClientBatchDescribeMergeConflictsResponseTypeDef",
    {
        "conflicts": List[ClientBatchDescribeMergeConflictsResponseconflictsTypeDef],
        "nextToken": str,
        "errors": List[ClientBatchDescribeMergeConflictsResponseerrorsTypeDef],
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
    },
    total=False,
)

ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseerrorsTypeDef = TypedDict(
    "ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseerrorsTypeDef",
    {"repositoryName": str, "errorCode": str, "errorMessage": str},
    total=False,
)

ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseTypeDef = TypedDict(
    "ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseTypeDef",
    {
        "disassociatedRepositoryNames": List[str],
        "errors": List[
            ClientBatchDisassociateApprovalRuleTemplateFromRepositoriesResponseerrorsTypeDef
        ],
    },
    total=False,
)

ClientBatchGetCommitsResponsecommitsauthorTypeDef = TypedDict(
    "ClientBatchGetCommitsResponsecommitsauthorTypeDef",
    {"name": str, "email": str, "date": str},
    total=False,
)

ClientBatchGetCommitsResponsecommitscommitterTypeDef = TypedDict(
    "ClientBatchGetCommitsResponsecommitscommitterTypeDef",
    {"name": str, "email": str, "date": str},
    total=False,
)

ClientBatchGetCommitsResponsecommitsTypeDef = TypedDict(
    "ClientBatchGetCommitsResponsecommitsTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "parents": List[str],
        "message": str,
        "author": ClientBatchGetCommitsResponsecommitsauthorTypeDef,
        "committer": ClientBatchGetCommitsResponsecommitscommitterTypeDef,
        "additionalData": str,
    },
    total=False,
)

ClientBatchGetCommitsResponseerrorsTypeDef = TypedDict(
    "ClientBatchGetCommitsResponseerrorsTypeDef",
    {"commitId": str, "errorCode": str, "errorMessage": str},
    total=False,
)

ClientBatchGetCommitsResponseTypeDef = TypedDict(
    "ClientBatchGetCommitsResponseTypeDef",
    {
        "commits": List[ClientBatchGetCommitsResponsecommitsTypeDef],
        "errors": List[ClientBatchGetCommitsResponseerrorsTypeDef],
    },
    total=False,
)

ClientBatchGetRepositoriesResponserepositoriesTypeDef = TypedDict(
    "ClientBatchGetRepositoriesResponserepositoriesTypeDef",
    {
        "accountId": str,
        "repositoryId": str,
        "repositoryName": str,
        "repositoryDescription": str,
        "defaultBranch": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "cloneUrlHttp": str,
        "cloneUrlSsh": str,
        "Arn": str,
    },
    total=False,
)

ClientBatchGetRepositoriesResponseTypeDef = TypedDict(
    "ClientBatchGetRepositoriesResponseTypeDef",
    {
        "repositories": List[ClientBatchGetRepositoriesResponserepositoriesTypeDef],
        "repositoriesNotFound": List[str],
    },
    total=False,
)

ClientCreateApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef = TypedDict(
    "ClientCreateApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef",
    {
        "approvalRuleTemplateId": str,
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateDescription": str,
        "approvalRuleTemplateContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
    },
    total=False,
)

ClientCreateApprovalRuleTemplateResponseTypeDef = TypedDict(
    "ClientCreateApprovalRuleTemplateResponseTypeDef",
    {"approvalRuleTemplate": ClientCreateApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef},
    total=False,
)

ClientCreateCommitDeleteFilesTypeDef = TypedDict(
    "ClientCreateCommitDeleteFilesTypeDef", {"filePath": str}
)

ClientCreateCommitPutFilessourceFileTypeDef = TypedDict(
    "ClientCreateCommitPutFilessourceFileTypeDef", {"filePath": str, "isMove": bool}, total=False
)

_RequiredClientCreateCommitPutFilesTypeDef = TypedDict(
    "_RequiredClientCreateCommitPutFilesTypeDef", {"filePath": str}
)
_OptionalClientCreateCommitPutFilesTypeDef = TypedDict(
    "_OptionalClientCreateCommitPutFilesTypeDef",
    {
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "fileContent": bytes,
        "sourceFile": ClientCreateCommitPutFilessourceFileTypeDef,
    },
    total=False,
)


class ClientCreateCommitPutFilesTypeDef(
    _RequiredClientCreateCommitPutFilesTypeDef, _OptionalClientCreateCommitPutFilesTypeDef
):
    pass


ClientCreateCommitResponsefilesAddedTypeDef = TypedDict(
    "ClientCreateCommitResponsefilesAddedTypeDef",
    {"absolutePath": str, "blobId": str, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)

ClientCreateCommitResponsefilesDeletedTypeDef = TypedDict(
    "ClientCreateCommitResponsefilesDeletedTypeDef",
    {"absolutePath": str, "blobId": str, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)

ClientCreateCommitResponsefilesUpdatedTypeDef = TypedDict(
    "ClientCreateCommitResponsefilesUpdatedTypeDef",
    {"absolutePath": str, "blobId": str, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)

ClientCreateCommitResponseTypeDef = TypedDict(
    "ClientCreateCommitResponseTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "filesAdded": List[ClientCreateCommitResponsefilesAddedTypeDef],
        "filesUpdated": List[ClientCreateCommitResponsefilesUpdatedTypeDef],
        "filesDeleted": List[ClientCreateCommitResponsefilesDeletedTypeDef],
    },
    total=False,
)

_RequiredClientCreateCommitSetFileModesTypeDef = TypedDict(
    "_RequiredClientCreateCommitSetFileModesTypeDef", {"filePath": str}
)
_OptionalClientCreateCommitSetFileModesTypeDef = TypedDict(
    "_OptionalClientCreateCommitSetFileModesTypeDef",
    {"fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)


class ClientCreateCommitSetFileModesTypeDef(
    _RequiredClientCreateCommitSetFileModesTypeDef, _OptionalClientCreateCommitSetFileModesTypeDef
):
    pass


ClientCreatePullRequestApprovalRuleResponseapprovalRuleoriginApprovalRuleTemplateTypeDef = TypedDict(
    "ClientCreatePullRequestApprovalRuleResponseapprovalRuleoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)

ClientCreatePullRequestApprovalRuleResponseapprovalRuleTypeDef = TypedDict(
    "ClientCreatePullRequestApprovalRuleResponseapprovalRuleTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientCreatePullRequestApprovalRuleResponseapprovalRuleoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)

ClientCreatePullRequestApprovalRuleResponseTypeDef = TypedDict(
    "ClientCreatePullRequestApprovalRuleResponseTypeDef",
    {"approvalRule": ClientCreatePullRequestApprovalRuleResponseapprovalRuleTypeDef},
    total=False,
)

ClientCreatePullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef = TypedDict(
    "ClientCreatePullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)

ClientCreatePullRequestResponsepullRequestapprovalRulesTypeDef = TypedDict(
    "ClientCreatePullRequestResponsepullRequestapprovalRulesTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientCreatePullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)

ClientCreatePullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "ClientCreatePullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)

ClientCreatePullRequestResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "ClientCreatePullRequestResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientCreatePullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)

ClientCreatePullRequestResponsepullRequestTypeDef = TypedDict(
    "ClientCreatePullRequestResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": Literal["OPEN", "CLOSED"],
        "authorArn": str,
        "pullRequestTargets": List[
            ClientCreatePullRequestResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List[ClientCreatePullRequestResponsepullRequestapprovalRulesTypeDef],
    },
    total=False,
)

ClientCreatePullRequestResponseTypeDef = TypedDict(
    "ClientCreatePullRequestResponseTypeDef",
    {"pullRequest": ClientCreatePullRequestResponsepullRequestTypeDef},
    total=False,
)

_RequiredClientCreatePullRequestTargetsTypeDef = TypedDict(
    "_RequiredClientCreatePullRequestTargetsTypeDef", {"repositoryName": str}
)
_OptionalClientCreatePullRequestTargetsTypeDef = TypedDict(
    "_OptionalClientCreatePullRequestTargetsTypeDef",
    {"sourceReference": str, "destinationReference": str},
    total=False,
)


class ClientCreatePullRequestTargetsTypeDef(
    _RequiredClientCreatePullRequestTargetsTypeDef, _OptionalClientCreatePullRequestTargetsTypeDef
):
    pass


ClientCreateRepositoryResponserepositoryMetadataTypeDef = TypedDict(
    "ClientCreateRepositoryResponserepositoryMetadataTypeDef",
    {
        "accountId": str,
        "repositoryId": str,
        "repositoryName": str,
        "repositoryDescription": str,
        "defaultBranch": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "cloneUrlHttp": str,
        "cloneUrlSsh": str,
        "Arn": str,
    },
    total=False,
)

ClientCreateRepositoryResponseTypeDef = TypedDict(
    "ClientCreateRepositoryResponseTypeDef",
    {"repositoryMetadata": ClientCreateRepositoryResponserepositoryMetadataTypeDef},
    total=False,
)

ClientCreateUnreferencedMergeCommitConflictResolutiondeleteFilesTypeDef = TypedDict(
    "ClientCreateUnreferencedMergeCommitConflictResolutiondeleteFilesTypeDef",
    {"filePath": str},
    total=False,
)

_RequiredClientCreateUnreferencedMergeCommitConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_RequiredClientCreateUnreferencedMergeCommitConflictResolutionreplaceContentsTypeDef",
    {"filePath": str},
)
_OptionalClientCreateUnreferencedMergeCommitConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_OptionalClientCreateUnreferencedMergeCommitConflictResolutionreplaceContentsTypeDef",
    {
        "replacementType": Literal[
            "KEEP_BASE", "KEEP_SOURCE", "KEEP_DESTINATION", "USE_NEW_CONTENT"
        ],
        "content": bytes,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)


class ClientCreateUnreferencedMergeCommitConflictResolutionreplaceContentsTypeDef(
    _RequiredClientCreateUnreferencedMergeCommitConflictResolutionreplaceContentsTypeDef,
    _OptionalClientCreateUnreferencedMergeCommitConflictResolutionreplaceContentsTypeDef,
):
    pass


ClientCreateUnreferencedMergeCommitConflictResolutionsetFileModesTypeDef = TypedDict(
    "ClientCreateUnreferencedMergeCommitConflictResolutionsetFileModesTypeDef",
    {"filePath": str, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)

ClientCreateUnreferencedMergeCommitConflictResolutionTypeDef = TypedDict(
    "ClientCreateUnreferencedMergeCommitConflictResolutionTypeDef",
    {
        "replaceContents": List[
            ClientCreateUnreferencedMergeCommitConflictResolutionreplaceContentsTypeDef
        ],
        "deleteFiles": List[
            ClientCreateUnreferencedMergeCommitConflictResolutiondeleteFilesTypeDef
        ],
        "setFileModes": List[
            ClientCreateUnreferencedMergeCommitConflictResolutionsetFileModesTypeDef
        ],
    },
    total=False,
)

ClientCreateUnreferencedMergeCommitResponseTypeDef = TypedDict(
    "ClientCreateUnreferencedMergeCommitResponseTypeDef",
    {"commitId": str, "treeId": str},
    total=False,
)

ClientDeleteApprovalRuleTemplateResponseTypeDef = TypedDict(
    "ClientDeleteApprovalRuleTemplateResponseTypeDef", {"approvalRuleTemplateId": str}, total=False
)

ClientDeleteBranchResponsedeletedBranchTypeDef = TypedDict(
    "ClientDeleteBranchResponsedeletedBranchTypeDef",
    {"branchName": str, "commitId": str},
    total=False,
)

ClientDeleteBranchResponseTypeDef = TypedDict(
    "ClientDeleteBranchResponseTypeDef",
    {"deletedBranch": ClientDeleteBranchResponsedeletedBranchTypeDef},
    total=False,
)

ClientDeleteCommentContentResponsecommentTypeDef = TypedDict(
    "ClientDeleteCommentContentResponsecommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)

ClientDeleteCommentContentResponseTypeDef = TypedDict(
    "ClientDeleteCommentContentResponseTypeDef",
    {"comment": ClientDeleteCommentContentResponsecommentTypeDef},
    total=False,
)

ClientDeleteFileResponseTypeDef = TypedDict(
    "ClientDeleteFileResponseTypeDef",
    {"commitId": str, "blobId": str, "treeId": str, "filePath": str},
    total=False,
)

ClientDeletePullRequestApprovalRuleResponseTypeDef = TypedDict(
    "ClientDeletePullRequestApprovalRuleResponseTypeDef", {"approvalRuleId": str}, total=False
)

ClientDeleteRepositoryResponseTypeDef = TypedDict(
    "ClientDeleteRepositoryResponseTypeDef", {"repositoryId": str}, total=False
)

ClientDescribeMergeConflictsResponseconflictMetadatafileModesTypeDef = TypedDict(
    "ClientDescribeMergeConflictsResponseconflictMetadatafileModesTypeDef",
    {
        "source": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "destination": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "base": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)

ClientDescribeMergeConflictsResponseconflictMetadatafileSizesTypeDef = TypedDict(
    "ClientDescribeMergeConflictsResponseconflictMetadatafileSizesTypeDef",
    {"source": int, "destination": int, "base": int},
    total=False,
)

ClientDescribeMergeConflictsResponseconflictMetadataisBinaryFileTypeDef = TypedDict(
    "ClientDescribeMergeConflictsResponseconflictMetadataisBinaryFileTypeDef",
    {"source": bool, "destination": bool, "base": bool},
    total=False,
)

ClientDescribeMergeConflictsResponseconflictMetadatamergeOperationsTypeDef = TypedDict(
    "ClientDescribeMergeConflictsResponseconflictMetadatamergeOperationsTypeDef",
    {"source": Literal["A", "M", "D"], "destination": Literal["A", "M", "D"]},
    total=False,
)

ClientDescribeMergeConflictsResponseconflictMetadataobjectTypesTypeDef = TypedDict(
    "ClientDescribeMergeConflictsResponseconflictMetadataobjectTypesTypeDef",
    {
        "source": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
        "destination": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
        "base": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
    },
    total=False,
)

ClientDescribeMergeConflictsResponseconflictMetadataTypeDef = TypedDict(
    "ClientDescribeMergeConflictsResponseconflictMetadataTypeDef",
    {
        "filePath": str,
        "fileSizes": ClientDescribeMergeConflictsResponseconflictMetadatafileSizesTypeDef,
        "fileModes": ClientDescribeMergeConflictsResponseconflictMetadatafileModesTypeDef,
        "objectTypes": ClientDescribeMergeConflictsResponseconflictMetadataobjectTypesTypeDef,
        "numberOfConflicts": int,
        "isBinaryFile": ClientDescribeMergeConflictsResponseconflictMetadataisBinaryFileTypeDef,
        "contentConflict": bool,
        "fileModeConflict": bool,
        "objectTypeConflict": bool,
        "mergeOperations": ClientDescribeMergeConflictsResponseconflictMetadatamergeOperationsTypeDef,
    },
    total=False,
)

ClientDescribeMergeConflictsResponsemergeHunksbaseTypeDef = TypedDict(
    "ClientDescribeMergeConflictsResponsemergeHunksbaseTypeDef",
    {"startLine": int, "endLine": int, "hunkContent": str},
    total=False,
)

ClientDescribeMergeConflictsResponsemergeHunksdestinationTypeDef = TypedDict(
    "ClientDescribeMergeConflictsResponsemergeHunksdestinationTypeDef",
    {"startLine": int, "endLine": int, "hunkContent": str},
    total=False,
)

ClientDescribeMergeConflictsResponsemergeHunkssourceTypeDef = TypedDict(
    "ClientDescribeMergeConflictsResponsemergeHunkssourceTypeDef",
    {"startLine": int, "endLine": int, "hunkContent": str},
    total=False,
)

ClientDescribeMergeConflictsResponsemergeHunksTypeDef = TypedDict(
    "ClientDescribeMergeConflictsResponsemergeHunksTypeDef",
    {
        "isConflict": bool,
        "source": ClientDescribeMergeConflictsResponsemergeHunkssourceTypeDef,
        "destination": ClientDescribeMergeConflictsResponsemergeHunksdestinationTypeDef,
        "base": ClientDescribeMergeConflictsResponsemergeHunksbaseTypeDef,
    },
    total=False,
)

ClientDescribeMergeConflictsResponseTypeDef = TypedDict(
    "ClientDescribeMergeConflictsResponseTypeDef",
    {
        "conflictMetadata": ClientDescribeMergeConflictsResponseconflictMetadataTypeDef,
        "mergeHunks": List[ClientDescribeMergeConflictsResponsemergeHunksTypeDef],
        "nextToken": str,
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
    },
    total=False,
)

ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleEventMetadataTypeDef = TypedDict(
    "ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleEventMetadataTypeDef",
    {"approvalRuleName": str, "approvalRuleId": str, "approvalRuleContent": str},
    total=False,
)

ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleOverriddenEventMetadataTypeDef = TypedDict(
    "ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleOverriddenEventMetadataTypeDef",
    {"revisionId": str, "overrideStatus": Literal["OVERRIDE", "REVOKE"]},
    total=False,
)

ClientDescribePullRequestEventsResponsepullRequestEventsapprovalStateChangedEventMetadataTypeDef = TypedDict(
    "ClientDescribePullRequestEventsResponsepullRequestEventsapprovalStateChangedEventMetadataTypeDef",
    {"revisionId": str, "approvalStatus": Literal["APPROVE", "REVOKE"]},
    total=False,
)

ClientDescribePullRequestEventsResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef = TypedDict(
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef",
    {"repositoryName": str, "sourceCommitId": str, "destinationCommitId": str, "mergeBase": str},
    total=False,
)

ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef = TypedDict(
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)

ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef = TypedDict(
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef",
    {
        "repositoryName": str,
        "destinationReference": str,
        "mergeMetadata": ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadatamergeMetadataTypeDef,
    },
    total=False,
)

ClientDescribePullRequestEventsResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef = TypedDict(
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    {"repositoryName": str, "beforeCommitId": str, "afterCommitId": str, "mergeBase": str},
    total=False,
)

ClientDescribePullRequestEventsResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef = TypedDict(
    "ClientDescribePullRequestEventsResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef",
    {"pullRequestStatus": Literal["OPEN", "CLOSED"]},
    total=False,
)

ClientDescribePullRequestEventsResponsepullRequestEventsTypeDef = TypedDict(
    "ClientDescribePullRequestEventsResponsepullRequestEventsTypeDef",
    {
        "pullRequestId": str,
        "eventDate": datetime,
        "pullRequestEventType": Literal[
            "PULL_REQUEST_CREATED",
            "PULL_REQUEST_STATUS_CHANGED",
            "PULL_REQUEST_SOURCE_REFERENCE_UPDATED",
            "PULL_REQUEST_MERGE_STATE_CHANGED",
            "PULL_REQUEST_APPROVAL_RULE_CREATED",
            "PULL_REQUEST_APPROVAL_RULE_UPDATED",
            "PULL_REQUEST_APPROVAL_RULE_DELETED",
            "PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN",
            "PULL_REQUEST_APPROVAL_STATE_CHANGED",
        ],
        "actorArn": str,
        "pullRequestCreatedEventMetadata": ClientDescribePullRequestEventsResponsepullRequestEventspullRequestCreatedEventMetadataTypeDef,
        "pullRequestStatusChangedEventMetadata": ClientDescribePullRequestEventsResponsepullRequestEventspullRequestStatusChangedEventMetadataTypeDef,
        "pullRequestSourceReferenceUpdatedEventMetadata": ClientDescribePullRequestEventsResponsepullRequestEventspullRequestSourceReferenceUpdatedEventMetadataTypeDef,
        "pullRequestMergedStateChangedEventMetadata": ClientDescribePullRequestEventsResponsepullRequestEventspullRequestMergedStateChangedEventMetadataTypeDef,
        "approvalRuleEventMetadata": ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleEventMetadataTypeDef,
        "approvalStateChangedEventMetadata": ClientDescribePullRequestEventsResponsepullRequestEventsapprovalStateChangedEventMetadataTypeDef,
        "approvalRuleOverriddenEventMetadata": ClientDescribePullRequestEventsResponsepullRequestEventsapprovalRuleOverriddenEventMetadataTypeDef,
    },
    total=False,
)

ClientDescribePullRequestEventsResponseTypeDef = TypedDict(
    "ClientDescribePullRequestEventsResponseTypeDef",
    {
        "pullRequestEvents": List[ClientDescribePullRequestEventsResponsepullRequestEventsTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientEvaluatePullRequestApprovalRulesResponseevaluationTypeDef = TypedDict(
    "ClientEvaluatePullRequestApprovalRulesResponseevaluationTypeDef",
    {
        "approved": bool,
        "overridden": bool,
        "approvalRulesSatisfied": List[str],
        "approvalRulesNotSatisfied": List[str],
    },
    total=False,
)

ClientEvaluatePullRequestApprovalRulesResponseTypeDef = TypedDict(
    "ClientEvaluatePullRequestApprovalRulesResponseTypeDef",
    {"evaluation": ClientEvaluatePullRequestApprovalRulesResponseevaluationTypeDef},
    total=False,
)

ClientGetApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef = TypedDict(
    "ClientGetApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef",
    {
        "approvalRuleTemplateId": str,
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateDescription": str,
        "approvalRuleTemplateContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
    },
    total=False,
)

ClientGetApprovalRuleTemplateResponseTypeDef = TypedDict(
    "ClientGetApprovalRuleTemplateResponseTypeDef",
    {"approvalRuleTemplate": ClientGetApprovalRuleTemplateResponseapprovalRuleTemplateTypeDef},
    total=False,
)

ClientGetBlobResponseTypeDef = TypedDict(
    "ClientGetBlobResponseTypeDef", {"content": bytes}, total=False
)

ClientGetBranchResponsebranchTypeDef = TypedDict(
    "ClientGetBranchResponsebranchTypeDef", {"branchName": str, "commitId": str}, total=False
)

ClientGetBranchResponseTypeDef = TypedDict(
    "ClientGetBranchResponseTypeDef", {"branch": ClientGetBranchResponsebranchTypeDef}, total=False
)

ClientGetCommentResponsecommentTypeDef = TypedDict(
    "ClientGetCommentResponsecommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)

ClientGetCommentResponseTypeDef = TypedDict(
    "ClientGetCommentResponseTypeDef",
    {"comment": ClientGetCommentResponsecommentTypeDef},
    total=False,
)

ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatacommentsTypeDef = TypedDict(
    "ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatacommentsTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)

ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatalocationTypeDef = TypedDict(
    "ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatalocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": Literal["BEFORE", "AFTER"]},
    total=False,
)

ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDataTypeDef = TypedDict(
    "ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDataTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatalocationTypeDef,
        "comments": List[
            ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDatacommentsTypeDef
        ],
    },
    total=False,
)

ClientGetCommentsForComparedCommitResponseTypeDef = TypedDict(
    "ClientGetCommentsForComparedCommitResponseTypeDef",
    {
        "commentsForComparedCommitData": List[
            ClientGetCommentsForComparedCommitResponsecommentsForComparedCommitDataTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatacommentsTypeDef = TypedDict(
    "ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatacommentsTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)

ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatalocationTypeDef = TypedDict(
    "ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatalocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": Literal["BEFORE", "AFTER"]},
    total=False,
)

ClientGetCommentsForPullRequestResponsecommentsForPullRequestDataTypeDef = TypedDict(
    "ClientGetCommentsForPullRequestResponsecommentsForPullRequestDataTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatalocationTypeDef,
        "comments": List[
            ClientGetCommentsForPullRequestResponsecommentsForPullRequestDatacommentsTypeDef
        ],
    },
    total=False,
)

ClientGetCommentsForPullRequestResponseTypeDef = TypedDict(
    "ClientGetCommentsForPullRequestResponseTypeDef",
    {
        "commentsForPullRequestData": List[
            ClientGetCommentsForPullRequestResponsecommentsForPullRequestDataTypeDef
        ],
        "nextToken": str,
    },
    total=False,
)

ClientGetCommitResponsecommitauthorTypeDef = TypedDict(
    "ClientGetCommitResponsecommitauthorTypeDef",
    {"name": str, "email": str, "date": str},
    total=False,
)

ClientGetCommitResponsecommitcommitterTypeDef = TypedDict(
    "ClientGetCommitResponsecommitcommitterTypeDef",
    {"name": str, "email": str, "date": str},
    total=False,
)

ClientGetCommitResponsecommitTypeDef = TypedDict(
    "ClientGetCommitResponsecommitTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "parents": List[str],
        "message": str,
        "author": ClientGetCommitResponsecommitauthorTypeDef,
        "committer": ClientGetCommitResponsecommitcommitterTypeDef,
        "additionalData": str,
    },
    total=False,
)

ClientGetCommitResponseTypeDef = TypedDict(
    "ClientGetCommitResponseTypeDef", {"commit": ClientGetCommitResponsecommitTypeDef}, total=False
)

ClientGetDifferencesResponsedifferencesafterBlobTypeDef = TypedDict(
    "ClientGetDifferencesResponsedifferencesafterBlobTypeDef",
    {"blobId": str, "path": str, "mode": str},
    total=False,
)

ClientGetDifferencesResponsedifferencesbeforeBlobTypeDef = TypedDict(
    "ClientGetDifferencesResponsedifferencesbeforeBlobTypeDef",
    {"blobId": str, "path": str, "mode": str},
    total=False,
)

ClientGetDifferencesResponsedifferencesTypeDef = TypedDict(
    "ClientGetDifferencesResponsedifferencesTypeDef",
    {
        "beforeBlob": ClientGetDifferencesResponsedifferencesbeforeBlobTypeDef,
        "afterBlob": ClientGetDifferencesResponsedifferencesafterBlobTypeDef,
        "changeType": Literal["A", "M", "D"],
    },
    total=False,
)

ClientGetDifferencesResponseTypeDef = TypedDict(
    "ClientGetDifferencesResponseTypeDef",
    {"differences": List[ClientGetDifferencesResponsedifferencesTypeDef], "NextToken": str},
    total=False,
)

ClientGetFileResponseTypeDef = TypedDict(
    "ClientGetFileResponseTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "filePath": str,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "fileSize": int,
        "fileContent": bytes,
    },
    total=False,
)

ClientGetFolderResponsefilesTypeDef = TypedDict(
    "ClientGetFolderResponsefilesTypeDef",
    {
        "blobId": str,
        "absolutePath": str,
        "relativePath": str,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)

ClientGetFolderResponsesubFoldersTypeDef = TypedDict(
    "ClientGetFolderResponsesubFoldersTypeDef",
    {"treeId": str, "absolutePath": str, "relativePath": str},
    total=False,
)

ClientGetFolderResponsesubModulesTypeDef = TypedDict(
    "ClientGetFolderResponsesubModulesTypeDef",
    {"commitId": str, "absolutePath": str, "relativePath": str},
    total=False,
)

ClientGetFolderResponsesymbolicLinksTypeDef = TypedDict(
    "ClientGetFolderResponsesymbolicLinksTypeDef",
    {
        "blobId": str,
        "absolutePath": str,
        "relativePath": str,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)

ClientGetFolderResponseTypeDef = TypedDict(
    "ClientGetFolderResponseTypeDef",
    {
        "commitId": str,
        "folderPath": str,
        "treeId": str,
        "subFolders": List[ClientGetFolderResponsesubFoldersTypeDef],
        "files": List[ClientGetFolderResponsefilesTypeDef],
        "symbolicLinks": List[ClientGetFolderResponsesymbolicLinksTypeDef],
        "subModules": List[ClientGetFolderResponsesubModulesTypeDef],
    },
    total=False,
)

ClientGetMergeCommitResponseTypeDef = TypedDict(
    "ClientGetMergeCommitResponseTypeDef",
    {"sourceCommitId": str, "destinationCommitId": str, "baseCommitId": str, "mergedCommitId": str},
    total=False,
)

ClientGetMergeConflictsResponseconflictMetadataListfileModesTypeDef = TypedDict(
    "ClientGetMergeConflictsResponseconflictMetadataListfileModesTypeDef",
    {
        "source": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "destination": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
        "base": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)

ClientGetMergeConflictsResponseconflictMetadataListfileSizesTypeDef = TypedDict(
    "ClientGetMergeConflictsResponseconflictMetadataListfileSizesTypeDef",
    {"source": int, "destination": int, "base": int},
    total=False,
)

ClientGetMergeConflictsResponseconflictMetadataListisBinaryFileTypeDef = TypedDict(
    "ClientGetMergeConflictsResponseconflictMetadataListisBinaryFileTypeDef",
    {"source": bool, "destination": bool, "base": bool},
    total=False,
)

ClientGetMergeConflictsResponseconflictMetadataListmergeOperationsTypeDef = TypedDict(
    "ClientGetMergeConflictsResponseconflictMetadataListmergeOperationsTypeDef",
    {"source": Literal["A", "M", "D"], "destination": Literal["A", "M", "D"]},
    total=False,
)

ClientGetMergeConflictsResponseconflictMetadataListobjectTypesTypeDef = TypedDict(
    "ClientGetMergeConflictsResponseconflictMetadataListobjectTypesTypeDef",
    {
        "source": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
        "destination": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
        "base": Literal["FILE", "DIRECTORY", "GIT_LINK", "SYMBOLIC_LINK"],
    },
    total=False,
)

ClientGetMergeConflictsResponseconflictMetadataListTypeDef = TypedDict(
    "ClientGetMergeConflictsResponseconflictMetadataListTypeDef",
    {
        "filePath": str,
        "fileSizes": ClientGetMergeConflictsResponseconflictMetadataListfileSizesTypeDef,
        "fileModes": ClientGetMergeConflictsResponseconflictMetadataListfileModesTypeDef,
        "objectTypes": ClientGetMergeConflictsResponseconflictMetadataListobjectTypesTypeDef,
        "numberOfConflicts": int,
        "isBinaryFile": ClientGetMergeConflictsResponseconflictMetadataListisBinaryFileTypeDef,
        "contentConflict": bool,
        "fileModeConflict": bool,
        "objectTypeConflict": bool,
        "mergeOperations": ClientGetMergeConflictsResponseconflictMetadataListmergeOperationsTypeDef,
    },
    total=False,
)

ClientGetMergeConflictsResponseTypeDef = TypedDict(
    "ClientGetMergeConflictsResponseTypeDef",
    {
        "mergeable": bool,
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
        "conflictMetadataList": List[ClientGetMergeConflictsResponseconflictMetadataListTypeDef],
        "nextToken": str,
    },
    total=False,
)

ClientGetMergeOptionsResponseTypeDef = TypedDict(
    "ClientGetMergeOptionsResponseTypeDef",
    {
        "mergeOptions": List[Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"]],
        "sourceCommitId": str,
        "destinationCommitId": str,
        "baseCommitId": str,
    },
    total=False,
)

ClientGetPullRequestApprovalStatesResponseapprovalsTypeDef = TypedDict(
    "ClientGetPullRequestApprovalStatesResponseapprovalsTypeDef",
    {"userArn": str, "approvalState": Literal["APPROVE", "REVOKE"]},
    total=False,
)

ClientGetPullRequestApprovalStatesResponseTypeDef = TypedDict(
    "ClientGetPullRequestApprovalStatesResponseTypeDef",
    {"approvals": List[ClientGetPullRequestApprovalStatesResponseapprovalsTypeDef]},
    total=False,
)

ClientGetPullRequestOverrideStateResponseTypeDef = TypedDict(
    "ClientGetPullRequestOverrideStateResponseTypeDef",
    {"overridden": bool, "overrider": str},
    total=False,
)

ClientGetPullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef = TypedDict(
    "ClientGetPullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)

ClientGetPullRequestResponsepullRequestapprovalRulesTypeDef = TypedDict(
    "ClientGetPullRequestResponsepullRequestapprovalRulesTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientGetPullRequestResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)

ClientGetPullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "ClientGetPullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)

ClientGetPullRequestResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "ClientGetPullRequestResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientGetPullRequestResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)

ClientGetPullRequestResponsepullRequestTypeDef = TypedDict(
    "ClientGetPullRequestResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": Literal["OPEN", "CLOSED"],
        "authorArn": str,
        "pullRequestTargets": List[
            ClientGetPullRequestResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List[ClientGetPullRequestResponsepullRequestapprovalRulesTypeDef],
    },
    total=False,
)

ClientGetPullRequestResponseTypeDef = TypedDict(
    "ClientGetPullRequestResponseTypeDef",
    {"pullRequest": ClientGetPullRequestResponsepullRequestTypeDef},
    total=False,
)

ClientGetRepositoryResponserepositoryMetadataTypeDef = TypedDict(
    "ClientGetRepositoryResponserepositoryMetadataTypeDef",
    {
        "accountId": str,
        "repositoryId": str,
        "repositoryName": str,
        "repositoryDescription": str,
        "defaultBranch": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "cloneUrlHttp": str,
        "cloneUrlSsh": str,
        "Arn": str,
    },
    total=False,
)

ClientGetRepositoryResponseTypeDef = TypedDict(
    "ClientGetRepositoryResponseTypeDef",
    {"repositoryMetadata": ClientGetRepositoryResponserepositoryMetadataTypeDef},
    total=False,
)

ClientGetRepositoryTriggersResponsetriggersTypeDef = TypedDict(
    "ClientGetRepositoryTriggersResponsetriggersTypeDef",
    {
        "name": str,
        "destinationArn": str,
        "customData": str,
        "branches": List[str],
        "events": List[Literal["all", "updateReference", "createReference", "deleteReference"]],
    },
    total=False,
)

ClientGetRepositoryTriggersResponseTypeDef = TypedDict(
    "ClientGetRepositoryTriggersResponseTypeDef",
    {"configurationId": str, "triggers": List[ClientGetRepositoryTriggersResponsetriggersTypeDef]},
    total=False,
)

ClientListApprovalRuleTemplatesResponseTypeDef = TypedDict(
    "ClientListApprovalRuleTemplatesResponseTypeDef",
    {"approvalRuleTemplateNames": List[str], "nextToken": str},
    total=False,
)

ClientListAssociatedApprovalRuleTemplatesForRepositoryResponseTypeDef = TypedDict(
    "ClientListAssociatedApprovalRuleTemplatesForRepositoryResponseTypeDef",
    {"approvalRuleTemplateNames": List[str], "nextToken": str},
    total=False,
)

ClientListBranchesResponseTypeDef = TypedDict(
    "ClientListBranchesResponseTypeDef", {"branches": List[str], "nextToken": str}, total=False
)

ClientListPullRequestsResponseTypeDef = TypedDict(
    "ClientListPullRequestsResponseTypeDef",
    {"pullRequestIds": List[str], "nextToken": str},
    total=False,
)

ClientListRepositoriesForApprovalRuleTemplateResponseTypeDef = TypedDict(
    "ClientListRepositoriesForApprovalRuleTemplateResponseTypeDef",
    {"repositoryNames": List[str], "nextToken": str},
    total=False,
)

ClientListRepositoriesResponserepositoriesTypeDef = TypedDict(
    "ClientListRepositoriesResponserepositoriesTypeDef",
    {"repositoryName": str, "repositoryId": str},
    total=False,
)

ClientListRepositoriesResponseTypeDef = TypedDict(
    "ClientListRepositoriesResponseTypeDef",
    {"repositories": List[ClientListRepositoriesResponserepositoriesTypeDef], "nextToken": str},
    total=False,
)

ClientListTagsForResourceResponseTypeDef = TypedDict(
    "ClientListTagsForResourceResponseTypeDef",
    {"tags": Dict[str, str], "nextToken": str},
    total=False,
)

ClientMergeBranchesByFastForwardResponseTypeDef = TypedDict(
    "ClientMergeBranchesByFastForwardResponseTypeDef", {"commitId": str, "treeId": str}, total=False
)

ClientMergeBranchesBySquashConflictResolutiondeleteFilesTypeDef = TypedDict(
    "ClientMergeBranchesBySquashConflictResolutiondeleteFilesTypeDef",
    {"filePath": str},
    total=False,
)

_RequiredClientMergeBranchesBySquashConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_RequiredClientMergeBranchesBySquashConflictResolutionreplaceContentsTypeDef",
    {"filePath": str},
)
_OptionalClientMergeBranchesBySquashConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_OptionalClientMergeBranchesBySquashConflictResolutionreplaceContentsTypeDef",
    {
        "replacementType": Literal[
            "KEEP_BASE", "KEEP_SOURCE", "KEEP_DESTINATION", "USE_NEW_CONTENT"
        ],
        "content": bytes,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)


class ClientMergeBranchesBySquashConflictResolutionreplaceContentsTypeDef(
    _RequiredClientMergeBranchesBySquashConflictResolutionreplaceContentsTypeDef,
    _OptionalClientMergeBranchesBySquashConflictResolutionreplaceContentsTypeDef,
):
    pass


ClientMergeBranchesBySquashConflictResolutionsetFileModesTypeDef = TypedDict(
    "ClientMergeBranchesBySquashConflictResolutionsetFileModesTypeDef",
    {"filePath": str, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)

ClientMergeBranchesBySquashConflictResolutionTypeDef = TypedDict(
    "ClientMergeBranchesBySquashConflictResolutionTypeDef",
    {
        "replaceContents": List[
            ClientMergeBranchesBySquashConflictResolutionreplaceContentsTypeDef
        ],
        "deleteFiles": List[ClientMergeBranchesBySquashConflictResolutiondeleteFilesTypeDef],
        "setFileModes": List[ClientMergeBranchesBySquashConflictResolutionsetFileModesTypeDef],
    },
    total=False,
)

ClientMergeBranchesBySquashResponseTypeDef = TypedDict(
    "ClientMergeBranchesBySquashResponseTypeDef", {"commitId": str, "treeId": str}, total=False
)

ClientMergeBranchesByThreeWayConflictResolutiondeleteFilesTypeDef = TypedDict(
    "ClientMergeBranchesByThreeWayConflictResolutiondeleteFilesTypeDef",
    {"filePath": str},
    total=False,
)

_RequiredClientMergeBranchesByThreeWayConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_RequiredClientMergeBranchesByThreeWayConflictResolutionreplaceContentsTypeDef",
    {"filePath": str},
)
_OptionalClientMergeBranchesByThreeWayConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_OptionalClientMergeBranchesByThreeWayConflictResolutionreplaceContentsTypeDef",
    {
        "replacementType": Literal[
            "KEEP_BASE", "KEEP_SOURCE", "KEEP_DESTINATION", "USE_NEW_CONTENT"
        ],
        "content": bytes,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)


class ClientMergeBranchesByThreeWayConflictResolutionreplaceContentsTypeDef(
    _RequiredClientMergeBranchesByThreeWayConflictResolutionreplaceContentsTypeDef,
    _OptionalClientMergeBranchesByThreeWayConflictResolutionreplaceContentsTypeDef,
):
    pass


ClientMergeBranchesByThreeWayConflictResolutionsetFileModesTypeDef = TypedDict(
    "ClientMergeBranchesByThreeWayConflictResolutionsetFileModesTypeDef",
    {"filePath": str, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)

ClientMergeBranchesByThreeWayConflictResolutionTypeDef = TypedDict(
    "ClientMergeBranchesByThreeWayConflictResolutionTypeDef",
    {
        "replaceContents": List[
            ClientMergeBranchesByThreeWayConflictResolutionreplaceContentsTypeDef
        ],
        "deleteFiles": List[ClientMergeBranchesByThreeWayConflictResolutiondeleteFilesTypeDef],
        "setFileModes": List[ClientMergeBranchesByThreeWayConflictResolutionsetFileModesTypeDef],
    },
    total=False,
)

ClientMergeBranchesByThreeWayResponseTypeDef = TypedDict(
    "ClientMergeBranchesByThreeWayResponseTypeDef", {"commitId": str, "treeId": str}, total=False
)

ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef = TypedDict(
    "ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)

ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesTypeDef = TypedDict(
    "ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)

ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)

ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)

ClientMergePullRequestByFastForwardResponsepullRequestTypeDef = TypedDict(
    "ClientMergePullRequestByFastForwardResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": Literal["OPEN", "CLOSED"],
        "authorArn": str,
        "pullRequestTargets": List[
            ClientMergePullRequestByFastForwardResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List[
            ClientMergePullRequestByFastForwardResponsepullRequestapprovalRulesTypeDef
        ],
    },
    total=False,
)

ClientMergePullRequestByFastForwardResponseTypeDef = TypedDict(
    "ClientMergePullRequestByFastForwardResponseTypeDef",
    {"pullRequest": ClientMergePullRequestByFastForwardResponsepullRequestTypeDef},
    total=False,
)

ClientMergePullRequestBySquashConflictResolutiondeleteFilesTypeDef = TypedDict(
    "ClientMergePullRequestBySquashConflictResolutiondeleteFilesTypeDef",
    {"filePath": str},
    total=False,
)

_RequiredClientMergePullRequestBySquashConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_RequiredClientMergePullRequestBySquashConflictResolutionreplaceContentsTypeDef",
    {"filePath": str},
)
_OptionalClientMergePullRequestBySquashConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_OptionalClientMergePullRequestBySquashConflictResolutionreplaceContentsTypeDef",
    {
        "replacementType": Literal[
            "KEEP_BASE", "KEEP_SOURCE", "KEEP_DESTINATION", "USE_NEW_CONTENT"
        ],
        "content": bytes,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)


class ClientMergePullRequestBySquashConflictResolutionreplaceContentsTypeDef(
    _RequiredClientMergePullRequestBySquashConflictResolutionreplaceContentsTypeDef,
    _OptionalClientMergePullRequestBySquashConflictResolutionreplaceContentsTypeDef,
):
    pass


ClientMergePullRequestBySquashConflictResolutionsetFileModesTypeDef = TypedDict(
    "ClientMergePullRequestBySquashConflictResolutionsetFileModesTypeDef",
    {"filePath": str, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)

ClientMergePullRequestBySquashConflictResolutionTypeDef = TypedDict(
    "ClientMergePullRequestBySquashConflictResolutionTypeDef",
    {
        "replaceContents": List[
            ClientMergePullRequestBySquashConflictResolutionreplaceContentsTypeDef
        ],
        "deleteFiles": List[ClientMergePullRequestBySquashConflictResolutiondeleteFilesTypeDef],
        "setFileModes": List[ClientMergePullRequestBySquashConflictResolutionsetFileModesTypeDef],
    },
    total=False,
)

ClientMergePullRequestBySquashResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef = TypedDict(
    "ClientMergePullRequestBySquashResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)

ClientMergePullRequestBySquashResponsepullRequestapprovalRulesTypeDef = TypedDict(
    "ClientMergePullRequestBySquashResponsepullRequestapprovalRulesTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientMergePullRequestBySquashResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)

ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)

ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)

ClientMergePullRequestBySquashResponsepullRequestTypeDef = TypedDict(
    "ClientMergePullRequestBySquashResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": Literal["OPEN", "CLOSED"],
        "authorArn": str,
        "pullRequestTargets": List[
            ClientMergePullRequestBySquashResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List[
            ClientMergePullRequestBySquashResponsepullRequestapprovalRulesTypeDef
        ],
    },
    total=False,
)

ClientMergePullRequestBySquashResponseTypeDef = TypedDict(
    "ClientMergePullRequestBySquashResponseTypeDef",
    {"pullRequest": ClientMergePullRequestBySquashResponsepullRequestTypeDef},
    total=False,
)

ClientMergePullRequestByThreeWayConflictResolutiondeleteFilesTypeDef = TypedDict(
    "ClientMergePullRequestByThreeWayConflictResolutiondeleteFilesTypeDef",
    {"filePath": str},
    total=False,
)

_RequiredClientMergePullRequestByThreeWayConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_RequiredClientMergePullRequestByThreeWayConflictResolutionreplaceContentsTypeDef",
    {"filePath": str},
)
_OptionalClientMergePullRequestByThreeWayConflictResolutionreplaceContentsTypeDef = TypedDict(
    "_OptionalClientMergePullRequestByThreeWayConflictResolutionreplaceContentsTypeDef",
    {
        "replacementType": Literal[
            "KEEP_BASE", "KEEP_SOURCE", "KEEP_DESTINATION", "USE_NEW_CONTENT"
        ],
        "content": bytes,
        "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"],
    },
    total=False,
)


class ClientMergePullRequestByThreeWayConflictResolutionreplaceContentsTypeDef(
    _RequiredClientMergePullRequestByThreeWayConflictResolutionreplaceContentsTypeDef,
    _OptionalClientMergePullRequestByThreeWayConflictResolutionreplaceContentsTypeDef,
):
    pass


ClientMergePullRequestByThreeWayConflictResolutionsetFileModesTypeDef = TypedDict(
    "ClientMergePullRequestByThreeWayConflictResolutionsetFileModesTypeDef",
    {"filePath": str, "fileMode": Literal["EXECUTABLE", "NORMAL", "SYMLINK"]},
    total=False,
)

ClientMergePullRequestByThreeWayConflictResolutionTypeDef = TypedDict(
    "ClientMergePullRequestByThreeWayConflictResolutionTypeDef",
    {
        "replaceContents": List[
            ClientMergePullRequestByThreeWayConflictResolutionreplaceContentsTypeDef
        ],
        "deleteFiles": List[ClientMergePullRequestByThreeWayConflictResolutiondeleteFilesTypeDef],
        "setFileModes": List[ClientMergePullRequestByThreeWayConflictResolutionsetFileModesTypeDef],
    },
    total=False,
)

ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef = TypedDict(
    "ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)

ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesTypeDef = TypedDict(
    "ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)

ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)

ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)

ClientMergePullRequestByThreeWayResponsepullRequestTypeDef = TypedDict(
    "ClientMergePullRequestByThreeWayResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": Literal["OPEN", "CLOSED"],
        "authorArn": str,
        "pullRequestTargets": List[
            ClientMergePullRequestByThreeWayResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List[
            ClientMergePullRequestByThreeWayResponsepullRequestapprovalRulesTypeDef
        ],
    },
    total=False,
)

ClientMergePullRequestByThreeWayResponseTypeDef = TypedDict(
    "ClientMergePullRequestByThreeWayResponseTypeDef",
    {"pullRequest": ClientMergePullRequestByThreeWayResponsepullRequestTypeDef},
    total=False,
)

ClientPostCommentForComparedCommitLocationTypeDef = TypedDict(
    "ClientPostCommentForComparedCommitLocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": Literal["BEFORE", "AFTER"]},
    total=False,
)

ClientPostCommentForComparedCommitResponsecommentTypeDef = TypedDict(
    "ClientPostCommentForComparedCommitResponsecommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)

ClientPostCommentForComparedCommitResponselocationTypeDef = TypedDict(
    "ClientPostCommentForComparedCommitResponselocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": Literal["BEFORE", "AFTER"]},
    total=False,
)

ClientPostCommentForComparedCommitResponseTypeDef = TypedDict(
    "ClientPostCommentForComparedCommitResponseTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": ClientPostCommentForComparedCommitResponselocationTypeDef,
        "comment": ClientPostCommentForComparedCommitResponsecommentTypeDef,
    },
    total=False,
)

ClientPostCommentForPullRequestLocationTypeDef = TypedDict(
    "ClientPostCommentForPullRequestLocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": Literal["BEFORE", "AFTER"]},
    total=False,
)

ClientPostCommentForPullRequestResponsecommentTypeDef = TypedDict(
    "ClientPostCommentForPullRequestResponsecommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)

ClientPostCommentForPullRequestResponselocationTypeDef = TypedDict(
    "ClientPostCommentForPullRequestResponselocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": Literal["BEFORE", "AFTER"]},
    total=False,
)

ClientPostCommentForPullRequestResponseTypeDef = TypedDict(
    "ClientPostCommentForPullRequestResponseTypeDef",
    {
        "repositoryName": str,
        "pullRequestId": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": ClientPostCommentForPullRequestResponselocationTypeDef,
        "comment": ClientPostCommentForPullRequestResponsecommentTypeDef,
    },
    total=False,
)

ClientPostCommentReplyResponsecommentTypeDef = TypedDict(
    "ClientPostCommentReplyResponsecommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)

ClientPostCommentReplyResponseTypeDef = TypedDict(
    "ClientPostCommentReplyResponseTypeDef",
    {"comment": ClientPostCommentReplyResponsecommentTypeDef},
    total=False,
)

ClientPutFileResponseTypeDef = TypedDict(
    "ClientPutFileResponseTypeDef", {"commitId": str, "blobId": str, "treeId": str}, total=False
)

ClientPutRepositoryTriggersResponseTypeDef = TypedDict(
    "ClientPutRepositoryTriggersResponseTypeDef", {"configurationId": str}, total=False
)

_RequiredClientPutRepositoryTriggersTriggersTypeDef = TypedDict(
    "_RequiredClientPutRepositoryTriggersTriggersTypeDef", {"name": str}
)
_OptionalClientPutRepositoryTriggersTriggersTypeDef = TypedDict(
    "_OptionalClientPutRepositoryTriggersTriggersTypeDef",
    {
        "destinationArn": str,
        "customData": str,
        "branches": List[str],
        "events": List[Literal["all", "updateReference", "createReference", "deleteReference"]],
    },
    total=False,
)


class ClientPutRepositoryTriggersTriggersTypeDef(
    _RequiredClientPutRepositoryTriggersTriggersTypeDef,
    _OptionalClientPutRepositoryTriggersTriggersTypeDef,
):
    pass


ClientTestRepositoryTriggersResponsefailedExecutionsTypeDef = TypedDict(
    "ClientTestRepositoryTriggersResponsefailedExecutionsTypeDef",
    {"trigger": str, "failureMessage": str},
    total=False,
)

ClientTestRepositoryTriggersResponseTypeDef = TypedDict(
    "ClientTestRepositoryTriggersResponseTypeDef",
    {
        "successfulExecutions": List[str],
        "failedExecutions": List[ClientTestRepositoryTriggersResponsefailedExecutionsTypeDef],
    },
    total=False,
)

_RequiredClientTestRepositoryTriggersTriggersTypeDef = TypedDict(
    "_RequiredClientTestRepositoryTriggersTriggersTypeDef", {"name": str}
)
_OptionalClientTestRepositoryTriggersTriggersTypeDef = TypedDict(
    "_OptionalClientTestRepositoryTriggersTriggersTypeDef",
    {
        "destinationArn": str,
        "customData": str,
        "branches": List[str],
        "events": List[Literal["all", "updateReference", "createReference", "deleteReference"]],
    },
    total=False,
)


class ClientTestRepositoryTriggersTriggersTypeDef(
    _RequiredClientTestRepositoryTriggersTriggersTypeDef,
    _OptionalClientTestRepositoryTriggersTriggersTypeDef,
):
    pass


ClientUpdateApprovalRuleTemplateContentResponseapprovalRuleTemplateTypeDef = TypedDict(
    "ClientUpdateApprovalRuleTemplateContentResponseapprovalRuleTemplateTypeDef",
    {
        "approvalRuleTemplateId": str,
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateDescription": str,
        "approvalRuleTemplateContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
    },
    total=False,
)

ClientUpdateApprovalRuleTemplateContentResponseTypeDef = TypedDict(
    "ClientUpdateApprovalRuleTemplateContentResponseTypeDef",
    {
        "approvalRuleTemplate": ClientUpdateApprovalRuleTemplateContentResponseapprovalRuleTemplateTypeDef
    },
    total=False,
)

ClientUpdateApprovalRuleTemplateDescriptionResponseapprovalRuleTemplateTypeDef = TypedDict(
    "ClientUpdateApprovalRuleTemplateDescriptionResponseapprovalRuleTemplateTypeDef",
    {
        "approvalRuleTemplateId": str,
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateDescription": str,
        "approvalRuleTemplateContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
    },
    total=False,
)

ClientUpdateApprovalRuleTemplateDescriptionResponseTypeDef = TypedDict(
    "ClientUpdateApprovalRuleTemplateDescriptionResponseTypeDef",
    {
        "approvalRuleTemplate": ClientUpdateApprovalRuleTemplateDescriptionResponseapprovalRuleTemplateTypeDef
    },
    total=False,
)

ClientUpdateApprovalRuleTemplateNameResponseapprovalRuleTemplateTypeDef = TypedDict(
    "ClientUpdateApprovalRuleTemplateNameResponseapprovalRuleTemplateTypeDef",
    {
        "approvalRuleTemplateId": str,
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateDescription": str,
        "approvalRuleTemplateContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
    },
    total=False,
)

ClientUpdateApprovalRuleTemplateNameResponseTypeDef = TypedDict(
    "ClientUpdateApprovalRuleTemplateNameResponseTypeDef",
    {
        "approvalRuleTemplate": ClientUpdateApprovalRuleTemplateNameResponseapprovalRuleTemplateTypeDef
    },
    total=False,
)

ClientUpdateCommentResponsecommentTypeDef = TypedDict(
    "ClientUpdateCommentResponsecommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)

ClientUpdateCommentResponseTypeDef = TypedDict(
    "ClientUpdateCommentResponseTypeDef",
    {"comment": ClientUpdateCommentResponsecommentTypeDef},
    total=False,
)

ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleoriginApprovalRuleTemplateTypeDef = TypedDict(
    "ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)

ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleTypeDef = TypedDict(
    "ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)

ClientUpdatePullRequestApprovalRuleContentResponseTypeDef = TypedDict(
    "ClientUpdatePullRequestApprovalRuleContentResponseTypeDef",
    {"approvalRule": ClientUpdatePullRequestApprovalRuleContentResponseapprovalRuleTypeDef},
    total=False,
)

ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef = TypedDict(
    "ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)

ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesTypeDef = TypedDict(
    "ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)

ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)

ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)

ClientUpdatePullRequestDescriptionResponsepullRequestTypeDef = TypedDict(
    "ClientUpdatePullRequestDescriptionResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": Literal["OPEN", "CLOSED"],
        "authorArn": str,
        "pullRequestTargets": List[
            ClientUpdatePullRequestDescriptionResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List[
            ClientUpdatePullRequestDescriptionResponsepullRequestapprovalRulesTypeDef
        ],
    },
    total=False,
)

ClientUpdatePullRequestDescriptionResponseTypeDef = TypedDict(
    "ClientUpdatePullRequestDescriptionResponseTypeDef",
    {"pullRequest": ClientUpdatePullRequestDescriptionResponsepullRequestTypeDef},
    total=False,
)

ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef = TypedDict(
    "ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)

ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesTypeDef = TypedDict(
    "ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)

ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)

ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)

ClientUpdatePullRequestStatusResponsepullRequestTypeDef = TypedDict(
    "ClientUpdatePullRequestStatusResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": Literal["OPEN", "CLOSED"],
        "authorArn": str,
        "pullRequestTargets": List[
            ClientUpdatePullRequestStatusResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List[ClientUpdatePullRequestStatusResponsepullRequestapprovalRulesTypeDef],
    },
    total=False,
)

ClientUpdatePullRequestStatusResponseTypeDef = TypedDict(
    "ClientUpdatePullRequestStatusResponseTypeDef",
    {"pullRequest": ClientUpdatePullRequestStatusResponsepullRequestTypeDef},
    total=False,
)

ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef = TypedDict(
    "ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef",
    {"approvalRuleTemplateId": str, "approvalRuleTemplateName": str},
    total=False,
)

ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesTypeDef = TypedDict(
    "ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesTypeDef",
    {
        "approvalRuleId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
        "ruleContentSha256": str,
        "lastModifiedDate": datetime,
        "creationDate": datetime,
        "lastModifiedUser": str,
        "originApprovalRuleTemplate": ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesoriginApprovalRuleTemplateTypeDef,
    },
    total=False,
)

ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsmergeMetadataTypeDef = TypedDict(
    "ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsmergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)

ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsTypeDef = TypedDict(
    "ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": str,
        "destinationCommit": str,
        "sourceCommit": str,
        "mergeBase": str,
        "mergeMetadata": ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsmergeMetadataTypeDef,
    },
    total=False,
)

ClientUpdatePullRequestTitleResponsepullRequestTypeDef = TypedDict(
    "ClientUpdatePullRequestTitleResponsepullRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
        "description": str,
        "lastActivityDate": datetime,
        "creationDate": datetime,
        "pullRequestStatus": Literal["OPEN", "CLOSED"],
        "authorArn": str,
        "pullRequestTargets": List[
            ClientUpdatePullRequestTitleResponsepullRequestpullRequestTargetsTypeDef
        ],
        "clientRequestToken": str,
        "revisionId": str,
        "approvalRules": List[ClientUpdatePullRequestTitleResponsepullRequestapprovalRulesTypeDef],
    },
    total=False,
)

ClientUpdatePullRequestTitleResponseTypeDef = TypedDict(
    "ClientUpdatePullRequestTitleResponseTypeDef",
    {"pullRequest": ClientUpdatePullRequestTitleResponsepullRequestTypeDef},
    total=False,
)

ApprovalRuleEventMetadataTypeDef = TypedDict(
    "ApprovalRuleEventMetadataTypeDef",
    {"approvalRuleName": str, "approvalRuleId": str, "approvalRuleContent": str},
    total=False,
)

ApprovalRuleOverriddenEventMetadataTypeDef = TypedDict(
    "ApprovalRuleOverriddenEventMetadataTypeDef",
    {"revisionId": str, "overrideStatus": Literal["OVERRIDE", "REVOKE"]},
    total=False,
)

ApprovalStateChangedEventMetadataTypeDef = TypedDict(
    "ApprovalStateChangedEventMetadataTypeDef",
    {"revisionId": str, "approvalStatus": Literal["APPROVE", "REVOKE"]},
    total=False,
)

PullRequestCreatedEventMetadataTypeDef = TypedDict(
    "PullRequestCreatedEventMetadataTypeDef",
    {"repositoryName": str, "sourceCommitId": str, "destinationCommitId": str, "mergeBase": str},
    total=False,
)

MergeMetadataTypeDef = TypedDict(
    "MergeMetadataTypeDef",
    {
        "isMerged": bool,
        "mergedBy": str,
        "mergeCommitId": str,
        "mergeOption": Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"],
    },
    total=False,
)

PullRequestMergedStateChangedEventMetadataTypeDef = TypedDict(
    "PullRequestMergedStateChangedEventMetadataTypeDef",
    {"repositoryName": str, "destinationReference": str, "mergeMetadata": MergeMetadataTypeDef},
    total=False,
)

PullRequestSourceReferenceUpdatedEventMetadataTypeDef = TypedDict(
    "PullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    {"repositoryName": str, "beforeCommitId": str, "afterCommitId": str, "mergeBase": str},
    total=False,
)

PullRequestStatusChangedEventMetadataTypeDef = TypedDict(
    "PullRequestStatusChangedEventMetadataTypeDef",
    {"pullRequestStatus": Literal["OPEN", "CLOSED"]},
    total=False,
)

PullRequestEventTypeDef = TypedDict(
    "PullRequestEventTypeDef",
    {
        "pullRequestId": str,
        "eventDate": datetime,
        "pullRequestEventType": Literal[
            "PULL_REQUEST_CREATED",
            "PULL_REQUEST_STATUS_CHANGED",
            "PULL_REQUEST_SOURCE_REFERENCE_UPDATED",
            "PULL_REQUEST_MERGE_STATE_CHANGED",
            "PULL_REQUEST_APPROVAL_RULE_CREATED",
            "PULL_REQUEST_APPROVAL_RULE_UPDATED",
            "PULL_REQUEST_APPROVAL_RULE_DELETED",
            "PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN",
            "PULL_REQUEST_APPROVAL_STATE_CHANGED",
        ],
        "actorArn": str,
        "pullRequestCreatedEventMetadata": PullRequestCreatedEventMetadataTypeDef,
        "pullRequestStatusChangedEventMetadata": PullRequestStatusChangedEventMetadataTypeDef,
        "pullRequestSourceReferenceUpdatedEventMetadata": PullRequestSourceReferenceUpdatedEventMetadataTypeDef,
        "pullRequestMergedStateChangedEventMetadata": PullRequestMergedStateChangedEventMetadataTypeDef,
        "approvalRuleEventMetadata": ApprovalRuleEventMetadataTypeDef,
        "approvalStateChangedEventMetadata": ApprovalStateChangedEventMetadataTypeDef,
        "approvalRuleOverriddenEventMetadata": ApprovalRuleOverriddenEventMetadataTypeDef,
    },
    total=False,
)

_RequiredDescribePullRequestEventsOutputTypeDef = TypedDict(
    "_RequiredDescribePullRequestEventsOutputTypeDef",
    {"pullRequestEvents": List[PullRequestEventTypeDef]},
)
_OptionalDescribePullRequestEventsOutputTypeDef = TypedDict(
    "_OptionalDescribePullRequestEventsOutputTypeDef", {"nextToken": str}, total=False
)


class DescribePullRequestEventsOutputTypeDef(
    _RequiredDescribePullRequestEventsOutputTypeDef, _OptionalDescribePullRequestEventsOutputTypeDef
):
    pass


CommentTypeDef = TypedDict(
    "CommentTypeDef",
    {
        "commentId": str,
        "content": str,
        "inReplyTo": str,
        "creationDate": datetime,
        "lastModifiedDate": datetime,
        "authorArn": str,
        "deleted": bool,
        "clientRequestToken": str,
    },
    total=False,
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {"filePath": str, "filePosition": int, "relativeFileVersion": Literal["BEFORE", "AFTER"]},
    total=False,
)

CommentsForComparedCommitTypeDef = TypedDict(
    "CommentsForComparedCommitTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": LocationTypeDef,
        "comments": List[CommentTypeDef],
    },
    total=False,
)

GetCommentsForComparedCommitOutputTypeDef = TypedDict(
    "GetCommentsForComparedCommitOutputTypeDef",
    {"commentsForComparedCommitData": List[CommentsForComparedCommitTypeDef], "nextToken": str},
    total=False,
)

CommentsForPullRequestTypeDef = TypedDict(
    "CommentsForPullRequestTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": LocationTypeDef,
        "comments": List[CommentTypeDef],
    },
    total=False,
)

GetCommentsForPullRequestOutputTypeDef = TypedDict(
    "GetCommentsForPullRequestOutputTypeDef",
    {"commentsForPullRequestData": List[CommentsForPullRequestTypeDef], "nextToken": str},
    total=False,
)

BlobMetadataTypeDef = TypedDict(
    "BlobMetadataTypeDef", {"blobId": str, "path": str, "mode": str}, total=False
)

DifferenceTypeDef = TypedDict(
    "DifferenceTypeDef",
    {
        "beforeBlob": BlobMetadataTypeDef,
        "afterBlob": BlobMetadataTypeDef,
        "changeType": Literal["A", "M", "D"],
    },
    total=False,
)

GetDifferencesOutputTypeDef = TypedDict(
    "GetDifferencesOutputTypeDef",
    {"differences": List[DifferenceTypeDef], "NextToken": str},
    total=False,
)

ListBranchesOutputTypeDef = TypedDict(
    "ListBranchesOutputTypeDef", {"branches": List[str], "nextToken": str}, total=False
)

_RequiredListPullRequestsOutputTypeDef = TypedDict(
    "_RequiredListPullRequestsOutputTypeDef", {"pullRequestIds": List[str]}
)
_OptionalListPullRequestsOutputTypeDef = TypedDict(
    "_OptionalListPullRequestsOutputTypeDef", {"nextToken": str}, total=False
)


class ListPullRequestsOutputTypeDef(
    _RequiredListPullRequestsOutputTypeDef, _OptionalListPullRequestsOutputTypeDef
):
    pass


RepositoryNameIdPairTypeDef = TypedDict(
    "RepositoryNameIdPairTypeDef", {"repositoryName": str, "repositoryId": str}, total=False
)

ListRepositoriesOutputTypeDef = TypedDict(
    "ListRepositoriesOutputTypeDef",
    {"repositories": List[RepositoryNameIdPairTypeDef], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
