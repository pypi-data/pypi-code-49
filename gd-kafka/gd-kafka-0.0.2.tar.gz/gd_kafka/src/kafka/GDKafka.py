from operator import itemgetter
import itertools
import json
import kafka
from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic

class GDKafka():

    '''
    GDKafka: used to send data to kafka server.
    Have two important functions: send_to_one, send_to_multi

    '''

    def __init__(self,IP_Port=""):

        """
        Establish the connection to Kafka server.
        """

        try:
            self.KAFKA_IP_PORT = IP_Port

            if self.KAFKA_IP_PORT is None:
                print("Please provide a valid KAFKA_IP_PORT")
            elif self.KAFKA_IP_PORT.strip() is "":
                print("KAFKA_IP_PORT can't be empty.")
            else:
                try:
                    self.kafka_client = kafka.KafkaClient(bootstrap_servers = self.KAFKA_IP_PORT)
                    
                    self.admin_client = KafkaAdminClient(bootstrap_servers=self.KAFKA_IP_PORT)
                    
                    self.destination_kafka_producer = KafkaProducer(bootstrap_servers=[self.KAFKA_IP_PORT], value_serializer = lambda x:json.dumps(x).encode('utf-8'))
                    
                    print("Kafka connection established successfully.")
                except Exception as e:
                    print("Couldn't connect to Kafka Server")
                    print(e)
                    raise 
        except Exception as e:
            print("\n"+str(e))
    

    def on_send_success(self,record_metadata):
        print('sent..')
        # print(record_metadata.topic)
        # print(record_metadata.partition)
        # print(record_metadata.offset)

    def on_send_error(self,post,excp):
        print('ERROR=============================================================>')
        print(excp)

    def topic_exists(self,topic_name='kafka_topic'):

        '''
        Checks whether the topic is already present in kafka or not.

        Returns: Bool value
        '''
        #kafka_client = kafka.KafkaClient(self.KAFKA_IP_PORT)
        try:
            if topic_name in self.kafka_client.topic_partitions:
                print("topic exists")
                return True
            else:
                return False
        except Exception as e:
            print(e)
            raise

    def get_destination_kafka_producer(self,topic_name='kafka_topic',retention_hours='168'):

        '''
        Returns: KafkaProducer instance, and also make sure that the topic exists

        If topic does not exists already, it creates the one!

        '''

        try:

            if self.topic_exists(topic_name):
                pass
            else:
                # admin_client = KafkaAdminClient(bootstrap_servers=self.KAFKA_IP_PORT)
                topic_list = [NewTopic(name=topic_name, num_partitions=10, replication_factor=1,topic_configs={'retention.ms': str(retention_hours), 'max.message.bytes':str(1000012)})]
                self.admin_client.create_topics(new_topics=topic_list, validate_only=False)

            # destination_kafka_producer = KafkaProducer(bootstrap_servers=[self.KAFKA_IP_PORT], value_serializer = lambda x:json.dumps(x).encode('utf-8'))
            return self.destination_kafka_producer

        except Exception as e:
            print(e)
            raise
        
    def enter_to_destination_databases_for_kafka(self,data, destination_kafka_producer,topic_name='kafka_topic'):

        '''
            Function used to send data to a particular kafka topic.

            Parameters:

            data: data(python list) that needs to be send
            topic_name: name of kafka topic to which the topic needs to be send
            destination_kafka_producer: instance of kafka producer

        '''

        try:
            if destination_kafka_producer is not None:
                # print(successes)

                print('sending to kafka')
                for one_data in data:

                    self.destination_kafka_producer.send(topic_name, value=one_data).add_callback(self.on_send_success).add_errback(self.on_send_error,one_data)

                    #print('sent..')
                    destination_kafka_producer.flush()

        except Exception as e:
            print(e)
            raise

    def send_to_multi(self,data,item_get_key=None,prefix='k_', suffix='_k'):

        """
        Function used to send data to multiple kafka topics.

        Arguements:

        data: list of items that needs to be send, (required)
        item_get_key: key name of items about which grouping needs to be done.(required)
        prefix: string that needs to be added before key in kafka topic name. (default: k_)
        suffix: string that needs to be added after key in kafka topic name. (default: _k)
        
        """
        
        if (not data) or (len(data)==0):
            print("There is no data to be added")
            # raise 
        else:
        
            #send data to multiple topics in kafka
            if not item_get_key:
                    
                print("there is no key for the same")
                # raise
                    
            else:

                #do keyitem getter
                try:
                    data = [json.loads(data_pt) for data_pt in data]
                except Exception as e:
                    print(e)

                sorted_data = sorted(data, key=itemgetter(item_get_key))
                    
                for key, value in itertools.groupby(sorted_data, key=itemgetter(item_get_key)):
                        
                    name = prefix + key + suffix
                    print("Topic name in Kafka: ",name)

                    self.enter_to_destination_databases_for_kafka(list(value),self.get_destination_kafka_producer(name,retention_hours=retention_hours),topic_name=name)
                
                print("Data sent to kafka successfully!")
                        
    def send_to_one(self,data,topic_name='kafka_topic',retention_hours='168'):

        """

        Function that sends the data to single kafka topic.

        Arguments:
        Data: (required) [Accepts list of items to be send to kafka topic]
        topic_name: Name of the kafka topic to which data needs to be send. Default value: kafka_topic
        retention_hours: number of hours to be set for kafka topic to be alive. Default value: "168"(string)
        """

        if (not data) or len(data)==0:
            print("Pass the required list of items that needs to be send")

        try:
            data = [json.loads(data_pt) for data_pt in data]
        except Exception as e:
            print(e)
            

        if not isinstance(topic_name,str):
            #topic name is not of type str
            try:
                #convert topic name to str
                topic_name = str(topic_name)
                self.enter_to_destination_databases_for_kafka(list(data),self.get_destination_kafka_producer(topic_name,retention_hours=retention_hours),topic_name=topic_name)
            except Exception as e:
                print(e)
                pass
        else:
             self.enter_to_destination_databases_for_kafka(list(data),self.get_destination_kafka_producer(topic_name,retention_hours=retention_hours),topic_name=topic_name)
             print("Data sent to kafka successfully!")
            