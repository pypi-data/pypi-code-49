#!/usr/bin/env python
# coding=utf-8

"""
CeCILL Copyright (c) 2016-2019, Libriciel SCOP
Initiated and by Libriciel SCOP

contact@libriciel.coop

Ce logiciel est régi par la licence CeCILL soumise au droit français et
respectant les principes de diffusion des logiciels libres. Vous pouvez
utiliser, modifier et/ou redistribuer ce programme sous les conditions
de la licence CeCILL telle que diffusée par le CEA, le CNRS et l'INRIA
sur le site "http://www.cecill.info".

En contrepartie de l'accessibilité au code source et des droits de copie,
de modification et de redistribution accordés par cette licence, il n'est
offert aux utilisateurs qu'une garantie limitée.  Pour les mêmes raisons,
seule une responsabilité restreinte pèse sur l'auteur du programme,  le
titulaire des droits patrimoniaux et les concédants successifs.

A cet égard  l'attention de l'utilisateur est attirée sur les risques
associés au chargement,  à l'utilisation,  à la modification et/ou au
développement et à la reproduction du logiciel par l'utilisateur étant
donné sa spécificité de logiciel libre, qui peut le rendre complexe à
manipuler et qui le réserve donc à des développeurs et des professionnels
avertis possédant  des  connaissances  informatiques approfondies.  Les
utilisateurs sont donc invités à charger  et  tester  l'adéquation  du
logiciel à leurs besoins dans des conditions permettant d'assurer la
sécurité de leurs systèmes et ou de leurs données et, plus généralement,
à l'utiliser et l'exploiter dans les mêmes conditions de sécurité.

Le fait que vous puissiez accéder à cet en-tête signifie que vous avez
pris connaissance de la licence CeCILL, et que vous en avez accepté les
termes.
"""

import hashlib
import io
import multiprocessing
import os
import glob
import platform
import socket
import subprocess
import sys
import time

from urlparse import urlparse

# import MySQLdb
import pymysql.cursors
import requests
# from packaging import version
from pkg_resources import parse_version
from pymysql.constants import ER

from parapheur.parapheur import pprint  # Colored printer

req_version = (3, 0)
cur_version = sys.version_info
isp3 = cur_version >= req_version
# pprint.log(cur_version)

if isp3:
    # noinspection PyCompatibility,PyUnresolvedReferences
    import configparser as ConfigParser
else:
    # noinspection PyCompatibility
    import ConfigParser

__author__ = 'Stephane Vast'
__version__ = '0.9.15'

defaut_install_depot = "/opt/_install"
defaut_iparapheur_root = "/opt/iParapheur"
versionIP_minimum = "4.4.0"
mysqluser = "alf"
mysqlpwd = ""
mysqlbase = ""


def isexistsdirectory(repertoire):
    pprint.header("#", False, ' ')
    pprint.info("Répertoire", False, ' ')
    pprint.info(repertoire.ljust(35), True, ' ')
    if os.path.exists(repertoire):
        pprint.success('{:>10s}'.format("OK"), True)
        return True
    else:
        pprint.warning('{:>10s}'.format("absent"))
        return False


def isexistssubdir(repertoire, sousrep):
    pprint.header("#", False, ' ')
    pprint.info("  subdir", False, ' ')
    pprint.info(sousrep.ljust(37), True, ' ')
    if os.path.exists("{0}/{1}".format(repertoire, sousrep)):
        pprint.success('{:>10s}'.format("OK"), True)
        return True
    else:
        pprint.warning('{:>10s}'.format("absent"))
        return False


def isexistsfile(repertoire, fichier):
    pprint.header("#", False, ' ')
    pprint.info(" fichier", False, ' ')
    pprint.info(fichier.ljust(37), True, ' ')
    if os.path.exists("{0}/{1}".format(repertoire, fichier)):
        pprint.success('{:>10s}'.format("OK"), True)
        return True
    else:
        pprint.warning('{:>10s}'.format("absent"))
        return False


def isfileproperlydeleted(repertoire, fichier):
    pprint.header("#", False, ' ')
    pprint.info(" fichier", False, ' ')
    pprint.info(fichier.ljust(37), True, ' ')
    if not os.path.exists("{0}/{1}".format(repertoire, fichier)):
        pprint.success('{:>10s}'.format("absent, OK"), True)
        return True
    else:
        pprint.error('{:>10s}'.format("Present !"), True)
        return False


def isfolderfromtoday(repertoire):
    pprint.header("#", False, ' ')
    pprint.info(" date de dossier", False, ' ')
    pprint.info(repertoire.ljust(29), True, ' ')

    datetime_creation = os.stat(repertoire).st_ctime
    datetime_now = time.time()

    if (datetime_now - datetime_creation) < 86400:
        pprint.success('{:>10s}'.format("OK"), True)
        return True
    else:
        pprint.error('{:>10s}'.format("KO"))
        return False


def istextinfile(file_to_test, text):
    pprint.header("#", False, ' ')
    pprint.info(" contenu du fichier", False, ' ')
    pprint.info(os.path.basename(file_to_test).ljust(26), True, ' ')

    with open(file_to_test, 'r') as f_open:
        filedata = f_open.read()

    if text in filedata:
        pprint.success('{:>10s}'.format("OK"), True)
        return True
    else:
        pprint.error('{:>10s}'.format("KO"))
        return False


def which(program):
    import os

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


def showtheheader():
    pprint.header('{:30s}{:>30s}'.format('Tests opérés pour i-Parapheur', 'Resultat'))
    pprint.header('=' * 60)
    pprint.header("# Check list pour", False, ' ')
    pprint.log("i-Parapheur", True, ' ')
    pprint.header("       résultats:", False, ' ')
    pprint.success("OK", True, ' ')
    pprint.warning("warn", True, ' ')
    pprint.error("Fail", True)
    pprint.header("# ")


