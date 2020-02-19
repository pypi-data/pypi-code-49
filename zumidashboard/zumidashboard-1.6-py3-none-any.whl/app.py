from flask import Flask
from flask_socketio import SocketIO
from flask import send_from_directory
from zumi.zumi import Zumi
from zumi.util.screen import Screen
from zumi.protocol import Note
import zumidashboard.scripts as scripts
import zumidashboard.sounds as sound
import zumidashboard.updater as updater
from zumidashboard.drive_mode import DriveMode
import time, subprocess, os, re, base64
from threading import Thread
import logging
from logging.handlers import RotatingFileHandler


if not os.path.isdir('/home/pi/Dashboard/debug'):
    os.mkdir('/home/pi/Dashboard/debug')

app = Flask(__name__, static_url_path="", static_folder='dashboard')
app.zumi = Zumi()
app.screen = Screen(clear=False)
app.ssid = ''
app.action = ''
app.action_payload = ''
app.new_blockly_project = ''
socketio = SocketIO(app)
usr_dir = '/home/pi/Dashboard/user/'
handler = RotatingFileHandler('/home/pi/Dashboard/debug/dashboard.log', maxBytes=10000, backupCount=1)
app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(handler)
lib_dir = os.path.dirname(os.path.abspath(__file__))
app.drive_mode = DriveMode(app.zumi)

# dashboard
vendor_static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dashboard/blockly/src/app/vendor")
blockly_static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dashboard/blockly/src/app/blockly-lib")
ui_library =  os.path.join(os.path.dirname(os.path.abspath(__file__)), "dashboard/blockly/src/app/ble-lib")
blockly_fonts =  os.path.join(os.path.dirname(os.path.abspath(__file__)), "dashboard/blockly/src/app/fonts")
blockly_images =  os.path.join(os.path.dirname(os.path.abspath(__file__)), "dashboard/blockly/src/app/images")
blockly_media =  os.path.join(os.path.dirname(os.path.abspath(__file__)), "dashboard/blockly/src/app/media")
blockly_msg =  os.path.join(os.path.dirname(os.path.abspath(__file__)), "dashboard/blockly/src/app/msg")


def _awake():
    app.screen.hello()
    sound.wake_up_sound(app.zumi)


def log(msge):
    app.logger.info(time.strftime('{%Y-%m-%d %H:%M:%S} ')+msge)


@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


# blockly ----------------------------------------------------------------------------------------------------
@app.route('/blockly')
def blockly():
    return app.send_static_file('./blockly/src/app/index.html')


@app.route('/vendor/<path:filename>')
def send_js(filename):
    return send_from_directory(vendor_static_dir, filename)


@app.route('/blockly-lib/<path:filename>')
def send_blocklydir(filename):
    return send_from_directory(blockly_static_dir, filename)


@app.route('/ble-lib/<path:filename>')
def send_ui_dir(filename):
    return send_from_directory(ui_library, filename)


@app.route('/fonts/<path:filename>')
def send_font_dir(filename):
    return send_from_directory(blockly_fonts, filename)


@app.route('/images/<path:filename>')
def send_images_dir(filename):
    return send_from_directory(blockly_images, filename)

@app.route('/media/<path:filename>')
def send_media_dir(filename):
    return send_from_directory(blockly_media, filename)

@app.route('/msg/<path:filename>')
def send_msg_dir(filename):
    return send_from_directory(blockly_msg, filename)


@socketio.on('zumi_run')
def print_message(source_code_base64):
    print('zumi run')
    message_deco = base64.b64decode(source_code_base64)
    print(message_deco)
    new_path = './blockly.py'
    new_days = open(new_path,'w+')

    new_days.write(str(message_deco, 'utf-8'))
    new_days.close()

    p1 = Thread(target = exec_thread, args = ('message_deco2',))
    p1.start()

    # await a successful emit of our reversed message
    # back to the client
    socketio.emit('robolink_run', '')


@socketio.on('check_output')
def check_output():
    print('output function')
    outputPath = './output.txt'
    try: 
        outputFile = open(outputPath, 'r')
        content = outputFile.read()
        print(content)
        socketio.emit('hello', content)
    except:
        print('output file not found')


