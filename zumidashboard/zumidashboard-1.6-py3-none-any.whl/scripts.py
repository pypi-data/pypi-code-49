import re, os
from time import sleep
import subprocess


def add_wifi(ssid, psw):
    #ssid = ssid.encode('utf-8').hex().upper()
    MyOut2 = subprocess.Popen(['sudo', 'killall', 'dhclient'])
    print('scripts.py : add_wifi start')
    print('scripts.py : copying wpa_supplicant.conf')
    MyOut = subprocess.Popen(['sudo', 'cp', '/usr/local/lib/python3.5/dist-packages/zumidashboard/wpa_supplicant.conf',
                                '/etc/wpa_supplicant/wpa_supplicant.conf'])
    MyOut.wait()
    print('scripts.py : copyed wpa_supplicant.conf')

    if len(psw) == 0:
        print('no password')
        fa = open("/etc/wpa_supplicant/wpa_supplicant.conf", "a")
        fa.write("\nnetwork={")
        fa.write("\nssid=\"" + ssid+ "\"")
        fa.write("\nkey_mgmt=NONE")
        fa.write("\nid_str=\"AP1\"")
        fa.write("\npriority=100")
        fa.write("\n}")
        fa.close()

    else:
        MyOut2 = subprocess.Popen(['wpa_passphrase', ssid, psw],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
        stdout,stderr = MyOut2.communicate()
        raw_psk = str(stdout[-67:][:-3], 'utf-8')
        wpa_psk = "\npsk="+raw_psk
        print(stderr)
        if len(stdout) == 0:
            pass

        with open("/etc/wpa_supplicant/wpa_supplicant.conf", "a") as f:
           f.write("\nnetwork={")
           f.write("\nssid=\"" + ssid + "\"")
           f.write(wpa_psk)
           f.write("\nid_str=\"AP1\"")
           f.write("\npriority=100")
           f.write("\nkey_mgmt=WPA-PSK")
           f.write("\n}")
           f.close()
    print('added wifi information to wpa_supplicant')
    sleep(3)
    print('force all rogue wpa_supplicant ...')

    print('kill all wpa_supplicant')
    MyOut2 = subprocess.Popen(['sudo', 'killall', 'wpa_supplicant'])
    MyOut2.wait()
    print('finish kill all wpa_supplicant')

    print('spa_supplicant setup')
    MyOut2 = subprocess.Popen(['sudo', 'wpa_supplicant','-B', '-iwlan0', '-c/etc/wpa_supplicant/wpa_supplicant.conf'])
    #sudo wpa_supplicant -B -iwlan0 -c/etc/wpa_supplicant/wpa_supplicant.conf

    MyOut2.wait()
    print('wpa_supplicant finished')

    print('dhclient start')
    MyOut3 = subprocess.Popen(['sudo', 'dhclient',  'wlan0'])
    sleep(6)
    print('dhclient end')
    print('getting an ip address')
    print('scripts.py : add_wifi end')


def kill_supplicant():
    myCmd = 'sudo killall -9 wpa_supplicant'
    os.system(myCmd)
    print('finish kill all wpa_supplicant')


def OSinfo(runthis):
    try:
        osstdout = subprocess.check_call(runthis.split())
    except (subprocess.CalledProcessError) as err:
        return 1
    return osstdout


def check_wifi():
    print('scripts.py : check_wifi start')
    ssid = os.popen("sudo iwconfig wlan0 | grep 'ESSID' \
                    | awk -F\\\" '{print$2}'").read().replace("\n","")
    print(ssid)

    numbers = re.findall('\\\\x[0-9a-fA-F][0-9a-fA-F]', ssid)

    # if character has unicode(UTF-8)
    if len(numbers) > 0:
        byte_string = b''
        for n in numbers:
            sp = ssid.split(n, 1)
            if sp[0] != '':
                byte_string += sp[0].encode('utf-8')
            ssid = sp[1]
            byte_string += string_to_hex(n).to_bytes(1, byteorder='big')
        byte_string += ssid.encode('utf-8')
        print(byte_string.decode())
        ssid = byte_string.decode()

    if len(ssid) <= 1:
        MyOut2 = subprocess.Popen(['sudo', 'killall', 'dhclient'])

        return False, "None"
    return True, ssid
    print('scripts.py : check_wifi end')


def check_internet():
    os.popen('sudo echo "nameserver 8.8.8.8">/etc/resolv.conf')
    output = ""
    new = ""
    cnt = 0
    while len(output) < 2 and cnt < 3:
        output = os.popen('curl -m 12 --fail https://raw.githubusercontent.com/RobolinkInc/zumi-version/master/version.txt').read()
        cnt +=1
    print(output)
    cnt = 0
    while len(new) < 2 and cnt < 3:
        new = os.popen("curl -m 12 --fail https://raw.githubusercontent.com/RobolinkInc/Zumi_Content/master/README.md").read().split()[0]
        cnt += 1
    print(new)
    try:
        current = open('/home/pi/Dashboard/Zumi_Content/README.md').readline().split()[0]
    except:
        current = None
    return {"dashboard_version": output, "update_content": (current != new)}


    #if output == 0:
    #    print('connected to internet')
    #    return True
    #else:
    #    print('internet not available')
    #    return False

def shutdown_ap():
    print('shutting down AP mode')
    subprocess.Popen(['sudo', 'ifdown', '--force', 'ap0'])


def get_ssid_list():
    MyOut = subprocess.Popen(['sudo', 'sh', os.path.dirname(os.path.abspath(__file__)) + '/shell_scripts/scan-ssid.sh', '.'],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT)
    stdout,stderr = MyOut.communicate()
    string = stdout.decode()
    numbers = re.findall('\\\\x[0-9a-fA-F][0-9a-fA-F]', string)

    # if character has unicode(UTF-8)
    if len(numbers) > 0:
        byte_string = b''
        for n in numbers:
            sp = string.split(n, 1)
            if sp[0] != '':
                byte_string += sp[0].encode('utf-8')
            string = sp[1]
            byte_string += string_to_hex(n).to_bytes(1, byteorder='big')
        byte_string += string.encode('utf-8')
        print(byte_string.decode())
        return byte_string.decode()
    else:
        print(stdout.decode())
        return stdout


def string_to_hex(str):
    if len(str) != 4:
        return str
    elif str[:2] != '\\x':
        return str
    else:
        f = char_to_hexnumber(str[2])
        s = char_to_hexnumber(str[3])
        if f is not None and s is not None:
            return f*16+s
        else:
            return str


def char_to_hexnumber(ch):
    if re.match('[0-9]',ch):
        return int(ch)
    elif re.match('[a-f]',ch):
        return ord(ch)-87
    elif re.match('[A-F]',ch):
        return ord(ch)-55
    elif True:
        return None


def ap_connected_ip():
    result = os.popen("arp -a").read()
    result = re.findall("(192.168.10.[^)]*)", result)
    return result


def shutdown():
    subprocess.call(["sudo", "shutdown", "now"])


def is_device_connected():
    if ap_connected_ip().__len__() == 0:
        return False
    return True


if __name__=='__main__':
    print(check_wifi())