# TESTS sur PRE-REQUIS: hardware (CPU  , RAM )
'''     Hardware    : nb CPU  , RAM , taille Disque ?
        OS Linux    : nom + version / NeSaitPas
        MySQL       : version? .... / NeSaitPas , local/déporté
        NginX       : version? .... / NeSaitPas , local/déporté
        JDK serveur : version? .... / NeSaitPas
        LibreOffice : version? .... / NeSaitPas
        GhostScript : version? .... / NeSaitPas
    Pour i-Parapheur, sécurité:
        Fournisseur certificats HTTPS (web,WS): ... , ... / NeSaitPas
        Date d'expiration cert. HTTPS (web,WS): ... , ... / NeSaitPas
        Version LiberSign : .....  / NeSaitPas	'''


def check_hardware():
    pprint.header("#", False, ' ')
    pprint.log("---- Check pre-requis systeme ----", True)

    pprint.header("#", False, ' ')
    pprint.info("Nombre de CPU disponibles (minimum 4)".ljust(46), False, ' ')
    nbcpu = multiprocessing.cpu_count()
    if nbcpu >= 4:
        pprint.success('{:>10d}'.format(nbcpu), True)
    elif nbcpu >= 2:
        pprint.warning('{:>10d}'.format(nbcpu))
    else:
        pprint.error('{:>10d}'.format(nbcpu))

    pprint.header("#", False, ' ')
    pprint.info("Taille Memoire totale (minimum 5 Go)".ljust(46), False, ' ')
    mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    mem_gib = mem_bytes / (1024. ** 3)  # e.g. 3.74
    if mem_gib >= 4.5:
        pprint.success('{:>7.2f} Go'.format(mem_gib), True)
    elif mem_gib > 3.75:
        pprint.warning('{:>7.2f} Go'.format(mem_gib))
    else:
        pprint.error('{:>7.2f} Go'.format(mem_gib))

    pprint.header("#", False, ' ')
    pprint.info("Plateforme {0} : architecture {1}".format(os.uname()[0], os.uname()[4]).ljust(46), False, ' ')
    l_arch = platform.architecture()[0]
    if l_arch == "64bit":
        pprint.success('{:>10s}'.format(l_arch), True)
    else:
        pprint.error('{:>10s}'.format(l_arch), True)
        pprint.error("Erreur: Le systeme doit etre 64bit pour recevoir i-Parapheur. STOP", True)
        sys.exit()
    # pprint.log(platform.platform())
    # pprint.log(platform.release())
    # pprint.log(platform.system()) # Linux
    # pprint.log(platform.version())
    pprint.header("#", False, ' ')
    # pprint.log(platform.linux_distribution())  #('Ubuntu', '16.04', 'xenial')
    pprint.info("Distribution: {0} {1} ({2})".format(
        platform.linux_distribution()[0],
        platform.linux_distribution()[1],
        platform.linux_distribution()[2]).ljust(46), False, ' ')
    if platform.linux_distribution()[0] == 'Ubuntu':
        if platform.linux_distribution()[1] == '18.04':
            pprint.success('{:>10s}'.format("OK"), True)
        elif platform.linux_distribution()[1] == '16.04':
            pprint.success('{:>10s}'.format("OK"), True)
        elif platform.linux_distribution()[1] == '14.04':
            pprint.warning('{:>10s}'.format("obsolete"), True)
        else:
            pprint.error('{:>10s}'.format("non conforme"), True)
    elif platform.linux_distribution()[0] == 'debian':
        if platform.linux_distribution()[1].startswith('9'):
            pprint.success('{:>10s}'.format("OK"), True)
        elif platform.linux_distribution()[1].startswith('8'):
            pprint.success('{:>10s}'.format("OK"), True)
        else:
            pprint.error('{:>10s}'.format("non conforme"), True)
    elif platform.linux_distribution()[0] == 'CentOS Linux':
        if platform.linux_distribution()[1].startswith('7'):
            pprint.success('{:>10s}'.format("OK"), True)
        else:
            pprint.error('{:>10s}'.format("non conforme"), True)
    elif platform.linux_distribution()[0] == 'Red Hat Enterprise Linux Server':
        if platform.linux_distribution()[1].startswith('7'):
            pprint.success('{:>10s}'.format("OK"), True)
        else:
            pprint.error('{:>10s}'.format("non conforme"), True)
    else:  # ajouter RHEL: 'SuSE', 'mandrake'
        pprint.error('{:>10s}'.format("inconnu"), True)

    pprint.header("#", False, ' ')
    pprint.info("swappiness (valeur <=10)".ljust(46), False, ' ')
    PROCFS_PATH = "/proc/sys/vm/swappiness"
    if os.path.isfile(PROCFS_PATH) and os.access(PROCFS_PATH, os.R_OK):
        myfile = open(PROCFS_PATH, 'r')
        for line in myfile:
            swappiness = int(line.rstrip("\n"))
            if swappiness > 10:
                pprint.error('{:>10d}'.format(swappiness), True)
            else:
                pprint.success('{:>10d}'.format(swappiness), True)
        myfile.close()


#  pprint.log(os.getlogin())
#  pprint.log(os.uname())


def check_server_socket(address, port):
    # Create a TCP socket
    s = socket.socket()
    # print "Attempting to connect to %s on port %s" % (address, port)
    try:
        s.connect((address, port))
        # print "Connected to %s on port %s" % (address, port)
        s.close()
        return True
    except socket.error as e:
        print("Connection to %s on port %s failed: %s" % (address, port, e))
        return False


def issitereachable(theurl):
    pprint.header("#", False, ' ')
    pprint.info(" {0}".format(theurl).ljust(46), False, ' ')

    try:
        # The timeout parameter is set to 5 seconds
        response = requests.get(theurl, verify=False, timeout=5)

        if not response.ok:
            pprint.error('{:>10s}'.format("Erreur"), True)
            pprint.error("Erreur lors de la requête {0}: Code d'erreur {1}".
                         format(theurl, response.status_code),
                         True)
            pprint.error(response.getvalue())
        else:
            pprint.success('{:>10s}'.format("OK"), True)

    except requests.exceptions.Timeout as toe:
        pprint.error('{:>10s}'.format("Erreur"), True)
        pprint.error("Erreur lors de la requête {0}: Time-out".
                     format(theurl))
    except requests.exceptions.ConnectionError as cee:
        pprint.error('{:>10s}'.format("Erreur"), True)
        pprint.error("Erreur de connexion à {0}: {1}".
                     format(theurl, cee))