def exec_thread(message_deco):
    print(message_deco)
    try:
        exec("""\n@socketio.on('zumi_run_thread')\nasync def print_message(sid, source_code_base64):\n    global zumiprocess\nlog = open("output.txt", "w")\np = subprocess.Popen(["sudo", "python3", "blockly.py"],stdin=subprocess.PIPE, stdout=log, stderr=log, close_fds=True)\n\n""")
    except Exception as err:
        print("error: ", err)


@socketio.on('stop')
def stop():
    stdoutdata = subprocess.getoutput("sudo kill $(pgrep -f blockly.py)")
    from zumi.zumi import Zumi
    zumi = Zumi()
    print("in emergency function")
    socketio.emit('disconnected', {'msg': 'Connection failed!', 'status': 'false'})    


# network connect -------------------------------------------------------------------------------------------
@app.route('/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')


@app.route('/select-network')
def select_network():
    return app.send_static_file('index.html')


@app.route('/success')
def success():
    return app.send_static_file('index.html')


@socketio.on('ssid_list')
def ssid_list(sid):
    print('getting ssid list')
    app.action = 'ssid_list'
    log('getting ssid list')

    _list = scripts.get_ssid_list()
    socketio.emit('ssid_list',str(_list))


@socketio.on('disconnect')
def test_disconnect():
    print('Socket disconnected')
    log('client disconnected')


@socketio.on('connect')
def test_connect():
    print('a client is connected')
    log('a client is connected')
    log(app.action)
    if app.action == 'check_internet' or app.action == 'check_last_network':
        time.sleep(1)
        socketio.emit(app.action, app.action_payload)
        app.action = ''
        app.action_payload = ''


# confirm check internet msge was receive
@socketio.on('acknowledge_check_internet')
def acknowledge_check_internet():
     log('msge check internet was receive')
     app.action = ''


# connect wifi functions
@socketio.on('connect_wifi')
def connect_wifi(ssid, passwd):
    print('app.py : connecting wifi start')
    log('app.py : connecting wifi start')

    print(str(type(ssid))+ssid)
    scripts.add_wifi(ssid, passwd)
    print("personality start")
    app.screen.draw_image_by_name("tryingtoconnect")
    sound.try_calibrate_sound(app.zumi)
    sound.try_calibrate_sound(app.zumi)
    print("personality done")
    log('app.py : connecting wifi:'+ssid+' end')
    print('app.py : connecting wifi end')


@socketio.on('check_internet')
def check_internet(emiter):
    if emiter == 'check_last_network':
        app.action = emiter
    else:
        app.action = 'check_internet'    
    connected, ssid = scripts.check_wifi()
    app.ssid = ssid
    if not connected:
        print('emit fail to connect')
        log('app.py : emit fail to connect - Silent Mode')
        if emiter == 'check_internet':
            app.screen.draw_text_center("Failed to connect.\n Try again.")
        socketio.emit(app.action, '')
        return
    time.sleep(5)

    app.connected_to_internet = scripts.check_internet()
    print("version check : {}".format(re.findall('[0-9]+.[0-9]+', app.connected_to_internet["dashboard_version"])[0]))
    if connected and "zumidashboard" in app.connected_to_internet['dashboard_version']:
        print('app.py: emit check internet success')
        log('app.py : emit check internet success')
        socketio.emit(app.action, app.connected_to_internet)
    elif connected:
        print('app.py : conected to local network but not internet')
        log('app.py : conected to local network but not internet')
        app.connected_to_internet = 'LOCAL_NETWORK'
        socketio.emit(app.action, 'LOCAL_NETWORK')
    else:
        print('emit fail to connect')
        log('app.py : emit fail to connect')
        if emiter == 'check_internet':
            app.screen.draw_text_center("Failed to connect.\n Try again.")
        socketio.emit(app.action, '')
    app.action_payload = app.connected_to_internet


@socketio.on('zumi_success')
def zumi_success():
    app.screen.draw_text_center("I'm connected to \"" + app.ssid + "\"")
    sound.calibrated_sound(app.zumi)
    time.sleep(2)
    # _awake()


