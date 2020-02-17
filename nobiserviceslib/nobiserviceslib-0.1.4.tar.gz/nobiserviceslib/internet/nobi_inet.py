from . import HttpConection
from .Errors import SocketError, SocketErrorCases
from ..encryption import nobi_cipher
from .. import nobi_file
import socket
import time
import struct
import csv
import os


def check_ip_and_port(ip:str, port:str):
    try:
        if HttpConection.check_ip_or_hostname(ip) == "IS_HOST":
            flag, ans = HttpConection.dns_query(ip)
            ip = str(ans) if flag else None

        if ip is None:
            raise SocketError(SocketErrorCases.IP_CANT_FIND)
        else:
            port = int(port)
    except (ValueError, OSError):
        raise SocketError(SocketErrorCases.IP_PORT_ERROR)

    if len(ip.split('.')) == 4:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    else:
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

    return s, (ip, port)


class ConnectionStatus:
    __locked = False
    __socket = socket
    __login_status = False
    __connection_start_from = 0
    __aes_key = bytes(16)
    __last_command = ""
    __last_command_result = ""
    __username = ""
    __password = ""
    __attachment = ""
    __disconnected = False

    def __init__(self, s):
        self.__socket = s
        self.__connection_start_from = time.time()

    def get_information(self):
        ip, port = self.__socket.getpeername()
        name = self.__username if self.__login_status else 'Anonymous'
        return name, ip, port, self.connection_duration()

    def get_login_status(self):
        return self.__login_status

    def set_login_status(self, login_status):
        self.__login_status = login_status

    def get_aes_key(self):
        return self.__aes_key

    def set_aes_key(self, aes_key: bytes):
        assert len(aes_key) == 16, "aes key must have 16 bytes."
        self.__aes_key = aes_key

    def get_last_cmd_result(self):
        return self.__last_command_result

    def set_last_cmd_result(self, result: str):
        assert isinstance(result, str), "result must be string."
        self.__last_command_result = result

    def get_last_cmd(self):
        return self.__last_command

    def set_last_cmd(self, command: str):
        assert isinstance(command, str), "result must be string."
        self.__last_command = command

    def get_username(self):
        return self.__username

    def set_username(self, username):
        assert isinstance(username, str), "username must be string."
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        assert isinstance(password, str), "password must be string."
        self.__password = password

    def set_attachment(self, attachment: str):
        assert isinstance(attachment, str), "attachment must be string."
        self.__attachment = attachment

    def get_attachment(self):
        return self.__attachment

    def is_blocked(self):
        return self.__locked

    def block(self):
        self.__locked = True

    def release(self):
        self.__locked = False

    '''
    Return connection duration in second.
    '''
    def connection_duration(self):
        return int(time.time() - self.__connection_start_from)

    def disconnect(self):
        self.__disconnected = True
        self.__socket.shutdown(2)
        self.__socket = None
        self.__username = ""
        self.__password = ""
        self.__attachment = ""
        self.__connection_start_from = 0
        self.__login_status = False

    def check_flag(self):
        return self.__disconnected

    def send(self, msg):
        self.__socket.send(msg)

    def receive(self, buffer=4096):
        return self.__socket.recv(buffer)