# besoin HTTP/HTTPS sortant, accès http://crl.adullact.org validca.libriciel.fr
# http://libersign.libriciel.fr
def check_network_needed():
    pprint.header("#", False, ' ')
    pprint.log("---- Check pre-requis accès internet ----", True)
    issitereachable("http://crl.adullact.org")
    issitereachable("http://validca.libriciel.fr")
    issitereachable("https://validca.libriciel.fr")
    issitereachable("https://libersign.libriciel.fr/extension.xpi")


def check_mandatory_command(thecommand):
    pprint.header("#", False, ' ')
    pprint.info("Commande : {0}".format(thecommand).ljust(46), False, ' ')
    if which(thecommand):
        pprint.success('{:>10s}'.format("OK"))
    else:
        pprint.error('{:>10s}'.format("Absent"), True)


def check_required_software():
    pprint.header("#", False, ' ')
    pprint.log("---- Check pre-requis logiciels selon manuel ----", True)

    if isexistsdirectory(defaut_install_depot):
        isexistssubdir(defaut_install_depot, "confs")
    if not isexistsdirectory(defaut_iparapheur_root):
        pprint.error("Erreur: Le répertoire {0} doit être présent. STOP".
                     format(defaut_iparapheur_root), True)
        sys.exit()

    da_commands = ['at', 'tar', 'crontab', 'unzip', 'mailx', 'openssl',
                   'mysql', 'mysqldump', 'mysqlcheck']
    for to_test in da_commands:
        check_mandatory_command(to_test)
    badGuess = barelyGuess_iParapheur_version_from_AMP(defaut_iparapheur_root)
    if badGuess != 'inconnu':
        if parse_version("4.5.2") <= parse_version(badGuess):
            da_commands45 = ['/opt/jdk1.8.0_161/bin/java']
            for to_test in da_commands45:
                check_mandatory_command(to_test)
        if parse_version("4.6.0") <= parse_version(badGuess):
            da_commands46 = ['redis-server']
            for to_test in da_commands46:
                check_mandatory_command(to_test)
        check_java_version("1.8")
    else:
        pprint.error("WARN : could not recognize AMP as official.", True)


def check_java_version(minversion):
    if which('java'):
        import re
        version = subprocess.check_output(['java', '-version'],
                                          stderr=subprocess.STDOUT)
        # print version  # e.g: java version "1.8.0_201" etc...
        pattern = '\"(\d+\.\d+).*\"'
        result = re.search(pattern, version).groups()[0]  # e.g: 1.8

        pprint.header("#", False, ' ')
        pprint.info("Version detectee JAVA:     {0}".format(result).ljust(46),
                    False, ' ')
        if parse_version("1.8") <= parse_version(result):
            # ok
            pprint.success('{:>10s}'.format(">= 1.8, OK"), True)
        else:
            pprint.error('{:>10s}'.format("< 1.8.0"), True)
    else:
        pprint.header("#", False, ' ')
        pprint.warning(" BIEN Vérifier la bonne présence de JAVA JDK8")


def check_smtp_needed(smtp_srv):
    pprint.header("#", False, ' ')
    pprint.log("---- Check SMTP ----", True)
    if check_server_socket(smtp_srv, 25):
        pprint.header("#", False, ' ')
        pprint.info("un service SMTP est présent sur {0}"
                    .format(smtp_srv).ljust(46), False, ' ')
        pprint.success('{:>10s}'.format("ok"), True)

        pprint.warning('{:>10s}'.format("TODO"), True)
        # TODO : check si mail send is possible?

    else:
        pprint.warning("  ko")


def check_https_service_config(varconfig):
    pprint.header("#", False, ' ')
    pprint.log("---- Check configuration service HTTPS basique ----", True)

    if not isexistsdirectory("/etc/nginx"):
        pprint.header("#   ", False, ' ')
        pprint.warning("Pas de configuration NginX, "
                       "c'est pourtant le serveur HTTPS à utiliser", True)
        return False
    checkforcerts = False
    if isexistsdirectory("/etc/nginx/conf.d"):
        if isexistsfile("/etc/nginx/conf.d", "parapheur_ssl.conf"):
            checkforcerts = True
    if isexistsdirectory("/etc/nginx/ssl"):
        isexistsfile("/etc/nginx/ssl", "recup_crl_nginx.sh")
        if isexistssubdir("/etc/nginx/ssl", "validca"):
            isfolderfromtoday("/etc/nginx/ssl/validca")

    # Vérifier process Nginx pas trop vieux (p/r lancement crontab) ?
    line = subprocess.check_output('nginx -v', stderr=subprocess.STDOUT,
                                   shell=True).decode("utf-8")
    outr = line.rstrip("\n").rstrip(" ").split("nginx/")[1].split(" ", 1)[0]
    pprint.header("#", False, ' ')
    pprint.info("Version detectee NginX:     {0}".format(outr.rstrip()).
                ljust(46), False, ' ')
    # if version.parse("1.8.0") < version.parse(outr.rstrip()):
    if parse_version("1.8.0") < parse_version(outr.rstrip()):
        pprint.success('{:>10s}'.format(">1.8.0, OK"), True)
    else:
        pprint.error('{:>10s}'.format("< 1.8.0"), True)

    nginxserver = "localhost"
    nginxport = 443
    pprint.header("#", False, ' ')
    pprint.info("Service NginX sur {0}:{1}".format(nginxserver, nginxport).
                ljust(46), False, ' ')
    if not check_server_socket(nginxserver, nginxport):
        pprint.warning('{:>10s}'.format("inactif"), True)
    else:
        pprint.success('{:>10s}'.format("actif"), True)

    nginxserver = varconfig.get("Parapheur", "parapheur.hostname")
    pprint.header("#", False, ' ')
    pprint.info("Service NginX sur {0}:{1}".format(nginxserver, nginxport).
                ljust(46), False, ' ')
    if not check_server_socket(nginxserver, nginxport):
        pprint.warning('{:>10s}'.format("inactif"), True)
    else:
        pprint.success('{:>10s}'.format("actif"), True)
    istextinfile("/var/www/parapheur/alfresco/iparapheur.wsdl", nginxserver)

    if checkforcerts:
        pprint.warning('{0:>10s}'.format("TODO"), True, ' ')
        print(" check sur certificat HTTPS: valide, etc.")

