import os
import glob


class Autodesk3dsmaxStruct(object):

    def __init__(self):
        super(Autodesk3dsmaxStruct, self).__init__()
        self.exe_filename = None
        self.max_root = None
        self.version = None
        self.version_str = None
        self.icon = None
        self.bit = None

        self.startup_script_path = None
        self.local_startup_script_path = None

    def __lt__(self, s):
        return self.version_int() < s.version_int()

    def __gt__(self, s):
        return self.version_int() > s.version_int()

    def __eq__(self, s):
        return self.version_int() == s.version_int()

    def __ge__(self, s):
        return self.version_int() >= s.version_int()

    def __le_(self, s):
        return self.version_int() <= s.version_int()

    def version_int(self):
        v = int(self.version_str.split(' ')[-1])
        return v


class Autodesk3dsmax(Autodesk3dsmaxStruct):
    """
    Autodesk 3dsmax 类

    识别插件版本
    installed_plugins

    """

    def __repr__(self):
        return '<{}_{}: \'{}\'>'.format(self.version_str, self.bit, self.__class__.__name__)

    def __init__(self):
        super(Autodesk3dsmax, self).__init__()
        self.plug_data = {
            'vray': self.find_vray_version,
            'corona': self.find_cr_version,
        }

    def find_vray_version(self, filename):
        """从DLL中识别VR版本信息"""
        with open(filename, 'rb') as ff:

            ff.seek(os.path.getsize(filename) - 1024 * 1024)
            filter = ('.0D', '.00001D')

            for a in ff.readlines():
                bb = a.decode('utf-8', errors='ignore')

                if 'P\x00r\x00o\x00d\x00u\x00c\x00t\x00V\x00e' in bb:
                    text = (bb.replace('\x00', '')).split('ProductVersion')[-1].split()[0].strip()
                    text = text.split('\x01')[0]

                    for f_s in filter:
                        if f_s in text:
                            text = text[:-len(f_s)]

                    text = 'Vray ' + text
                    return text

        return 'Vray ?'

    def find_cr_version(self, filename):
        """从DLL中识别CR版本信息"""
        with open(filename, 'rb') as ff:

            flag = ff.read()[128]

            if flag == 15:
                return 'Corona 1.7.4'
            elif flag == 116:
                return 'Corona 2.0'
            elif flag == 254:
                return 'Corona 3.1'
            elif flag == 220:
                return 'Corona 4.1'
            else:
                return 'Corona {}'.format(flag)

    def find_plug_by_folder(self, folder):
        found_lst = []

        dll_file_lst = [k for k in os.listdir(folder) if '.dll' in k]

        for plug_name in self.plug_data:

            for f in dll_file_lst:
                if f.lower().startswith(plug_name):
                    filename = os.path.join(folder, f)
                    result = self.plug_data[plug_name](filename)
                    if result:
                        found_lst.append(result)

                    break

        return found_lst

    def installed_plugins(self):
        return self.find_plug_by_folder(self.max_root)

    def max_histroy_files(self):
        '''
        当前max对象的文件打开记录
        '''

        import xmltodict
        max_file_lst = []
        xml_lst = []
        max_obj = self

        xml_lst += glob.glob(max_obj.local_startup_script_path + "\\*\\RecentDocuments.xml", recursive=True)

        for f in xml_lst:

            with open(f, 'rb') as fd:
                doc = xmltodict.parse(fd.read())

                items = doc['MaxApp.RecentDocumentListMemento']['Items']

                first_key = list(items.keys())[0]

                if items[first_key]:
                    data = items[first_key]['MaxApp.RecentDocument']

                    filename = None
                    if isinstance(data, list):
                        for _ in data:
                            filename = _['FilePath']
                    else:
                        filename = data['FilePath']

                    max_file_lst.append({'FileName': filename, 'Exists': os.path.exists(filename)})

        return max_file_lst

    @classmethod
    def max_backup_list(cls):
        """全部max自动保存文件"""
        import winshell
        my_documents_path = winshell.my_documents()

        max_file_lst = []
        max_lst = glob.glob(my_documents_path + "\\3dsMax\\autoback\\*.max", recursive=True)

        for index, max_filename in enumerate(max_lst):
            max_file_lst.append({'FileName': max_filename, 'Exists': os.path.exists(max_filename)})

        return max_file_lst

    @classmethod
    def get_default_exe(cls):
        """
        获取ftype 关联
        :return:
        """
        data = os.popen('ftype 3dsmax').read()
        if '=' in data:
            exe = data.split('=')[1].split('" ')[0][1:]
            exe = os.path.abspath(exe)
            if os.path.exists(exe):
                return exe

    @classmethod
    def get_hwnd_lst(cls):
        """获取正在运行的3dsmax窗口句柄"""
        import win32gui
        hwnds = []

        def hwnd_s(a, h):
            try:
                if win32gui.IsWindow(a) and win32gui.IsWindowVisible(a) and \
                        win32gui.IsWindowEnabled(a):
                    h.append((win32gui.GetClassName(a), win32gui.GetWindowText(a), a))
            except:
                pass

        win32gui.EnumWindows(hwnd_s, hwnds)

        hwnd_infos = []
        set_list = []
        for c_name, w_title, hwnd in hwnds:

            if c_name == "3DSMAX" and hwnd not in set_list:
                set_list.append(hwnd)
                hwnd_infos.append([w_title, hwnd])
                continue

            if c_name == 'Qt5QWindowIcon' and '3ds Max 2' in w_title:
                if hwnd not in set_list:
                    set_list.append(hwnd)
                    hwnd_infos.append([w_title, hwnd])

        return hwnd_infos

    def mxs_base64(self, code):
        """代码转换为base64方式执行"""
        import base64
        base_64_data = base64.b64encode(code.encode('gbk')).decode('utf-8')
        data = '''base64data = "{}"
dotnet_encoding = dotnetclass "System.Text.Encoding"
ascii_object = dotnet_encoding.ASCII
dotnet_convert = dotnetclass "Convert"
bytes_data = dotnet_convert.FromBase64String(base64data)
real_data = ascii_object.Default.GetString(bytes_data);
execute(real_data);
        '''.format(base_64_data)
        data = data
        return data

    def filein_script_code(self, script_filename):
        """
        生成filein脚本的mxs代码
        :param script_filename:
        """
        code = 'try(filein @"{}")catch(print "error: {}")'.format(script_filename, os.path.basename(script_filename))
        code = self.mxs_base64(code)
        code = code.encode()
        return code

    def ready_data_from_finder(self, data):
        self.exe_filename = data['path']
        self.version = data['version']
        self.version_str = data['version_string']
        self.icon = data['icon']
        self.bit = int(data['bit'])

        self.max_root = os.path.dirname(self.exe_filename)

        self.startup_script_path = os.path.join(self.max_root, 'scripts\Startup')
        self.local_startup_script_path = data['local_path']

    def remove_file(self, filename):
        if os.path.exists(filename):
            os.remove(filename)

    def write_code_to_file(self, filename, code):
        if os.path.exists(filename):
            with open(filename, 'rb') as old_f:
                f_code = old_f.read()
                if f_code == code:
                    return True

            os.remove(filename)

        try:
            with open(filename, 'wb') as f:
                f.write(code)
                return True
        except:
            pass

    def check_startup_script(self, base_filename, lib_filename):
        """
        检查脚本安装状态
        :param base_filename:
        :param lib_filename:
        :param menu_name:
        :return:
        """
        status = '未安装'
        file_in_code = self.filein_script_code(lib_filename)

        lang_exists_lst = []

        # 语言配置
        lang_lst = glob.glob(self.local_startup_script_path + "\\*\\scripts\\startup")
        for lang_folder in lang_lst:
            full_script_filename = os.path.join(lang_folder, base_filename)

            if os.path.exists(full_script_filename):
                with open(full_script_filename, 'rb') as f:
                    if f.read() != file_in_code:
                        status = '需更新'
                    else:
                        lang_exists_lst.append(full_script_filename)

        full_script_filename = os.path.join(self.startup_script_path, base_filename)
        if os.path.exists(full_script_filename):
            with open(full_script_filename, 'rb') as f:
                if f.read() != file_in_code:
                    status = '需更新'
                else:
                    status = '已安装'

        if len(lang_exists_lst) >= len(lang_lst):
            status = '已安装'

        return status

    def install_startup_script(self, base_filename, lib_filename, menu_name=None, uninstall=False):
        """
        安装启动脚本
        :param base_filename: 脚本文件名，非完整路径
        :param lib_filename: 脚本库文件名，完整路径
        """
        successed = False
        file_in_code = self.filein_script_code(lib_filename)

        # 删除卸载菜单脚本
        self.build_clear_menu_script(self.startup_script_path, menu_name, by_install=True)

        # 安装到语言配置
        lang_lst = glob.glob(self.local_startup_script_path + "\\*\\scripts\\startup")
        for lang_folder in lang_lst:
            full_script_filename = os.path.join(lang_folder, base_filename)

            if uninstall:
                # 卸载脚本
                self.remove_file(full_script_filename)
                self.build_clear_menu_script(lang_folder, menu_name)
                continue

            if self.write_code_to_file(full_script_filename, file_in_code):
                successed = True

            self.build_clear_menu_script(lang_folder, menu_name, by_install=True)

        if successed:
            return True

        # 尝试安装到主目录
        full_script_filename = os.path.join(self.startup_script_path, base_filename)

        if uninstall:
            self.remove_file(full_script_filename)
            self.build_clear_menu_script(self.startup_script_path, menu_name)
            return True

        if self.write_code_to_file(full_script_filename, file_in_code):
            return True

    def build_clear_menu_script(self, folder, menu_name=None, by_install=False):
        """
        :param folder:
        :param menu_name:
        :param by_install: 正常安装模式，删除卸载菜单脚本
        :return:
        """
        mxs_code = u'''
        -- AutoMenuClear
        try(
        temp_source_filename = filenamefrompath(getsourcefilename())
        temp_filter_str = filterstring temp_source_filename "."
        menu_name = temp_filter_str[1]
        manMenu = menuMan.getMainMenuBar()
        for i in 1 to manMenu.numItems() do
        (
        try(menu = manMenu.getItem(i))catch()
        if menu.getTitle() == menu_name do(
        manMenu.removeItem menu;
        menuMan.updateMenuBar()
        )
        )
        )catch()
        try(deletefile (getsourcefilename()))catch()
        '''

        temp_filename = os.path.join(folder, '{}.ms'.format(menu_name))

        if by_install:
            self.remove_file(temp_filename)
            return True

        try:
            with open(temp_filename, 'wb') as f:
                f.write(mxs_code.encode('gbk'))
        except:
            return False


if __name__ == '__main__':
    from cgtools.Finder import Autodesk3dsMaxFinder

    a = Autodesk3dsMaxFinder()
    a.run()

    print(a[2016].installed_plugins())

    a[2018].install_startup_script('test.ms', 'd:\\test_lib.ms', '测试菜单', uninstall=True)
