# TotoEventConsumer is a utility class to manage the consumption of events in a PubSub architecture
# It is right now made for Google Pubsub

import os
import json
import datetime

from google.cloud import pubsub_v1
from google.api_core.exceptions import NotFound, AlreadyExists
from toto_logger.logger import TotoLogger

# Read the project id from an ENV variable
project_id = os.environ['TOTO_EVENTS_GCP_PROJECT_ID']

# Create a publisher
publisher = pubsub_v1.PublisherClient()

logger = TotoLogger()

class TotoEventPublisher: 

    def __init__(self, microservice, topics):
        '''
        Constructor
        
        Parameters: 
        microservice (string): the name of the toto microservice
        topics (list): a list of topic names (just the name, no project id)
        '''
        self.microservice = microservice
        self.topics = topics

        # Create the subscriptions
        for i in range(len(topics)): 

            topic = topics[i]

            topic_name = 'projects/{project_id}/topics/{topic}'.format( project_id=project_id, topic=topic )

            # Try to create the topic
            try: 
                publisher.create_topic(topic_name)
            except AlreadyExists:
                pass
            

    def publish(self, topic, event): 
        '''
        Publishes the specified event to the specified topic.
        Note that the topic is just the name, not inclusive of the project (that will be generated automatically).

        Parameters: 
        topic (string): the name of the topic
        event (dict): a dict representing the event, that will be transformed in json and encoded in utf-8 when publishing it
        '''
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]
        cid = event['correlationId']
        mid = ''

        # Define the topic name
        topic_name = 'projects/{project_id}/topics/{topic}'.format( project_id=project_id, topic=topic )

        msg = json.dumps(event)

        publisher.publish(topic_name, msg.encode('utf-8'))

        logger.event_out(cid, topic, mid)

    