# # OpenSSL: récupérer la chaîne de certificats SSL d’un host
# # https://blog.hbis.fr/2017/02/11/openssl-certificate_chain/
# echo | openssl s_client -connect iparapheurfl.demonstrations.libriciel.fr:443 -showcerts 2>&1 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > mycert.pem


def check_mysql_service_config(varconf):
    pprint.header("#", False, ' ')
    pprint.log("---- Check configuration service MySQL ----  TODO", True)

    # Extract mysqlserver from db.url schema:
    # defaults to: db.url=jdbc:mysql://localhost/alfresco
    # so cut out the 'jdbc:' stream and parse the resulting URL afterwards
    mysqldburl = varconf.get("Parapheur", "db.url")
    urlparsed = urlparse(mysqldburl[5:])
    # pprint.info(urlparsed)
    mysqlserver = urlparsed.hostname  # "localhost"
    mysqlport = 3306

    pprint.header("#", False, ' ')
    pprint.info("Service MySQL sur {0}:{1}".format(mysqlserver, mysqlport).
                ljust(46), False, ' ')
    if not check_server_socket(mysqlserver, mysqlport):
        pprint.warning('{:>10s}'.format("inactif"), True)
        return False
    else:
        pprint.success('{:>10s}'.format("actif"), True)

        mysqluser = varconf.get("Parapheur", "db.username")
        mysqlpwd = varconf.get("Parapheur", "db.password")
        mysqlbase = varconf.get("Parapheur", "db.name")
        pprint.header("#", False, ' ')
        pprint.info("DB '{3}' sur {0}@{1}:{2}".
                    format(mysqluser, mysqlserver, mysqlport, mysqlbase).
                    ljust(46), False, ' ')

        try:
            cur_max_cnx = ""
            parametre_mysql = ""

            cnx = pymysql.connect(user=mysqluser, password=mysqlpwd,
                                  host=mysqlserver, database=mysqlbase)
            pprint.success('{:>10s}'.format("OK"), True)

            cursor = cnx.cursor()
            query = "SELECT @@GLOBAL.max_connections as res;"
            cursor.execute(query)
            for res in cursor:
                cur_max_cnx = res[0]
            pprint.header("#", False, ' ')
            pprint.info('Nombre de connexions maxi      = {:>6d}'.format(cur_max_cnx).ljust(46), False, ' ')
            if cur_max_cnx < 360:
                pprint.error('{:>10s}'.format("< 360"), True)
            else:
                pprint.success('{:>10s}'.format(">=360, OK"), True)

            query = "SELECT @@GLOBAL.innodb_file_per_table as res;"
            cursor.execute(query)
            for res in cursor:
                parametre_mysql = res[0]
            pprint.header("#", False, ' ')
            pprint.info('innodb_file_per_table          = {0:>6d}'.format(parametre_mysql).ljust(46), False, ' ')
            if parametre_mysql != 1:
                pprint.error('{0:>10s}'.format("!= 1"), True)
            else:
                pprint.success('{0:>10s}'.format("=1, OK"), True)

            query = "SELECT @@GLOBAL.open_files_limit as res;"
            cursor.execute(query)
            for res in cursor:
                parametre_mysql = res[0]
            pprint.header("#", False, ' ')
            pprint.info('open_files_limit               = {0:>6d}'.format(parametre_mysql).ljust(46), False, ' ')
            if parametre_mysql < 8192:
                pprint.error('{0:>10s}'.format("< 8192"), True)
            else:
                pprint.success('{0:>10s}'.format(" OK"), True)

            query = "SELECT @@GLOBAL.wait_timeout as res;"
            cursor.execute(query)
            for res in cursor:
                parametre_mysql = res[0]
            pprint.header("#", False, ' ')
            pprint.info('wait_timeout                   = {0:>6d}'.format(parametre_mysql).ljust(46), False, ' ')
            if parametre_mysql < 28800:
                pprint.error('{0:>10s}'.format("< 28800"), True)
            else:
                pprint.success('{0:>10s}'.format("  OK"), True)

            query = "SELECT @@GLOBAL.innodb_locks_unsafe_for_binlog as res;"
            cursor.execute(query)
            for res in cursor:
                parametre_mysql = res[0]
            pprint.header("#", False, ' ')
            pprint.info('innodb_locks_unsafe_for_binlog = {0:>6d}'.format(parametre_mysql).ljust(46), False, ' ')
            if parametre_mysql != 1:
                pprint.error('{0:>10s}'.format("!= 1"), True)
            else:
                pprint.success('{0:>10s}'.format("=1, OK"), True)

            # Latest queries : test for DB integrity
            # -- Find children of nodes with no parents
            query = "SELECT COUNT(*) FROM alf_child_assoc " \
                    "WHERE parent_node_id IN " \
                    "( SELECT id FROM alf_node WHERE node_deleted =0 AND " \
                    "id NOT IN ( SELECT root_node_id FROM alf_store ) AND " \
                    "id NOT IN ( SELECT child_node_id FROM alf_child_assoc ) "\
                    ");"
            cursor.execute(query)
            for res in cursor:
                parametre_mysql = res[0]
            pprint.header("#", False, ' ')
            pprint.info('Recherche noeuds orphelins 1/2 = {0:>6d}'
                        .format(parametre_mysql).ljust(46), False, ' ')
            if parametre_mysql != 0:
                pprint.error('{0:>10s}'.format("REINDEXER"), True)
            else:
                pprint.success('{0:>10s}'.format("=0, OK"), True)
            # -- find nodes with no parent
            query = "SELECT COUNT(*) FROM alf_node " \
                    "WHERE node_deleted =0 AND " \
                    "id NOT IN ( SELECT root_node_id FROM alf_store ) AND " \
                    "id NOT IN ( SELECT child_node_id FROM alf_child_assoc );"
            cursor.execute(query)
            for res in cursor:
                parametre_mysql = res[0]
            pprint.header("#", False, ' ')
            pprint.info('Recherche noeuds orphelins 2/2 = {0:>6d}'
                        .format(parametre_mysql).ljust(46), False, ' ')
            if parametre_mysql != 0:
                pprint.error('{0:>10s}'.format("REINDEXER"), True)
            else:
                pprint.success('{0:>10s}'.format("=0, OK"), True)

            # Performance: how long for 1000 queries? must be inferior to 2ms
            import timeit
            loops = 1000
            setup = "import MySQLdb \n" \
            "db = MySQLdb.connect(host='" + str(mysqlserver) + \
            "', user='" + mysqluser + \
            "', passwd='" + mysqlpwd + \
            "', db='" + mysqlbase + "') \n" \
            "c = db.cursor()"
            stmt = 'c.execute("SELECT 1")'
            t = timeit.Timer(stmt, setup)
            total_time = t.timeit(number=loops)
            pprint.header("#", False, ' ')
            pprint.info('Temps pour 1000 requêtes  = {:>f}'.format(total_time).ljust(46), False, '  ')
            if total_time > 2:
                pprint.error('{0:>10s}'.format(">2s, KO"), True)
            else:
                pprint.success('{0:>10s}'.format("<2s, OK"), True)

            cursor.close()

        except pymysql.InternalError as ie:
            icode, imessage = ie.args
            pprint.error('internal error')
            print ">>>>>>>>>>>>>>>>", icode, imessage
        except pymysql.Error as err:
            pprint.error('{0:>10s}'.format("Erreur"), True)
            if err.errno == ER.ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == ER.BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.close()
        pprint.warning('{0:>10s}'.format("TODO"), True)


