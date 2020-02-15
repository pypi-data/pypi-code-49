import json
import subprocess


class StatsCollector:
    def collect(self, device):
        result = subprocess.run(["lvs", 
            "--reportformat", "json", 
            "--noheadings", 
            "-o", "cache_read_hits,cache_read_misses,cache_write_hits,cache_write_misses,cache_dirty_blocks", 
            device], 
            capture_output=True, 
            check=True)

        json_result = json.loads(result.stdout.decode('UTF-8'))

        # TODO Do some checkong on the output.
        return self._zero_when_blank(json_result['report'][0]['lv'][0])


    def _zero_when_blank(self, json):
        for item in json:
            if json.get(item) is "":
                json[item] = "0"

        return json

