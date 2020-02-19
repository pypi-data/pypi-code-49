# -*- coding: UTF-8 -*-
import sys, getopt, time
import monitor
import version

def main():
    argv = sys.argv[1:]
    configfile = ''

    try:
        opts, args = getopt.getopt(argv,"-h-c:-v",["help", "version", "config="])
    except getopt.GetoptError:
        print 'autoscaling -c <config>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "help"):
            print ('[*] autoscaling -c <config>')
            sys.exit()
        elif opt in ("-v", "--version"):
            print ('[*] autoscaling version : %s' % version.__VERSION__)
            sys.exit()
        elif opt in ("-c", "--config"):
            configfile = arg

    if configfile == '':
        print '[*] NoConfigFile: autoscaling -c <config>'
        sys.exit(2)

    while 1:
        m = monitor.Moniter(configfile)
        try:
            m.OneRound()
        except:
            m.logger.info("Error")
        time.sleep(m.moniter_interval)

    m.logger.info("Module exist")

if __name__ == "__main__":
   main()