def check_isexists_alfrescoglobal():
    pprint.header("#", False, ' ')
    pprint.log("---- Exists alfresco-global.properties  ? ----  ", True)

    # Alfresco-global.properties
    isexistsdirectory(defaut_iparapheur_root)
    isexistssubdir(defaut_iparapheur_root, "tomcat/shared/classes")
    return isexistsfile("{0}/tomcat/shared/classes"
                        .format(defaut_iparapheur_root),
                        "alfresco-global.properties")


def analyse_is_param_in_conf(keyarray, paramconfarray, prefix):
    for param_key in keyarray:
        try:
            param_value = paramconfarray.get("Parapheur", param_key)
            pprint.header("#", False, ' ')
            pprint.info("{2} {0} = {1}".format(param_key, param_value, prefix))
        except ConfigParser.NoOptionError as e:
            pprint.header("#", False, ' ')
            pprint.error("{1}  OMG, need this: {0}".format(param_key, prefix))


def check_config_alfrescoglobal(varconf, ihmvarconf, version_presente):
    pprint.header("#", False, ' ')
    pprint.log("---- Check alfresco-global.properties ----  TODO", True)

    alf_dir_root = varconf.get("Parapheur", "dir.root")
    db_url = varconf.get("Parapheur", "db.url")
    # pprint.info(varconf.options("Parapheur"))
    # pprint.info(varconf.items("Parapheur"))

    pprint.header("#", False, ' ')
    pprint.info("alf_dir_root = {0}".format(alf_dir_root))
    pprint.header("#", False, ' ')
    pprint.info("database URL = {0}".format(db_url))

    needed_alfresco_global = ['dir.root',
                              'db.url',
                              'index.recovery.mode']
    for param_key in needed_alfresco_global:
        try:
            param_value = varconf.get("Parapheur", param_key)
            pprint.header("#", False, ' ')
            pprint.info("  {0} = {1}".format(param_key, param_value))
        except ConfigParser.NoOptionError as e:
            pprint.header("#", False, ' ')
            pprint.error("  OMG, need this: {0}".format(param_key))
    if parse_version("4.3.2") <= parse_version(version_presente):
        alfresco_4_3_2 = ['parapheur.ihm.creerdossier.maindocuments.max',
                          'parapheur.libersign.tag.signature.name',
                          'parapheur.libersign.tag.signature.name.tenants']
        for param_key in alfresco_4_3_2:
            try:
                param_value = varconf.get("Parapheur", param_key)
                pprint.header("#", False, ' ')
                pprint.info("  {0} = {1}".format(param_key, param_value))
            except ConfigParser.NoOptionError as e:
                pprint.error("  OMG, need this: {0}".format(param_key))
        iparapheur_4_3_2 = ['parapheur.ihm.creerdossier.maindocuments.max']
        analyse_is_param_in_conf(iparapheur_4_3_2, ihmvarconf, "I")

    if parse_version("4.4.0") <= parse_version(version_presente):
        needed_alfresco_global_params_4_4_0 = [
            'openOffice.test.cronExpression',
            'parapheur.exploit.xemelios.command']
        needed_iparapheur_global_params_4_4_0 = [
            'parapheur.ihm.password.strength',
            'parapheur.ihm.aide.libersign.url',
            'parapheur.extension.libersign.firefox.url',
            'parapheur.extension.libersign.chrome.url',
            'parapheur.extension.libersign.native.url']
        for param_key in needed_alfresco_global_params_4_4_0:
            try:
                param_value = varconf.get("Parapheur", param_key)
                pprint.header("#", False, ' ')
                pprint.info("  {0} = {1}".format(param_key, param_value))
            except ConfigParser.NoOptionError as e:
                pprint.error("  OMG, need this: {0}".format(param_key))
        analyse_is_param_in_conf(needed_iparapheur_global_params_4_4_0,
                                 ihmvarconf, "I")

    if parse_version("4.4.1") <= parse_version(version_presente):
        needed_alfresco_global_params_4_4_1 = [
            'parapheur.document.lockedPDF.accept',
            'parapheur.hostname']
        needed_iparapheur_global_params_4_4_1 = [
            'parapheur.ihm.admin.users.connected.threshold']
        for param_key in needed_alfresco_global_params_4_4_1:
            try:
                param_value = varconf.get("Parapheur", param_key)
                pprint.header("#", False, ' ')
                pprint.info("  {0} = {1}".format(param_key, param_value))
            except ConfigParser.NoOptionError as e:
                pprint.error("  OMG, need this: {0}".format(param_key))
        analyse_is_param_in_conf(needed_iparapheur_global_params_4_4_1,
                                 ihmvarconf, "I")

    if parse_version("4.5.0") <= parse_version(version_presente):
        needed_alfresco_global_params_4_5 = [
            'parapheur.cachetserver.security.key',
            'parapheur.libersign.tag.cachet.name',
            'parapheur.libersign.tag.cachet.name.tenants',
            'parapheur.notification.retards.cron',
            'parapheur.cachetserver.warnexpiration.cronexpression',
            'parapheur.cachetserver.warnexpiration.daysuntilexpiration']
        needed_iparapheur_global_params_4_5 = ['parapheur.ihm.archives.show']
        for param_key in needed_alfresco_global_params_4_5:
            try:
                param_value = varconf.get("Parapheur", param_key)
                pprint.header("#", False, ' ')
                pprint.info("  {0} = {1}".format(param_key, param_value))
            except ConfigParser.NoOptionError as e:
                pprint.error("  OMG, need this: {0}".format(param_key))
        analyse_is_param_in_conf(needed_iparapheur_global_params_4_5,
                                 ihmvarconf, "I")

    # has_db_url = False
    # if not has_db_url:
    #    pprint.header("#    ", False, ' ')
    #    pprint.warning("     Il manque '{1}' dans le {0}".format(alf_dir_root, "ulimit -Sn 16384"))


