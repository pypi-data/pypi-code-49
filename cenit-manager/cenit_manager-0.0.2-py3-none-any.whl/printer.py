PRINTER_NAME = "EPSON LX-350 ESC/P"

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import os
import glob
import logging
from c import c

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

_logger = logging.getLogger("matrix printer >>> ")

app = Flask(__name__)
CORS(app)
out = {'status':'OK'}
config_file = ""
domain_name = ""

homepath = os.path.expanduser(os.getenv('USERPROFILE'))
cert_directory = "{}{}{}".format(homepath, os.path.sep, "printer_certificate")

if os.name == 'nt':
    import win32print
else:
    import cups

def get_input_and_config_parser():
    try:
        import ConfigParser
        return  raw_input, ConfigParser.RawConfigParser()
    except Exception as e:
        from configparser import ConfigParser
        return  input, ConfigParser()

def make_certificate():
    if not os.path.exists(cert_directory):
        os.makedirs(cert_directory)

    inp, configParser = get_input_and_config_parser()
    #opt = str(inp(c.BOLD + "\n\nSelect the TENANT number that use: " + c.ENDC))
    opt = str(inp("\n\nEnter a FQDN 'domain name' for this printer: "))

    _logger.info("{}: [{}]".format("You are enter the domain", opt))

    pass

def get_certificate():
    if not os.path.exists(cert_directory):
        _logger.info("Unable exists Directory: [{}]".format(cert_directory))
        return

    tmp_dict = {}
    i = 0
    for f in glob.glob("{}/*".format(cert_directory)):
        if os.path.isdir(f) and not f.endswith("backup"):
            i += 1
            tmp_dict.update({i: f.split("/")[-1]})
            _logger.info("\n{}.- {}\n".format(i, f.split("/")[-1]))

    if not tmp_dict:
        make_certificate()

    return ("winserver.local\cert.pem", "winserver.local\key.pem")
    #return ("printer.developer.net\cert.pem", "printer.developer.net\key.pem")

def _windows_mode_get():
    _logger.info("{}".format("> list all printers attached to this computer"))
    printers = win32print.EnumPrinters(3)
    printer_dict = {}
    for printer in printers:
        print(printer)
        #printer_dict.update({printer[1]: printer[2]})
        printer_data = printer[1].split(",")
        printer_dict.update({printer_data[0]: printer_data[1]})
    return printer_dict

def _windows_mode_post():
    printer_data = request.form['printer_data']
    printer_name = request.form['printer_name']
    _logger.info(printer_name)
    _logger.info(printer_data)
    p = win32print.OpenPrinter(printer_name)
    job = win32print.StartDocPrinter(p, 1, ("DOTMATRIX", None, "RAW"))
    win32print.StartPagePrinter(p)
    win32print.WritePrinter(p, printer_data.encode())
    win32print.EndPagePrinter(p)
    return jsonify(out)

def _linux_mode_get():
    pass

def _linux_mode_post():
    pass

@app.route('/dotmatrix/print.php', methods=['POST', 'GET'])
def index():
    if request.method == "GET":
        if os.name == "nt":
            return jsonify(_windows_mode_get())
        else:
            _linux_mode_get()
    else:
        if os.name == "nt":
            return _windows_mode_post()
        else:
            return _linux_mode_post()

    return jsonify(out)

def main():

    print(get_certificate())
    ssl_context = get_certificate()
    app.run(port=8080, host="0.0.0.0", ssl_context=ssl_context)
    #app.run(port=8080, host="0.0.0.0")

if __name__ == '__main__':
    main()

#cd certifier
#go build -o certifier.exe
#certifier.exe --domains winserver.local --ip-addresses 192.168.1.200
