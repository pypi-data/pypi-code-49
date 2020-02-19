import subprocess
import time
import os
import signal

device_id = 0

p = subprocess.Popen(
        [
            'nvidia-smi', '--loop=5'
        ], preexec_fn=os.setsid)
for i in range(5):
    time.sleep(2)
    result = subprocess.check_output(
        [
            'nvidia-smi', '--id=' + str(device_id), '--query-gpu=memory.used,memory.total,utilization.gpu',
            '--format=csv,nounits,noheader'
        ], encoding='utf-8')
    print('iter {}'.format(i))
    print(result)

os.killpg(os.getpgid(p.pid), signal.SIGTERM)