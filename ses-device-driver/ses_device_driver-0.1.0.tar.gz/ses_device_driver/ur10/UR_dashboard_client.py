#!/usr/bin/python3.6

import threading
import time
import enum
import yaml
import logging
import io
import socket
from settings_file import settings_file_handler
import traceback
import re
#from gevent import monkey; monkey.patch_all()


class Robot_mode(enum.Enum):
    NO_CONTROLLER_MODE = -1
    ROBOT_RUNNING_MODE = 0
    ROBOT_FREEDRIVE_MODE = 1
    ROBOT_READY_MODE = 2
    ROBOT_INITIALIZING_MODE = 3
    ROBOT_SECURITY_STOPPED_MODE = 4
    ROBOT_EMERGENCY_STOPPED_MODE = 5
    ROBOT_FAULT_MODE = 6
    ROBOT_NO_POWER_MODE = 7
    ROBOT_NOT_CONNECTED_MODE = 8
    ROBOT_SHUTDOWN_MODE = 9

class PState(enum.Enum):
    START = -1
    INIT = 0
    WAIT_FINISH = 1
    LOAD_PROGRAM_INIT = 2
    LOAD_PROGRAM_DONE = 3
    START_PROG = 4
    WAIT_PROG = 5
    WAIT_END = 6
    END = 7
    ERROR = 8


        