class ConnectionManager:
    def __init__(self, ip: str, port: str, username: str, password: str, timeout=60):
        s, ip_port = check_ip_and_port(ip, port)
        self.__socket = None
        self.__c_s = None
        self.__socket_timeout = timeout
        self.__socket_family = s.family
        self.__socket_type = s.type
        self.__ip_port = ip_port
        self.__username = username
        self.__password = password

    def __establish_connection(self):
        try:
            self.__socket = socket.socket(self.__socket_family, self.__socket_type)
            self.__socket.settimeout(self.__socket_timeout)
            self.__socket.connect(self.__ip_port)
        except socket.timeout:
            raise SocketError(SocketErrorCases.SOCKET_CONNECTION_TIMEOUT)
        self.__c_s = ConnectionStatus(self.__socket)
        self.__c_s.set_aes_key(nobi_cipher.RSAPlusAES.generate_aes_key(16))
        self.__login(self.__username, self.__password)

    def __close_connection(self):
        self.__c_s.disconnect()
        self.__c_s = None
        self.__socket = None

    def __login(self, username, password):
        self.__c_s.set_last_cmd('log in')
        self.__c_s.set_last_cmd_result("")
        self.__c_s.set_username(username)
        self.__c_s.set_password(password)
        self.__c_s.set_last_cmd('')
        self.__c_s.set_last_cmd_result("")
        self.__c_s.block()
        try:
            aes_key = self.__c_s.get_aes_key()
            self.__c_s.send("i want to log in".encode('utf-8'))
            data = self.__c_s.receive().decode('utf-8')
            encrypted_data = nobi_cipher.RSAPlusAES.rsa_encrypt(data, self.__c_s.get_aes_key())
            if encrypted_data is None:
                raise SocketError(SocketErrorCases.LOGIN_FAILED)
            self.__c_s.send(encrypted_data)
            data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
            if data != "key exchange success":
                raise SocketError(SocketErrorCases.LOGIN_FAILED)
            self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, username))
            data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
            if data != "how about the password":
                raise SocketError(SocketErrorCases.USERNAME_ERROR)
            self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, password))
            data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
            if data != "last question":
                raise SocketError(SocketErrorCases.PASSWORD_ERROR)
            self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, "Guava Loves Nobi Forever"))
            data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
            if data != "Nobi Loves Guava too":
                raise SocketError(SocketErrorCases.LOGIN_FAILED)
            self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, "NO NEED"))
        except SocketError as e:
            self.__c_s.set_last_cmd_result('login has failed.')
            raise SocketError(e.case)
        else:
            self.__c_s.set_login_status(True)
            self.__c_s.set_last_cmd_result("login has succeeded.")
            self.__c_s.release()

    def __set_model(self, model_path):
        self.__c_s.block()
        self.__c_s.set_last_cmd('set tensorflow model')
        aes_key = self.__c_s.get_aes_key()
        self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, "set tensorflow model"))
        data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
        if data != "Enter the model path":
            self.__c_s.set_last_cmd_result('model setting has failed.')
            raise SocketError(SocketErrorCases.SET_TENSORFLOW_MODEL_ERROR)
        self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, model_path))
        data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
        if data != "Setting has completed":
            self.__c_s.set_last_cmd_result('model setting has failed.')
            raise SocketError(SocketErrorCases.SET_TENSORFLOW_MODEL_ERROR)
        self.__c_s.set_last_cmd_result("model setting has succeeded.")
        self.__c_s.release()
        return True

    def view_ppg(self, buffer: list, options=""):
        self.__establish_connection()
        if not self.__c_s.get_login_status():
            raise SocketError(SocketErrorCases.NOT_LOGIN_ERROR)
        self.__c_s.block()
        self.__c_s.set_last_cmd('view ppg database')
        aes_key = self.__c_s.get_aes_key()
        self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, "view ppg"))
        data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
        if data != "Enter the options":
            self.__c_s.set_last_cmd_result('log in has failed.')
            raise SocketError(SocketErrorCases.VIEW_PPG_ERROR)
        self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, options))
        while True:
            data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
            if data[-14:] == "FINISH SENDING":
                if len(data[0:-14]) != 0:
                    buffer.append(data)
                break
            else:
                buffer.append(data)
                self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, "next"))
        self.__c_s.set_last_cmd_result("view ppg has succeeded.")
        self.__c_s.release()
        self.__close_connection
        return True

    def download_ppg(self, fmt="[:]", out_dir='.'):
        self.__establish_connection()
        self.__c_s.block()
        self.__c_s.set_last_cmd('download ppg')
        try:
            aes_key = self.__c_s.get_aes_key()
            self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, "download ppg"))
            count = 0
            data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
            if data != "Enter the format":
                self.__c_s.set_last_cmd_result('download ppg has failed.')
                raise SocketError(SocketErrorCases.DOWNLOAD_PPG_ERROR)
            self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, fmt))

            while True:
                buffer = b''
                while len(buffer) < 4:
                    buffer += self.__c_s.receive()
                    if len(buffer) == 0:
                        raise SocketError(SocketErrorCases.DOWNLOAD_PPG_ERROR)
                total_len = struct.unpack(">I", buffer)[0]
                if total_len == 0:
                    break
                buffer = b''
                self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, "next"))
                while len(buffer) < total_len:
                    temp = self.__c_s.receive()
                    if len(temp) == 0:
                        raise SocketError(SocketErrorCases.DOWNLOAD_PPG_ERROR)
                    buffer += temp
                count += 1
                data_id = struct.unpack(">I", buffer[0:4])[0]
                with open("%s/ppg_%d.bin" % (out_dir, data_id), "wb") as f:
                    f.write(buffer)
                self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, "finish"))
        except SocketError as e:
            self.__c_s.set_last_cmd_result('download ppg has failed.')
            raise SocketError(e.case)
        else:
            self.__c_s.set_last_cmd_result("download ppg has succeeded.")
            self.__c_s.release()
            self.__close_connection()
            return True

    def spectrum_predict(self, model_path, data, predict_mode, buffer_size=4096, out_dir='.', parm: dict = None):
        predict_data = []
        predict_result = []
        if predict_mode == 0 and isinstance(data, str):
            if not os.path.isfile(data): raise SocketError(SocketErrorCases.SPECTRUM_PREDICT_DATA_TYPE_ERROR, '0: file')
            filename = data
            file_size = os.path.getsize(filename)
        elif predict_mode == 1:
            if isinstance(data, list):
                predict_data = data
            elif isinstance(data, str):
                if nobi_file.check_fmt(data) == 'csv':
                    data_list = nobi_file.read_csv(data, ignore_first_line=True)
                    predict_data = [nobi_file.strlist_to_floatlist(row) for row in data_list]
            else:
                raise SocketError(SocketErrorCases.SPECTRUM_PREDICT_DATA_TYPE_ERROR, '1: list or file')
        elif predict_mode == 107318049:
            pass
        else:
            raise SocketError(SocketErrorCases.SPECTRUM_PREDICT_DATA_TYPE_ERROR, 'Unknown type')
        self.__establish_connection()
        if predict_mode != 107318049: self.__set_model(model_path)
        self.__c_s.block()
        self.__c_s.set_last_cmd('spectrum predict')
        aes_key = self.__c_s.get_aes_key()
        self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, "spectrum predict"))
        data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
        if data != "Enter the predict mode (0: file, 1: list)":
            self.__c_s.set_last_cmd_result('log in has failed.')
            raise SocketError(SocketErrorCases.SPECTRUM_PREDICT_FAILED)
        self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, str(predict_mode)))

        if predict_mode == 0:
            data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
            if data != "Enter the file size":
                self.__c_s.set_last_cmd_result('spectrum predict has failed.')
                raise SocketError(SocketErrorCases.SPECTRUM_PREDICT_FAILED, "Data mode error.")
            with open(filename, 'rb') as f:
                data = f.read(file_size)
                file_data = nobi_cipher.pack_aes_data(aes_key, data)
            file_size = len(file_data)
            self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, struct.pack(">I", file_size)))
            data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
            if data != "Enter the file name":
                    self.__c_s.set_last_cmd_result('spectrum predict has failed.')
                    raise SocketError(SocketErrorCases.SPECTRUM_PREDICT_FAILED, "File size error.")
            self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, os.path.basename(filename)))
            data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
            if data != "Ready to receive the file":
                    self.__c_s.set_last_cmd_result('spectrum predict has failed.')
                    raise SocketError(SocketErrorCases.SPECTRUM_PREDICT_FAILED, "File name error.")
            for i in range(int(file_size / buffer_size) + 1):
                msg = file_data[i * buffer_size: (i + 1) * buffer_size]
                self.__c_s.send(msg)
            data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
            if data == "Ready to receive result?":
                self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, "Enter the file size"))
            elif data == "Finish":
                self.__c_s.set_last_cmd_result("spectrum predict has succeeded.")
                self.__c_s.release()
                self.__close_connection
                return True
            else:
                self.__c_s.set_last_cmd_result('spectrum predict has failed.')
                raise SocketError(SocketErrorCases.SPECTRUM_PREDICT_FAILED)
            data_length = struct.unpack(">I", nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()))[0]
            self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, "Enter the file name"))
            filename = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
            self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, "Ready to receive the result"))
            tmp = b''
            while len(tmp) < data_length:
                tmp += self.__c_s.receive()
            data = nobi_cipher.unpack_aes_data(aes_key, tmp)
            self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, "Finish"))
            with open('%s/%s' % (out_dir, filename), 'wb') as f:
                f.write(data)
            self.__c_s.set_last_cmd_result("spectrum predict has succeeded.")
            self.__c_s.release()
            self.__close_connection
            return "%s/%s" % (out_dir, filename)
        elif predict_mode == 1:
            data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
            if data != "Enter the data length":
                self.__c_s.set_last_cmd_result('spectrum predict has failed.')
                raise SocketError(SocketErrorCases.SPECTRUM_PREDICT_FAILED, "Data mode error.")
            msg = nobi_cipher.pack_aes_data(aes_key, struct.pack(">%df" % len(predict_data[0]), *predict_data[0]))
            self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, struct.pack(">I", len(msg))))
            for index, p in enumerate(predict_data):
                data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
                if data != "Enter the data":
                    self.__c_s.set_last_cmd_result('spectrum predict has failed.')
                    raise SocketError(SocketErrorCases.SPECTRUM_PREDICT_FAILED)
                msg = nobi_cipher.pack_aes_data(aes_key, struct.pack(">%df" % len(p), *p))
                for i in range(int(((len(msg) * 4) / buffer_size)) + 1):
                    self.__c_s.send(msg[i * buffer_size: (i + 1) * buffer_size])
                data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
                if data[:7] != "Result:":
                    self.__c_s.set_last_cmd_result('spectrum predict has failed.')
                    raise SocketError(SocketErrorCases.SPECTRUM_PREDICT_FAILED)
                predict_result.append(data[7:])
                msg = "Finish" if index == len(predict_data) - 1 else "Next"
                self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, msg))
        elif predict_mode == 107318049:
            data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
            if data != "Enter the info length":
                self.__c_s.set_last_cmd_result('spectrum predict has failed.')
                raise SocketError(SocketErrorCases.SPECTRUM_PREDICT_FAILED)
            prefix = "Guava loves Nobi FOREVER".encode('utf-8')
            if parm is not None:
                try:
                    prediction_job = str(parm['id']).encode('utf-8')
                    prediction_file = parm['input_file'].encode('utf-8')
                except Exception:
                    raise SocketError(SocketErrorCases.SPECTRUM_PREDICT_PARAMETER_ERROR)
            else:
                raise SocketError(SocketErrorCases.SPECTRUM_PREDICT_PARAMETER_ERROR)
            servo_dir = model_path.encode('utf-8')
            username = self.__c_s.get_username().encode('utf-8')
            msg = nobi_cipher.pack_aes_data(aes_key, prefix + servo_dir + prediction_job + prediction_file + username)
            info_length = struct.pack(">5I", len(servo_dir), len(prediction_job),
                                    len(prediction_file), len(username), len(msg))
            self.__c_s.send(nobi_cipher.pack_aes_data(aes_key, info_length))
            data = nobi_cipher.unpack_aes_data(aes_key, self.__c_s.receive()).decode('utf-8')
            if data != "Enter the info":
                self.__c_s.set_last_cmd_result('spectrum predict has failed.')
                raise SocketError(SocketErrorCases.SPECTRUM_PREDICT_FAILED)
            for i in range(int((len(msg) / buffer_size) + 1)):
                    self.__c_s.send(msg[i * buffer_size: (i + 1) * buffer_size])
        self.__c_s.set_last_cmd_result("spectrum predict has succeeded.")
        self.__c_s.release()
        self.__close_connection
        return predict_result 