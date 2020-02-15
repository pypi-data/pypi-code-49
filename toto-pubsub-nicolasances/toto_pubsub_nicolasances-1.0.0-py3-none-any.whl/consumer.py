# TotoEventConsumer is a utility class to manage the consumption of events in a PubSub architecture
# It is right now made for Google Pubsub

import os
import json
import datetime

from google.cloud import pubsub_v1
from google.api_core.exceptions import NotFound, AlreadyExists
from toto_logger.logger import TotoLogger
from json.decoder import JSONDecodeError

# Read the project id from an ENV variable
project_id = os.environ['TOTO_EVENTS_GCP_PROJECT_ID']

# Create subscriber and publisher
# We create a publisher because in case the topic doesn't exist it needs to be created
subscriber = pubsub_v1.SubscriberClient()
publisher = pubsub_v1.PublisherClient()

logger = TotoLogger()

def handler_decorator(handler, topic): 
    '''
    Generates decorators of event handlers
    Decorators add additional behaviour to the handler, like: 
     - correlation id management
     - logging
    
    Parameters:
    dest_handler (func): the target callback function that will handle the message
    '''
    def _handler(message):
        
        # Convert to json 
        try: 
            msg_dict = json.loads(message.data)
        except JSONDecodeError as e: 
            logger.compute('no-id', "Event {} was not in the expected format. Got error {}".format(message.data, e), 'error')
            message.ack()
            return

        # Extract the correlation Id 
        cid = 'no-cid'
        mid = 'no-mid'
        try: 
            cid = msg_dict['correlationId']
        except TypeError as e:
            logger.compute('no-id', "Processing of event {} got TypeError: {}".format(message.data, e), 'error')
            message.ack()
            return
        except KeyError as ke: 
            pass
        try: 
            mid = msg_dict['msgId']
        except KeyError as ke: 
            pass

        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]

        logger.event_in(cid, topic, mid)

        handler(msg_dict)

        message.ack()
    
    return _handler

class TotoEventConsumer: 

    def __init__(self, microservice, topics, on_message_funcs):
        '''
        Constructor
        
        Parameters: 
        microservice (string): the name of the toto microservice
        topics (list): a list of topic names (just the name, no project id)
        on_message_funcs (list): a list of functions (handlers for the messages of each topic)
        '''
        self.microservice = microservice
        self.topics = topics
        self.on_message_funcs = on_message_funcs

        # Create the subscriptions
        for i in range(len(topics)): 

            topic = topics[i]
            on_message = on_message_funcs[i]

            topic_name = 'projects/{project_id}/topics/{topic}'.format( project_id=project_id, topic=topic )
            sub_name = topic + '-' + microservice

            subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format( project_id=project_id, sub=sub_name)

            # Try to create the subscription
            # If the topic is not found, then create it! 
            try: 
                subscriber.create_subscription(name=subscription_name, topic=topic_name)
            except NotFound: 
                logger.compute('no-id', 'Topic {} not found. Creating it...'.format(topic_name), 'info')
                publisher.create_topic(topic_name)
                subscriber.create_subscription(name=subscription_name, topic=topic_name)
            except AlreadyExists:
                logger.compute('no-id', 'Subscription {} already exists'.format(subscription_name), 'info')
                pass
            
            subscriber.subscribe(subscription_name, handler_decorator(on_message, topic))

    