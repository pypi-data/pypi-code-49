from getpass import getpass
import os, shelve

db = None
db_path = '/eduroam/'

def openDB(args):
    global db
    global db_path

    db = shelve.open(os.path.join(db_path, 'config'), writeback=True)
    if len(db.keys()) == 0 and (args.update or args.test):
        raise EnvironmentError("Cannot update the configuration because the configuration was never initialized. "
                               "Please rerun eduroam-config without --update.")

    if  len(db.keys()) == 0: os.system('sudo chmod 777 ' + os.path.join(db_path, 'config.db'))

    db['wifi_id'] = db['wifi_id'] if 'wifi_id' in db and args.wifi_id is None else args.wifi_id
    db['email_list'] = db['email_list'] if 'email_list' in db and not args.email_list else []
    db['priority'] = db['priority'] if 'priority' in db and args.priority is None else args.priority if args.priority is not None else 0
    db['delay_time'] = db['delay_time'] if 'delay_time' in db and args.delay_time is None else args.delay_time if args.delay_time is not None else 30

    db.close()
    db = shelve.open(os.path.join(db_path, 'config'), writeback=True)


def closeDB():
    global db
    db.close()


def saveDB():
    global db
    global db_path
    db.close()
    db = shelve.open(os.path.join(db_path, 'config'), writeback=True)


def getConfig(key):
    global db
    return db[str(key)]


def setConfig(key, value):
    global db
    db[str(key)] = value


def getID():
    id = input('Eduroam ID [' + str(getConfig('wifi_id')) + ']: ')
    while id == '' and getConfig('wifi_id') is None:
        print('Eduroam ID cannot be blank. Try your school email.')
        id = input('Eduroam ID [' + str(getConfig('wifi_id')) + ']: ')

    return id


def getPW():
    pw1 = ''
    pw2 = ''
    while pw1 != pw2 or pw1 == '' and pw2 == '':
        pw1 = getpass('Eduroam Password: ')
        pw2 = getpass('Confirm Eduroam Password: ')
        if pw1 != pw2: print('Passwords do not match. Please try again.')
        elif pw1 == '' or pw2 == '': print('Password cannot be blank. Please try again.')

    return pw1


def getPriority():
    invalid = True
    while invalid:
        try:
            priority = input('Eduroam Connection Priority [' + str(getConfig('priority')) + ']: ')
            if priority == '':
                invalid = False
            else:
                priority = int(priority)
                if priority < 0: raise ValueError('Value cannot be negative.')
                invalid = False
        except Exception:
            print('The priority level was invalid. Please enter a positive integer.')

    return priority


def getEmailList():
    ans = ' '
    while ans != 'y' and ans != '':
        ans = ' '
        emails = input('List of Emails to Be Notified (separated by commas) [' + str(getConfig('email_list')) + ']: ')
        while emails == '' and getConfig('email_list') is None:
            print('List of Emails cannot be blank. You need to be notified via email if your Pi\'s IP changes.')
            emails = input('List of Emails to Be Notified (separated by commas) [' + str(getConfig('email_list')) + ']: ')
        if emails == '': break

        try:
            emails = (''.join(emails.split(' '))).split(',')
            print('Your email list is the following:\n', emails)
            while ans != '' and ans != 'y' and ans != 'n':
                ans = input('Are you satisfied with this list? (y)/n: ')
        except Exception:
            print('There is an error with your email list input. Please try again... "email1@mail.com,email2@mail.com')

    return emails


def getTimeDelay():
    invalid = True
    while invalid:
        try:
            time_delay = input('Notification Delay in Seconds [' + str(getConfig('delay_time')) + ']: ')
            if time_delay == '':
                invalid = False
            else:
                time_delay = int(time_delay)
                if time_delay < 0: raise ValueError('Value cannot be negative.')
                invalid = False
        except Exception:
            print('The delay time was invalid. Please enter a positive integer.')

    return time_delay


def getWifiCredentials(args):
    id = getID()
    pw = getPW()
    priority = getPriority()

    if id != '': setConfig('wifi_id', id)
    if priority != '': setConfig('priority', priority)
    args.wifi_pw = pw
    print()

    return args


def configNotificationService(update=False):
    emails = getEmailList() if not update else getConfig('email_list')
    time_delay = getTimeDelay() if not update else getConfig('delay_time')

    if emails != "": setConfig('email_list', emails)
    if time_delay != "": setConfig('delay_time', time_delay)


# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()