@socketio.on('kill_supplicant')
def kill_supplicant():
    scripts.kill_supplicant()


@socketio.on('zumi_fail')
def zumi_fail():
    app.screen.draw_text_center("Failed to connect.\n Try again.")
    app.zumi.play_note(Note.A5, 100)
    app.zumi.play_note(Note.F5, 2 * 100)
    time.sleep(2)
    app.screen.draw_text_center("Go to \"zumidashboard.ai\" in your browser")


@socketio.on('open_eyes')
def open_eyes():
    print("unused state")
    # app.screen.hello()
    # sound.calibrated_sound(app.zumi)


# zumi run demo and lesson event link is in frontend already
@socketio.on('activate_offline_mode')
def activate_offline_mode():
    app.screen.draw_text_center("Starting offline mode")
    subprocess.Popen(['sudo', 'killall', 'wpa_supplicant'])
    time.sleep(3)
    _awake()


# are we use this?? ----------------------------------------------------------------------------
@socketio.on('run_demos')
def run_demos():
    print('Run demos event from dashboard')


@socketio.on('goto_lessons')
def goto_lessons():
    print('Go to lessons event from dashboard')


# updater ----------------------------------------------------------------------------------------------------
@app.route('/update')
def update():
    return app.send_static_file('index.html')


@socketio.on('update_firmware')
def update_firmware():
    print('update firmware from dashboard')
    print('server down soon')
    time.sleep(1)
    print(re.findall('[0-9]+.[0-9]+', app.connected_to_internet["dashboard_version"])[0])
    command = "sudo killall -9 python3 && sudo python3 -c 'import zumidashboard.updater as update; "
    command += "update.run(v=\"{}\")'".format(re.findall('[0-9]+.[0-9]+', app.connected_to_internet["dashboard_version"])[0])
    subprocess.run([command], shell=True)


@socketio.on('update_everything')
def update_everything():
    print('update firmware & content from dashboard')
    print('server down soon')
    time.sleep(1)
    print(re.findall('[0-9]+.[0-9]+', app.connected_to_internet["dashboard_version"])[0])
    command = "sudo killall -9 python3 && sudo python3 -c 'import zumidashboard.updater as update; "
    command += "update.run_everything(v=\"{}\")'".format(re.findall('[0-9]+.[0-9]+', app.connected_to_internet["dashboard_version"])[0])
    subprocess.run([command], shell=True)


@socketio.on('update_content')
def update_content():
    print('update content from dashboard')
    if updater.check_content_version():
        print("need update")
        updater.update_content(app.zumi, app.screen)
    else:
        print("up-to-date")
    print('emit update content')
    socketio.emit('update_content')


# for check OS/setup update
def firmware_updater_check(base):
    print("checker")
    if not os.path.isdir(base+'update'):
        os.mkdir(base+'update')
    if not os.path.isfile(base+'update/update_log.txt'):
        f = open(base+'update/update_log.txt','w')
        f.close()

    try:
        update_list = os.listdir(lib_dir + '/update_scripts/')
        for line in open(base + 'update/update_log.txt'):
            try:
                update_list.remove(line.rstrip('\n'))
            except:
                pass

    except FileNotFoundError:
        update_list = []

    if len(update_list):
        firmware_updater(update_list)
        return "updated"
    else:
        return "no update"


