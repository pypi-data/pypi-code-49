from netxlib.paramiko import send_cmd

def show_version(remote_connection):
    cmd = "show version\n"
    return send_cmd(remote_connection, cmd)

def show_ip_route(remote_connection):
    cmd = "show ip route\n"
    return send_cmd(remote_connection, cmd)
