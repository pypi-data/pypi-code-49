# Imports from Django.
from django.urls import path
from django.urls import re_path


# Imports from election_loader.
from election_loader.views import MetadataImportView
from election_loader.viewsets import StateDetail
from election_loader.viewsets import StateList


urlpatterns = [
    path("metadata/import/", MetadataImportView.as_view()),
    re_path(
        r"^api/elections/(?P<date>\d{4}-\d{2}-\d{2})/states/$",
        StateList.as_view(),
        name="electionnight_api_state-election-list",
    ),
    re_path(
        r"^api/elections/(?P<date>\d{4}-\d{2}-\d{2})/states/(?P<pk>.+)/$",
        StateDetail.as_view(),
        name="electionnight_api_state-election-detail",
    ),
]
