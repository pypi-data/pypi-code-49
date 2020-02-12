def push_ssh_keys(ssh_key, container):
    cmd = 'echo "{ssh_key}" | lxc exec {container} -- sh -c "cat >> ~/.ssh/authorized_keys"'
    return cmd.format(ssh_key=ssh_key, container=container)


def cmd(container, cmd):
    return "lxc exec {container} -- '{cmd}'".format(container=container, cmd=cmd)
