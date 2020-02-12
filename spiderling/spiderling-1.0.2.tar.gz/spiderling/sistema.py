import datetime
import time
import platform
import psutil
import netifaces
import os


class Sistema:
    """
    Classe que define o Sistema
    """
    def __init__(self):
        self.memoria_perc = ''
        self.memoria_usada = ''
        self.swap_perc = ''
        self.swap_usada = ''
        self.disco = ''
        self.hostname = ''
        self.ip = ''
        self.cpu = ''

    def pegar_health_sistema(self):
        self.memoria_perc, self.memoria_usada = self.pegarMemoria()
        self.swap_perc, self.swap_usada = self.pegarSwap()
        self.disco = self.pegarDiscos()
        self.hostname = platform.uname()[1]
        self.ip = self.pegarIPs()
        self.cpu = self.pegarCPU()

    def pegarSistema(self):
        """
        Função que coleta e retorna as informações do Sistema
        """
        resposta = 'Sistema: \n'
        resposta += f'OS: {platform.system()} - {platform.release()}\n'
        resposta += f'Máquina: {platform.node()} - {platform.machine()}\n'
        resposta += f'Uptime: {str(datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time()))}\n\n'
        resposta += f'{self.pegarUptime()}\n\n'

        resposta += 'Uso: \n'
        resposta += f'CPU: {str(psutil.cpu_percent())}%\n'
        resposta += f'RAM: {str(psutil.virtual_memory().percent)}% de {str(round(psutil.virtual_memory().total / (10**9), 2))} Giga \n'
        resposta += f'SWAP: {str(psutil.swap_memory().percent)}% de {str(round(psutil.swap_memory().total / (10**9), 2))} Giga \n'
        resposta += 'Discos: \n'
        resposta += f'{self.pegarDiscosTexto()} \n'

        resposta += 'Temperatura: \n'
        if ('armv7' in platform.machine()):
            res = os.popen('/opt/vc/bin/vcgencmd measure_temp').readline()
            res = res.replace("temp=", "").replace("C \n", " ºC")
            resposta += f'CPU: {res}'
        else:
            temps = psutil.sensors_temperatures()
            chaves = set(temps.keys())

            for chave in chaves:
                resposta += chave + '\n'
                if chave in temps:
                    for entrada in temps[chave]:
                        resposta += f'{entrada.label or chave}: {entrada.current}°C (pico={entrada.high}°C, crítica={entrada.critical}°C) \n'
        return resposta

    def pegarApp(self):
        """
        Função que realiza a coleta das informações do App
        """
        resposta = 'Uso Vovô bot: \n'
        pid = os.getpid()
        processo = psutil.Process(pid)
        resposta += f'PID: {str(pid)}\n'
        resposta += f'CPU: {str(processo.cpu_percent())}%\n'
        resposta += f'Memória: {str(round(processo.memory_percent(), 2))}% de {str(round(psutil.virtual_memory().total / (10**9), 2))} Giga \n'
        resposta += f'Uptime: {str(datetime.datetime.now() - datetime.datetime.fromtimestamp(processo.create_time()))} \n\n'

        return resposta

    def pegarCPUProcesso(self):
        """
        Função que coleta e retorna o percentual de processo de CPU
        """
        pid = os.getpid()
        processo = psutil.Process(pid)
        perc = round(processo.cpu_percent(), 2)
        return perc

    def pegarMemoriaProcesso(self):
        """
        Função que coleta e retorna o percentual de processo e de uso da Memoria
        """
        pid = os.getpid()
        processo = psutil.Process(pid)
        perc = round(processo.memory_percent() / (10**6), 2)
        usage = round(((psutil.virtual_memory().total / (10**6)) * processo.memory_percent()) / 100, 2)
        return perc, usage

    def pegarCPU(self):
        """
        Função que retorna o percentual de utilização do CPU
        """
        perc = round(psutil.cpu_percent(), 2)
        return perc

    def pegarMemoria(self):
        """
        Função que retorna o percentual e uso da memoria
        """
        perc = round(psutil.virtual_memory().percent, 2)
        usage = round(((psutil.virtual_memory().total / (10**6)) * psutil.virtual_memory().percent) / 100, 2)
        return perc, usage

    def pegarSwap(self):
        """
        Função que retorna o percentual e uso da memoria swap
        """
        perc = round(psutil.swap_memory().percent, 2)
        usage = round(psutil.swap_memory().used / (10**6), 2)
        return perc, usage

    def pegarIPs(self):
        """
        Função que coleta e retorna os IPs
        """
        interfaces = netifaces.interfaces()
        for i in interfaces:
            if i == 'lo':
                continue
            iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
            if iface is not None:
                return iface[0]['addr']

    def pegarDiscosTexto(self):
        """
        Função que coleta e retorna as informações do disco
        """
        resposta = ''
        # disk.device para pegar o nome mesmo /dev/sdaX
        for disk in psutil.disk_partitions(all=False):
            resposta += str(disk.mountpoint) + ': ' + str(psutil.disk_usage(disk.mountpoint).percent) + '% de ' + str(round(psutil.disk_usage(disk.mountpoint).total / (10**9), 2)) + ' Gb \n'

        return resposta

    def pegarDiscos(self):
        """
        Função que coleta e retorna as informações de disco
        """
        resposta = []
        # disk.device para pegar o nome mesmo /dev/sdaX
        for disk in psutil.disk_partitions(all=False):
            if disk.opts == 'cdrom':
                continue
            # print("Mountpoint: ", disk.mountpoint)
            resposta.append({disk.mountpoint: {"perc": psutil.disk_usage(disk.mountpoint).percent, "gb": round(psutil.disk_usage(disk.mountpoint).used / (10**9), 2)}})

        return resposta

    def pegarUptime(self):
        """
        Função que retorna o tempo da atividade
        """
        minute = 60
        hour = minute * 60
        day = hour * 24

        d = h = m = 0

        s = int(time.time()) - int(psutil.boot_time())

        d = s / day
        s -= d * day
        h = s / hour
        s -= h * hour
        m = s / minute
        s -= m * minute

        uptime = ""
        if d > 1:
            uptime = f"{d} dias, "
        elif d == 1:
            uptime = "1 dia, "

        return f'{str(uptime)} {h}{m:.2f}{s:.2f}'
