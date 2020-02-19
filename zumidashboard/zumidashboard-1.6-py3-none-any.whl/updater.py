from zumi.zumi import Zumi
from zumi.util.screen import Screen
from zumi.protocol import Note
import os, subprocess, time, signal
from threading import Thread
from PIL import Image, ImageDraw
import numpy as np


def __progress(screen, img, start, end):
    while start != end:
        draw = ImageDraw.Draw(img)
        draw.point([(start + 13, 35), (start + 13, 36), (start + 13, 37)])
        screen.draw_image(img.convert('1'))
        start += 1


def __finished_updating(_internal_zumi, _screen, text):
    _zumi = _internal_zumi
    img = _screen.path_to_image('/usr/local/lib/python3.5/dist-packages/zumi/util/images/happy1.ppm')
    time.sleep(.5)
    _screen.draw_text(text, x=10, y=5, image=img.convert('1'), font_size=12, clear=False)

    tempo = 60
    time.sleep(0.5)
    _zumi.play_note(41, tempo)
    _zumi.play_note(43, tempo)
    _zumi.play_note(45, tempo)


def __kill_updater(proc, timeout):
    print("timeout!")
    os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
    timeout["value"] = True


def update_version(_zumi, _screen, v=None):
    if v is None:
        _screen.draw_text_center("didn't get the version number try again")
        return
    p = subprocess.Popen('sudo pip3 install zumidashboard=={}'.format(v),
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

    img_arr = np.asarray(Image.open('/usr/local/lib/python3.5/dist-packages/zumi/util/images/blankbar.ppm'))
    img = Image.fromarray(img_arr.astype('uint8'))

    _screen.draw_text("Updating Dashboard", x=9, y=8, image=img.convert('1'), font_size=12, clear=False)
    img = _screen.screen_image.convert('RGB')

    updater_thread = Thread(target=__progress, args=(_screen,img, 0, 51))
    updater_thread.start()

    try:
        while p.poll() is None:
            line = p.stdout.readline().decode()
            print(line)

            if 'Error' in line:
                updater_thread.join()
                _screen.draw_text_center("Error!\nPlease Try Again")
                time.sleep(2)
                return

            if 'Collecting' in line:
                updater_thread.join()
                updater_thread = Thread(target=__progress, args=(_screen, img, 51, 88))
                updater_thread.start()

            elif 'Installing collected packages' in line:
                updater_thread.join()
                updater_thread = Thread(target=__progress, args=(_screen, img, 88, 96))
                updater_thread.start()

            elif 'Successfully installed' in line:
                updater_thread.join()
                updater_thread = Thread(target=__progress, args=(_screen, img, 96, 101))
                updater_thread.start()
                version_info = line.split('-')[-1]

        print(version_info)
        updater_thread.join()

        time.sleep(1)
        __finished_updating(_zumi, _screen, "Dashboard updated!")
        _screen.draw_text_center("Dashboard updated to v" + str(version_info), font_size=15)

    except Exception as e:
        updater_thread.join()
        _screen.draw_text_center("Zumi already up-to-date")
        print(e)


def update_content(_zumi, _screen):
    path = '/home/pi/Dashboard/'
    log_folder = _change_to_log_folder()

    img_arr = np.asarray(Image.open('/usr/local/lib/python3.5/dist-packages/zumi/util/images/blankbar.ppm'))
    img = Image.fromarray(img_arr.astype('uint8'))
    _screen.draw_text("Updating Content", x=12, y=8, image=img.convert('1'), font_size=12, clear=False)
    img = _screen.screen_image.convert('RGB')
    p = subprocess.Popen(
        'git clone https://github.com/RobolinkInc/Zumi_Content ' + path + 'Zumi_Content',
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, preexec_fn=os.setsid)
    print("start clone")

    time.sleep(1)
    try:
        content_updater_thread = Thread(target=__progress, args=(_screen, img, 0, 101))
        while p.poll() is None:
            line = p.stdout.readline().decode()
            print(line)

            if 'Cloning into ' in line:
                content_updater_thread.start()

            elif 'fatal: ' in line:
                content_updater_thread.join()
                _roll_back_folder(_screen, _zumi, log_folder, path)
                return False

            elif 'Already up-to-date' in line:
                _screen.draw_text_center('Zumi content is already latest')
                break
        content_updater_thread.join()
    except:
        content_updater_thread.join()
        print("error")
        _roll_back_folder(_screen, _zumi, log_folder, path)
        return False
    time.sleep(1)
    subprocess.Popen("sudo chown -R pi " + path + "Zumi_Content",
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    # update_lessonlist_file()
    updated_version = open(path + 'Zumi_Content/README.md').readline().split()[0]
    __finished_updating(_zumi, _screen, "Updated to v{} !".format(updated_version))

    time.sleep(3)
    return True


def _roll_back_folder(_screen, _zumi, log_folder, path):
    if log_folder is not None:
        print("revert folder")
        subprocess.Popen("sudo rm -rf /home/pi/Dashboard/Zumi_Content",
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        time.sleep(1)
        subprocess.Popen('mv ' + log_folder + " " + path + "Zumi_Content",
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        time.sleep(1)
        subprocess.Popen("sudo chown -R pi " + path + "Zumi_Content",
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    _screen.draw_text_center("Fail to update content")
    time.sleep(2)
    _zumi.play_note(Note.A5, 100)
    _zumi.play_note(Note.F5, 2 * 100)


def _change_to_log_folder(path='/home/pi/Dashboard/'):
    current = None
    try:
        current = open(path+'Zumi_Content/README.md').readline().split()[0]
    except FileNotFoundError:
        print("content folder is not exsist")
        return current

    folder_name = 'log_v' + str(current) + '_content'
    log_folder = path + folder_name
    # print(log_folder)
    cnt = 1
    while os.path.isdir(log_folder):
        log_folder = path + folder_name + '_{}'.format(cnt)
        cnt += 1
        # print(log_folder)
    subprocess.Popen('mv ' + path + 'Zumi_Content ' + log_folder,
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    # print('mv ' + path + 'Zumi_Content ' + log_folder)
    time.sleep(1)
    # print("sudo chown -R pi " + log_folder)
    subprocess.Popen("sudo chown -R pi " + log_folder,
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    print("change name : {}".format(log_folder))
    return log_folder


def restart_threads(_screen):
    Thread(target=restart_app, args=()).start()
    Thread(target=go_to_zumi_dashboard_msg, args=(_screen,)).start()


def restart_app():
    subprocess.run(["sudo python3 /home/pi/Dashboard/dashboard.py"], shell=True)


def go_to_zumi_dashboard_msg(_screen):
    _screen.draw_text_center("Dashboard restarting...")
    for x in range(20):
        time.sleep(1)
    _screen.draw_text_center("Go to \"zumidashboard.ai\" in your browser")


def check_user_content(base_dir_path, usr_dir_path):
    try:
        base = open(base_dir_path + 'Zumi_Content/README.md').readline().split()[0]
    except:
        return False
    try:
        usr_version = open(usr_dir_path+'Zumi_Content/README.md').readline().split()[0]
    except:
        return False

    if usr_version != base:
        return True
    else:
        return False


def copy_content(base_dir_path, usr_dir_path):
    _change_to_log_folder(usr_dir_path)
    subprocess.Popen(['cp', '-r', base_dir_path + 'Zumi_Content', usr_dir_path])
    time.sleep(1)
    subprocess.Popen("sudo chown -R pi " + usr_dir_path + 'Zumi_Content',
                     stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)


def check_content_version():
    url = "https://raw.githubusercontent.com/RobolinkInc/Zumi_Content/master/README.md"
    new = os.popen("curl -m 12 --fail "+url).read().split()[0]
    try:
        current = open('/home/pi/Dashboard/Zumi_Content/README.md').readline().split()[0]
    except:
        current = None

    if new != current:
        return True
    else:
        return False


# def update_lessonlist_file():
#     import json
#
#     lesson_files_path = "/home/pi/Dashboard/Zumi_Content/Lesson/"
#     lesson_file_list = os.listdir(lesson_files_path)
#     lesson_file_list.sort()
#
#     lesson_list = []
#
#     lesson_id = 0
#     for lesson_name in lesson_file_list:
#         if lesson_name != '.ipynb_checkpoints':
#             with open(lesson_files_path + lesson_name, 'r') as lesson_file:
#                 file_content = json.loads(lesson_file.read())
#             try:
#                 description = file_content["cells"][1]["source"][2].split(">")[1].split("<")[0].replace("\n", " ")
#
#                 if len(description) > 175:
#                     description = description[:175] + "..."
#             except:
#                 description = " "
#             lesson_info = {"id": lesson_id, "title": lesson_name[:-6], "description": description}
#             lesson_list.append(lesson_info)
#             lesson_id = lesson_id + 1
#
#     lesson_list_json = {"LessonList": lesson_list}
#
#     with open('/usr/local/lib/python3.5/dist-packages/zumidashboard/dashboard/LessonList.json', 'w') as lesson_list_file:
#         json.dump(lesson_list_json, lesson_list_file)


def update_develop_version(_zumi, _screen):
    option = '--upgrade'
    git_url = 'https://develop:ehhwu3qQn5Es5aJVuFS9@gitlab.com/robolink-team/Flask-AP.git@develop#egg=zumidashboard'
    p = subprocess.Popen('sudo pip3 install {} git+{}'.format(option, git_url),
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

    img_arr = np.asarray(Image.open('/usr/local/lib/python3.5/dist-packages/zumi/util/images/blankbar.ppm'))
    img = Image.fromarray(img_arr.astype('uint8'))

    _screen.draw_text("Updating from git", x=9, y=8, image=img.convert('1'), font_size=12, clear=False)
    img = _screen.screen_image.convert('RGB')

    updater_thread = Thread(target=__progress, args=(_screen,img, 0, 21))
    updater_thread.start()

    try:
        while p.poll() is None:
            line = p.stdout.readline().decode()
            print(line)

            if 'Error' in line:
                updater_thread.join()
                _screen.draw_text_center("Error!\nPlease Try Again")
                time.sleep(2)
                return

            if 'Cloning' in line:
                updater_thread.join()
                updater_thread = Thread(target=__progress, args=(_screen, img, 21, 88))
                updater_thread.start()

            elif 'Installing collected packages' in line:
                updater_thread.join()
                updater_thread = Thread(target=__progress, args=(_screen, img, 88, 96))
                updater_thread.start()

            elif 'Successfully installed' in line:
                updater_thread.join()
                updater_thread = Thread(target=__progress, args=(_screen, img, 96, 101))
                updater_thread.start()
                version_info = line.split('-')[-1]

        print(version_info)
        updater_thread.join()

        time.sleep(1)
        __finished_updating(_zumi, _screen, "Dashboard updated!")
        _screen.draw_text_center("Dashboard updated to v" + str(version_info), font_size=15)

    except Exception as e:
        updater_thread.join()
        _screen.draw_text_center("Zumi already up-to-date")
        print(e)


def update_eveything_pipeline(_zumi, _screen, v):
    update_version(_zumi, _screen, v)
    time.sleep(2)
    update_content(_zumi, _screen)
    restart_threads(_screen)


def update_dashboard_pipeline(_zumi, _screen, v):
    update_version(_zumi, _screen, v)
    time.sleep(2)
    restart_threads(_screen)


def update_develop_pipeline(_zumi, _screen):
    update_develop_version(_zumi, _screen)
    time.sleep(2)
    restart_threads(_screen)


def run_develop():
    zumi = Zumi()
    screen = Screen(clear=False)
    update_develop_pipeline(zumi, screen)


def run(v=None):
    zumi = Zumi()
    screen = Screen(clear=False)
    update_dashboard_pipeline(zumi, screen, v)


def run_everything(v=None):
    zumi = Zumi()
    screen = Screen(clear=False)
    update_eveything_pipeline(zumi, screen, v)


if __name__ == '__main__':
    zumi = Zumi()
    screen = Screen(clear=False)
    check_user_content('whoseop')

