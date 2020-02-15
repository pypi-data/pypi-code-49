import json
import time

import paho.mqtt.client as mqtt

from . import Config, StatsCollector

def main():
    last_call = {}

    config_file = 'config.yml'
    config = Config(config_file)

    mqtt_config = config.get_mqtt()
    mq = mqtt.Client()
    mq.connect_async(mqtt_config['host'])
    mq.loop_start()
    mq.on_log = log

    collector = StatsCollector()
    while(True):
        for device in config.get_devices():
            data = collector.collect(device['device'])
            data['device'] = device['device']
            data['device_alias'] = device['device_alias']
            last_run = last_call.get(device['target_topic'])
            if last_run != None:
                data['cache_read_hits_percentage'] = _calculate_percentage(int(last_run['cache_read_hits']), 
                                                                        (int(last_run['cache_read_hits']) + int(last_run['cache_read_misses'])),
                                                                        int(last_run['cache_read_hits_percentage']),
                                                                        int(data['cache_read_hits']), 
                                                                        (int(data['cache_read_hits']) + int(data['cache_read_misses']))) 
                data['cache_write_hits_percentage'] = _calculate_percentage(int(last_run['cache_write_hits']), 
                                                                        (int(last_run['cache_write_hits']) + int(last_run['cache_write_misses'])),
                                                                            int(last_run['cache_read_hits_percentage']),
                                                                            int(data['cache_write_hits']), 
                                                                            (int(data['cache_write_hits']) + int(data['cache_write_misses'])))
                print(data)
                last_call[device['target_topic']] = data
                mq.publish(device['target_topic'], json.dumps(data))
            else:
                data['cache_write_hits_percentage'] = 0
                data['cache_read_hits_percentage'] = 0
                print('Skipping publish due to first run')
                print(data)
                last_call[device['target_topic']] = data

        time.sleep(30)

def _calculate_percentage(last_run_fraction, last_run_total, last_percentage, fraction, total):
    if last_run_fraction == fraction and last_run_total == total:
        return last_percentage
    
    if total != 0:
        return (fraction-last_run_fraction) / (total-last_run_total) * 100
    
    return 0

def log(self, client, userdata, level, buf):
    if level >= client.MQTT_LOG_INFO:
        print(buf)

if __name__ == '__main__':
    main()
