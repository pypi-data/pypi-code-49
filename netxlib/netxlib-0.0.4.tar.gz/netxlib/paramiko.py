import time

def send_cmd(remote_connection, cmd):
    remote_connection.send(cmd)
    time.sleep(1)
    output = remote_connection.recv(65535).decode('ascii')
    return output

def send_cmd10(remote_connection, cmd):
    remote_connection.send(cmd)
    time.sleep(10)
    output = remote_connection.recv(65535).decode('ascii')
    return output

def send_cmd30(remote_connection, cmd):
    remote_connection.send(cmd)
    time.sleep(30)
    output = remote_connection.recv(65535).decode('ascii')
    return output
