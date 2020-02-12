import os
import docker 
import time
from .docker_util import docker_login, docker_pull_image, get_timestamp, save_stdout, save_stderr

def run_dast_scanner(params):
    client = docker_login(params['scan_info'])
    url = params['url']
    scanner = params['scanner']
    build_dir = params['build_dir']

    print('Launching scanner %s ' % params['scanner'])

    docker_image = 'owasp/zap2docker-stable:latest'
    print('Pulling latest image for %s ' % scanner)
    docker_pull_image(client, docker_image)
    scan_start = get_timestamp()
    
    if params['full_scan']:
        print('full scan started for ' + url) 
        # check context file
        if os.path.exists(build_dir + 'dast.context'):
            cs = 'zap-full-scan.py -n /zap/wrk/dast.context -t ' + url +' -J sken-dast-output.json'
        else:
            cs = 'zap-full-scan.py -t ' + url +' -J sken-dast-output.json'

        container = client.containers.run(docker_image, cs, volumes={build_dir:{'bind':'/zap/wrk','mode':'rw'}}, detach=True, tty=False, stdout=True, stderr=True) 
        container.wait()
        print(container.logs().decode('UTF-8'))

        # write stdout and stderr output
        save_stdout(scanner, container.logs(stdout=True, stderr=False).decode('UTF-8'))
        save_stderr(scanner, container.logs(stdout=False, stderr=True).decode('UTF-8'))

        scan_end = get_timestamp()
        output_file = build_dir + 'sken-dast-output.json'
    else:
        print('quick scan started for ' + url)
        cs = 'zap.sh -daemon -port 8090 -host 0.0.0.0 -config api.disablekey=true'
        
        container = client.containers.run(docker_image, command=cs, name='zap-proxy', user='root', volumes={build_dir: {'bind':'/scan','mode':'rw'}}, ports={'8090/tcp':8090}, detach=True, tty=False, stdout=False)
        # wait the daemon to start
        time.sleep(30)
        cs = 'zap-cli -p 8090 quick-scan -r ' + url
        resp = container.exec_run(cs)
        output_log = resp.output.decode('UTF-8')
        print(output_log)
        save_stdout(scanner, output_log)

        cs = 'zap-cli -p 8090 report -f xml -o /scan/sken-dast-qs-output.xml'
        resp = container.exec_run(cs)
        print(resp.output.decode('UTF-8'))
        container.stop()
        client.containers.prune()
        scan_end = get_timestamp()
        output_file = build_dir + 'sken-dast-qs-output.xml'

    return output_file, scan_start, scan_end

