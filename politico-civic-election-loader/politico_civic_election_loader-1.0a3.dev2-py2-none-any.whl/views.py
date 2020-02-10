# Imports from python.
import json


# Imports from other dependencies.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# Imports from election_loader.
from election_loader.tasks.process_metadata import process_election_metadata
from election_loader.utils.api_auth import CsrfExemptSessionAuthentication
from election_loader.utils.api_auth import TokenAPIAuthentication


class MetadataImportView(APIView):
    authentication_classes = [
        CsrfExemptSessionAuthentication,
        TokenAPIAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        json_body = json.loads(request.body)

        process_election_metadata.delay(json_body)

        # TODO: Queue a Celery task to process this data. Return its ID here.

        # A separate process will be responsible for pulling race and candidate
        # metadata back _out_ of Civic when it's ready, and having this task ID
        # will help that process determine when it can start that step.
        task_id = "TK"

        content = {
            "status": 202,
            "task_id": task_id,
            "queued_items": len(json_body),
            "message": (
                f"Queued {len(json_body)} metadata objects for insertion."
            ),
            "requested_by": request.auth.uid,
        }

        return Response(content, status=status.HTTP_202_ACCEPTED)