# for check OS/setup update
def firmware_updater(update_list):
    print(update_list)
    update_list.sort()
    print(update_list)
    f = open('/home/pi/Dashboard/update/update_log.txt', 'a')
    for version in update_list:
        print("update {}".format(version))
        p = subprocess.Popen(
            ['sudo', 'sh', lib_dir + '/update_scripts/'+version, '.'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        stdout, stderr = p.communicate()
        p.wait()
        f.write(version+"\n")


@app.route('/develop')
def develop():
    print('update develop firmware from dashboard')
    print('server down soon')
    time.sleep(1)

    command = "sudo killall -9 python3 && sudo python3 -c 'import zumidashboard.updater as update; update.run_develop()'"
    subprocess.run([command], shell=True)
    return app.send_static_file('index.html')


# main dashboard page related ---------------------------------------------------------------------------------
@app.route('/step2')
def step2():
    return app.send_static_file('index.html')


@app.route('/shutting-down')
def shutting_down():
    return app.send_static_file('index.html')


@app.route('/lesson')
def lesson():
    # update_lessonlist_file()
    return app.send_static_file('index.html')


@socketio.on('shutdown')
def shutdown():
    app.screen.draw_text_center("Please switch off after 15 seconds.")
    scripts.shutdown()


@socketio.on('battery_percent')
def battery_percent():
   socketio.emit('battery_percent',str(app.zumi.get_battery_percent()))


@socketio.on('hardware_info')
def hardware_info():
    import psutil, uuid
    from gpiozero import CPUTemperature

    cpu_info = str(int(psutil.cpu_percent()))
    ram_info = str(int(psutil.virtual_memory().percent))
    mac_address = str(':'.join(re.findall('..', '%012x' % uuid.getnode())))
    cpu_temp = CPUTemperature(min_temp=50, max_temp=90)
    cpu_temp_info = str(int(cpu_temp.temperature))
    with open('/home/pi/Dashboard/Zumi_Content/README.md', 'r') as zumiContentVersionFile:
        content_version = zumiContentVersionFile.readline().replace("\n", "")
    board_version = str(app.zumi.get_board_firmware_version())

    hardward_info = {"cpu_info": cpu_info, "ram_info": ram_info, "mac_address": mac_address,
                     "cpu_temp": cpu_temp_info, "content_version": content_version, "board_version": board_version}

    socketio.emit('hardware_info', hardward_info)
    socketio.emit('battery_percent', str(app.zumi.get_battery_percent()))


# lesson page
@socketio.on('update_lessonlist_file')
def update_lessonlist_file(usr_name):
    import json
    print("update lesson json")
    lesson_files_path = "/home/pi/Dashboard/user/{}/Zumi_Content/Lesson/".format(usr_name)
    lesson_file_list = os.listdir(lesson_files_path)
    lesson_file_list.sort()

    lesson_list = []

    lesson_id = 0
    for lesson_name in lesson_file_list:
        if lesson_name != '.ipynb_checkpoints':
            with open(lesson_files_path + lesson_name, 'r') as lesson_file:
                file_content = json.loads(lesson_file.read())
            try:
                description = file_content["cells"][1]["source"][2].split(">")[1].split("<")[0].replace("\n", " ")

                if len(description) > 175:
                    description = description[:175] + "..."
            except:
                description = " "
            lesson_info = {"id": lesson_id, "title": lesson_name[:-6], "description": description}
            lesson_list.append(lesson_info)
            lesson_id = lesson_id + 1

    lesson_list_json = {"LessonList": lesson_list}

    with open('/usr/local/lib/python3.5/dist-packages/zumidashboard/dashboard/LessonList.json', 'w') as lesson_list_file:
        json.dump(lesson_list_json, lesson_list_file)


# multiple user ----------------------------------------------------------------------------------------------------
@app.route('/login')
def login():
    return app.send_static_file('index.html')


@socketio.on('get_users')
def get_users():
    # this is not happen but put in here
    if not os.path.isdir(usr_dir):
        os.makedirs(usr_dir)
    usr_list = os.listdir(usr_dir)
    # try:
    #     usr_list.remove('guest')
    # except:
    #     generate_guest_user()
    socketio.emit('get_users', usr_list)


@socketio.on('add_user')
def add_user(usr_name):
    add_usr_dir = usr_dir + usr_name
    if os.path.isdir(add_usr_dir):
        # socketio.emit(add_user, False)
        print("user is already exist")
    else:
        os.makedirs(add_usr_dir)
        os.mkdir(add_usr_dir + '/My_Projects')
        os.mkdir(add_usr_dir + '/My_Projects/Jupyter')
        os.mkdir(add_usr_dir + '/My_Projects/Blockly')
        # for multiple user updater
        subprocess.Popen(['cp', '-r', '/home/pi/Dashboard/Zumi_Content', add_usr_dir])
        print("generate user : {}".format(usr_name))
        time.sleep(2)
        subprocess.Popen(['sudo', 'chown', '-R', 'pi', add_usr_dir])
        # socketio.emit(add_user, True)


@socketio.on('start_user')
def start_user(usr_name):
    base_dir_path = "/home/pi/Dashboard/"
    usr_dir_path = base_dir_path + 'user/' + usr_name + '/'

    subprocess.call(['sudo', 'pkill', '-9', 'jupyter'])
    time.sleep(1)
    subprocess.call(['sudo', 'bash', lib_dir + '/shell_scripts/jupyter.sh', usr_dir_path])
    _awake()

    if updater.check_user_content(base_dir_path, usr_dir_path):
        updater.copy_content(base_dir_path, usr_dir_path)
        update_lessonlist_file(usr_name)
        socketio.emit("need_update_user_content", True)
    else:
        socketio.emit("need_update_user_content", False)

    # maybe printout something on zumi or reaction


@socketio.on('change_user_name')
def change_user_name(user_names):
    previous_user_dir = usr_dir + user_names[0]
    new_user_dir = usr_dir + user_names[1]
    # if changing name is already exist
    if os.path.isdir(new_user_dir):
        # socketio.emit('change_user_name', False)
        print("changing name {} is already".format(user_names[1]))
    # if current name is not exist
    elif not os.path.isdir(previous_user_dir):
        # socketio.emit('change_user_name', False)
        print("current user {} is not exist".format(user_names[0]))
    else:
        subprocess.Popen(['mv', previous_user_dir, new_user_dir])
        # socketio.emit('change_user_name', False)
        print("change user {} to {}".format(user_names[0], user_names[1]))


@socketio.on('delete_user')
def delete_user(user_name):
    delete_usr_dir = usr_dir + user_name;
    if os.path.isdir(delete_usr_dir):
        subprocess.Popen(['rm', '-r', delete_usr_dir])
        print("user {} is deleted".format(user_name))
        # socketio.emit('delete_user', True)
    else:
        print("user {} is not exist or already deleted".format(user_name))
        # socketio.emit('delete_user', False)

# ---might use later----
# def generate_guest_user():
#     guest_usr_dir = usr_dir + 'guest'
#     os.mkdir(guest_usr_dir)
#     os.mkdir(guest_usr_dir + '/My_Projects')
#     os.mkdir(guest_usr_dir + '/My_Projects/Jupyter')
#     os.mkdir(guest_usr_dir + '/My_Projects/Blockly')
#     subprocess.Popen(['cp', '-r', '/home/pi/Dashboard/Zumi_Content', guest_usr_dir])
#     subprocess.Popen(['sudo', 'chown', '-R', 'pi', guest_usr_dir])


@socketio.on('check_jupyter_server')
def check_jupyter_server():
    p = subprocess.Popen(
        ['sudo', 'bash', lib_dir + '/shell_scripts/check_port.sh', '5555'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    stdout, stderr = p.communicate()
    p.wait()
    if len(stdout) > 1:
        print('jupyter server is not ready')
        socketio.emit('check_jupyter_server', False)
    else:
        print('jupyter server is ready')
        socketio.emit('check_jupyter_server', True)


# drive mode --------------------------------------------------------------------------------------------------------
@app.route('/drive')
def drive():
    return app.send_static_file('index.html')


@socketio.on('open_drive_mode')
def open_drive_mode():
    p = subprocess.Popen(
        ['sudo', 'sh', os.path.dirname(os.path.abspath(__file__)) + '/shell_scripts/drivemode.sh', '.'])


@socketio.on('zumi_direction')
def zumi_direction(input_key):
    app.drive_mode.zumi_direction(input_key)


@socketio.on('zumi_stop')
def zumi_stop():
    app.drive_mode.zumi_stop()


@socketio.on('camera_stop')
def drive_mode_camera_stop():
    print('camera should be stopped')
    subprocess.Popen(['fuser', '-k', '3456/tcp'])


# code mode --------------------------------------------------------------------------------------------------------
@app.route('/code-mode')
def code_mode():
    return app.send_static_file('index.html')


@socketio.on('code_mode')
def code_mode(user_name):

    blockly = os.listdir(usr_dir + '/' + user_name + '/My_Projects/Blockly')
    jupyter = [file.split(".ipynb")[0] for file in os.listdir(usr_dir + '/' + user_name + '/My_Projects/Jupyter') if
               file.endswith(".ipynb")]
    # #code for return [tag, project_name]
    # for x in len(project_list):
    #     tag = re.findall('<[a-z]+>', project_list[x])[0]
    #     project_list[x] = [tag, project_list[x].replace(tag,'')]
    socketio.emit('code_mode', {"jupyter": jupyter, "blockly": blockly})


@socketio.on('create_jupyter')
def create_jupyter(user_name, project_name):
    jupyter_folder = "{}/My_Projects/Jupyter/".format(usr_dir + user_name)
    subprocess.call(['cp', lib_dir + '/shell_scripts/Untitled.ipynb', jupyter_folder])
    time.sleep(1)
    subprocess.call(['mv', "{}Untitled.ipynb".format(jupyter_folder), "{}{}.ipynb".format(jupyter_folder, project_name)])
    time.sleep(1)
    subprocess.Popen(['sudo', 'chown', '-R', 'pi', jupyter_folder])


@socketio.on('get_blockly_project')
def get_blockly_project(user_name, selected_project):
    print('app: get xml project')
    if app.new_blockly_project:
        app.new_blockly_project = False
        socketio.emit('get_blockly_project', '')
    else:
        project_file = open("{}/My_Projects/Blockly/{}.xml".format(usr_dir + user_name, selected_project), 'r')
        socketio.emit('get_blockly_project', str(project_file.read()))


@socketio.on('save_blockly_file')
def save_blockly_file(user_name, project_name, xml_content):
    print('app: saving blockly file')
    myfile = open("{}/My_Projects/Blockly/{}.xml".format(usr_dir + user_name, project_name), 'w')
    myfile.write(xml_content)
    myfile.close() 


@socketio.on('create_blockly')
def create_blockly(user_name, project_name):
    app.new_blockly_project = True
    # need to copy from blank project xml file
    myfile = open("{}/My_Projects/Blockly/{}.xml".format(usr_dir + user_name, project_name), 'w')
    myfile.close()


@socketio.on('rename_blockly')
def rename_blockly(user_name, project_name, new_name):
    blockly_dir = "{}/My_Projects/Blockly/".format(usr_dir + user_name)
    subprocess.call(['mv', "{}.xml".format(blockly_dir+project_name), "{}.xml".format(blockly_dir+new_name)])
    time.sleep(1)

@socketio.on('rename_jupyter')
def rename_jupyter(user_name, project_name, new_name):
    jupyter_dir = "{}/My_Projects/Jupyter/".format(usr_dir + user_name)
    subprocess.call(['mv', "{}.ipynb".format(jupyter_dir+project_name), "{}.ipynb".format(jupyter_dir+new_name)])
    time.sleep(1)

@socketio.on('delete_blockly')
def delete_blockly(user_name, project_name):
    blockly_dir = "{}/My_Projects/Blockly/".format(usr_dir + user_name)
    subprocess.call(['rm',"-rf", "{}.xml".format(blockly_dir + project_name)])
    time.sleep(1)

@socketio.on('delete_jupyter')
def delete_jupyter(user_name, project_name):
    blockly_dir = "{}/My_Projects/Jupyter/".format(usr_dir + user_name)
    subprocess.call(['rm',"-rf", "{}.ipynb".format(blockly_dir + project_name)])
    time.sleep(1)

# main ----------------------------------------------------------------------------------------------------
def run(_debug=False):
    if not os.path.isfile('/usr/local/lib/python3.5/dist-packages/zumidashboard/dashboard/hostname.json'):
        subprocess.run(["sudo ln -s /etc/hostname /usr/local/lib/python3.5/dist-packages/zumidashboard/dashboard/hostname.json"], shell=True)
    firmware_updater_check('/home/pi/Dashboard/')

    socketio.run(app, debug=_debug, host='0.0.0.0', port=80)


if __name__ == '__main__':
    run()
