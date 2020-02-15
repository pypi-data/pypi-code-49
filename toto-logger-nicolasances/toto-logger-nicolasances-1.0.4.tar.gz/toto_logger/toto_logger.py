import datetime

class TotoLogger: 

    def __init__(self):
        pass

    def api_in(self, cid, method, path, mid=None): 
        
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]
        
        if mid == None:
            mid = 'no-id'

        print ('[{ts}] - [{cid}] - [api-in] - [info] - [{mid}] - Received HTTP call {method} {path}'.format(ts=timestamp, cid=cid, mid=mid, method=method, path=path))

    def api_out(self, cid, microservice, method, path, mid=None):
        
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]
        
        if mid == None:
            mid = 'no-id'

        print ('[{ts}] - [{cid}] - [api-out:{ms}] - [info] - [{mid}] - Performing HTTP call {method} {path}'.format(ts=timestamp, cid=cid, ms=microservice, mid=mid, method=method, path=path))

    def event_in(self, cid, topic, mid): 
                
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]
        
        if mid == None:
            mid = 'no-id'

        print ('[{ts}] - [{cid}] - [event-in] - [info] - [{mid}] - Received event from topic {topic}'.format(ts=timestamp, cid=cid, mid=mid, topic=topic))

    def event_out(self, cid, topic, mid): 
                
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]
        
        if mid == None:
            mid = 'no-id'

        print ('[{ts}] - [{cid}] - [event-in] - [info] - [{mid}] - Sending event to topic {topic}'.format(ts=timestamp, cid=cid, mid=mid, topic=topic))

    def compute(self, cid, msg, log_level): 
                
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]
        
        print ('[{ts}] - [{cid}] - [compute] - [{level}] - {msg}'.format(ts=timestamp, cid=cid, level=log_level, msg=msg))
