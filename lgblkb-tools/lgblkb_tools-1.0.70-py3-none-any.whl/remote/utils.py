import functools
import sys
from invoke.exceptions import UnexpectedExit
from lgblkb_tools import logger,Folder
from fabric import Connection,Result
from invoke import Context
from lgblkb_tools.common.proxies import RecursiveProxy

RemoteFolder:Folder=functools.partial(Folder,reactive=False)

class FabricConnection(RecursiveProxy):
	def __init__(self,host,user=None,port=None,config=None,gateway=None,forward_agent=None,
	             connect_timeout=None,connect_kwargs=None,inline_ssh_env=None,):
		wrapped=Connection(host,user=user,port=port,config=config,gateway=gateway,forward_agent=forward_agent,
		                   connect_timeout=connect_timeout,connect_kwargs=connect_kwargs,inline_ssh_env=inline_ssh_env,)
		super(FabricConnection,self).__init__(wrapped=wrapped)
	
	def inherit_out(self,out):
		return RecursiveProxy(out)
	
	@logger.trace()
	def run(self,command,raw=False,**kwargs) -> Result:
		logger.debug('command: %s',command)
		try:
			out=self.__wrapped__.run(command,**kwargs)
			# if kwargs.get('hide'): logger.debug('out:\n%s',out)
			if raw: return out
			else: return out.stdout.strip()
		except UnexpectedExit as exc:
			# logger.debug('dir(exc): %s',dir(exc))
			logger.error('exc: %s',exc)
			sys.exit(-1)
	
	def cd(self,path):
		if isinstance(path,Folder): path=path.path
		return self.__wrapped__.cd(path)

