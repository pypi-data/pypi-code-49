import os, time


def configWPA(id, pw, priority, path):
    wpa_struct = list()
    temp_start_index = None
    start_index = None
    end_index = None
    print('Reconfiguring wpa_suplicant.conf', end='\r')
    time.sleep(0.7)
    print('Reconfiguring wpa_suplicant.conf.', end='\r')
    time.sleep(0.7)
    print('Reconfiguring wpa_suplicant.conf..', end='\r')
    time.sleep(0.7)
    print('Reconfiguring wpa_suplicant.conf...', end='\r')
    time.sleep(0.7)
    with open(os.path.join(path, 'wpa_supplicant.conf')) as f:
        line = f.readline()
        while line:
            wpa_struct.append(line)
            if '{' in line:
                temp_start_index = len(wpa_struct) - 1

            if 'eduroam' in line:
                start_index = temp_start_index

            if start_index is not None and '}' in line:
                end_index = len(wpa_struct)

            line = f.readline()

        wpa_struct_begin = wpa_struct[:start_index]
        wpa_struct_end = wpa_struct[end_index:]

    eduroam_wpa_struct = ['network={\n',
                          '  ssid="eduroam"\n',
                          '  key_mgmt=WPA-EAP\n',
                          '  pairwise=CCMP\n',
                          '  eap=PEAP\n',
                          '  identity="' + str(id) + '"\n',
                          '  password="' + str(pw) + '"\n',
                          '  ca_cert="/etc/ssl/certs/AddTrust_External_Root.pem"\n',
                          '  phase2="auth=MSCHAPV2"\n',
                          '  priority=' + str(priority) + '\n',
                          '}\n']

    eduroam_wpa_struct_print = ['network={\n',
                          '  ssid="eduroam"\n',
                          '  key_mgmt=WPA-EAP\n',
                          '  pairwise=CCMP\n',
                          '  eap=PEAP\n',
                          '  identity="' + str(id) + '"\n',
                          '  password="****"\n',
                          '  ca_cert="/etc/ssl/certs/AddTrust_External_Root.pem"\n',
                          '  phase2="auth=MSCHAPV2"\n',
                          '  priority=' + str(priority) + '\n',
                          '}\n']

    if start_index is None:
        wpa_struct_print = wpa_struct + ['\n'] + eduroam_wpa_struct_print
        wpa_struct += ['\n'] + eduroam_wpa_struct
    else:
        wpa_struct = wpa_struct_begin + eduroam_wpa_struct + wpa_struct_end
        wpa_struct_print = wpa_struct_begin + eduroam_wpa_struct_print + wpa_struct_end

    with open(os.path.join(path, 'wpa_supplicant.conf'), 'w') as f:
        f.writelines(wpa_struct)
        print('\nReconfigured wpa_supplicant.conf:\n')
        print('\n' + '=' * 60)
        print(' ' * 20 + 'wpa_supplicant.conf' + ' ' * 25)
        print('-' * 60)
        print(''.join(wpa_struct_print))
        print('=' * 60 + '\n')
