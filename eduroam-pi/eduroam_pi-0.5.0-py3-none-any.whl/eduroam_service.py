import os, subprocess, time
import eduroam_config.utils as module
from eduroam_config.utils import saveDB, configNotificationService, getConfig, printProgressBar


def testService():
    delay_time = getConfig('delay_time')
    input('\nNotification service is configured and enabled. We are going to test the service. If you have good internet'
          ' connection, you should expect to receive your test email in roughly ' + str(delay_time + 10) +
          ' seconds with your current connection IP.\n\nPress enter when ready to start test...')

    ans = ' '
    again = ' '
    while ans != '' and ans != 'y' and again != 'n':
        ans = ' '
        again = ' '
        print('Running test...')
        subprocess.call(['sudo', '-S', 'systemctl', 'start', 'eduroam.service'])
        time.sleep(1)
        print('Gathering eduroam service test data...')
        os.system('sudo -S systemctl status eduroam.service')
        t = 0
        while t <= delay_time + 10:
            time.sleep(0.01)
            printProgressBar(t, delay_time + 10, 'Time Before Notification:', str(round(t, 2)) + ' seconds', 0, 25)
            t = round(t + 0.01, 2)
        print()

        while ans != '' and ans != 'y' and ans != 'n':
            ans = input('Did you receive an email? (y)/n: ')

        while ans != 'y' and again != '' and again != 'y' and again != 'n':
            print('Gathering service status data...')
            time.sleep(1)
            os.system('sudo -S systemctl status eduroam.service')
            time.sleep(1)
            again = input('Do you want to try again? (y)/n: ')

    if ans == 'y' or ans == '':
        print('Congratulations! If you enter valid credentials, you successfully configured your Raspberry Pi to '
              'connect to eduroam and notify you! Thanks!  =(^_^)=')
    elif ans == 'n':
        print('Fear not! Sometimes running this command from your bin fails to test successfully.\nCopy and Paste '
              'this into your terminal to test the service again.\n\n    sudo eduroam-config --test\n\nIf it is '
              'still not working, Copy and Paste this into your terminal and wait patiently for ' + str(delay_time + 10) +
              ' seconds.\n\n    sudo systemctl start eduroam.service\n')

def constructServiceTemplate():
    bin = os.path.join('/'.join(os.path.abspath(module.__file__).split('/')[:-1]), 'bin')

    with open('/eduroam/eduroam.service.template', 'w') as f:
        temp = '[Unit]\n'\
                'Description=eduroam-config is dependent on this service\n'\
                'Wants=network-online.target\n'\
                'After=network-online.target\n'\
                '\n'\
                '[Service]\n'\
                'Type=simple\n'\
                'User=' + os.getenv('USER') + '\n'\
                'WorkingDirectory=' + bin + '\n'\
                'ExecStart=' + os.path.join(bin, 'notify') + '\n'\
                '\n'\
                '[Install]\n'\
                'WantedBy=multi-user.target'
        f.write(temp)


def createService(update=False):
    print('Creating notification service template...', end='\r')
    constructServiceTemplate()
    print('Creating notification service template... Done.')

    if os.path.exists('/etc/systemd/system/eduroam.service'):
        print('Previous service configuration found. Deleting...')
        os.system('sudo -S systemctl stop eduroam.service')
        os.system('sudo -S systemctl disable eduroam.service')
        time.sleep(1)
        os.system('sudo rm -r /etc/systemd/system/eduroam.*;')
        print('Service removed.')

    print('Creating new notification service eduroam.service:')
    print('\n' + '=' * 60)
    print(' ' * 20 + 'eduroam.service' + ' ' * 25)
    print('-' * 60)
    os.system('sudo -S SYSTEMD_EDITOR=tee systemctl edit --force --system eduroam.service < /eduroam/eduroam.service.template')
    time.sleep(1)
    print('\n' + '-' * 60)
    print()

    print('Enabling notification service:')
    time.sleep(1)  
    os.system('sudo -S systemctl enable eduroam.service')
    time.sleep(1)

    print('Reloading daemon...', end='\r')
    os.system('sudo -S systemctl daemon-reload')
    time.sleep(0.5)
    print('Reloading daemon... Done.')

    print('eduroam.service status:')
    os.system('sudo -S systemctl status eduroam.service')    
    print('\nPlease enter the following:')
    configNotificationService(update)
    saveDB()
    if not update: testService()