class Remote(object):
	def __init__(self,connection):
		self.conn: Connection=connection
		self.folder: Folder=RemoteFolder(self.conn.run('pwd'))
	
	def create_file(self,filepath,file_contents):
		file_contents=file_contents.replace('"','""')
		self.conn.run(f'sudo bash -c "cat <<EOF > {filepath}\n{file_contents}\nEOF"')
		return self
	
	def backup(self,filepath):
		self.conn.run(f'sudo cp {filepath} {filepath}.bak')
		return self
	
	def replace_in_file(self,filepath,old,new):
		out=self.conn.run(f'cat {filepath}',raw=True).stdout
		avahi_modified=out.replace(old,new)
		self.create_file(filepath,avahi_modified)
		return self
	
	@logger.trace()
	def share_wifi_over_lan(self,first_time=False):
		netplan_folder: Folder=RemoteFolder('/etc/netplan')
		with self.conn.cd(netplan_folder):
			filenames=self.conn.run(f'ls').split('\n')
			yaml_file=[filename for filename in filenames if filename.endswith('.yaml')][0]
			logger.debug('yaml_file: %s',yaml_file)
			yaml_contents=f"""
# This file is generated from information provided by
# the datasource.  Changes to it will not persist across an instance.
# To disable cloud-init's network configuration capabilities, write a file
# /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg with the following:
# network: {{config: disabled}}
network:
    ethernets:
        eth0:
            dhcp4: true
            optional: true
    version: 2
    wifis:
        wlan0:
            optional: true
            access-points:
                NU:
                    password: 1234512345
            dhcp4: true
"""
		# self.create_file(yaml_file,yaml_contents)
		# self.conn.run('sudo netplan --debug try')
		# self.conn.run('sudo netplan --debug generate')
		# self.conn.run('sudo netplan --debug apply')
		crda_filepath='/etc/default/crda'
		# self.conn.run(f'sudo touch {crda_filepath}')
		crda_content="""
# Define your country code here as explained above or in this format if not explained:
# ISO/IEC 3166-1 alpha2 country code
REGDOMAIN=KZ
"""
		# self.create_file(crda_filepath,crda_content)
		# self.conn.run(f'cat {crda_filepath}')
		# self.conn.run(f'sudo apt-get update && sudo apt-get dist-upgrade')
		# self.conn.run(f'sudo apt-get install wireless-tools wpasupplicant openssh-server')
		# self.conn.run(f'sudo apt-get install parprouted dhcp-helper avahi-daemon')
		dhcp_relay_file='/etc/default/dhcp-helper'
		dhcp_contents="""
# relay dhcp requests as broadcast to wlan0
DHCPHELPER_OPTS="-b wlan0"
"""
		if first_time: self.backup(dhcp_relay_file)
		# self.create_file(dhcp_relay_file,dhcp_contents)
		# self.conn.run(f'cat {dhcp_relay_file}')
		avahi_conf_file=r'/etc/avahi/avahi-daemon.conf'
		if first_time: self.backup(avahi_conf_file)
		# self.replace_in_file(avahi_conf_file,'[reflector]',
		#                      """
		# 					 [reflector]
		# 					 enable-reflector=yes""")
		arp_bridge_service_file=r'/lib/systemd/system/arp-bridge.service'
		arp_bridge_service_content="""
[Unit]
Description=ARP Bridge over Wireless Interface
Wants=network-online.target
After=network-online.target

[Service]
Type=idle
RemainAfterExit=yes
ExecStart=/lib/systemd/system/set-arp-routing

[Install]
WantedBy=multi-user.target
"""
		# self.create_file(arp_bridge_service_file,arp_bridge_service_content)
		starting_script_path=r'/lib/systemd/system/set-arp-routing'
		starting_script_content="""
#!/bin/bash

## Start Process
ETHERNET_IFACE=eth0
WIRELESS_IFACE=wlan0

## Setup system forwarding
echo "Enable IP forwarding"
echo 1 > /proc/sys/net/ipv4/ip_forward
## Uncomment lines below if you don't want to use parprouted.
#echo "Enable ARP forwarding"
# Comment for all interfaces
#echo 1 > /proc/sys/net/ipv4/conf/${WIRELESS_IFACE}/proxy_arp
# Uncomment for all interfaces
#echo 1 > /proc/sys/net/ipv4/conf/all/proxy_arp

## Fix the 'eth0' interface that don't want to mount at boot on 3b+
## Uncomment this part if the 'eth0' interface is not mounted at boot
#/usr/sbin/netplan apply

## A little sleep
sleep 5

## Assign address
echo "Cloning IP from ${WIRELESS_IFACE} to ${ETHERNET_IFACE}"
/sbin/ip addr add $(/sbin/ip addr show $WIRELESS_IFACE | perl -wne 'm|^\s+inet (.*)/| && print $1')/32 dev $ETHERNET_IFACE

## Uncomment lines below in case you're encountering the same issues
#echo "Removing bad APIPA IP from ${ETHERNET_IFACE}"
#/sbin/ip addr del $(/sbin/ip addr show $ETHERNET_IFACE | perl -wne 'm|^\s+inet (169.254.*)/| && print $1')/16 dev $ETHERNET_IFACE
#echo "Removing bad APIPA route from ${ETHERNET_IFACE}"
#/sbin/ip route del 169.254.0.0/16 dev $ETHERNET_IFACE

## Make sure that the eth0 interface is up
echo "Setting up lan interface"
/sbin/ip link set $ETHERNET_IFACE up

## Setup ARP forwarding
echo "Starting paraprouted"
/usr/bin/killall -KILL parprouted 2> /dev/null
/usr/sbin/parprouted $ETHERNET_IFACE $WIRELESS_IFACE

## Reloading DHCP Relay
echo "Start / Reload DHCP Relay"
/bin/systemctl restart dhcp-helper

## A little sleep
sleep 5

## Refresh local ARP cache
/sbin/ip -s -s neigh flush all

## Disable wireless power management
## Uncomment if your wireless speed is too low
#/sbin/iwconfig $WIRELESS_IFACE power off

## Not related to network at all but useful for me,
## as my keyboard does not have an English layout.
## Uncomment if you find it useful too.
#loadkeys ch

## End Process
"""
		# self.create_file(starting_script_path,starting_script_content)
		# self.conn.run(f'sudo chmod -v u+x {starting_script_path}')
		self.conn.run("""
sudo systemctl daemon-reload
sudo systemctl enable arp-bridge.service
sudo systemctl start arp-bridge.service
systemctl status wpa_supplicant.service arp-bridge.service dhcp-helper.service
""")
		
		pass

def main():
	connection=FabricConnection('10.1.143.179',user='ubuntu')
	remote=Remote(connection)
	remote.share_wifi_over_lan()
	
	pass

if __name__=='__main__':
	main()

# msg="Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
# print(msg.format(result))