class UR_dashboard_client:
    def __init__(self, ip_address, loglevel=logging.DEBUG):
        self.ip_address = ip_address  # "172.22.222.10";
        self.port = 29999
        #logging.basicConfig(level=loglevel, format='%(message)s')
        self.logger = logging.getLogger(__name__)
        self.robot_mode = Robot_mode.NO_CONTROLLER_MODE

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.settimeout(10)
        self.scenario_handler = settings_file_handler("scenarios.yml")
        self.lock = threading.Lock()

        self.execution_flag = 0
        self.connection_flag = False
        self.connect_to_robot()

    def connect_to_robot(self):
        try:
            self.client_socket.connect((self.ip_address, self.port))
            self.connection_flag = True
            self.receive_status()

        except (ConnectionRefusedError, OSError) as e:
            self.logger.critical(
                "Connection Failed Error : {} type: {}".format(e,type(e)))
            self.robot_mode = Robot_mode(-1)
            self.connection_flag = False


    def send_command(self, command):
        if self.connection_flag:
            terminated_command = command+"\n"
            self.logger.debug("SND {}".format(command))
            self.lock.acquire()
            try:
                # with self.lock:
                self.client_socket.send(terminated_command.encode('utf-8'))
            except Exception as e:
                self.robot_mode = Robot_mode(-1)
                self.logger.error(f"Sending failed, check connectivity {e} type {type(e)}")
                #traceback.print_exc()
            finally:
                self.lock.release()
                time.sleep(0.1)
        else:
            self.logger.debug("Sending Failed : Not connected")

    def receive_status(self):
        if self.connection_flag:
            time.sleep(0.1)
            self.lock.acquire()
            r_status = "None"
            r_status = r_status.encode()
            try:
                # with self.lock:
                r_status = self.client_socket.recv(1024)
            except Exception as e:
                #self.robot_mode = Robot_mode(-1)
                r_status = "ERROR"
                r_status = r_status.encode()
                self.logger.error(f"Receiving failed, check connectivity {e} type: {type(e)}")
            
            finally:
                self.lock.release()
                self.logger.debug("RCV: {}".format(r_status.decode('utf-8')))
                return r_status.decode('utf-8')
        else:
            self.logger.debug("RCVing Failed:  Not connected")
            r_status = "NOT CONNECTED"
            r_status = r_status.encode()
            return r_status.decode('utf-8')

    def start_program_statemachine(self, programname):
        state = PState(-1)
        mode = Robot_mode(-1)
        status = ""
        command = ""
        result = dict()
        while True:
            # Start state, proceed to wait for robot mode
            if state == PState.START:              
                self.logger.debug(f"state:  {state}, status: {status}")
                command = "robotmode"
                state = PState.INIT

            # Wait for robot running mode
            elif state == PState.INIT:      
                self.logger.debug(f"state:  {state}, status: {status}")
                if re.search(r'Robotmode: \d',status):
                    mode = (status.split(":")[1]).strip()
                    if mode.isdigit():
                        self.robot_mode = Robot_mode(int(mode.strip()))
                        if self.robot_mode == Robot_mode.ROBOT_RUNNING_MODE:
                            state = PState.WAIT_FINISH
                            command = "running"
                        else:
                            state = PState.ERROR
                            command = "robotmode"
                elif status == "NOT CONNECTED":
                        state = PState.ERROR
                        command = "robotmode"

            # Wait for last program to finish, check if program is loaded
            elif state == PState.WAIT_FINISH:
                self.logger.debug(f"state:  {state}, status: {status}")
                if "false" in status:
                    state = PState.LOAD_PROGRAM_INIT
                    command = "load "+programname

            elif state == PState.LOAD_PROGRAM_INIT:
                self.logger.debug(f"state:  {state}, status: {status}")
                if "Loading program: " in status:
                    state = PState.LOAD_PROGRAM_DONE
                    command = "get loaded program"

            elif state == PState.LOAD_PROGRAM_DONE:
                self.logger.debug(f"state:  {state}, status: {status}")
                if "Loaded program" in status:
                    state = PState.START_PROG
                    command = "play"
            
            elif state == PState.START_PROG:
                self.logger.debug(f"state:  {state}, status: {status}")
                if status == "Starting program":
                    state = PState.WAIT_PROG
                    command = "running"

            elif state == PState.WAIT_PROG:
                self.logger.debug(f"state:  {state}, status: {status}")
                if "false" in status:
                    pass
                elif "true" in status:
                    state = PState.WAIT_END
                    command = "running"
                   
            elif state == PState.WAIT_END:
                self.logger.debug(f"state:  {state}, status: {status}")
                if "false" in status:
                    state = PState.END

            elif state == PState.ERROR:
                self.logger.debug(f"state:  {state}, status: {status}")
                result = {"state":"ERROR", "program_name": programname,"status":status}
                break


            elif state == PState.END:
                self.logger.debug(f"state:  {state}, status: {status}")
                self.logger.info(f" Finisied executing {programname}")
                result = {"state":"END", "program_name": programname,"status":"Completed"}
                break
            else:
                self.logger.debug("Invald state")
                result = {"state":"INVALID", "program_name": programname,"status":"Invalid state"}
                break
            # Update events
            time.sleep(0.1)
            self.send_command(command)
            reply = self.receive_status()
            status = reply.split("\n")[0]
            self.logger.debug(f"Updating events, Got reply:  {reply}")
        # Finished execution
         
        self.logger.debug("state machine finished")
        return result



    def get_robot_mode(self):
        try:
            self.send_command("robotmode")
            status_mode = self.receive_status()
            if re.search(r'Robotmode: \d',status_mode):                
                mode = status_mode.split(":")[1]
                self.logger.debug(f"Robot mode is in status : {status_mode} mode : {mode}")
                self.robot_mode = Robot_mode(int(mode.strip()))
                self.logger.warn(f"got_robot_mode {self.robot_mode.name}")
            else:
                self.logger.error(f"No robot mode found received status {status_mode}")
                
        except Exception as e:
            self.logger.debug(f"get robot mode error: {e} type: {type(e)}")
        finally:
            return self.robot_mode # return previous mode in case of error


    def execute_scenario(self, scenario_name):
        self.scenario_handler = settings_file_handler("scenarios.yml")
        program_list = self.scenario_handler.get_setting("scenario", scenario_name)

        for progName in program_list:
            self.execution_flag = 0
            self.logger.info(f"Starting program {progName}")
            status = self.start_program_statemachine(progName)
            self.logger.info(f"Execution flag {self.execution_flag}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)s [%(levelname)s] : %(message)s')
    testClient = UR_dashboard_client("172.22.222.10", logging.DEBUG)

    mode = testClient.get_robot_mode()
    print(mode.name)
    # testClient.load_program("/programs/ses/test.urp")
    # testClient.load_program("/programs/ses/test1.urp")
    # testClient.load_program("/programs/ses/test.urp")
    #testClient.execute_scenario("test")
    # time.sleep(5)
    # testClient.execute_scenario("test")

    testClient.start_program_statemachine("/programs/ses/rg6/alt/rad_luft.urp")
    testClient.start_program_statemachine("/programs/ses/rg6/alt/test.urp")
    testClient.start_program_statemachine("/programs/ses/rg6/alt/test.urp")
    # testClient.is_program_running("/programs/ses/test.urp")
    # testClient.receive_status()
    # testClient.send_command("load /programs/ses/test.urp")
    # status = ''
    # progName = 'Loaded program: /programs/ses/test.urp\n'.encode('utf-8')
    # while progName != status:
    #   testClient.send_command("get loaded program")
    #   status = testClient.receive_status()
    #   time.sleep(0.1)

    # testClient.send_command("play")
    # testClient.receive_status()
    # testClient.send_command("running")
    # testClient.receive_status()
