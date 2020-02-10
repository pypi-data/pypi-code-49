# Imports from other dependencies.
from celery import shared_task
from celery.utils.log import get_task_logger


# Imports from election_loader.
from election_loader.loaders.election import create_candidate_election


logger = get_task_logger(__name__)


@shared_task
def process_election_metadata(races):
    for race in races:
        try:
            create_candidate_election(race)
        except Exception as e:
            print(e)