def check_config_ghostscript():
    pprint.header("#", False, ' ')
    pprint.log("---- Check config GhostScript ----", True)
    libgs_path = defaut_iparapheur_root + "/common/lib/libgs.so"
    if not isexistsfile("{0}/common/lib".format(defaut_iparapheur_root), "libgs.so"):
        return
    libgsstat = os.stat(libgs_path)
    pprint.header("#", False, ' ')
    pprint.info("Taille libgs.so = {0} octets".format(libgsstat.st_size).ljust(46), False, ' ')
    if libgsstat.st_size < 19 * 1024 * 1024:
        pprint.error('{0:>10s}'.format("< 19Mo"), True)
    else:
        pprint.success('{0:>10s}'.format("> 19Mo, OK"), True)
    command_line = "ldconfig -n /opt/iParapheur/common/lib/ -v | grep libgs.so"
    output = subprocess.check_output(command_line, shell=True)
    outl, outr = output.split("-> ")
    pprint.header("#", False, ' ')
    # pprint.info("Version detectee: {0}".format(outr.rstrip()), False, ' ')
    pprint.info("Version detectee: {0}".format(outr.rstrip()).ljust(46), False, ' ')
    if parse_version("libgs.so.9.19") < parse_version(outr.rstrip()):
        pprint.success('{:>10s}'.format("> 9.19, OK"), True)
    else:
        pprint.error('{:>10s}'.format("< 9.20"), True)


def check_files_needed():
    pprint.header("#", False, ' ')
    pprint.log("---- Check présence fichiers post-config ----", True)
    da_files = ['backup_parapheur.sh', 'custom-wsdl.sh',
                'deployWarIparapheur.sh', 'iparaph-updateAMP.sh',
                'logrotate-iparapheur.conf', 'nettoieEntrepot.sh',
                'nettoieLogs.sh', 'purge-xemwebview.sh', 'srgb.profile',
                'verdanai.ttf', 'warn_needPurge.sh']
    for to_test in da_files:
        isexistsfile("/opt/iParapheur", to_test)


def check_tomcat_libs_cleanup():
    pprint.header("#", False, ' ')
    pprint.log("---- Check nettoyage common/libs ----", True)
    da_files = ['libz.so']
    for to_test in da_files:
        isfileproperlydeleted(defaut_iparapheur_root+"/common/lib", to_test)


# chapitre  XEMELIOS
def check_xemwebview_service_config():
    pprint.header("#", False, ' ')
    pprint.log("---- Check configuration service Xemwebviewer ----  TODO", True)
    isexistsfile("/etc/init.d", "xemwebview")
    if not isexistsdirectory("/var/tmp/bl-xemwebviewer"):
        pprint.header("#   ", False, ' ')
        pprint.warning("Le service Xemelios ne fonctionnera pas: "
                       "manquent les répertoires temporaires.")
    else:
        da_reps = ['xwv-cache', 'xwv-extract', 'xwv-shared']
        for to_test in da_reps:
            if not isexistssubdir("/var/tmp/bl-xemwebviewer", to_test):
                pprint.header("#   ", False, ' ')
                pprint.warning("Le service Xemelios ne fonctionnera pas: manque le répertoire {0}.".format(to_test))


# chapitre  Pastell Connector
def check_pastellconnector_service_config():
    pprint.header("#", False, ' ')
    pprint.log("---- Check configuration service Pastell-Connector ----", True)
    isexistsfile("/etc/systemd/system/", "pastell-connector.service")
    if not isexistsdirectory("/opt/pastell-connector"):
        pprint.header("#   ", False, ' ')
        pprint.warning("Le service Pastell-Connector ne semble pas être en place.")
    else:
        import pwd
        try:
            pwd.getpwnam('pastell-connector')
            pprint.success('{:>10s}'.format("OK"), True)
        except KeyError:
            pprint.header("#   ", False, ' ')
            pprint.warning('Le service Pastell-Connector est mal installé, '
                           'l\'utilisateur "pastell-connector" n\'existe pas.')


