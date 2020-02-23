from eduroam_config import wpa_supplicant_config
from eduroam_config.utils import openDB, closeDB, getConfig, getEmailList, getPW, getWifiCredentials, setConfig
from eduroam_config.eduroam_service import createService, testService
import argparse, os, time

wpa_path = '/etc/wpa_supplicant/'


def main():
    global wpa_path

    parser = argparse.ArgumentParser(description='A command line tool to configure your raspberry pi to connect to an '
                                                 'eduroam enterprise network and notify the end-user of ip changes for '
                                                 'ssh connections.\nCopy and Paste the following to be walked-through '
                                                 'the configuration process\n\n    sudo eduroam-config')
    parser.add_argument('-dt', '--delay-time', type=int, action='store',
                        help='Time delay in seconds between network connection and sending the ip-change email. It is '
                             'recommended to have at least a 30 second delay.')
    parser.add_argument('-id', '--wifi-id', type=str, action='store',
                        help='The identification (email) assocaited with your eduroam wifi credentials.')
    parser.add_argument('-pw', '--wifi-pw', action='store_true', default=False,
                        help='No argument flag. This will prompt you to reset your password safely. --update is '
                             'implicitly called with this flag.')
    parser.add_argument('-e', '--email-list', action='store_true', default=False,
                        help='No argument flag. This will prompt you to create your email list.')
    parser.add_argument('-p', '--priority', type=int, action='store',
                        help='Sets the priority of eduroam connection. Higher integers correlate to higher '
                             'priority. See here for more details. '
                             'https://www.raspberrypi.org/forums/viewtopic.php?t=42378')
    parser.add_argument('-u', '--update', action='store_true', default=False,
                        help='No argument flag. Mutes the configuration prompts and simply applies the changes specified in the call '
                             'arguments.')
    parser.add_argument('-t', '--test', action='store_true', default=False, help='Only executes a notification test for the '
                        'eduroam.service.')

    args = parser.parse_args()

    if args.wifi_pw:
        args.update = True

    if args.delay_time is not None and args.delay_time < 0:
        raise ValueError('Delay time must be a positive number')

    if args.priority is not None and args.priority < 0:
        raise ValueError('Priority must be a positive number')

    print('Setting environment...')

    if not os.path.exists('/eduroam/'):
        print('Creating directory /eduroam/...', end='\r')
        os.mkdir('/eduroam/')
        print('Creating directory /eduroam/... Done.')

    print('Opening config database...', end='\r')
    openDB(args)
    print('Opening config database... Done.\n')

    if args.email_list:
        setConfig('email_list', getEmailList())

    if args.test:
        testService()
    elif args.update:
        if args.wifi_id is not None or args.wifi_pw or args.priority is not None:
            args.wifi_pw = getPW()
            wpa_supplicant_config.configWPA(getConfig('wifi_id'), args.wifi_pw, getConfig('priority'), wpa_path)
        if args.delay_time is not None or args.email_list:
            createService(update=True)
        print('Changes to you eduroam configuration were successful. Thanks!  =(^_^)=')
    else:
        print('Beginning configuration process...')
        print('Please enter the following:')
        args = getWifiCredentials(args)
        wpa_supplicant_config.configWPA(getConfig('wifi_id'), args.wifi_pw, getConfig('priority'), wpa_path)
        time.sleep(1)
        createService(update=False)

    closeDB()


if __name__ == '__main__':
    main()
