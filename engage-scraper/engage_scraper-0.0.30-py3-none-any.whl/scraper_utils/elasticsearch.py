import requests
import os
import json

ES_HOSTNAME = os.environ.get('ES_HOSTNAME', 'es01')
ES_INDEX_NAME = os.environ.get('ES_INDEX_NAME', 'agenda_items')


class ElasticsearchUtility():
    def __init__(self):
        # Check if ES_INDEX_NAME exists, if not, create it
        agenda_items = {
            "settings": {
                "number_of_shards": 1
            },
            "mappings": {
                "dynamic": "strict",
                "properties": {
                    "date": {
                        "type": "date"
                    },
                    "agenda_item_id": {
                        "type": "long"
                    },
                    "agenda_id": {
                        "type": "long"
                    },
                    "title": {
                        "type": "text",
                        "index": "true",
                        "index_phrases": "true"
                    },
                    "recommendations": {
                        "type": "text",
                        "index": "true",
                        "index_phrases": "true"
                    },
                    "body": {
                        "type": "text",
                        "index": "true",
                        "index_phrases": "true"
                    },
                    "department": {
                        "type": "keyword"
                    },
                    "sponsors": {
                        "type": "text"
                    },
                    "tags": {
                        "type": "keyword"
                    },
                    "committee": {
                        "type": "text"
                    },
                    "committee_id": {
                        "type": "long",
                        "index": "true"
                    }
                }
            }
        }
        r = requests.head(f"http://{ES_HOSTNAME}/{ES_INDEX_NAME}:9200"Ï)
        self.status = r.status_code

    def postItems(self, items=None):
        """
        helper function to load scrapped agenda item to elastic search

            Args: 
                items: dict, key/value pairs representing elasticseaech index fileds. The accepted
                        keys are:
                            - date: date, meeting date
                            - agenda_item_id: int, agenda item id
                            - agenda_id: int, the id of the specific meeting
                            - title: str, the title of the agenda
                            - recommendations: str, the propposed recommendation from the city
                            - body: str, details about the items
                            - department: list, all departments concerned with the item
                            - sponsors: str,
                            - tags: None
                            - committee: str, the name of the comittee,
                            - committee_id: int, the id of the comitte
            Returns:
                str, 
        """

        url = f'http://{ES_ENPOINT_NAME}:9200/{ES_INDEX_NAME}/_doc/'

        payload = {
            'date': items.get('date'),
            'agenda_item_id': int(items.get('agenda_item_id')),
            'agenda_id': items.get('agenda_id'),
            'title': items.get('title'),
            'recommendations': items.get('recommendations'),
            'body': items.get('body'),
            'department': items.get('department').split(','),
            'sponsors': items.get('sponsors'),
            'tags': items.get('tags'),
            'committee': items.get('committee'),
            'committee_id': items.get('committee_id'),
        }

        r = requests.post(url, json=payload)
        response = json.loads(r.text)

        if not response.get('_shards'):
            err = response.get("error")
            return False
        else:
            index, id = response.get('_index'), response.get('_id')
            return True