def check_alfresco_sh(basedir, filename):
    IP_ALFRESCO_SH = "{0}/{1}".format(basedir, filename)
    if not isexistsfile(basedir, filename):
        pprint.header("#   ", False, ' ')
        pprint.warning("Mais où diable se cache '{0}' ?".format(filename))
        return -1
    # TODO: detect 'ulimit' statements, 'cd $INSTALLDIR' statement
    hasInstallDir = False
    hasUlimit1 = False
    hasUlimit2 = False
    with open(IP_ALFRESCO_SH, 'r') as f:
        for line in f:
            if 'cd $INSTALLDIR' in line:
                hasInstallDir = True
            if 'ulimit -Hn' in line:
                hasUlimit1 = True
            if 'ulimit -Sn' in line:
                hasUlimit2 = True
    if not hasInstallDir:
        pprint.header("#    ", False, ' ')
        pprint.warning("     Il manque '{1}' dans le {0}".format(filename, "cd $INSTALLDIR"))
    if not hasUlimit1:
        pprint.header("#    ", False, ' ')
        pprint.warning("     Il manque '{1}' dans le {0}".format(filename, "ulimit -Hn 16384"))
    if not hasUlimit2:
        pprint.header("#    ", False, ' ')
        pprint.warning("     Il manque '{1}' dans le {0}".format(filename, "ulimit -Sn 16384"))


def barelyGuess_iParapheur_version_from_AMP(basedir):
    hashVersionDict = dict([
        ('fcfaea0654fb04547bf9ae3d3dac993bf0128b1653da794720621a6ee1b6e2eb', '4.4.0'),
        ('f154b03e4b7f460a6c010476e4f7a3e9ae0c7537b7da588ab1789c4eb119d022', '4.4.1'),
        ('5f83fe48ff110bae2262aef085255a582e06c85025f7bcfbbe3991cec318f75b', '4.4.2'),
        ('a9cf1bdaa16a7a32452d6a7e16a420ef0e01d4ee56492a4e8842cad6c94b5e2e', '4.4.2'),
        ('cf347fc3a6226c30b8c684c8e7ebcef857d8bb1d45628f7b98a0d30b44bf72ff', '4.5.0'),
        ('9848b8ceda248e77a6bdc2eaab244cd482f4232126dbb99cf2a1f12df31fa8ea', '4.5.1'),
        # ('f5f34f098894ee7865ce9dc9b0d7aa46a633a9ae30f3782ab6bd671948ebea8f', '4.5.2'),
        ('f5f34f098894ee7865ce9dc9b0d7aa46a633a9ae30f3782ab6bd671948ebea8f', '4.5.3'),
        ('2a3f529706af89e1ed1ce9cb4ecf722b3537e8487de90518a91b68d44793d713', '4.6.0'),
        ('ff25b2080959a09d4e066c9f7fd208a1abf57a1eb60d6a322963c7d0b230e685', '4.6.1'),
        ('8c1b803042cd0f180bdcbca550878e513a380a636e38c2e9b4216ff0358536ae', '4.6.2'),
        ('397580a00697ee8b3926d6a458caeba05f5838e4f591971e6befce57301db852', '4.6.3'),
        ('129bde0c2b32566582f632673862a4a7e666dfcbfa5534b4f0c3903c26a035d4', '4.6.4'),
        ('0f453910fedef480c3ee4a2652bb9de3eef08aa2a165c9b5b9294f713a97497a', '4.6.5'),
        ('not-known-hash--------------------------------------------------', '4.6.6'),
        ('56a7f952d0c6925be159843b7c6665e87446a3edb290b17a7b740d86ba2c54d6', '4.6.7'),
        ('d48d3a0cabf978751b61891d4b63346a7bd91c827ba6ff71ef16995a2cf87498', '4.6.8')
        ])
    IP_AMP_PATH = glob.glob("{0}/{1}".format(
        basedir, "amps/iparapheur-amp-*.amp"))[0]
    if os.path.exists(IP_AMP_PATH):
        ampHash = sha256_checksum(IP_AMP_PATH)
        return hashVersionDict.get(ampHash, 'inconnu')
    else:
        return 'inconnu'


def barelyGuess_iParapheur_version_from_WAR(ipWarHash):
    hashVersionDict = dict([
        ('ce248f4f3a7d56e15e5b030432bab8b226c019b21c1067a7b7ea29f0142d2476', '4.4.0'),
        ('a8efc9f586530f2fcce01afe65ee3030c4722424585557f77a4f0138d205627c', '4.4.1'),
        ('a5435b34b255d51a8f121da90dc8399d7ee5df1ee098601f64f25e063d11b40f', '4.4.2'),  # official
        ('be105b1f7ea85d7240ab401560a4a69d1e2abd4d93ac7cc9ccc50bbde058f378', '4.4.2'),
        ('not-known-hash--------------------------------------------------', '4.5.0'),
        ('not-known-hash--------------------------------------------------', '4.5.1'),
        ('3ac125b9ba0c82003f8e2410ede004c7062c1f3c32964567e9a5c2510e7ed210', '4.5.2'),
        ('08b4ad4bad639018e20057a7763205251996280d8ff23aa7c0b431ffef1c593e', '4.5.3'),
        ('not-known-hash--------------------------------------------------', '4.6.0'),
        ('not-known-hash--------------------------------------------------', '4.6.1'),
        ('not-known-hash--------------------------------------------------', '4.6.2'),
        ('not-known-hash--------------------------------------------------', '4.6.3'),
        ('not-known-hash--------------------------------------------------', '4.6.4'),
        ('747fa8ec7f2eb076033d26cde0072ec05ae0798eb2e929e465e095b8cb934610', '4.6.5'),
        ('not-known-hash--------------------------------------------------', '4.6.6'),
        ('not-known-hash--------------------------------------------------', '4.6.7'),
        ('8d5360a9bb34aba7b61797f6ea5f813c43e6ec7a22df53ff13ef88a1c7a84737', '4.6.8')
        ])
    return hashVersionDict.get(ipWarHash, 'inconnu')


