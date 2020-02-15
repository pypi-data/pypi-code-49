class AverageCalculator:
    def __init__(self): 
        self._volumes = {}

    def calculate_average(self, volume):
        old_data = self._volumes.get(volume['device'])
        
        average = {}
        average['read_hits_percentage'] = self._calculate_average(old_data['cache_read_hits'], 
                                                                  old_data['cache_read_misses'],
                                                                  volume['cache_read_hits'], 
                                                                  volume['cache_read_misses'])

        average['write_hits_percentage'] = self._calculate_average(old_data['cache_write_hits'], 
                                                                  old_data['cache_write_misses'],
                                                                  volume['cache_write_hits'], 
                                                                  volume['cache_write_misses'])

        return average                                                                

    def _calculate_average(self, old_hits, old_misses, new_hits, new_misses):
        total_since_last = (new_hits + new_misses) - (old_hits + old_misses)

        hits_since_last = new_hits - old_hits

        return hits_since_last / total_since_last * 100