# chapitre anti-fraude
def guess_iParapheur_version(basedir):
    pprint.header("#", False, ' ')
    IP_MODULE_PATH = "{0}/{1}".format(
        basedir,
        "tomcat/webapps/iparapheur/META-INF/maven/org.adullact.iparapheur/"
        "iparapheur-surf-webapp/pom.properties")
    if not os.path.exists(IP_MODULE_PATH):
        pprint.error("Impossible de deviner la version de i-Parapheur")
        return -1
    with open(IP_MODULE_PATH, 'r') as f:
        module_string = '[Parapheur]\n' + f.read()
    module_fp = io.BytesIO(module_string)
    leMdodule = ConfigParser.RawConfigParser()
    leMdodule.readfp(module_fp)
    versionIP = leMdodule.get("Parapheur", "version")
    pprint.info("Version detectee sur le serveur:", False, ' ')
    if "SNAPSHOT" in versionIP:
        pprint.warning('{:>13s}'.format("Problème de détection"), True)
    elif parse_version(versionIP_minimum) <= parse_version(versionIP):
        pprint.success('{:>10s}'.format(versionIP), False, ' ')
        pprint.success('{:>13s}'.format(" >{0}, OK".format(versionIP_minimum)), True)
    else:
        pprint.success('{:>10s}'.format(versionIP), False, ' ')
        pprint.error('{:>13s}'.format("non supportée"), True)
    return versionIP


def sha256_checksum(filename, block_size=65536):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
    return sha256.hexdigest()


def hash_the_binfile(basedir, subdir, binfile):
    da_fullfile = "{0}/{1}/{2}".format(basedir, subdir, binfile)
    if os.path.exists(da_fullfile):
        # pprint.info("   {0}  trouvé".format(binfile))
        return sha256_checksum(da_fullfile)
    else:
        pprint.header("#   ", False, ' ')
        pprint.warning(" '{0}' introuvable, normal???".format(binfile))
        return -1


def check_iParapheur_version_is_valid(basedir):
    pprint.header("#", False, ' ')
    pprint.log("---- Check i-Parapheur version ----  TODO", True)
    # NB: Le hash(alfresco.war) est inutile, puisque contextuel à l'instance.
    # Celui du fichier AMP est "presque" plus pertinent...
    versionFromAMP = barelyGuess_iParapheur_version_from_AMP(basedir)
    da_hash = hash_the_binfile(basedir, "tomcat/webapps", "iparapheur.war")
    # pprint.info("Hash WAR: {0}".format(da_hash), False)
    versionFromWAR = barelyGuess_iParapheur_version_from_WAR(da_hash)
    pprint.header("#", False, ' ')
    pprint.info("Version detectee sur AMP: {0}".format(versionFromAMP), False)
    pprint.header("#", False, ' ')
    pprint.info("Version detectee sur WAR: {0}".format(versionFromWAR), False)
    da_version = guess_iParapheur_version(basedir)
    if da_version == -1:
        return -1
    return da_version


def check_crontab_jobs():
    pprint.header("#", False, ' ')
    pprint.log("---- Check CRONTAB entries ----  TODO", True)
    pprint.warning('{0:>10s}'.format("TODO"), True)


################################################################
################################################################
showtheheader()
check_hardware()
check_network_needed()
check_required_software()
check_smtp_needed("localhost")

if not check_isexists_alfrescoglobal():
    pprint.error("BAD")
    sys.exit()

ALF_CONFIG_PATH = "{0}/tomcat/shared/classes/alfresco-global.properties".format(defaut_iparapheur_root)
IHM_CONFIG_PATH = "{0}/tomcat/shared/classes/iparapheur-global.properties".format(defaut_iparapheur_root)
'''
def get_config_app(varfichier):
 ### lire https://stackoverflow.com/questions/2819696/parsing-properties-file-in-python/25493615#25493615
 ####   https://stackoverflow.com/questions/2885190/using-pythons-configparser-to-read-a-file-without-section-name
 with open(varfichier, 'r') as f:
     config_string = '[Parapheur]\n' + f.read()
 # config_fp = StringIO.StringIO(config_string)
 config_fp = io.BytesIO(config_string)
 config = ConfigParser.RawConfigParser()
 return config.readfp(config_fp)
'''
with open(ALF_CONFIG_PATH, 'r') as f:
    config_string = '[Parapheur]\n' + f.read()
config_fp = io.BytesIO(config_string)
config = ConfigParser.RawConfigParser()
config.readfp(config_fp)
# alfrescoconfig = get_config_app(CONFIG_PATH)
# print(config.items("Parapheur"))
# print(config.get("Parapheur", "dir.root"))
with open(IHM_CONFIG_PATH, 'r') as f:
    ihmconfig_string = '[Parapheur]\n' + f.read()
ihmconfig_fp = io.BytesIO(ihmconfig_string)
ihmconfig = ConfigParser.RawConfigParser()
ihmconfig.readfp(ihmconfig_fp)

check_https_service_config(config)

# check health of MySQL configuration
check_mysql_service_config(config)

# tests nettoyage libs obsoletes dans common/lib
check_tomcat_libs_cleanup()

# check "libgs" bien comme il faut
check_config_ghostscript()

# tests présence verdanai.ttf , srgb.profile ,etc.
check_files_needed()

# ulimit ET la commande "cd" dans alfresco.sh
check_alfresco_sh(defaut_iparapheur_root, "alfresco.sh")

# ctl.sh : limite à 30 mini pour shutdown

# Controles anti-fraude
version_ip = check_iParapheur_version_is_valid(defaut_iparapheur_root)

check_xemwebview_service_config()

# Le connecteur PA a été introduit en v4.6
if parse_version("4.6.0") <= parse_version(version_ip):
    check_pastellconnector_service_config()

# ne manque-t-il pas quelques paramètres?
check_config_alfrescoglobal(config, ihmconfig, version_ip)

# check CRONTAB
check_crontab_jobs()

pprint.info(".end.")
